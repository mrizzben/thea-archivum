import streamlit as st
import plotly.express as px

keys = [
    x for x in st.session_state.keys() if isinstance(x, str) and "_flavours" not in x
]
if keys:
    scoresheet = st.selectbox("Which score sheet you would like to view?", keys)
    with st.expander("Flavour Chart", expanded=True):
        fig = px.line_polar(
            r=st.session_state[scoresheet + "_flavours"].values(),
            theta=st.session_state[scoresheet + "_flavours"].keys(),
            line_close=True,
        )
        fig.update_traces(fill="toself")
        st.plotly_chart(fig)
    st.dataframe(st.session_state[scoresheet])

else:
    st.info("You've not filled any score sheet yet!")
