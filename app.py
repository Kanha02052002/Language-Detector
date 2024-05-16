import streamlit as st
import string
import pickle
import webbrowser


global Lrdetect_Model

LrdetectFile=open('model.pckl','rb')
Lrdetect_Model=pickle.load(LrdetectFile)
LrdetectFile.close()

st.title("Language Detector Model")
inputText=st.text_input("Provide your text here")
buttonCheck=st.button("Check the Language name")
if buttonCheck:
    st.text(Lrdetect_Model.predict([inputText]))
