"""Bloom's Taxonomy related functions and data."""

import streamlit as st


# Dictionary of cognitive levels and their descriptions
COGNITIVE_LEVELS = {
    "Remember": "Recall facts and basic concepts",
    "Understand": "Explain ideas or concepts",
    "Apply": "Use information in new situations",
    "Analyze": "Draw connections among ideas",
    "Evaluate": "Justify a stand or decision",
    "Create": "Produce new or original work"
}

# Dictionary of action verbs associated with each cognitive level
ACTION_VERBS = {
    "Remember": "define, list, name, identify, recall, recognize, state, repeat, reproduce, label",
    "Understand": "explain, describe, interpret, summarize, paraphrase, classify, compare, contrast, discuss",
    "Apply": "implement, execute, use, demonstrate, operate, solve, calculate, complete, illustrate",
    "Analyze": "differentiate, organize, attribute, compare, contrast, distinguish, examine, experiment, question",
    "Evaluate": "check, critique, judge, test, monitor, assess, defend, appraise, argue, value",
    "Create": "design, construct, plan, produce, invent, develop, compose, formulate, generate, write"
}

# Example learning objectives for each cognitive level
EXAMPLE_OBJECTIVES = {
    "Remember": "By the end of this course, students will be able to list the key components of a computer system.",
    "Understand": "By the end of this course, students will be able to explain the principles of object-oriented programming.",
    "Apply": "By the end of this course, students will be able to implement sorting algorithms to solve specific problems.",
    "Analyze": "By the end of this course, students will be able to compare and contrast different machine learning approaches for a given dataset.",
    "Evaluate": "By the end of this course, students will be able to critique research papers in the field of artificial intelligence.",
    "Create": "By the end of this course, students will be able to design and develop a web application using modern frameworks."
}

# Rubric criteria for effective learning objectives
RUBRIC_CRITERIA = {
    "Specific": "Clearly defines what the student will be able to do",
    "Measurable": "Can be assessed and evaluated",
    "Action-oriented": "Uses action verbs from Bloom's Taxonomy",
    "Realistic": "Achievable within the constraints of the course",
    "Time-bound": "Specifies when the objective should be achieved (usually by the end of the course)",
    "Aligned": "Supports program-level and institutional learning outcomes"
}


def display_blooms_overview() -> None:
    """Display the overview section of Bloom's Taxonomy."""
    st.subheader("Overview of Bloom's Taxonomy")
    st.write("""
    Bloom's Taxonomy divides educational objectives into three domains:
    
    1. **Cognitive Domain** (knowledge-based)
    2. **Affective Domain** (emotion-based)
    3. **Psychomotor Domain** (action-based)
    
    For course learning objectives, we primarily focus on the cognitive domain, which deals with knowledge acquisition and intellectual skills.
    """)
    
    st.image("https://cft.vanderbilt.edu/wp-content/uploads/sites/59/Blooms-Taxonomy-650x366.jpg", 
             caption="Bloom's Taxonomy Pyramid", width=600)


def display_cognitive_domain() -> None:
    """Display information about the cognitive domain levels."""
    st.subheader("Cognitive Domain Levels")
    
    for level, description in COGNITIVE_LEVELS.items():
        st.markdown(f"**{level}**: {description}")
        
    st.write("""
    The levels are hierarchical, with each level building upon the previous one. Higher-level objectives 
    (Analyze, Evaluate, Create) are generally more valuable for deeper learning and critical thinking skills.
    """)


def display_action_verbs() -> None:
    """Display action verbs for each cognitive level."""
    st.subheader("Action Verbs by Cognitive Level")
    
    for level, verbs in ACTION_VERBS.items():
        st.markdown(f"**{level}**")
        verb_list = verbs.split(", ")
        cols = st.columns(3)
        for i, verb in enumerate(verb_list):
            cols[i % 3].markdown(f"- {verb}")
        st.markdown("---")


def display_example_objectives() -> None:
    """Display example learning objectives for each cognitive level."""
    st.subheader("Example Learning Objectives")
    
    for level, example in EXAMPLE_OBJECTIVES.items():
        st.markdown(f"**{level}**: {example}")


def display_rubric() -> None:
    """Display the rubric for effective learning objectives."""
    st.subheader("Rubric for Effective Learning Objectives")
    
    st.write("""
    An effective learning objective should be:
    """)
    
    for criterion, description in RUBRIC_CRITERIA.items():
        st.markdown(f"**{criterion}**: {description}")
    
    st.write("""
    ### Scoring Rubric
    
    Rate each learning objective on a scale of 1-5 for each criterion:
    
    - **1**: Does not meet the criterion
    - **2**: Partially meets the criterion
    - **3**: Meets the basic expectation
    - **4**: Exceeds the basic expectation
    - **5**: Exemplary
    
    A strong learning objective should score at least 4 in most categories.
    """)


def show_blooms_taxonomy() -> None:
    """Display comprehensive information about Bloom's Taxonomy."""
    st.header("Bloom's Taxonomy for Learning Objectives")
    
    st.write("""
    Bloom's Taxonomy is a framework used to classify educational learning objectives into levels of complexity.
    The taxonomy was first introduced by Benjamin Bloom in 1956 and later revised in 2001.
    It provides a structured approach to writing effective learning objectives.
    """)
    
    # Create tabs for different aspects of Bloom's taxonomy
    tabs = st.tabs(["Overview", "Cognitive Domain", "Action Verbs", "Example Objectives", "Rubric"])
    
    with tabs[0]:  # Overview
        display_blooms_overview()
    
    with tabs[1]:  # Cognitive Domain
        display_cognitive_domain()
    
    with tabs[2]:  # Action Verbs
        display_action_verbs()
    
    with tabs[3]:  # Example Objectives
        display_example_objectives()
    
    with tabs[4]:  # Rubric
        display_rubric()