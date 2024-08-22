

import streamlit as st


st.markdown("""
    ### Code
    Lập trình nhận tin nhắn dùng nhập và hiển thị tin nhắn này
    ```
    prompt = st.chat_input("Say something")
    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
    ```
    ### Demo
    ---
""")



prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)