import streamlit as st

st.markdown(
    """
    ### Code
    Lập trình nhận tin nhắn dùng nhập
    ```
    title = st.text_input("Movie title", "Life of Brian")
    st.write("The current movie title is", title)
    ```
    
    ### Demo
    ---
    """
)

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)