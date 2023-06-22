import math
import streamlit as st

st.set_page_config(layout="wide")

st.title('Flight Line Spacing Calculator')

st.sidebar.image('./logo.png', width = 260)
st.sidebar.markdown('#')
st.sidebar.write('This application determines the flight line spacing for a given Wingtra payload.')
st.sidebar.write('Please note that values computed by the application are approximations under ideal conditions. Expect some deviation in actual flight.')
st.sidebar.write('If you have any questions regarding the application, please contact us at support@wingtra.com.')
st.sidebar.markdown('#')
st.sidebar.info('This is a prototype application. Wingtra AG does not guarantee correct functionality. Use with discretion.')

camera = {'RGB61': {'f': 24, 'w': 35.7, 'h': 23.9},
          'RX1': {'f': 32.6, 'w': 35, 'h': 23.3},
          'a6100 Nadir': {'f': 20, 'w': 23.5, 'h': 15.6},
          'a6100 Oblique': {'f': 12, 'w': 23.5, 'h': 15.6},
          'Micasense RedEdge-P': {'f': 10.3, 'w': 8.5, 'h': 7.1}}

choice = st.selectbox('📷 Select Payload Used :',
                      ('[Payload]', 
                       'RGB61', 
                       'RX1', 
                       'a6100 Nadir', 
                       'a6100 Oblique', 
                       'Micasense RedEdge-P'))

h = st.number_input('🛫 Height Above Ground (meters)')
ovr = st.number_input('⏹️ Side Overlap (%)')/100

if choice == '[Payload]':
    st.stop()

else:
    f = camera[choice]["f"]
    w = camera[choice]["w"]
    
    fov = 2*math.atan(w/(2*f))
    d = 2*h*math.tan(fov/2)
    
    s = (1-ovr)*d

if h == 0 or ovr == 0:
    st.stop()
else:
    if st.button('Compute Flight Line Spacing'):
        st.text(f'Line spacing for the mission is {round(s,2):.2f} meters.')
