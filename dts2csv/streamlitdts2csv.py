#local import
import dts2csv as d2c
#imports
import streamlit as st
import json
import urllib.request
import requests
import os
from os.path import expanduser
import base64

#def next_button():
 #   if st.button('MOVE TO NEXT STEP'):


def create_download_zip(filename):

    fileBasename=os.path.basename(filename)

    with open(filename, "rb") as f:
        bytes = f.read()
        b64 = base64.b64encode(bytes).decode()
        href = f'<a href="data:file/zip;base64,{b64}" download="'+fileBasename+'" >Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

def home():
    st.title('I. URL')
    st.write('--------------------')
    st.header('A. URL Input')
    
    cola, colb = st.columns(2)
    with cola:

        with st.form('url_form'):
            url_input = st.text_input('To start, enter an url: ') #rootUrl
            submit_url = st.form_submit_button('SUBMIT URL')
            if submit_url:
                check_url(url_input)
                st.session_state.url = url_input

    with colb:
        with st.expander('Use stored URLs instead'):
            with st.form('url_form2'):
                # * should expand this list
                dts_urls = ['https://texts.alpheios.net/api/dts', 'https://dts.perseids.org/', 'https://betamasaheft.eu/api/dts', 'https://edh-www.adw.uni-heidelberg.de/api/dts/']
                #just to try out
                urls = ['https://streamlit.io/', 'https://scaife.perseus.org/library/'] # instead, have a line of code gather all the urls in the dedicated folder
                url_input2 = st.selectbox('Pick one', dts_urls)
                submit_url2 = st.form_submit_button('SUBMIT URL')
                if submit_url2:
                    check_url(url_input2)
                    st.session_state.url = url_input2


    st.subheader('B. JSON CONFIG FILE (for advanced users)')
    st.info('ROADMAP FEATURE ONLY!')
    with st.expander('+'):
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            dummy()


    with st.expander('Help'):
        st.write('Unsure how to use this webapp? Click on VI. Settings/Help in the sidebar to your left')

def init_session_state():
    if 'mode' not in st.session_state:
        st.session_state.mode = 'I. URL'
    if 'url' not in st.session_state:
        st.session_state.url = ''
    if 'step2_output' not in st.session_state:
        st.session_state.step2_output = []
    if 'collections' not in st.session_state:
        st.session_state.collections = []
    if 'resources' not in st.session_state:
        st.session_state.resources = []

def opening_style():
    col1, col2 = st.columns(2)
    col1.title(' Welcome to DTS2CSV!')
    col1.write('Hackathon Version, October 2021, Ver. 3.2 (1.0)')
    col2.image('https://raw.githubusercontent.com/AudricWannaz/DTS2CSV/main/dts2csv/logo.png')
    st.header('convert any DTS data in a CSV within seconds')
    # *want more?

def see_saved_urls(): # this function shall create a list of urls in folder and in cache/session_state? 
    home = expanduser("~")
    url_files = os.listdir(r"C:\Users\Audric\Documents\GitHub\DTS2CSV\dts2csv\saved_urls")
    #st.write(url_files)
    #!!! still some work to do here

def set_vars(): # we can use this function to declare variables that we ont change in this script
    maison = expanduser("~")
    SAXON_JAR_PATH=maison+"/dev/tei/install/SaxonHE10-5J/saxon-he-10.5.jar"
    TEI_XSL_STYLESHEETS_PATH = maison + "/dev/tei/install/tei-xsl"
    #see_saved_urls()

def sidebar():

    sb_mode = st.sidebar.selectbox('Navigate by clicking', ['I.URL', 'II.Parameters', 'III.Collections', 'IV.Resources', 'V.Download CSV', 'VI.Settings/Help'])
    st.session_state.mode = sb_mode

    st.sidebar.write('*')
    with st.sidebar.expander(f'Session state upon entry ({st.session_state.mode})'):

        st.write('url')
        st.write(st.session_state.url)
        st.write('step2_output')
        st.write(st.session_state.step2_output)
        st.write('collections')
        st.write(st.session_state.collections)
        st.write('resources')
        st.write(st.session_state.resources)
    st.sidebar.write('Progress:')
    if st.session_state.mode == 'I.URL':
        st.sidebar.progress(20)
    elif st.session_state.mode == 'II.Parameters':
        st.sidebar.progress(40)
    elif st.session_state.mode == 'III.Collections':
        st.sidebar.progress(60)
    elif st.session_state.mode == 'IV.Resources':
        st.sidebar.progress(80)
    elif st.session_state.mode == 'V.Download CSV':
        st.sidebar.progress(100)

