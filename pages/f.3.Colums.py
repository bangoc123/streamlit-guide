import streamlit as st

st.markdown("""
    #### Chia cột
    Có thể điều chỉnh độ dài của từng cột
    ```
    col1, col2, col3 = st.columns([4, 2, 2])

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")
    ```
    ---
""")



col1, col2, col3 = st.columns([4, 2, 2])

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")