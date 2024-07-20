import streamlit as st
import plotly.express as px


def flavour_intensity_chart(flavour_intensity_dict: dict):
    with st.expander("Flavour Chart", expanded=True):
        fig = px.line_polar(
            r=flavour_intensity_dict.values(),
            theta=flavour_intensity_dict.keys(),
            line_close=True,
        )
        fig.update_traces(fill="toself")
        st.plotly_chart(fig)
