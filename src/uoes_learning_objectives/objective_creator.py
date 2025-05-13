"""Learning Objective Creator Page."""

import streamlit as st

COURSE_LEVELS = [
    "100-level (introductory)",
    "200-level (foundation)",
    "300-level (intermediate)",
    "400-level (advanced)",
    "Graduate"
]

LEVEL_SUGGESTIONS = {
    "100-level (introductory)": "Focus on Remember, Understand",
    "200-level (foundation)": "Focus on Understand, Apply",
    "300-level (intermediate)": "Focus on Apply, Analyze",
    "400-level (advanced)": "Focus on Analyze, Evaluate",
    "Graduate": "Focus on Evaluate, Create"
}

def objective_creator():
    st.header("Learning Objective Creator")
    st.write("""
    Use this form to enter your course information. You'll receive guidance on writing effective learning objectives aligned with Bloom's Taxonomy.
    """)

    with st.form("objective_creator_form"):
        course_title = st.text_input("Course Title", placeholder="e.g., Introduction to Biology")
        course_level = st.selectbox("Course Level", COURSE_LEVELS)
        subject_area = st.text_input("Subject Area", placeholder="e.g., Biology")
        key_topics = st.text_area(
            "Key Topics or Takeaways",
            placeholder="List 3-5 major topics or concepts covered in your course, separated by commas."
        )
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("Course information submitted!")
        st.markdown(f"**Course Title:** {course_title}")
        st.markdown(f"**Course Level:** {course_level}")
        st.markdown(f"**Subject Area:** {subject_area}")
        st.markdown(f"**Key Topics:** {key_topics}")
        st.info(f"Suggested Bloom's Taxonomy focus: {LEVEL_SUGGESTIONS[course_level]}")
        st.markdown("---")
        st.write("Next, use these details to draft learning objectives. Refer to the action verbs and examples in the Bloom's Taxonomy Guide.")