def url_sine_qua_non():
    if st.session_state.url == '':
        st.warning('You have not entered an URL yet. Please go to I. URL using the sidebar')
        closing_style()
        st.stop()
    else:
        pass

def params():

    url_sine_qua_non()
    st.title('II. Parameters')
    st.write('-----------------')
    col_1, col_2 = st.columns(2)
    with col_1:
        screen_one()
    #col_2.write(stuff)
    with col_2:
        st.write('-----------------------------')
        st.subheader('JSON VIEWER')
        #st.write(stuff)
        json_viewer(st.session_state.json_url)

def json_viewer(a_json):
    st.write(a_json)

def mk_list(name):
    url_sine_qua_non()
    st.title(f'Describe the {name}')

    dicts_num = st.slider('How many parameters do you need?', 0, 10, 1)

    with st.form('mk_list'):
        for i in range(dicts_num):
            st.write('Enter')
            a = st.text_input('dts_id?', key=i)
            b = st.text_input('csv_name?', key=i)
            st.session_state[f'test{i}'] = {'dts_id': a, 'csv_name': b}
        submit = st.form_submit_button(f'submit {name}')
        if submit:
            #! change stuff here
            st.session_state[f'{name}'] = [st.session_state[f'test{i}'] for i in range(dicts_num)]
            st.success(f'{name} updated')

def extras():
    st.title('SETTINGS')

    with st.expander('Streamlit Settings'):
        st.write('This app is powered by Streamlit. This means you can access native Streamlit visual settings by clicking the top right corner of your screen.')
    with st.expander('Advanced Settings'):
    #with st.expander('Manage stored URLS'):
        st.write('ROADMAP FEATURE')
    with st.expander('Personalise Graphics'):
        st.write('ROADMAP FEATURE')
        st.write('wow such empty')    

    st.write('*')

    st.title('HELP')
    with st.expander('What is DTS?'):
        st.write('DTS is')
    with st.expander('Why should I convert DTS to CSV?'):
        st.write('The CSV format...')
    with st.expander('Can I use this tool from the terminal?'):
        st.write('Yes! Go to ...')

    st.title('ROADMAP')
    with st.expander('see roadmap'):
        roadmap_list = ['json input jumps from step I. to step V.','"next" and "reset" button at each screen', 'more complex json viewer', 'more help infos', 'better collections/resources input UI', 'user can change widget values in settings', 'dts2pdf collaboration', 'screencast tutorial']
        st.write(roadmap_list)

def closing_style():
    st.image('https://raw.githubusercontent.com/AudricWannaz/DTS2CSV/main/dts2csv/logo.png')
    #add collapser bar
    with st.expander('CREDITS'):
        about()
        dts_info = '''This version of DTS2CSV was produced during the 2021 DTS Hackathon
        \n(https://distributed-text-services.github.io/workshops/events/2021-hackathon/).

        '''
        st.write(dts_info)

def about():

    infos ='''DTS2CSV is also a part of the MetaindeX Toolbox: https://metaindex.fr/webapp/toolbox
    \nAuthors: Laurent ML (backend), Audric Wannaz (GUI) 2021
     
     
    License: GNU GENERAL PUBLIC LICENSE
    Version 3.2 (Streamlit Version 1.0), 8th October 2021
     
    Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
     
    See full version of LICENSE in <https://fsf.org/>

    If you use this tool please be fair and cite it, if possible as follows:
    DTS2CSV 3.2 (Streamlit Version 1.0), Laurent ML and Audric Wannaz, https://github.com/AudricWannaz/DTS2CSV

    '''
    st.write(infos)

