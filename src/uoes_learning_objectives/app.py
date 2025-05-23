"""Main Streamlit application module for UOES Learning Objectives."""

import streamlit as st

from uoes_learning_objectives.blooms_taxonomy import show_blooms_taxonomy
from uoes_learning_objectives.objective_analyzer import objective_analyzer
from uoes_learning_objectives.sample_objectives import display_sample_objectives_page
from uoes_learning_objectives.objective_creator import objective_creator
from uoes_learning_objectives.ui_components import sidebar_navigation


def main() -> None:
    """Main Streamlit application entry point."""
    st.set_page_config(
        page_title="Learning Objectives Builder", 
        page_icon="📚", 
        layout="wide"
    )

    st.title("Learning Objectives Assistant")
    st.write("""
    Welcome to the Learning Objectives Builder! This tool is offered to  instructors to assist them in creating effective high quality learning 
    objectives for their material. \n
    It is based on Bloom's Taxonomy and provides a variety of features to help you create, analyze, and refine your learning objectives. Use the sidebar to navigate through a short explanation on Bloom's or review some sample objectives.
    """)

    # Define page mapping - reordered to make Objective Creator first
    pages = {
        "Objective Creator": objective_creator,
        "Bloom's Taxonomy Guide": show_blooms_taxonomy,
        "Objective Analyzer": objective_analyzer,
        "Sample Objectives": display_sample_objectives_page
    }

    # Use the sidebar navigation component to handle page selection
    selected_page = sidebar_navigation(pages)
    
    # Display the selected page by calling its function
    pages[selected_page]()


if __name__ == "__main__":
    main()
