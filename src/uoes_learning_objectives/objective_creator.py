"""Learning Objective Creator Page."""

import streamlit as st
from uoes_learning_objectives.blooms_taxonomy import ACTION_VERBS
import random
import os
import anthropic
from dotenv import load_dotenv
load_dotenv()

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

LEVEL_TO_BLOOMS = {
    "100-level (introductory)": ["Remember", "Understand"],
    "200-level (foundation)": ["Understand", "Apply"],
    "300-level (intermediate)": ["Apply", "Analyze"],
    "400-level (advanced)": ["Analyze", "Evaluate"],
    "Graduate": ["Evaluate", "Create"],
}

def generate_objectives(course_level, key_topics, course_title):
    blooms_levels = LEVEL_TO_BLOOMS[course_level]
    topics = [t.strip() for t in key_topics.split(",") if t.strip()]
    objectives = []
    for topic in topics:
        for level in blooms_levels:
            verbs = ACTION_VERBS[level].split(", ")
            verb = random.choice(verbs)
            objectives.append(
                f"By the end of this course, students will be able to {verb} {topic}."
            )
    return objectives

def get_anthropic_objectives(course_level, key_topics, course_title):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return ["Anthropic API key not found. Please set ANTHROPIC_API_KEY in your environment."]
    client = anthropic.Anthropic(api_key=api_key)
    prompt = (
        f"You are an expert in educational assessment and Bloom's Taxonomy. "
        f"Given the following course information, expand on each key topic or takeaway by suggesting 1-2 detailed learning objectives for each, using appropriate Bloom's action verbs for the course level. "
        f"Format each objective as: 'By the end of this course, students will be able to [action verb] [expanded topic/skill].'\n"
        f"Course Title: {course_title}\n"
        f"Course Level: {course_level}\n"
        f"Key Topics: {key_topics}\n"
        f"Respond with a markdown bullet list grouped by topic, with 1-2 objectives per topic."
    )
    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=512,
            temperature=0.2,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.split("\n") if hasattr(response, 'content') else [str(response)]
    except Exception as e:
        return [f"Error communicating with Anthropic API: {e}"]

def objective_creator():
    st.header("Learning Objective Creator")
    st.write("""
    Use this form to enter your course information. You'll receive guidance on writing effective learning objectives aligned with Bloom's Taxonomy.
    """)

    # First row: Course Level (left), Course Title (right)
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        course_level = st.selectbox("Course Level", COURSE_LEVELS, key="course_level")
    with row1_col2:
        course_title = st.text_input("Course Title", key="course_title", placeholder="e.g., Introduction to Biology")

    # Suggested Bloom's Taxonomy focus and verbs below course level
    if course_level:
        st.info(f"Suggested Bloom's Taxonomy focus: {LEVEL_SUGGESTIONS[course_level]}")
        blooms_levels = LEVEL_TO_BLOOMS[course_level]
        for level in blooms_levels:
            verbs = ACTION_VERBS[level].split(", ")
            st.markdown(f"**{level}**: {', '.join(verbs)}")

    # Second row: Subject Area (left), Key Topics (right)
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        subject_area = st.text_input("Subject Area", key="subject_area", placeholder="e.g., Biology")
    with row2_col2:
        key_topics = st.text_area(
            "Key Topics or Takeaways",
            key="key_topics",
            placeholder="List 3-5 major topics or concepts covered in your course, separated by commas."
        )

    use_claude = st.checkbox("Suggest additional objectives with Anthropic Claude AI (requires API key)")
    generate = st.button("Generate Objectives")

    if generate:
        st.success("Course information submitted!")
        st.subheader("Suggested Learning Objectives")
        objectives = generate_objectives(course_level, key_topics, course_title)
        for obj in objectives:
            st.markdown(f"- {obj}")
        if use_claude:
            st.markdown("---")
            st.subheader("Anthropic Claude AI Suggestions")
            with st.spinner("Contacting Anthropic Claude..."):
                ai_objectives = get_anthropic_objectives(course_level, key_topics, course_title)
            for line in ai_objectives:
                if line.strip():
                    st.markdown(line)
