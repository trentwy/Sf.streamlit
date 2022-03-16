import folium
import pandas as pd
import geopandas as gpd
import streamlit as st
from streamlit_folium import folium_static



st.set_page_config(layout="centered")

st.markdown("""<style>.big-font {font-size:25px !important;}</style>""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Geography of Median Income & Minority Population</p>', unsafe_allow_html=True)

st.write("This app is designed as a supplement to other data visualization within the teams report and presentation:")

st.write("You are viewing Minority & Income data for San Francisco Census Blocks!")

@st.cache
def load_metadata():
    g_data = 'geo_TNCdata.GeoJSON'
    return gpd.read_file(g_data)

json1 = load_metadata()

json1["GEOID"] = pd.to_numeric(json1['GEOID'],errors = 'coerce')

m = folium.Map(location=[37.78, -122.42], tiles='CartoDB positron',name="Light Map",
           zoom_start=11,
           attr='My Data Attribution')

sf_data = pd.read_csv('DATA.csv')

choice = ['MedIncome', 'p_NonWhite']
choice_selected = st.selectbox("Select Choice ", choice)
folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=sf_data,
    columns=["GEOID_10", choice_selected],
    key_on="feature.properties.GEOID",
    fill_color="YlOrRd",
    fill_opacity=0.5,
    line_opacity=.1,
    legend_name=choice_selected+"(income/percent)",
).add_to(m)


folium_static(m, width=1000, height=700)

st.markdown('<p class="big-font">Geography of Ride-Share Quartile Data & Time Windows</p>', unsafe_allow_html=True)

st.write("You are viewing Ride-Share quartile data for San Francisco's Average Pickups and Dropoffs!")

m = folium.Map(location=[37.78, -122.42], tiles='CartoDB positron',name="Light Map",
           zoom_start=13,
           attr='My Data Attribution')

sf_transport_data = json1

choice = ['am_q', 'pm_q', 'n_q']
choice_selected = st.selectbox("Select Choice ", choice)
folium.Choropleth(
    geo_data=json1,
    name="choropleth",
    data=sf_transport_data,
    columns=["GEOID", choice_selected],
    key_on="feature.properties.GEOID",
    fill_color="YlOrRd",
    fill_opacity=0.5,
    line_opacity=.1,
    legend_name=choice_selected+"(quartile)",
).add_to(m)


folium_static(m, width=1000, height=700)

st.write("Thanks for viewing our data visualization, have a good day!")







