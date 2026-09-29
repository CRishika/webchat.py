import streamlit as st
from ollama import chat

st.title("My AI Bot: Synora")
name = "Rishi"
st.write("Welcome, ",name)
question = st.text_input("Ask a question")
if st.button("Ask"):
    #st.write("You asked: ", question)
    response = chat(model = "gemma3:latest",messages=[
        {
            "role":"system",
            "content":"You are a friendly tutor. You explain concepts in a very simple way. Explain in 50 words max."
        },
        {
            "role":"user",
            "content":question
        }
    ])
    answer = response.message.content
    st.write(answer)
    #dropdown
    #options = ["C++","Java","Python",]
    #choice = st.selectbox("Select your favorite language :",options)
    #st.write(f"You selected {choice}")

