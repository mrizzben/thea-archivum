import streamlit as st

if isinstance(st.session_state.keys(), str):
    keys = [x for x in st.session_state.keys() if isinstance(x, str)]
    scoresheet = st.selectbox(
        "Which score sheet you would like to view?", st.session_state.keys()
    )
    st.dataframe(st.session_state[scoresheet])
