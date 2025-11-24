import streamlit as st

st.write("Hello, Streamlit!")

st.title("User Information Form")

form_values = {
    "name": None,
    "age": None,
    "gender": None,
    "dob": None
}

with st.form(key='user_info_form'):
    form_values["name"] = st.text_input("Enter your name")
    form_values["age"] = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
    form_values["gender"] = st.selectbox("Select your gender", options=["Male", "Female", "Other"])
    form_values["dob"] = st.date_input("Select your date of birth")

    submitted = st.form_submit_button(label="Submit")

    if submitted:
        if not all(form_values.values()):
            st.error("Please fill in all the fields.")
        else:
            st.balloons()
            st.success("Form submitted successfully!")
            st.write("Here is the information you provided:")
            st.write(f"Name: {form_values['name']}")
            st.write(f"Age: {form_values['age']}")