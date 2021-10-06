# questions to Laurent are noted with *

#MAIN QUESTIONS:
# * is there merit to keep track of both step and mode, or should only mode be used?
# * reset button everywhere
# * json viewer next to 3 and 4 not only 2

#imports
import streamlit as st
import os
from os.path import expanduser


def home():
    st.header('I. URL')
    with st.form('url_form'):
        url_input = st.text_input('To start, enter an url: ') #rootUrl
        submit_url = st.form_submit_button('II. Parameters')
        if submit_url:
            st.session_state.url = url_input
            st.session_state.mode = 'II. Parameters'
         

    with st.expander('Use stored URLs instead'):
        with st.form('url_form2'):
            # * should expand this list
            dts_urls = ['https://texts.alpheios.net/api/dts', 'https://dts.perseids.org/', 'https://betamasaheft.eu/api/dts', 'https://edh-www.adw.uni-heidelberg.de/api/dts/']
            #just to try out
            urls = ['https://streamlit.io/', 'https://scaife.perseus.org/library/'] # instead, have a line of code gather all the urls in the dedicated folder
            url_input2 = st.selectbox('Pick one', dts_urls)
            submit_url2 = st.form_submit_button('II. Parameters')
            if submit_url2:
                st.session_state.url = url_input2
                st.session_state.mode = 'II. Parameters'
    


    with st.expander('Help'):
        st.write('Unsure how to use this webapp? Click on VI. Settings/Help in the sidebar to your left')
    with st.expander('Settings'):
        st.write('manage url list, ...')


def init_session_state():
    if 'mode' not in st.session_state:
        st.session_state.mode = 'I. URL'
    if 'url' not in st.session_state:
        st.session_state.url = ''
    if 'step2_output' not in st.session_state:
        st.session_state.step2_output = []
    if 'collections' not in st.session_state:
        st.session_state.collections = []
    if 'ressources' not in st.session_state:
        st.session_state.ressources = []


def opening_style():
    col1, col2 = st.columns(2)
    col1.title(' Welcome to DTS2CSV!')
    col1.write('Hackathon Version, October 2021, Ver. 1.0')
    col2.image('logo.png')
    st.header('convert any DTS data in a CSV within seconds')
    # *want more?

def see_saved_urls(): # this function shall create a list of urls in folder and in cache/session_state? 
    home = expanduser("~")
    url_files = os.listdir(r"C:\Users\Audric\Documents\GitHub\DTS2CSV\dts2csv\saved_urls")
    #st.write(url_files)
    #!!! still some work to do here

def set_vars(): # we can use this function to declare variables that we ont change in this script
    home = expanduser("~")
    SAXON_JAR_PATH=home+"/dev/tei/install/SaxonHE10-5J/saxon-he-10.5.jar"
    TEI_XSL_STYLESHEETS_PATH = home + "/dev/tei/install/tei-xsl"
    #see_saved_urls()

def sidebar():

    sb_mode = st.sidebar.selectbox('Navigate by clicking', ['I. URL', 'II. Parameters', 'III.Collections', 'IV.Ressources', 'V. Download CSV', 'VI. Settings/Help'])
    st.session_state.mode = sb_mode

    st.sidebar.write('*')
    st.sidebar.write('Current mode:')
    st.sidebar.write(st.session_state.mode)
    st.sidebar.write('url')
    st.sidebar.write(st.session_state.url)
    st.sidebar.write('step2_output')
    st.sidebar.write(st.session_state.step2_output)
    st.sidebar.write('collections')
    st.sidebar.write(st.session_state.collections)
    st.sidebar.write('ressources')
    st.sidebar.write(st.session_state.ressources)
    st.sidebar.write('Progress:')
    if st.session_state.mode == 'I. URL':
        st.sidebar.progress(20)
    elif st.session_state.mode == 'II. Parameters':
        st.sidebar.progress(40)
    elif st.session_state.mode == 'III.Collections':
        st.sidebar.progress(60)
    elif st.session_state.mode == 'IV.Ressources':
        st.sidebar.progress(80)
    elif st.session_state.mode == 'V. Download CSV':
        st.sidebar.progress(100)


stuff = [[1,2,3],[3,2,3]]
def params():
    col_1, col_2 = st.columns(2)
    with col_1:
        screen_one()
    #col_2.write(stuff)
    with col_2:
        st.write('Here comes The JSON to view')
        #st.write(stuff)
        json_viewer(stuff)



def json_viewer(a_json):
    st.write(a_json)


def mk_list(name):
    st.title(f'Describe the {name}')

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
            st.session_state[f'{name}'] = [st.session_state[f'test{i}'] for i in range(dicts_num)]
            st.write('*')
            st.write('collections')
            st.write(st.session_state.collections)
            st.write('ressources')
            st.write(st.session_state.ressources)

def extras():
    st.title('SETTINGS')

    with st.expander('Streamlit Settings'):
        st.write('This app is powered by Streamlit. This means you can access native Streamlit visual settings by clicking the top right corner of your screen.')
    with st.expander('Advanced Settings'):
    #with st.expander('Manage stored URLS'):
        st.write('porbably roadmap only')
    with st.expander('Personalise Graphics'):
        st.write('porbably roadmap only')
        st.write('wow such empty')    

    st.write('*')

    st.title('HELP')
    with st.expander('What is DTS?'):
        st.write('DTS is')
    with st.expander('Why should I convert DTS to CSV?'):
        st.write('The CSV format...')
    with st.expander('Can I use this tool from the terminal?'):
        st.write('Yes! Go to ...')


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

#def home():
#    st.write('home')

def end_screen():
    st.header('READY TO GENERATE THE CSV')


    st.title('&#8595')
    if st.button('DOWNLOAD CSV'):
        st.write('boum')
    st.title('&#8593')

    with st.expander('more'):
        if st.button('export json config file'):
            st.write('little bam')

    if st.button('RESET APP'):
        st.write('bim')
    #download_csv_button
    #save_config
    #restart
    st.write('last screen')


# after app works we can add if session_state.step != x then print warning or stuff
def step_redirector():
    if  st.session_state.step == 1:
        st.session_state.mode = 'I. URL'
        home()
    elif st.session_state.step == 2:
        st.session_state.mode = 'II. Parameters'
        params()
    elif st.session_state.step == 3:
        st.session_state.mode = 'III.Collections'
        mk_list('collections')
    elif st.session_state.step == 4:
        st.session_state.mode = 'IV.Ressources'
        mk_list('ressources')
    elif st.session_state.step == 5:
        end_screen()


def mode_director():
    if st.session_state.mode == 'I. URL':
        home()
    elif st.session_state.mode == 'II. Parameters':
        params()
    elif st.session_state.mode == 'III.Collections':
        mk_list('collections')
    elif st.session_state.mode == 'IV.Ressources':
        mk_list('ressources')
    elif st.session_state.mode == 'V. Download CSV':
        end_screen()
    else:
        extras()



def main():
    opening_style()
    #set_vars()>instead only call in functions that need them
    init_session_state()
    sidebar()
    
    mode_director()
    closing_style()

    


#task: finish in one way the pipe home>params>mkcol>mkres>finish 

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



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

#this is old main

    #check_url()
    #st.session_state.state == 2
    #screen_one()
    #st.session_state.state == 3
    #mk_list('collection')


def form_screen_one(out_name):
    out = False
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
        #st.stop()
        st.write('--------------------')

def screen_one():
    set_vars()
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



if __name__ == '__main__':
    main()

#////////////////////////////////////////
# lets see if needed: > bon garde-fou


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