def end_screen():
    st.header('READY TO GENERATE THE CSV')    


    st.title('&#8595')
    #find better arrows at https://unicode-table.com/en/sets/arrow-symbols/
    maison = expanduser("~")
    SAXON_JAR_PATH=maison+"/dev/tei/install/SaxonHE10-5J/saxon-he-10.5.jar"
    TEI_XSL_STYLESHEETS_PATH = maison + "/dev/tei/install/tei-xsl"
    if st.button('EXTRACT CSV'):
       #set_vars()
        # what is optional
        json_output = {
    "SAXON_JAR_PATH":SAXON_JAR_PATH,
    "TEI_XSL_STYLESHEETS_PATH":TEI_XSL_STYLESHEETS_PATH,
    "DTS_URL":st.session_state.url+'/',
    "DTS_COLLECTIONS_ENTRYPOINT":"collections", #handled in settings/sidebar?
    "DTS_DOCUMENTS_ENTRYPOINT":"document", #handled in settings/sidebar?
    "START_COLLECTION_ID": st.session_state.step2_output["ROOT_COLLECTION_ID"],
    "MAX_DEPTH":st.session_state.step2_output["MAX_DEPTH"],
    "RETRIEVE_FILES":st.session_state.step2_output["RETRIEVE_FILES"],
    "TRANSFORM_TEI_TO_TXT":st.session_state.step2_output["TRANSFORM_TEI_TO_TXT"],
    "TRANSFORM_TEI_TO_HTML":st.session_state.step2_output["TRANSFORM_TEI_TO_HTML"],
    "INLINE_TXT_IN_CSV":st.session_state.step2_output["INLINE_TXT_IN_CSV"],
    "COLLECTIONS": st.session_state.collections,
    "RESOURCES": st.session_state.resources
    }
        
        st.write(json_output)
        try:
            with st.spinner('EXTRACTING ... This might take some time, depending on target size'):
                extracted = d2c.extract_all(json_output, True)
                create_download_zip(extracted)
                #st.write(extracted)
                #st.write(type(extracted))
                #with st.download_button('DOWNLOAD EXTRACTED CSV',extracted, file_name='output', mime=None, key=None, help=None,
                #        on_click=st.balloons, args=None, kwargs=None):
                #    #st.balloons()
                #    st.success('DTS SUCCESSFULLY DOWNLOADED AS CSV')
                    
            st.success('CSV successfully extracted!')
        except Exception as e:            
            st.info('Sorry, the web version does not fully work yet! To run this app locally, download the Github repo, install Streamlit with pip install streamlit and run "streamlit run streamlitdtscsv.py" in a terminal in the dtscsv folder. Alternatively, use the tool from the terminal as specified in the docs')
            st.error("Error while extracting contents: "+str(e))
        

    st.title('&#8593')

    with st.expander('more'):
        if st.button('export json config file'):
            st.write('little bam')

    if st.button('RESET APP'):
        st.info('ROADMAP FEATURE')
    

def mode_director():
    if st.session_state.mode == 'I.URL':
        home()
    elif st.session_state.mode == 'II.Parameters':
        params()
    elif st.session_state.mode == 'III.Collections':
        mk_list('collections')
    elif st.session_state.mode == 'IV.Resources':
        mk_list('resources')
    elif st.session_state.mode == 'V.Download CSV':
        end_screen()
    else:
        extras()

def check_url(to_check): #if no url in session states, launches start screen, else passes
    try:
        
        with urllib.request.urlopen(to_check) as url:
            st.session_state.json_url = json.loads(url.read().decode())
        
        st.success('URL saved in session')
        #st.write(st.session_state.json_url)
        
        #response = requests.get(st.session_state.url)
        #if response.status_code == 200:
         #st.success('This URL seems valid! You can now select how you want to build your CSV with the modes II-IV or'
                       #' jump directly to the Download menu V')
        #else:
         #   st.error('Web site does not exist')
    except:
        st.error('Not a valid URL. Please try again')

