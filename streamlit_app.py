import streamlit as st
from transformers import pipeline

# تحميل النموذج
chatbot = pipeline("text-generation", model="gpt2")

# واجهة التطبيق
st.title("بوت الدردشة التفاعلي 🚀")
st.write("أدخل النص لتتحدث مع البوت:")

# إدخال المستخدم
user_input = st.text_input("أدخل النص هنا:")

if user_input:
    response = chatbot(user_input, max_length=100, do_sample=True)
    bot_reply = response[0]['generated_text']
    
    # عرض الرد
    st.write(f"البوت: {bot_reply}")
