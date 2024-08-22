import streamlit as st
import numpy as np

st.markdown(
    """
    ### Code
    Hiển thị tin nhắn
    ```
    with st.chat_message("user"):
        st.write("Hello 👋")

    with st.chat_message("assistant"):
        st.write("How can I help you!")
    ```

    Tham số của hàm st.chat_message
    ```name ("user", "assistant", "ai", "human", or str)```
    
    ### Demo
    ---
    """
)



with st.chat_message("user"):
    st.write("Hello 👋")

with st.chat_message("assistant"):
    st.write("How can I help you!")