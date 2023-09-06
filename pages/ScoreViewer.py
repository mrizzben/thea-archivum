import streamlit as st

keys = [x for x in st.session_state.keys() if isinstance(x, str)]
if keys:
    scoresheet = st.selectbox(
        "Which score sheet you would like to view?", st.session_state.keys()
    )
    st.dataframe(st.session_state[scoresheet])

else:
    st.info("You've not filled any score sheet yet!")
