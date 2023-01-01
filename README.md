# Earth-Engine-Catalog

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/Earth-Engine-Catalog/blob/master/gee_catalog.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/Earth-Engine-Catalog/HEAD?labpath=gee_catalog.ipynb)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

The [Google Earth Engine](https://earthengine.google.com/) platform hosts a lot of publicly available geospatial datasets. This repo compiles the list of all geospatial datasets on Earth Engine as a CSV file and as a JSON file, making it easier to find and use them programmatically. The list is updated daily.

A complete list of geospatial datasets on Earth Engine is available [here](https://developers.google.com/earth-engine/datasets/).

## Usage

This repo provides the list of geospatial datasets on Planetary Computer in two formats:

- Tab separated values (TSV) file: [gee_catalog.tsv](https://github.com/giswqs/Earth-Engine-Catalog/blob/master/gee_catalog.tsv)
- JSON file: [gee_catalog.json](https://github.com/giswqs/Earth-Engine-Catalog/blob/master/gee_catalog.json)

The TSV file can be easily read into a Pandas DataFrame using the following code:

```python
import pandas as pd

url = 'https://github.com/giswqs/Earth-Engine-Catalog/raw/master/gee_catalog.tsv'
df = pd.read_csv(url, sep='\t')
df.head()
```

## Related Projects

- A list of open datasets on AWS: [aws-open-data](https://github.com/giswqs/aws-open-data)
- A list of open geospatial datasets on AWS: [aws-open-data-geo](https://github.com/giswqs/aws-open-data-geo)
- A list of open geospatial datasets on AWS with a STAC endpoint: [aws-open-data-stac](https://github.com/giswqs/aws-open-data-stac)
- A list of STAC endpoints from stacindex.org: [stac-index-catalogs](https://github.com/giswqs/stac-index-catalogs)
- A list of geospatial datasets on Microsoft Planetary Computer: [Planetary-Computer-Catalog](https://github.com/giswqs/Planetary-Computer-Catalog)
- A list of geospatial datasets on Google Earth Engine: [Earth-Engine-Catalog](https://github.com/giswqs/Earth-Engine-Catalog)
- A list of geospatial datasets on NASA's Common Metadata Repository (CMR): [NASA-CMR-STAC](https://github.com/giswqs/NASA-CMR-STAC)
- A list of geospatial data catalogs: [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs)
