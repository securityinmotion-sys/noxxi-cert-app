import streamlit as st

st.set_page_config(page_title="NoxxiCert", layout="wide")
st.title("NoxxiCert")
st.subheader("AI ISO 27001 & GDPR Generator by cybernoxxi")

if st.button("Generate Full Compliance Pack"):
    with st.spinner("Creating your policies..."):
        st.success("Complete pack ready!")
        st.balloons()
        st.download_button("Download NoxxiCert Pack", "Your ISO & GDPR files here", "noxxicert_pack.zip")
