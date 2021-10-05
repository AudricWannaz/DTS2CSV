# questions to Laurent are noted with *

#imports
import streamlit as st

# not used?
from os.path import expanduser

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#def init_sidebar():
#    # initialises home and outputs
#    if 'step' not in st.session_state:
#        st.session_state.step = 1
#    if 'gui_output' not in st.session_state:
#        st.session_state.gui_output = []
#    if 'collections' not in st.session_state:
#        st.session_state.collections = []
#    if 'ressources' not in st.session_state:
#        st.session_state.ressources = []
#
#    sb_mode = st.sidebar.selectbox('Navigate by clicking', ['home', 'collections', 'ressources'])
#    st.session_state.mode = sb_mode
#
#    st.sidebar.write('*')
#    st.sidebar.write('collections')
#    st.sidebar.write(st.session_state.collections)
#    st.sidebar.write('ressources')
#    st.sidebar.write(st.session_state.ressources)
#
#
#def home():
#    st.title('fix col - a part of the dts2csv hack')
#
#
#def collections():
#    st.title('collections here')
#    mk_list('collections')
#
#
#def ressources():
#    st.title('ressources here')
#    mk_list('ressources')
#
#
#def main():
#    init_sidebar()
#    if st.session_state.mode == 'home':
#        home()
#    elif st.session_state.mode == 'collections':
#        collections()
#    elif st.session_state.mode == 'ressources':
#        ressources()
#
#
## in: an empty list
#if 'col_list' not in st.session_state:
#    st.session_state.col_list = []
#
#
## out: a list of dicts with 2 els always named 'dbs_id' and 'csv_name'
#
#
## A option serait de:
## 1 demander le nb de dicts
## 2 looper pour le nombre précis et collecter le idn et le csvn
#
#
#def mk_list(name):
#    st.title(f'Describe the {name}')
#
#    dicts_num = st.slider('How many parameters do you need?', 0, 20, 1)
#
#    with st.form('mk_list'):
#        for i in range(dicts_num):
#            st.write('Enter')
#            a = st.text_input('dbs_id?', key=i)
#            b = st.text_input('csv_name?', key=i)
#            st.session_state[f'test{i}'] = {'dbs_id': a, 'csv_name': b}
#        submit = st.form_submit_button('submit')
#        if submit:
#            st.balloons()
#            # st.session_state.col_list = ['list_of_widgets']
#            st.session_state[f'{name}'] = [st.session_state[f'test{i}'] for i in range(dicts_num)]
#            st.write('*')
#            st.write('collections')
#            st.write(st.session_state.collections)
#            st.write('ressources')
#            st.write(st.session_state.ressources)
#
#
## B encore mieux serait:
## 0 bouton go soumet la liste telle quelle
## 1 bouton xn genere un dict
## >2 form yn demande idn et wdn du bouton xn
#
#if __name__ == '__main__':
#    main()
#
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


#initialises steps
#if 'step' not in st.session_state:
#    st.session_state.step = 1
#
#def step_redirector():
#    if  st.session_state.step == 1:
#        check_url()
#    elif st.session_state.step == 2:
#        screen_one()
#    elif st.session_state.step == 3:
#        mk_list('collections')
#

#st.write('test1')

# functions
def opening_style():
    col1, col2 = st.columns(2)
    col1.title(' Welcome to DTS2CSV!')
    col1.write('Hackathon Version, October 2021, Ver. 1.0')
    col2.image('logo.png')
    st.header('convert any DTS data in a CSV within seconds')
    # *want more?

def closing_style():
    st.image('logo.png')
    #add collapser bar
    with st.expander('CREDITS'):
        about()
        st.write('This tool war written during the DTS Hackathon (https://distributed-text-services.github.io/workshops/events/2021-hackathon/). License=open(which one?). '
             'Please refer to this software as following: DTS2CSV Ver 1.0 by Laurent ML (backend) and Audric Wannaz (streamlit GUI)')

