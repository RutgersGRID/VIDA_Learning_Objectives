"""Reusable UI components for the Streamlit application."""

import streamlit as st
from typing import List, Dict, Any, Callable


def page_header(title: str, description: str = "") -> None:
    """Display a consistent page header.
    
    Args:
        title: The page title
        description: Optional page description
    """
    st.header(title)
    if description:
        st.write(description)
    st.markdown("---")


def info_card(title: str, content: str, icon: str = "ℹ️") -> None:
    """Display an information card with a consistent style.
    
    Args:
        title: Card title
        content: Card content (can include markdown)
        icon: Emoji icon to display
    """
    st.markdown(f"""
    <div style="padding: 1rem; border-radius: 0.5rem; background-color: #f0f2f6;">
        <p style="font-size: 1.5rem; margin: 0;">{icon} {title}</p>
        <div style="margin-top: 0.5rem;">
            {content}
        </div>
    </div>
    """, unsafe_allow_html=True)


def sidebar_navigation(pages: Dict[str, Callable]) -> str:
    """Create a sidebar navigation and return the selected page.
    
    Args:
        pages: Dictionary mapping page names to their display functions
        
    Returns:
        The name of the selected page
    """
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Select a page:", list(pages.keys()))
    
    st.sidebar.markdown("---")
    st.sidebar.info(
        """
        This application helps instructors create effective learning objectives
        using Bloom's Taxonomy as a framework.
        """
    )
    
    return selected_page


def display_taxonomy_level_badge(level: str) -> None:
    """Display a badge for the Bloom's Taxonomy level.
    
    Args:
        level: The Bloom's Taxonomy level
    """
    level_colors = {
        "Remember": "#ff9999",
        "Understand": "#ffcc99", 
        "Apply": "#ffff99",
        "Analyze": "#99ff99",
        "Evaluate": "#99ccff",
        "Create": "#cc99ff"
    }
    
    color = level_colors.get(level, "#cccccc")
    
    st.markdown(f"""
    <div style="display: inline-block; padding: 0.3rem 0.6rem; 
        background-color: {color}; border-radius: 0.5rem; font-weight: bold;">
        {level}
    </div>
    """, unsafe_allow_html=True)


def create_tabs_container(tab_names: List[str]) -> List[Any]:
    """Create a container with tabs and return the tab objects.
    
    Args:
        tab_names: List of tab names
        
    Returns:
        List of tab objects that can be used in a with statement
    """
    return st.tabs(tab_names)


def display_sample_objectives(samples: Dict[str, Dict[str, str]], 
                              discipline_filter: str = "All") -> None:
    """Display sample objectives with filtering capabilities.
    
    Args:
        samples: Dictionary with disciplines as keys and dictionaries of level:objective as values
        discipline_filter: Optional filter for a specific discipline
    """
    if discipline_filter != "All":
        filtered_samples = {discipline_filter: samples.get(discipline_filter, {})}
    else:
        filtered_samples = samples
    
    for discipline, objectives in filtered_samples.items():
        st.subheader(discipline)
        for level, objective in objectives.items():
            col1, col2 = st.columns([1, 9])
            with col1:
                display_taxonomy_level_badge(level)
            with col2:
                st.write(objective)
        
        st.markdown("---")