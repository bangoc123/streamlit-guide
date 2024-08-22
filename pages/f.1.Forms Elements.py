

import streamlit as st

st.markdown("""
    #### Box lựa chọn
    ```
    option = st.selectbox(
        "APIs",
        ("GPT", "LLAMA", "Claude"),
    )

    st.write("You selected:", option)
    ```
    ---
""")

option = st.selectbox(
    "APIs",
    ("GPT", "LLAMA", "Claude"),
)

st.write("You selected:", option)

st.markdown("""
    #### Range
    ```
    temp = st.slider("Temperatures", 0.0, 1.0, 0.1)
    st.write("Current Temperatures", temp)
    ```
    ---
""")

temp = st.slider("Temperatures", 0.0, 1.0, 0.1)
st.write("Current Temperatures", temp)

st.markdown("""
    #### Xem thêm các API khác
    [Link](https://docs.streamlit.io/develop/api-reference/widgets)
    ---
""")