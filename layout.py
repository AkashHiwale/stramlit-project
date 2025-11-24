import streamlit as st

st.sidebar.title("This is a sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text here.")
sidebar_input = st.sidebar.text_input("Enter some text in the sidebar:")

# Tabs layout
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.header("Welcome to Tab 1")
    st.write("This is the content of Tab 1.")
    st.write(f"You entered: {sidebar_input}")

with tab2:
    st.header("Welcome to Tab 2")
    st.write("This is the content of Tab 2.")
    st.write(f"You entered: {sidebar_input}")

# Columns layout
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This is the first column.")
    st.write(f"You entered: {sidebar_input}")
with col2:
    st.header("Column 2")
    st.write("This is the second column.")
    st.write(f"You entered: {sidebar_input}")

# Container layout
with st.container(border=True):
    st.header("This is a container")
    st.write("You can group elements together in a container.")
    st.write(f"You entered: {sidebar_input}")

# Empty Placeholder
placeholder = st.empty()
placeholder.write("This is an empty placeholder. You can update it later.")

if st.button("Update Placeholder"):
    placeholder.write(f"Placeholder updated with: {sidebar_input}")

# Expander layout
with st.expander("Click to expand"):
    st.write("This is an expander. You can hide content here.")
    st.write(f"You entered: {sidebar_input}")

# popover example
st.write("### Popover Example")
st.button("Click me for popover", help="This is a popover message providing additional information.")

# Sidbar input handling
if sidebar_input:
    st.write(f"You entered: {sidebar_input}")