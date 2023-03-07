import json
import os
import pandas as pd
from pystac_client import Client

out_dir = "datasets"

url = "https://earthengine-stac.storage.googleapis.com/catalog/catalog.json"

root = Client.open(url, headers=[])

catalogs = []

for link in root.get_child_links():
    if link.rel == "child":
        catalogs.append(link.target)

datasets = []

i = 0
for catalog in catalogs:
    cat = Client.open(catalog, headers=[])
    print(cat.title)

    try:
        for index, collection in enumerate(cat.get_all_collections()):
            data = collection.to_dict()
            print(f'{i}: {data["id"]}')
            i = i + 1
            dataset = {}
            output = out_dir + "/" + data["id"].replace("/", "_") + ".json"
            if not os.path.exists(os.path.dirname(output)):
                os.makedirs(os.path.dirname(output))
            with open(output, "w") as f:
                json.dump(data, f, indent=4)

            dataset["id"] = data["id"]
            dataset["title"] = data["title"]
            dataset["type"] = data["gee:type"]
            if dataset["type"] == "image":
                dataset["snippet"] = f"ee.Image('{dataset['id']}')"
            elif dataset["type"] == "image_collection":
                dataset["snippet"] = f"ee.ImageCollection('{dataset['id']}')"
            else:
                dataset["snippet"] = f"ee.FeatureCollection('{dataset['id']}')"

            dataset["provider"] = data["providers"][0]["name"].replace("\n", " ")
            dataset["state_date"] = data["extent"]["temporal"]["interval"][0][0].split(
                "T"
            )[0]
            dataset["end_date"] = data["extent"]["temporal"]["interval"][0][1].split(
                "T"
            )[0]
            dataset["bbox"] = ", ".join(
                [str(coord) for coord in data["extent"]["spatial"]["bbox"][0]]
            )
            if "deprecated" in data:
                dataset["deprecated"] = data["deprecated"]
            else:
                dataset["deprecated"] = False
            dataset["keywords"] = ", ".join(data["keywords"])

            link = ""
            thumbnail = ""
            terms_of_use = ""
            script = ""

            for l in data["links"]:
                if l["rel"] == "self":
                    link = l["href"]
                if l["rel"] == "preview":
                    thumbnail = l["href"]
                if l["rel"] == "license":
                    terms_of_use = l["href"]
                if l["rel"] == "related":
                    script = l["href"]
            dataset["catalog"] = link
            url_prefix = "https://developers.google.com/earth-engine/datasets/catalog"
            dataset["url"] = f"{url_prefix}/{data['id'].replace('/', '_')}"
            dataset["thumbnail"] = thumbnail
            dataset["script"] = script
            dataset["terms_of_use"] = terms_of_use
            dataset["license"] = data["license"]

            datasets.append(dataset)
    except Exception as e:
        print(e)

print("Total datasets: ", len(datasets))

df = pd.DataFrame(datasets)
df.sort_values(by=["id"], inplace=True)
# remove the script and terms_of_use columns because it contains ? and # characters, GitHub can't render it.
df.drop(["script", "terms_of_use", "thumbnail"], axis=1).to_csv(
    "gee_catalog.tsv", index=False, sep="\t"
)

with open("gee_catalog.json", "w") as f:
    json.dump(df.to_dict("records"), f, indent=4)
