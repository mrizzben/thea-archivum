import streamlit as st
import plotly.express as px

if st.session_state.submission:
    submissions = st.session_state.submission
    keys = submissions.keys()
    submission_name = st.selectbox("Which score sheet you would like to view?", keys)
    data = submissions[submission_name]
    with st.expander("Flavour Chart", expanded=True):
        flavourwhl = data["flavourwhl"]
        fig = px.line_polar(
            r=flavourwhl.values(),
            theta=flavourwhl.keys(),
            line_close=True,
        )
        fig.update_traces(fill="toself")
        st.plotly_chart(fig)
    st.dataframe(data["scoresheet"])

else:
    st.info("You've not filled any score sheet yet!")
