

import streamlit as st


st.markdown("""
    ### Code
    Người dùng có thể upload ảnh
    ```
    import streamlit as st
    import pandas as pd
    from io import StringIO


    uploaded_files = st.file_uploader(
        "Choose a CSV file", accept_multiple_files=True
    )
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
            
    ```
    ### Demo
    ---
""")

import streamlit as st
import pandas as pd
from io import StringIO


uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)

    st.image(bytes_data, caption="Sunrise by the mountains")