def about():

    infos ='''Dts2csv is also a part of the MetaindeX Toolbox https://metaindex.fr/webapp/toolbox
    Author: Laurent ML - metaindex.fr + Audric Wannaz 2021
    If you find this tools useful somehow, please reference MetaindeX project when possible.
     
    GNU GENERAL PUBLIC LICENSE
    Version 3.2?, x September 2021
     
    Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
     
    See full version of LICENSE in <https://fsf.org/>'''
    st.write(infos)

def check_url(): #if no url in session states, launches start screen, else passes
    if 'url' not in st.session_state:
        get_url_input()
        st.stop()
    else:
        import requests
        try:
            response = requests.get(st.session_state.url)
        except:
            st.error('Not a valid URL')
            del st.session_state['url']
            back = st.button('BACK')
            if back:
                main()
            st.stop()
        if response.status_code == 200:
            st.success('This URL seems valid! You can now select how you want to build your CSV')
        else:
            st.error('Web site does not exist')
            back = st.button('BACK')
            if back:
                main()
            st.stop()

        # other errors to handle? like 404?


def add_coll_or_res(depart_list):
    out = depart_list
    with st.form('collres_form'):
        out_key = st.text_input('enter new key')
        out_value = st.text_input('enter new value')
        submitted_2 = st.form_submit_button('submit')
        if submitted_2:
            st.write(depart_list.append({out_key:out_value}))
            out.append({out_key:out_value})
            st.write(out)
            st.stop()

def empty_list_in_fulle_list_out(a_list):
    done = False
    if 'count' not in st.session_state:
        st.session_state.count = []

    add_one = st.button('click to add one', key=0)
    if add_one:
        st.write(st.session_state.count)
        add_coll_or_res(['test',4])
        st.stop()
        #st.session_state.count = add_coll_or_res(st.session_state.count)
        #st.write(st.session_state.count)
    st.write(f'the value is currently {st.session_state.count}', key=1)
    done = st.button('DONE')
    if done:
        st.balloons()
    st.stop()


#this is the screen where 
def screen_two(out_screen_one):
    collections = []
    resources = []



    tryit = add_coll_or_res()
    st.write(tryit)
    ready = st.button('col ready?')

    if not ready:
        st.stop()
    else:
        new_dic = {'COLLECTIONS':collections, 'RESOURCES':resources}
        new_dic2 = {'COLLECTIONS':collections}
        out_screen_one.update(new_dic2)
        return out_screen_one

def fake_home():
    st.title('FAKE HOME')
    if st.button('describe collection'):
        mk_list('collection')
    if st.button('describe utils'):
        mk_list('utils')

def main():

    #fake_home()
    #mk_list('collection')
    #mk_list('utils')
    #st.write(st.session_state.collection)
    #st.write(st.session_state.utils)

    #st.stop()
    #empty = []
    #empty_list_in_fulle_list_out(empty)
    #dummy_dic = {'test':'yeah', 'really':'good'}
    #st.write(dummy_dic)
    #st.write('*')
    #out2 = screen_two(dummy_dic)
    #st.write(out2)
    #st.stop()
    #see_saved_urls()
    #st.write('test3')
    opening_style()
    #st.write('test4')
    check_url()
    st.session_state.state == 2
    screen_one()
    st.session_state.state == 3
    mk_list('collection')
    closing_style()

def screen1_vars():
    home = expanduser("~")
    SAXON_JAR_PATH=home+"/dev/tei/install/SaxonHE10-5J/saxon-he-10.5.jar"
    TEI_XSL_STYLESHEETS_PATH = home + "/dev/tei/install/tei-xsl"


def mk_list(name):
    st.title(f'Describe the {name}')
    if name not in st.session_state:
        st.session_state[f'{name}'] = []
    dicts_num = st.slider('How many parameters do you need?', 0, 20, 1)

    with st.form('mk_list'):
        for i in range(dicts_num):
            st.write('Enter')
            a = st.text_input('dbs_id?', key=i)
            b = st.text_input('csv_name?', key=i)
            st.session_state[f'test{i}'] = {'dbs_id': a, 'csv_name': b}
        submit = st.form_submit_button('submit')
        if submit:
            st.balloons()
            # st.session_state.col_list = ['list_of_widgets']
            st.session_state[f'{name}'] = [st.session_state[f'test{i}'] for i in range(dicts_num)]


