"""Sample learning objectives by discipline."""

from typing import Dict


# Sample learning objectives organized by discipline and Bloom's taxonomy level
SAMPLE_OBJECTIVES: Dict[str, Dict[str, str]] = {
    "Computer Science": {
        "Remember": "By the end of this course, students will be able to identify the key components of a computer system architecture.",
        "Understand": "By the end of this course, students will be able to explain the principles of object-oriented programming.",
        "Apply": "By the end of this course, students will be able to implement sorting algorithms to solve specific problems.",
        "Analyze": "By the end of this course, students will be able to compare and contrast different machine learning approaches for a given dataset.",
        "Evaluate": "By the end of this course, students will be able to critique research papers in the field of artificial intelligence.",
        "Create": "By the end of this course, students will be able to design and develop a web application using modern frameworks."
    },
    "Mathematics": {
        "Remember": "By the end of this course, students will be able to recall the fundamental theorems of calculus.",
        "Understand": "By the end of this course, students will be able to describe the relationship between differentiation and integration.",
        "Apply": "By the end of this course, students will be able to solve differential equations using appropriate methods.",
        "Analyze": "By the end of this course, students will be able to examine the convergence of infinite series using various tests.",
        "Evaluate": "By the end of this course, students will be able to assess the validity of mathematical proofs.",
        "Create": "By the end of this course, students will be able to formulate original mathematical proofs for given theorems."
    },
    "Biology": {
        "Remember": "By the end of this course, students will be able to list the stages of cell division.",
        "Understand": "By the end of this course, students will be able to explain the process of natural selection and its role in evolution.",
        "Apply": "By the end of this course, students will be able to demonstrate proper laboratory techniques for DNA extraction.",
        "Analyze": "By the end of this course, students will be able to differentiate between various types of genetic mutations and their effects.",
        "Evaluate": "By the end of this course, students will be able to judge the ethical implications of genetic engineering technologies.",
        "Create": "By the end of this course, students will be able to design an experiment to test a hypothesis about ecosystem dynamics."
    },
    "Psychology": {
        "Remember": "By the end of this course, students will be able to identify the major psychological perspectives.",
        "Understand": "By the end of this course, students will be able to describe the relationship between neural activity and behavior.",
        "Apply": "By the end of this course, students will be able to use psychological theories to explain real-world behaviors.",
        "Analyze": "By the end of this course, students will be able to distinguish between correlation and causation in research findings.",
        "Evaluate": "By the end of this course, students will be able to appraise the methodological strengths and weaknesses of psychological studies.",
        "Create": "By the end of this course, students will be able to develop a research proposal addressing a current issue in psychology."
    },
    "Business": {
        "Remember": "By the end of this course, students will be able to recognize the components of a business plan.",
        "Understand": "By the end of this course, students will be able to summarize the key principles of marketing management.",
        "Apply": "By the end of this course, students will be able to calculate financial ratios to assess company performance.",
        "Analyze": "By the end of this course, students will be able to examine market trends to identify business opportunities.",
        "Evaluate": "By the end of this course, students will be able to assess the effectiveness of different leadership styles in various contexts.",
        "Create": "By the end of this course, students will be able to construct a comprehensive business strategy for a startup company."
    },
    "Education": {
        "Remember": "By the end of this course, students will be able to list the major learning theories in education.",
        "Understand": "By the end of this course, students will be able to explain how developmental factors influence learning.",
        "Apply": "By the end of this course, students will be able to demonstrate effective teaching strategies for diverse learners.",
        "Analyze": "By the end of this course, students will be able to examine assessment data to inform instructional decisions.",
        "Evaluate": "By the end of this course, students will be able to critique curriculum materials based on research-based standards.",
        "Create": "By the end of this course, students will be able to design a lesson plan that incorporates differentiated instruction."
    }
}


def display_sample_objectives_page() -> None:
    """Display the sample objectives page in the Streamlit app."""
    import streamlit as st
    from uoes_learning_objectives.ui_components import page_header, display_taxonomy_level_badge
    
    page_header(
        "Sample Learning Objectives by Discipline", 
        "Browse example learning objectives across different disciplines and Bloom's taxonomy levels."
    )
    
    # Create a discipline filter
    disciplines = list(SAMPLE_OBJECTIVES.keys())
    disciplines.insert(0, "All")
    
    selected_discipline = st.selectbox("Select a discipline:", disciplines)
    
    st.markdown("---")
    
    # Display filtered objectives
    if selected_discipline == "All":
        for discipline, objectives in SAMPLE_OBJECTIVES.items():
            st.subheader(discipline)
            for level, objective in objectives.items():
                col1, col2 = st.columns([1, 9])
                with col1:
                    display_taxonomy_level_badge(level)
                with col2:
                    st.write(objective)
            st.markdown("---")
    else:
        objectives = SAMPLE_OBJECTIVES.get(selected_discipline, {})
        for level, objective in objectives.items():
            col1, col2 = st.columns([1, 9])
            with col1:
                display_taxonomy_level_badge(level)
            with col2:
                st.write(objective)
                
    # Add an explanation section
    st.subheader("Using These Examples")
    st.write("""
    These sample learning objectives demonstrate how to write effective objectives across different disciplines
    using Bloom's Taxonomy. When adapting these examples:
    
    1. Consider the specific content of your course
    2. Choose appropriate action verbs for your desired cognitive level
    3. Ensure objectives are measurable and aligned with assessments
    4. Tailor the complexity to your students' level
    
    Remember that higher-level objectives (Analyze, Evaluate, Create) promote deeper learning but may not be 
    appropriate for introductory courses.
    """)