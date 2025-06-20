import streamlit as st
from streamlit.runtime.state import session_state
import utils


st.set_page_config(page_title="ChatBot Básico" ,page_icon='🤖' ,layout="wide")

st.title("ChatBot Básico 166")

#historial
if "history" not in st.session_state:
    st.session_state.history = []

#contexto
if "contex" not in st.session_state:
    st.session_state.contex = []

#construimos el espacio, emisor-mesaje
for sender, msg in st.session_state.history:
    if sender == "Tú":
        st.markdown(f'**😊☁ {sender}:**{msg}')   
    else:
        st.markdown(f'**🤖{sender}:**{msg}') 

#sino hay entrada
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

#procesamiento de la entrada
def send_msg():
    user_input = st.session_state.user_input.strip()
    if user_input:
        tag = utils.predict_class(user_input)
        st.session_state.contex.append(tag)
        response = utils.get_response(tag,st.session_state.contex)
        st.session_state.history.append(('Tú',user_input))
        st.session_state.history.append(('Bot',response))
        st.session_state.user_input = ""

#creamos el campo de texto
st.text_input("Escribe tu mensaje:", key = "user_input", on_change=send_msg)

