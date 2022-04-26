import streamlit as st
import plotly.graph_objects as go
import numpy as np
from utils.classes import *
from utils.const import *
from utils.functions import *

st.set_page_config(layout=ConstPageConfig.LAYOUT, page_title=ConstPageConfig.TITLE, menu_items=ConstPageConfig.MENU)

# ===== Menu & Title ===== #
maincol1, _, maincol2 = st.columns([1, 3, 1])
with maincol2:
    with st.expander("Menu"):
        page = st.radio(label="Select a page", options=["Overview", "Data"], index=0)

# ===== Pages ===== #

if page == "Data":
    # ===== input data ===== #
    with maincol1:
        st.title("Data")
    st.write(ConstString.SPACE)

elif page == "Overview":

    # ===== Dashboard ===== #
    with maincol1:
        st.title("Overview")
    st.write(ConstString.SPACE)


    # ===== Box current weather ===== #
    with st.expander(label=ConstFrontText.WEATHER, expanded=True):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
        fig = go.Figure()
        fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
        fig.update_layout(
            paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
            plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
            margin=ConstPlotly.LAYOUT_MARGIN
        )
        # TODO : subplots 2 lines 4 cols with plotly image of sun, cloud, rain etc
        st.plotly_chart(fig, use_container_width=True)


    # ===== layout ===== #
    line1_col1, line1_col2, line1_col3 = st.columns([1] * 3)
    st.write(ConstString.SPACE)
    # st.markdown(ConstString.SEPARATOR)
    st.write(ConstString.SPACE)
    line2_col1, line2_col2, line2_col3 = st.columns([1] * 3)


    # ===== Boxes ===== #
    with line1_col1:
        with st.expander(label=ConstFrontText.AIRQUALITY, expanded=True):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
            fig = go.Figure()
            fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
            fig.update_layout(
                paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
                plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
                margin=ConstPlotly.LAYOUT_MARGIN
            )
            st.plotly_chart(fig, use_container_width=True)
            st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")

    with line2_col1:
        with st.expander(label="See explanation", expanded=True):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
            fig = go.Figure()
            fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
            fig.update_layout(
                paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
                plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
                margin=ConstPlotly.LAYOUT_MARGIN
            )
            st.plotly_chart(fig, use_container_width=True)
            st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")

    with line1_col2:
        with st.expander(label=ConstFrontText.AIRQUALITY, expanded=True):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
            fig = go.Figure()
            fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
            fig.update_layout(
                paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
                plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
                margin=ConstPlotly.LAYOUT_MARGIN
            )
            st.plotly_chart(fig, use_container_width=True)
            st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")

    with line2_col2:
        with st.expander(label="See explanation", expanded=True):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
            fig = go.Figure()
            fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
            fig.update_layout(
                paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
                plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
                margin=ConstPlotly.LAYOUT_MARGIN
            )
            st.plotly_chart(fig, use_container_width=True)
            st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")

    with line1_col3:
        with st.expander(label=ConstFrontText.AIRQUALITY, expanded=True):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
            fig = go.Figure()
            fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
            fig.update_layout(
                paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
                plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
                margin=ConstPlotly.LAYOUT_MARGIN
            )
            st.plotly_chart(fig, use_container_width=True)
            st.metric(label="Accurancy", value=-10, delta=10, delta_color="inverse")

    with line2_col3:
        with st.expander(label="See explanation", expanded=True):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
            fig = go.Figure()
            fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
            fig.update_layout(
                paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
                plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
                margin=ConstPlotly.LAYOUT_MARGIN
            )
            st.plotly_chart(fig, use_container_width=True)
            st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")