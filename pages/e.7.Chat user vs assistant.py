

import streamlit as st


st.markdown("""
    ### Code
    Lập trình nhận tin nhắn dùng nhập và hiển thị lịch sử nhắn tin với vai trò
    ```
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for item in st.session_state.messages:
        role = item["role"]
        content = item["content"]
        with st.chat_message(role):
            st.markdown(content)
    prompt = st.chat_input("Say something")

    if prompt:
        bot_msg = "I am a bot"
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(bot_msg)
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_msg
        })
            
    ```
    ### Demo
    ---
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

for item in st.session_state.messages:
    role = item["role"]
    content = item["content"]
    with st.chat_message(role):
        st.markdown(content)
prompt = st.chat_input("Say something")

if prompt:
    bot_msg = "I am a bot"
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown(bot_msg)
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_msg
    })
        