def form_screen_one(out_name):
    out = False
    st.header('step 2/3')
    with st.form('main_form'):
        st.header('1. Mandatory inputs')
        # where to start from
        ROOT_COLLECTION_ID = "urn" + st.text_input('Enter a valid collection ID')

        # where to store generated files
        # TARGET_PATH=home+st.text_input('Enter a valid PATH') # update this with better st features> at best not used, downloads is ok

        # set to None for no max depth
        depths = [None, 1, 2, 3, 'custom']  # where should it stop?
        if depths == 'custom':
            depths2 = st.slider('Pick a value', 4, 10)

        MAX_DEPTH = st.selectbox('Choose Depth (None=max)', depths)

        # set True to download TEI files
        # RETRIEVE_FILES=True

        st.header('2. Optional inputs')
        with st.expander('show'):
            RETRIEVE_FILES = st.checkbox('RETRIEVE_FILES', True)

            # Transorm TEI into Text and HTML requires SAXON and TEI-XSL
            # TRANSFORM_TEI_TO_TXT=True
            # TRANSFORM_TEI_TO_HTML=True

            TRANSFORM_TEI_TO_TXT = st.checkbox('TRANSFORM_TEI_TO_TXT', True)
            TRANSFORM_TEI_TO_HTML = st.checkbox('TRANSFORM_TEI_TO_HTML', True)
            # if true, put TEI plain text contents into (resources) CSV file
            # This option needs TRANSFORM_TEI_TO_TXT=True
            if TRANSFORM_TEI_TO_TXT:
                # INLINE_TXT_IN_CSV=True
                INLINE_TXT_IN_CSV = st.checkbox('INLINE_TXT_IN_CSV', True)
            else:
                INLINE_TXT_IN_CSV = False

        # end of form
        submitted = st.form_submit_button('GO TO STEP 3')
    if submitted:
        #mk_list('collection')
        out = {'DTS_URL':st.session_state.url,
                'ROOT_COLLECTION_ID':ROOT_COLLECTION_ID,
               'MAX_DEPTH':MAX_DEPTH,
               'RETRIEVE_FILES':RETRIEVE_FILES,
              'TRANSFORM_TEI_TO_TXT':TRANSFORM_TEI_TO_TXT,
              'TRANSFORM_TEI_TO_HTML':TRANSFORM_TEI_TO_HTML,
               'INLINE_TXT_IN_CSV':INLINE_TXT_IN_CSV}
        st.session_state['2of3'] = out #this is a dictionary

        st.write(out)
        import json




    if out:
        #if st.button('Save JSON'):
         #   json.dump(out, open("filepath", 'w'))

        json_out = json.dumps(out)
        download_csv = st.download_button('DOWNLOAD', json_out, file_name=out_name + '.json', mime=None, key=None, help=None,
                            on_click=st.balloons, args=None, kwargs=None)
        # problem, right now, click on download_out creates a jump back
        #if download_csv: revoir ca

            #save used url in the correct folder
    else:
        st.stop()

def see_saved_urls():
    home = expanduser("~")
    import os
    url_files = os.listdir(r"C:\Users\Audric\Documents\GitHub\DTS2CSV\dts2csv\saved_urls")
    st.write(url_files)


def screen_one():
    screen1_vars()
    #st.write('test5')
    #SB of screen1
    rootUrl = st.session_state.url
    # * make default def_col, def_doc and if changed provide button to change it
    with st.sidebar.expander('+'):
        colls = st.text_input('Collections name:', 'collections')
        doc = st.text_input('Documents name:', 'document')
        navi = st.text_input('Navigation name:', 'navigation')
        COLLECTIONS_URL = rootUrl + colls
        DOCUMENTS_URL = rootUrl + doc
        NAVIGATION_URL = rootUrl + navi  # 3 last are default this way and can be changed in sb
        default_id = str(st.session_state.url)
        DATASET_ID = st.text_input('Dataset ID:', default_id)
        #make split of default id string
    out_name = st.sidebar.text_input('Name of the CSV file: ', 'output')
    st.sidebar.image('logo.png')
    form_screen_one(out_name)

    #

    #
    #END of screen1
    reset_app = st.button('RESET')
    del st.session_state['url']
    #from streamlit import caching
    #caching.clear_cache()
    if reset_app:
        #del st.session_state['url']
        main()

