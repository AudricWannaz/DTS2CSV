#imports
import streamlit as st
from os.path import expanduser

# functions
def opening_style():
    col1, col2 = st.columns(2)
    col1.title(' Welcome to DTS2CSV!')
    col2.image('logo.png')
    st.header('convert any DTS data in a CSV within seconds')

    # stuff happens

def closing_style():
    st.write('This tool war written during the DTS Hackathon (https://distributed-text-services.github.io/workshops/events/2021-hackathon/). License=open(which one?). '
             'Please refer to this software as following: DTS2CSV Ver 1.0 by Laurent ML (backend) and Audric Wannaz (streamlit GUI)')

def about():

    infos ='''Dts2csv is also a part of the MetaindeX Toolbox https://metaindex.fr/webapp/toolbox
    Author: Laurent ML - metaindex.fr + Audric Wannaz 2021
    If you find this tools useful somehow, please reference MetaindeX project when possible.
     
    GNU GENERAL PUBLIC LICENSE
    Version 3, 29 June 2007
     
    Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
     
    See full version of LICENSE in <https://fsf.org/>'''

    st.write(infos)

def main():
    if 'url' not in st.session_state:
        get_url_input()

# main code

# doing the sidebar
mode = st.sidebar.selectbox('choose a mode:', ['DTS2CSV', 'DTS2PDF', 'Load input file', 'Manual input (main mode)','Settings'])
# settings in sidebar
out_name = st.sidebar.text_input('Name of the CSV file: ', 'output')
out = False

# main window
opening_style()

#def dtscsv_input():

home = expanduser("~")

# path to dependencies. We suppose here we work under Linux style path separator
# only needed if TRANSFORM_TEI_TO_TXT or TRANSFORM_TEI_TO_HTML are set to True
SAXON_JAR_PATH=home+"/dev/tei/install/SaxonHE10-5J/saxon-he-10.5.jar"

## Path to TEI-XSL Stylesheets
## only needed if TRANSFORM_TEI_TO_TXT or TRANSFORM_TEI_TO_HTML are set to True
## shall contain at least following files:
## <TEI_XSL_STYLESHEETS_PATH>/html5/html5.xsl
## <TEI_XSL_STYLESHEETS_PATH>/txt/tei-to-text.xsl
TEI_XSL_STYLESHEETS_PATH=home+"/dev/tei/install/tei-xsl"

# API URLs
rootUrl="https://dev.chartes.psl.eu/api/nautilus/dts/"
COLLECTIONS_URL=rootUrl+"collections"
DOCUMENTS_URL=rootUrl+"document"
NAVIGATION_URL=rootUrl+"navigation"
DATASET_ID="thesesENC"

with st.form('main_form'):
    st.header('1. Mandatory inputs')
# where to start from
    ROOT_COLLECTION_ID="urn"+st.text_input('Enter a valid collection ID')

    # where to store generated files
    #TARGET_PATH=home+st.text_input('Enter a valid PATH') # update this with better st features> at best not used, downloads is ok

    # set to None for no max depth
    depths = [None, 1, 2, 3, 'custom'] # where should it stop?
    if depths == 'custom':
        depths2 = st.slider('Pick a value', 4, 10)

    MAX_DEPTH= st.selectbox('Choose Depth (None=max)', depths)

    # set True to download TEI files
    #RETRIEVE_FILES=True

    st.header('2. Optional inputs')
    with st.expander('show'):
        RETRIEVE_FILES= st.checkbox('RETRIEVE_FILES', True)


    # Transorm TEI into Text and HTML requires SAXON and TEI-XSL
    #TRANSFORM_TEI_TO_TXT=True
    #TRANSFORM_TEI_TO_HTML=True

        TRANSFORM_TEI_TO_TXT=st.checkbox('TRANSFORM_TEI_TO_TXT', True)
        TRANSFORM_TEI_TO_HTML=st.checkbox('TRANSFORM_TEI_TO_HTML', True)
    # if true, put TEI plain text contents into (resources) CSV file
    # This option needs TRANSFORM_TEI_TO_TXT=True
        if TRANSFORM_TEI_TO_TXT:
        #INLINE_TXT_IN_CSV=True
            INLINE_TXT_IN_CSV=st.checkbox('INLINE_TXT_IN_CSV', True)
        else:
            INLINE_TXT_IN_CSV = False

    # end of form
    submitted = st.form_submit_button('MAKE CSV')
    if submitted:
        out = [ROOT_COLLECTION_ID, MAX_DEPTH, RETRIEVE_FILES, TRANSFORM_TEI_TO_TXT, TRANSFORM_TEI_TO_HTML, INLINE_TXT_IN_CSV]


# TARGET_PATH,


        st.write('This is the current output of the GUI:')
        st.write(out)

if out:
    st.download_button('DOWNLOAD', str(out), file_name=out_name+'.txt', mime=None, key=None, help=None, on_click=None, args=None, kwargs=None)
else:
    st.stop()

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
    return dtsId.replace('urn:','').replace(':','.').replace('urn.','') # the first replace must probably be fixed

# -------------------------------------------

# utility function called from DTS/CSV mapping table
# replace carriage return by "__CR__" string, so that it can stay in a single line in CSV file.
# this string is typically replaced back to carriage return when importing CSV file into metaindex app:
# "__CR__" is transcoded to newline by MetaindeX during import
# "__MX_ESCAPED_SEPARATOR__" is transcoded to ';' by MetaindeX during import
def normalizeText(text):
    return text.replace("\n","__CR__").replace("  "," ").replace(";","__MX_ESCAPED_SEPARATOR__")

# -------------------------------------------

# DTS/CSV mapping table
# list of DTS 'path' to put into CSV columns
# at least 'url', 'urn', '@id', 'members' (and 'parent'), and '@type' are generated by default, others shall be listed hereunder

# ask Laurent about that
ATTRS_LIST={
     "Collection" :{ "totalItems" : {"csvName":"nbChildren", "mandatory":True}, 
                    "title" : {"csvName":"title", "mandatory":True, "transform":normalizeText},
                    "dts:extensions/ns2:creator[0]/@value" : {"csvName":"author", "mandatory":False},
                    "dts:extensions/ns2:date" : {"csvName":"date", "mandatory":False},
                },
    
    
    "Resource":{ 
                "dts:extensions/ns2:language" : {"csvName":"language", "mandatory":True},
                
                
            }
 }

def gui_main():
    return gui_out


closing_style()

# to do:
# adjust code in dtscsv.py and config.py



