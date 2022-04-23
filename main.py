import streamlit as st
from utils.classes import *
from utils.const import *
from utils.functions import *

st.set_page_config(layout="wide", page_title="My app", menu_items={
    'About': "My app made with love"
})

st.title("Overview")
st.write("##")

_, c1, c2, c3, c4 = st.columns((0.55, 1, 1, 1, 1))

with c1:
    st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")
with c2:
    st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")
with c3:
    st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")
with c4:
    st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")
