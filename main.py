import streamlit as st
from langchain_code_logic import get_qa_chain, create_vector_db

# Add a link to your GitHub repository at the top of the webpage
st.markdown("[GitHub Repository](https://github.com/sahiltambe/Insightful-Q-A-Chatbot)", unsafe_allow_html=True)

st.title("Insightful Q & A Chatbot")
btn = st.button("Create Knowledgebase") # Create a button to create the vector database
if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])