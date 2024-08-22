

import streamlit as st


st.markdown("""
    ### Code
    Bot có thể trả về ảnh
    ```
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for item in st.session_state.messages:
        role = item["role"]
        content = item["content"]
        with st.chat_message(role):
            if role == "user":
                st.markdown(content)
            else:
                st.image(content, caption="Sunrise by the mountains")

    prompt = st.chat_input("Say something")

    if prompt:
        img_url = "https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80"
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.image(img_url, caption="Sunrise by the mountains")
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        st.session_state.messages.append({
            "role": "assistant",
            "content": img_url
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
        if role == "user":
            st.markdown(content)
        else:
            st.image(content, caption="Sunrise by the mountains")

prompt = st.chat_input("Say something")

if prompt:
    img_url = "https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80"
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.image(img_url, caption="Sunrise by the mountains")
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    st.session_state.messages.append({
        "role": "assistant",
        "content": img_url
    })
        