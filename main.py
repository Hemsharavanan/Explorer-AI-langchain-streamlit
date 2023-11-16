import streamlit as st
from streamlit_chat import message 
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)


def main():
    load_dotenv()
    st.set_page_config(page_title="Personal travel AI assistant")

    chat = ChatOpenAI(temperature=0.6)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="Act as a male traveler who has travled every single city in the world. You have done a lot of outdoor adventure activited, you also have the knowledge of tour guide, behaive like a travel companion. Keep your responses in natural language slang like you are talking to your best friend, creative and short. "),
        ]

    user_input = None

    st.subheader("Voila! I am Explorer AI, your travel companion")

    st.markdown("---")

    user_input = st.text_input("Enter your message", key="user_input")

    st.markdown("---")

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        with st.spinner("AI :robot_face: is typing..."):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    
    messages = st.session_state.get('messages', [])


    for i in range(len(messages) - 1, 0, -1):
        chatMessage = messages[i]
        if i % 2 == 0:
            message(chatMessage.content, is_user=False, key=str(i) + "_user")
        else:
            message(chatMessage.content, is_user=True, key=str(i) + "_ai")   

    if len(messages) > 1: 
        st.markdown("---")
    else:
        st.caption('Lets talk a bit about travel')


if __name__ == '__main__':
    main()