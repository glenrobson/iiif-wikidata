# iiif-wikidata
IIIF and Wikidata experiements

Wikidata now has a relation property for IIIF Manifests allowing wikidata items to point to [IIIF](https://iiif.io) manifests. The wikidata property is [Property:P6108](https://www.wikidata.org/wiki/Property:P6108).

This project aims to demonstrate the different uses of this new property. 

## Scripts

### addWikiManifest.py

Currently only setup for [NLW](https://www.library.wales/) but retrieves a collection from WikiData and adds a link to a manifest. It does this in this example by converting the handle to a manifest link. This extra data is then stored in a CSV file for upload to WikiData. This can be run as follows:

```
./addWikiManifest.py /tmp/wikidata_with_manifest.csv
```

and if you want a different collection this can be passed in:

```
./addWikiManifest.py Q21542493 /tmp/wikidata_with_manifest.csv
```
