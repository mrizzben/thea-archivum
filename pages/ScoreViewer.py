import streamlit as st

if st.session_state:
    scoresheet = st.selectbox(
        "Which score sheet you would like to view?", st.session_state.keys()
    )
    st.dataframe(st.session_state[scoresheet])