def form_screen_one():
    rootUrl = st.session_state.url
    out = False
    with st.form('main_form'):
        st.subheader('Explore target API and select parameters')
        out_name = st.text_input('Name of the CSV file: ', 'output')
        with st.expander('Collections and Documents'):
            colls = st.text_input('Collections name:', 'collections')
            doc = st.text_input('Documents name:', 'document')
            #navi = st.text_input('Navigation name:', 'navigation')
            COLLECTIONS_URL = rootUrl + colls
            DOCUMENTS_URL = rootUrl + doc
            #NAVIGATION_URL = rootUrl + navi  # 3 last are default this way and can be changed in sb
            default_id = str(st.session_state.url)
            #DATASET_ID = st.text_input('Dataset ID:', default_id)
            #make split of default id string
    
        with st.expander('Advanced'):

        # where to start from
            ROOT_COLLECTION_ID = st.text_input('Enter a valid collection ID', 'default')

            # where to store generated files
            # TARGET_PATH=home+st.text_input('Enter a valid PATH') # update this with better st features> at best not used, downloads is ok

            # set to None for no max depth
            depths = [None, 1, 2, 3, 'custom']  # where should it stop?
            if depths == 'custom':
                depths2 = st.slider('Pick a value', 4, 10)

            MAX_DEPTH = st.selectbox('Choose Depth (None=max)', depths)

            # set True to download TEI files
            # RETRIEVE_FILES=True

            
            
            RETRIEVE_FILES = st.checkbox('RETRIEVE_FILES', True)

            # Transorm TEI into Text and HTML requires SAXON and TEI-XSL
            # TRANSFORM_TEI_TO_TXT=True
            # TRANSFORM_TEI_TO_HTML=True

            TRANSFORM_TEI_TO_TXT = st.checkbox('TRANSFORM_TEI_TO_TXT', False)
            TRANSFORM_TEI_TO_HTML = st.checkbox('TRANSFORM_TEI_TO_HTML', False)
            # if true, put TEI plain text contents into (resources) CSV file
            # This option needs TRANSFORM_TEI_TO_TXT=True
            if TRANSFORM_TEI_TO_TXT:
                # INLINE_TXT_IN_CSV=True
                INLINE_TXT_IN_CSV = st.checkbox('INLINE_TXT_IN_CSV', True)
            else:
                INLINE_TXT_IN_CSV = False

            # end of form
        submitted = st.form_submit_button('Submit Collections')
        if submitted:

            st.session_state.step2_output = {
                    'DTS_COLLECTIONS_ENTRYPOINT':'collections',
                    'DTS_RESOURCES_ENTRYPOINT':'document', #where put option to change it
                    'DTS_URL':st.session_state.url,
                    'ROOT_COLLECTION_ID':ROOT_COLLECTION_ID,
                   'MAX_DEPTH':MAX_DEPTH,
                   'RETRIEVE_FILES':RETRIEVE_FILES,
                  'TRANSFORM_TEI_TO_TXT':TRANSFORM_TEI_TO_TXT,
                  'TRANSFORM_TEI_TO_HTML':TRANSFORM_TEI_TO_HTML,
                   'INLINE_TXT_IN_CSV':INLINE_TXT_IN_CSV}

def screen_one():
    set_vars()
    rootUrl = st.session_state.url
    # * make default def_col, def_doc and if changed provide button to change it
    
    
    form_screen_one()

    #

    #
    #END of screen1
    #reset_app = st.button('RESET')
    #del st.session_state['url']
    #from streamlit import caching
    #caching.clear_cache()
    #if reset_app:
        #del st.session_state['url']
     #   main()

def main():
    
    opening_style()
    init_session_state()
    sidebar()
    mode_director()
    closing_style()

if __name__ == '__main__':
    main()


#&&&&&&&&&&&&& UNUSED &&&&&&&&&&&&&&&&&&&&&&&&
def sendJSON_button(pre_json):
    json_out = json.dumps(pre_json)
    download_csv = st.download_button('DOWNLOAD', json_out, file_name=out_name + '.json', mime=None, key=None, help=None,
                        on_click=st.balloons, args=None, kwargs=None)   

