# Overview

DTS2CSV allows you to extract contents from a DTS API as local CSV file.
It can also retrieve corresônding TEI files and, if Saxon and TEI-XSL are available on your computer, automatically convert them as Text and HTML files.

In that las t case, basic statistical info in generated (nbWords for example) and added to CSV contents.

# Architecture

## Python Extractor
dts2csv,py takes a JSON config file as input, and walk through DTS API to extract contents.

JSON file shall have following contents:
```
 {
    "DTS_URL":"https://dev.chartes.psl.eu/api/nautilus/dts/",
    "DTS_COLLECTIONS_ENTRYPOINT":"collections",
    "DTS_DOCUMENTS_ENTRYPOINT":"document",
    "START_COLLECTION_ID":"default",
    "MAX_DEPTH":"None",
    "RETRIEVE_FILES":"True",
    "TRANSFORM_TEI_TO_TXT":"True",
    "TRANSFORM_TEI_TO_HTML":"False",
    "INLINE_TXT_IN_CSV":"True",
    "COLLECTIONS": [
        {"dts_id":"title"},
        {"dts_id":"dts:extensions/ns1:creator[0]/@value", "csv_name":"author"},
        {"dts_id":"dts:extensions/ns1:date", "csv_name":"year"},
        {"dts_id":"dts:extensions/ns1:language", "csv_name":"language"}
    ],
    "RESOURCES": [
        {"dts_id":"dts:extensions/ns1:language", "csv_name":"language"},
        {"dts_id":"title","mandatory":"True"},
        {"dts_id":"dts:extensions/cts:description[0]/value", "csv_name":"description"}
    ],
    
    "SAXON_JAR_PATH":"HOME/dev/tei/install/SaxonHE10-5J/saxon-he-10.5.jar",
    "TEI_XSL_STYLESHEETS_PATH":"HOME/dev/tei/install/tei-xsl"
}
```

## Front-End GUI

# Run it
