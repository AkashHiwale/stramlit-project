import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display a simple message
st.write("Hello, Streamlit! from Akash")

st.title("My First Streamlit App")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is a **markdown** text with _formatting_.")
st.caption("This is a caption text.")
st.code("print('Hello, Streamlit!')", language='python')

code_example = '''
def greet(name):
    return f"Hello, {name}!"
    print(greet("Streamlit"))
'''
st.code(code_example, language='python')

st.divider()

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo")

st.image(os.path.join(os.getcwd(), "static", "meeting.jpg"), caption="Meeting Image")

# Display a sample DataFrame

st.subheader("Sample DataFrame")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
st.dataframe(df)

st.subheader("Data Editor")
edited_df = st.data_editor(df)

st.subheader("Data Table")
st.table(df)

st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(), 1))

# JSON and Dictionary display
st.subheader("JSON Display")
sample_json = {
    "employees": [
        {"name": "Alice", "age": 24, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "Los Angeles"},
        {"name": "Charlie", "age": 22, "city": "Chicago"}
    ]
}
st.json(sample_json)
st.write("Dictionary Display:", sample_json)



# Matplotlib Tutorial

st.title("Matplotlib Tutorial in Streamlit")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("scatter chart using matplotlib")
scatter_data = pd.DataFrame(
    {
        'x': np.random.randn(100),
        'y': np.random.randn(100)
    }
)
st.scatter_chart(scatter_data)