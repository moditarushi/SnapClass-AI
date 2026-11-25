import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of the new subject")

    sub_name = st.text_input(
        "Subject Name",
        placeholder="Introduction to Computer Science",
        key="new_subject_name"
    )

    sub_id = st.text_input(
        "Subject Code",
        placeholder="CS101",
        key="new_subject_code"
    )

    sub_section = st.selectbox(
        "Section",
        ["A", "B", "C", "D"],
        key="new_subject_section"
    )

    if st.button(
        "Create Subject Now",
        type="primary",
        width="stretch",
        key="create_subject_button"
    ):
        sub_name = sub_name.strip()
        sub_id = sub_id.strip().upper()

        if not sub_name or not sub_id:
            st.warning("Please fill in all fields.")
            return

        try:
            create_subject(
                sub_id,
                sub_name,
                sub_section,
                teacher_id
            )

            st.success(
                f"{sub_name} ({sub_id}) — Section {sub_section} created!"
            )
            st.rerun()

        except Exception as e:
            st.error(f"Could not create subject: {e}")
