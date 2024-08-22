import streamlit as st

st.markdown(
    """
    ### Code
    Lập trình nhận tin nhắn dùng nhập

    ```
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
    ```
    
    ### Demo
    ---
    """
)

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")