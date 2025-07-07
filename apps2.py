import streamlit as st

st.title("Hierarchical Data Viewer")
Time = st.time_input("select a time")
st.write("You selected:",Time)

st.header("This is a header")
st.subheader("Second header")
st.caption("code caption")
st.text("This is a Text")
st.markdown("*Bold*")
st.divider()
st.latex("************")

st.error("error")
st.info("info")
st.warning("warning")
st.success("success")

st.balloons()

