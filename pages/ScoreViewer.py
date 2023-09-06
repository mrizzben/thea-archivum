import streamlit as st
import plotly.express as px

if st.session_state.keys():
    keys = [x for x in st.session_state.keys() if isinstance(x, str)]
    if keys:
        scoresheet = st.selectbox(
            "Which score sheet you would like to view?",
            [x for x in keys if "_flavours" not in x],
        )
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
