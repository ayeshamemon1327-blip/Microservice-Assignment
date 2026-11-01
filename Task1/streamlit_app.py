
import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:5000/students"

st.title("Student Management System")

# ADD STUDENT
st.header("Add Student")

with st.form("student_form"):
    name = st.text_input("Student Name")
    department = st.text_input("Department")
    email = st.text_input("Email")

    submit = st.form_submit_button("Add Student")

    if submit:
        if name and department and email:
            data = {
                "name": name,
                "department": department,
                "email": email
            }

            try:
                response = requests.post(API_URL, json=data)

                if response.status_code in [200, 201]:
                    st.success("Student added successfully!")
                    st.rerun()
                else:
                    st.error(f"Error: {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("Flask API is not connected.")
        else:
            st.warning("Please fill all fields.")


# STUDENT RECORDS
st.header("Student Records")

if st.button("Refresh Records"):
    st.rerun()

try:
    response = requests.get(API_URL)

    if response.status_code == 200:
        students = response.json()

        if students:
            st.dataframe(pd.DataFrame(students))

            # SELECT STUDENT
            st.header("Update Student")

            selected_student = st.selectbox(
                "Select Student",
                students,
                format_func=lambda student: (
                    f"{student['id']} - {student['name']}"
                )
            )

            # UPDATE FORM
            with st.form("update_form"):
                updated_name = st.text_input(
                    "Student Name",
                    value=selected_student["name"]
                )

                updated_department = st.text_input(
                    "Department",
                    value=selected_student["department"]
                )

                updated_email = st.text_input(
                    "Email",
                    value=selected_student["email"]
                )

                update_button = st.form_submit_button("Update Student")

                if update_button:
                    if updated_name and updated_department and updated_email:
                        data = {
                            "name": updated_name,
                            "department": updated_department,
                            "email": updated_email
                        }

                        update_response = requests.put(
                            f"{API_URL}/{selected_student['id']}",
                            json=data
                        )

                        if update_response.status_code == 200:
                            st.success("Student updated successfully!")
                            st.rerun()
                        else:
                            st.error(update_response.text)
                    else:
                        st.warning("Please fill all fields.")

            # DELETE STUDENT
            st.header("Delete Student")

            confirm_delete = st.checkbox(
                "I confirm that I want to delete this student."
            )

            if st.button("Delete Student"):
                if confirm_delete:
                    delete_response = requests.delete(
                        f"{API_URL}/{selected_student['id']}"
                    )

                    if delete_response.status_code == 200:
                        st.success("Student deleted successfully!")
                        st.rerun()
                    else:
                        st.error(delete_response.text)
                else:
                    st.warning("Please confirm before deleting.")

        else:
            st.info("No students found yet.")

    else:
        st.error("Could not fetch student records.")

except requests.exceptions.ConnectionError:
    st.error("Flask API is not connected.")
