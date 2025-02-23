import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

chatbot = pipeline("text-generation", model="distilgpt2")


def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "Please consult Doctor for accurate Advice"
    elif "appointment" in user_input:
        return "Would you like to Book your Appointment with Doctor"
    elif "medication" in user_input:
        return "it's important to take prescribed Medicines regularly.If you have concern,consult your Doctor"
    else:
        response = chatbot(user_input,max_length = 500,num_return_sequences=1)
        return response[0]['generated_text']


    return response


def main():
    st.title("Health Assistant Chatbot")
    user_input=st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User :",user_input)
            with st.spinner("Processing your query,Please wait"):
                response=healthcare_chatbot(user_input)
            st.write("Healthcare Assistant :",response)
            print(response)


        else:
            st.write("Please enter a message to get a response")
main()