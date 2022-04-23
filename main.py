import streamlit as st
from utils.classes import *
from utils.const import *
from utils.functions import *

st.set_page_config(layout="wide", page_title="My app", menu_items={
    'About': "My app made with love"
})

st.title("Overview")
st.write("##")

line1_col1, line1_col2, line1_col3, line1_col4 = st.columns((1, 1, 1, 1))
st.write("##")
st.markdown("---")
st.write("##")
line2_col1, line2_col2, line2_col3, line2_col4 = st.columns((1, 1, 1, 1))

with line1_col1:
    with st.expander(label="See explanation", expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")

with line2_col1:
    with st.expander(label="See explanation", expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")

with line1_col2:
    with st.expander(label="See explanation", expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")

with line2_col2:
    with st.expander(label="See explanation", expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")

with line1_col3:
    with st.expander(label="See explanation", expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")

with line2_col3:
    with st.expander(label="See explanation", expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")

with line1_col4:
    with st.expander(label="See explanation", expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")

with line2_col4:
    with st.expander(label="See explanation", expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")
