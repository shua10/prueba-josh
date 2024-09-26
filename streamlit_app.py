import streamlit as st
import pandas as pd

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

df = pd.DataFrame({
    'Fecha': ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04'],
    'Datos': [1, 2, 3, 4]
})

st.line_chart(df)
