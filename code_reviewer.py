import streamlit as st
from openai import OpenAI



f = open("Data/.open_ai_api_key.txt")

api_key = f.read()

client = OpenAI(api_key=api_key)

st.header("Billion Dollor 🧑‍💻 Code Reviewer! 🧑‍💻")
st.subheader("Credits to our, mentor Mr. Kanav Bansal for providing us with an OpenAI api_key to facilitate development of this application.")
prompt = st.text_area("Enter your code here...")

if st.button("Review")==True:
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{"role":"system", "content":"""You are a helpful AI assistant. 
                   Given a code written in any programming language, you are supposed to review it and list all the errors in detail found in the code as well suggest the corrected code with proper remarks. """},{"role":"user", "content":prompt}]
    )

    st.write(response.choices[0].message.content)