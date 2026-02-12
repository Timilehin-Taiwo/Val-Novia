import streamlit as st
import google.generativeai as genai
from duckduckgo_search import DDGS

# 1. Setup the Free Google Brain
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("My Strategy AI Clone")

# 2. Simple Web Search Tool (Free)
def web_search(query):
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=3)]
        return results

# 3. Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me about Nigerian Real Estate..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Brain generates response
    response = model.generate_content(f"You are a Strategy Associate with an MBA. Answer this: {prompt}")
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
