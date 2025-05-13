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

    st.title("Learning Objectives Builder")
    st.write("""
    Welcome to the Learning Objectives Builder! This tool helps instructors create effective learning 
    objectives for their courses using Bloom's Taxonomy.
    """)

    # Define page mapping
    pages = {
        "Bloom's Taxonomy Guide": show_blooms_taxonomy,
        "Objective Analyzer": objective_analyzer,
        "Objective Creator": objective_creator,
        "Sample Objectives": display_sample_objectives_page
    }

    # Use the sidebar navigation component to handle page selection
    selected_page = sidebar_navigation(pages)
    
    # Display the selected page by calling its function
    pages[selected_page]()


if __name__ == "__main__":
    main()
