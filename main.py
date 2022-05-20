from utils.classes import *


st.set_page_config(layout=ConstPageConfig.LAYOUT, page_title=ConstPageConfig.TITLE, menu_items=ConstPageConfig.MENU)

# ===== Update json data if necessary ===== #
set_current_airQuality()
set_xhours_airQuality_forecast()
set_last_24hours_airQuality_history()

# ===== Menu & Title ===== #
maincol1, _, maincol2 = st.columns([1, 5, 1])
with maincol2:
    st.title(get_current_airQuality_json()["city_name"])

# ===== Header ===== #
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
        margin=ConstPlotly.LAYOUT_MARGIN,
        height=ConstPlotly.HEIGHT
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
        st.subheader("""
            Air quality index
        """)
        st.caption("This index is between 0 and 500, where 0 corresponds to a pure air")
        fig = go.Figure()
        fig.add_scatter(
            x=[datetime.strptime(get_history_airQuality_json()["data"][i]["timestamp_local"], "%Y-%m-%dT%H:%M:%S") for i
               in range(72)],
            y=[get_history_airQuality_json()["data"][j]["aqi"] for j in range(72)])
        fig.update_layout(
            paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
            plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
            margin=ConstPlotly.LAYOUT_MARGIN,
            height=ConstPlotly.HEIGHT
        )
        st.plotly_chart(fig, use_container_width=True)
        st.metric(label="3 day variation",
                  value=int(get_current_airQuality_json()['data'][0]['aqi']),
                  delta=get_history_airQuality_json()["data"][0]["aqi"]-get_history_airQuality_json()["data"][71]["aqi"],
                  delta_color="inverse")

with line1_col2:
    with st.expander(label=ConstFrontText.AIRQUALITY, expanded=True):
        st.subheader("""
                    Particle concentration < 2.5 microns
                """)
        st.caption("Values in µg/m³")
        fig = go.Figure()
        fig.add_scatter(
            x=[datetime.strptime(get_history_airQuality_json()["data"][i]["timestamp_local"], "%Y-%m-%dT%H:%M:%S") for i
               in range(72)],
            y=[get_history_airQuality_json()["data"][j]["pm25"] for j in range(72)])
        fig.update_layout(
            paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
            plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
            margin=ConstPlotly.LAYOUT_MARGIN,
            height=ConstPlotly.HEIGHT
        )
        st.plotly_chart(fig, use_container_width=True)
        st.metric(label="3 day variation",
                  value=f"{round(get_current_airQuality_json()['data'][0]['pm25'], 2)} µg/m³",
                  delta=round(get_history_airQuality_json()["data"][0]["pm25"]-get_history_airQuality_json()["data"][71]["pm25"], 3),
                  delta_color="inverse")

with line1_col3:
    with st.expander(label=ConstFrontText.AIRQUALITY, expanded=True):
        st.subheader("""
            Concentration of carbon monoxide
        """)
        st.caption("Values in µg/m³")
        fig = go.Figure()
        fig.add_scatter(
            x=[datetime.strptime(get_history_airQuality_json()["data"][i]["timestamp_local"], "%Y-%m-%dT%H:%M:%S") for i
               in range(72)],
            y=[get_history_airQuality_json()["data"][j]["co"] for j in range(72)])
        fig.update_layout(
            paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
            plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
            margin=ConstPlotly.LAYOUT_MARGIN,
            height=ConstPlotly.HEIGHT
        )
        st.plotly_chart(fig, use_container_width=True)
        st.metric(label="3 day variation",
                  value=f"{round(get_current_airQuality_json()['data'][0]['co'], 2)} µg/m³",
                  delta=round(get_history_airQuality_json()["data"][0]["co"] - get_history_airQuality_json()["data"][71][
                      "co"], 3),
                  delta_color="inverse")

with line2_col1:
    with st.expander(label="See explanation", expanded=True):
        st.subheader("""
                    Blabla
                """)
        st.caption("blabla")
        fig = go.Figure()
        fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
        fig.update_layout(
            paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
            plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
            margin=ConstPlotly.LAYOUT_MARGIN,
            height=ConstPlotly.HEIGHT
        )
        st.plotly_chart(fig, use_container_width=True)
        st.metric(label="Accurancy", value=0, delta=-9, delta_color="inverse")

with line2_col2:
    with st.expander(label="See explanation", expanded=True):
        st.subheader("""
                    Blabla
                """)
        st.caption("blabla")
        fig = go.Figure()
        fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
        fig.update_layout(
            paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
            plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
            margin=ConstPlotly.LAYOUT_MARGIN,
            height=ConstPlotly.HEIGHT
        )
        st.plotly_chart(fig, use_container_width=True)
        st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")

with line2_col3:
    with st.expander(label="See explanation", expanded=True):
        st.subheader("""
                    Blabla
                """)
        st.caption("blabla")
        fig = go.Figure()
        fig.add_scatter(x=np.linspace(-10, 10, 1000), y=np.sin(np.linspace(-10, 10, 1000)))
        fig.update_layout(
            paper_bgcolor=ConstPlotly.PAPER_BGCOLOR,
            plot_bgcolor=ConstPlotly.PLOT_BGCOLOR,
            margin=ConstPlotly.LAYOUT_MARGIN,
            height=ConstPlotly.HEIGHT
        )
        st.plotly_chart(fig, use_container_width=True)
        st.metric(label="Accurancy", value=98, delta=-9, delta_color="inverse")
