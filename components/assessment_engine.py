import streamlit as st


def render_question(question):

    question_id = question["id"]

    label = question["label"]

    question_type = question["type"]

    if question_type == "text":

        return st.text_input(
            label,
            key=question_id
        )

    elif question_type == "select":

        return st.selectbox(
            label,
            question["options"],
            key=question_id
        )

    elif question_type == "radio":

        return st.radio(
            label,
            question["options"],
            key=question_id
        )
    