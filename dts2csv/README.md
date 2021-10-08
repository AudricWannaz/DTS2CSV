# Overview

DTS2CSV allows you to extract contents from a DTS API as local CSV file.
It can also retrieve corresponding TEI files and, if Saxon and TEI-XSL are available on your computer, automatically convert them as Text and HTML files (and compute basic statistics out of textual version).

In that last case, basic statistical info in generated (nbWords for example) and added to CSV contents.

# Architecture

## Python Extractor
dts2csv,py takes a JSON config file as input, and walk through DTS API to extract contents.

JSON file shall have following fields:
- __DTS_URL__: URL fo the DTS API server
- __DTS_COLLECTIONS_ENTRYPOINT__ and __DTS_DOCUMENTS_ENTRYPOINT__: entrypoint names for collections and documents. 
(Navigation API is not used at all by the tool)
- __START_COLLECTION_ID__: DTS ID of the collection where to start from. Generally start from 'default' to start from the root.
- __MAX_DEPTH__: how deep to go in the collections. For example stop at '2' just to get an overview of the main groups. 'None' means go as deep as you can.
- __RETRIEVE_FILES__ (True|False) : if True, download also TEI files.
- __TRANSFORM_TEI_TO_TXT__: convert TEI file to text (requires Saxon and TEI-XSL - see below). When activated, lines, words and chars counts are performed and aggregated also to each parent collections, in order to facilitate potential quantitative study of the corpus.
- __TRANSFORM_TEI_TO_HTML__: convert TEI file to HTML (requires Saxon and TEI-XSL - see below)
- __INLINE_TXT_IN_CSV__: put text contents into CSV file itself (replacing new lines by special "\_\_CR\_\_" marker). This can be useful to load contents at once in third party application such as https://metaindex.fr.

- __COLLECTIONS__ and __RESOURCES__: list of custom json attributes to extract into CSV. Each element of the list shall be a dictionary with at least 'dts_id' field, and optionally 'csv_name' field.
'dts_id' shall be the path to the required DTS attribute in the json file returned by the server, starting from json root, using '/' as separator (like a folders hierarchy for example). 
For example { 'dts_id'="dts:extensions/ns1:language", "cvs_name"="language" } will extract parameter <root>/dts:extensions/ns1:language from json contents and store it in a 'language' column of the generated CSV file. 
For arrays, the <param>[n] syntax can be used to reach the nth element of the list (starting from 0).

 - __SAXON_JAR_PATH__: location in host of the saxon-he-10.5.jar file (see https://sourceforge.net/projects/saxon/files/Saxon-HE/). (optional, only needed for conversion of TEI files to text or html)
 - __TEI_XSL_STYLESHEETS_PATH__: location in host of folder containing html5/html5.xsl and text/tei-to-text.xsl files (see https://github.com/TEIC/Stylesheets). (optional, only needed for conversion of TEI files to text or html)
 
Full example:

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

GUI front-end allows you to generate JSON config file more easily. You shall fill in the forms and after each step, submit and then go to next panel thanks to menu on top left of the GUI.
 
# Run it
 
## Online instance
Running server available at: https://github.com/TEIC/Stylesheets

## Run local GUI:
 ```
 $ streamlit run ./streamlitdts2csv.py
 ```
 
## Run directly backend python script:
```
$ python dts2csv.py my_conf.json -o ~/tmp/my_results
```
 
 
 
 
