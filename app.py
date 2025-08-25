import streamlit as st
import requests

# --- page config ---
st.set_page_config(
    page_title="Financial Doc Assistant",
    layout="wide"
)
st.title("Banky The Finance Doc Assistant")

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "assistant", "content": "Hi! Upload all those docs so I can start helping you :D"}]

with st.sidebar:
    st.header("Upload Doc")
    # TODO: add extra documents functionality
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if st.button("Process Documents"):
        if uploaded_file is not None:
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
            try:
                with st.spinner("Processing documents..."):
                    response = requests.post("http://localhost:8000/upload/", files=files)
                    if response.status_code == 200:
                        st.success("Documents processed successfully YAY!")
                    else:
                        st.error(f"Error: {response.json().get('error', 'Unknown error')}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please upload a PDF file first >:(.")

# ---Main chat interface---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything about your documents!"):
    # Add a user message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("suer"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post("http://127.0.0.1:8000/chat/", data={"query": prompt})
                if response.status_code == 200:
                    full_response = response.json().get("response")
                    st.markdown(full_response)
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
                else:
                    st.error(f"Error from API: {response.text}")

            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