def get_url_input():
    st.header('step 1/3')
    with st.form('url_form'):
        url_input = st.text_input('To start, enter an url: ') #rootUrl
        submit_url = st.form_submit_button('GO TO STEP 2')
        if submit_url:
            st.session_state.url = url_input
    with st.expander('Use stored URLs instead'):
        with st.form('url_form2'):
            #should expand this list
            dts_urls = ['https://texts.alpheios.net/api/dts', 'https://dts.perseids.org/', 'https://betamasaheft.eu/api/dts', 'https://edh-www.adw.uni-heidelberg.de/api/dts/']
            #just to try out
            urls = ['https://streamlit.io/', 'https://scaife.perseus.org/library/'] # instead, have a line of code gather all the urls in the dedicated folder
            url_input2 = st.selectbox('Pick one', dts_urls)
            submit_url2 = st.form_submit_button('GO TO STEP 2')
            if submit_url2:
                st.session_state.url = url_input2
    with st.expander('Help'):
        '*insert small video demo hosted on YT?*'
        'mention streamlit options on the upper right'
    with st.expander('Settings'):
        st.write('manage url list, ...')


# main code
#st.write('test2')
if __name__ == '__main__':
    main()

#////////////////////////////////////////
# END OF CLEAN CODE
st.stop()
#currently up to test5
#only at the end of session remove all tests write

#////////////////////////////////
def use_later_maybe():
    mode = st.sidebar.selectbox('choose a mode:', ['DTS2CSV', 'DTS2PDF', 'Load input file', 'Manual input (main mode)','Settings'])

    # This function is called every time we try to download a TEI file
    # if this function returns False we will skip the file
    # it it returns True we will actually download it.
    #
    # * can this happen elsewhere?
    # if this function is missing, it is assumed to be always True
    def config_filterResource(resourceCsvData, resourceJsonData):
        return True  # retrieve all TEI files
        # return resourceCsvData["language"]=="en" # retrieve only TEI files marked as english language

    # -------------------------------------------

    # CSV ids might have some unicity or syntaxic constraints which can be handled here,
    # to be compatible with Lucene query syntax (used by MetaindeX)
    def config_idDts2idCsv(dtsId, dtsJsonData):
        return dtsId.replace('urn:', '').replace(':', '.').replace('urn.',
                                                                   '')  # the first replace must probably be fixed

    # -------------------------------------------

    # utility function called from DTS/CSV mapping table
    # replace carriage return by "__CR__" string, so that it can stay in a single line in CSV file.
    # this string is typically replaced back to carriage return when importing CSV file into metaindex app:
    # "__CR__" is transcoded to newline by MetaindeX during import
    # "__MX_ESCAPED_SEPARATOR__" is transcoded to ';' by MetaindeX during import
    def normalizeText(text):
        return text.replace("\n", "__CR__").replace("  ", " ").replace(";", "__MX_ESCAPED_SEPARATOR__")

    # -------------------------------------------

    # DTS/CSV mapping table
    # list of DTS 'path' to put into CSV columns
    # at least 'url', 'urn', '@id', 'members' (and 'parent'), and '@type' are generated by default, others shall be listed hereunder

    # ask Laurent about that
    ATTRS_LIST = {
        "Collection": {"totalItems": {"csvName": "nbChildren", "mandatory": True},
                       "title": {"csvName": "title", "mandatory": True, "transform": normalizeText},
                       "dts:extensions/ns2:creator[0]/@value": {"csvName": "author", "mandatory": False},
                       "dts:extensions/ns2:date": {"csvName": "date", "mandatory": False},
                       },

        "Resource": {
            "dts:extensions/ns2:language": {"csvName": "language", "mandatory": True},

        }
    }

# une fois fni premier clean aller regarder code non github et comms

### !!! collaboration to plug in the vue js

