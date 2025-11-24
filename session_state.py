# Session state code for counter incrementing application

import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to: {st.session_state.counter}")

if st.button("Reset Counter"):
    st.session_state.counter = 0
    st.write("Counter reset to 0")


st.write(f"Current Counter Value: {st.session_state.counter}")