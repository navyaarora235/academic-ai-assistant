import streamlit as st
import requests


st.set_page_config(page_title="Academic AI Assistant", page_icon="🎓")
st.title("🎓 Academic AI Assistant")
st.subheader("Query your academic documents with Gemini 2.5-Flash")

API_URL = st.sidebar.text_input("Backend API URL", value="http://127.0.0.1:8000")

uploaded_file = st.file_uploader("Upload an Academic PDF", type=["pdf"])

query = st.text_input("Ask a question about the document:")

if st.button("Submit Query"):
    if uploaded_file is not None and query:
        with st.spinner("Extracting text and querying Gemini..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                data = {"question": query}
                
                response = requests.post(f"{API_URL}/query-pdf", files=files, data=data)
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("Analysis Complete!")
                    st.markdown("### Answer:")
                    st.write(result.get("answer", "No answer found."))
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to backend service: {e}")
    else:
        st.warning("Please upload a PDF and type a question first.")
