

#
# Demo config file for dts2csv.py from MetaindeX Toolbox https://metaindex.fr/webapp/toolbox
#
# In this example, we retrieve Latin Collections from Perseids project DTS API.
#
# Author: Laurent ML - metaindex.fr 2021
# If you find this tools useful somehow, please reference MetaindeX project when possible.
# 
# GNU GENERAL PUBLIC LICENSE
# Version 3, 29 June 2007
# 
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# 
# See full version of LICENSE in <https://fsf.org/>
#

from os.path import expanduser
home = expanduser("~")

# path to dependencies. We suppose here we work under Linux style path separator
# Those deps are only needed if TRANSFORM_TEI_TO_TXT or TRANSFORM_TEI_TO_HTML are set to True
SAXON_JAR_PATH=home+"/dev/tei/install/SaxonHE10-5J/saxon-he-10.5.jar"
TEI_XSL_STYLESHEETS_PATH=home+"/dev/tei/install/tei-xsl"

# API URLs
rootUrl="https://dts.perseids.org/"
COLLECTIONS_URL=rootUrl+"collections"
DOCUMENTS_URL=rootUrl+"documents"
NAVIGATION_URL=rootUrl+"navigation"
DATASET_ID="perseids"

# where to start from
ROOT_COLLECTION_ID="urn:perseids:latinLit"

# where to store generated files
TARGET_PATH=home+"/tmp/dts/perseids/"+"latin"

# set to None for no max depth
MAX_DEPTH=None

# set True to download TEI files
RETRIEVE_FILES=True

# Transorm TEI into Text and HTML requires SAXON and TEI-XSL
TRANSFORM_TEI_TO_TXT=True
TRANSFORM_TEI_TO_HTML=False

# if true, put TEI plain text contents into (resources) CSV file
# This option needs TRANSFORM_TEI_TO_TXT=True
INLINE_TXT_IN_CSV=True

# -------------------------------------------

# This function is called every time we try to download a TEI file
# if this function returns False we will skip the file
# it it returns True we will actually download it.
#
# if this function is missing, it is assumed to be always True
def config_filterResource(resourceCsvData,resourceJsonData):
    return True # retrieve all TEI files
    #return resourceCsvData["language"]=="en" # retrieve only TEI files marked as english language

# CSV ids might have some unicity or syntaxic constraints which can be handled here,
# to be compatible with Lucene query syntax (used by MetaindeX)
def config_idDts2idCsv(dtsId,dtsJsonData):
    return dtsId.replace('urn:','').replace(':','.').replace('urn.','')


# -------------------------------------------

def normalizeText(text):
    return text.replace("\n","__CR__").replace("  "," ").replace(";",".")

# -------------------------------------------

# at least 'url', 'urn', '@id', 'members' (and 'parent'), and '@type' are generated by default, others shall be listed hereunder
# <dts-id> : <csv-id>
ATTRS_LIST={
    "Collection" :{ "totalItems" : {"csvName":"nbChildren", "mandatory":True}, 
                    "title" : {"csvName":"title", "mandatory":True, "transform":normalizeText},
                    
                },
    
    
    "Resource":{ 
                "title" : {"csvName":"title", "mandatory":True, "transform":normalizeText},
                "description" : {"csvName":"description", "mandatory":True, "transform":normalizeText},
                "dts:dublincore/dc:language" : {"csvName":"language", "mandatory":True},
                
                
            }
 }