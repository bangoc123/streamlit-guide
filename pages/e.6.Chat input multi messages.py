

import streamlit as st


st.markdown("""
    ### Code
    Lập trình nhận tin nhắn dùng nhập và hiển thị lịch sử nhắn tin
    ```
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for item in st.session_state.messages:
        with st.chat_message("assistant"):
            st.markdown(item)
    prompt = st.chat_input("Say something")

    if prompt:
        with st.chat_message("assistant"):
            st.markdown(prompt)
        st.session_state.messages.append(prompt)
    ```
    ### Demo
    ---
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

for item in st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(item)
prompt = st.chat_input("Say something")

if prompt:
    with st.chat_message("assistant"):
        st.markdown(prompt)
    st.session_state.messages.append(prompt)
        