"""Learning objective analyzer module."""

import re
import streamlit as st
import os
import anthropic
from typing import Dict, List, Tuple, Optional

from dotenv import load_dotenv
load_dotenv()

from uoes_learning_objectives.blooms_taxonomy import ACTION_VERBS, RUBRIC_CRITERIA


def contains_action_verb(objective: str, level: str) -> bool:
    """Check if the objective contains an action verb from the specified level.
    
    Args:
        objective: The learning objective text
        level: The Bloom's taxonomy level to check against
        
    Returns:
        True if the objective contains an action verb from the specified level
    """
    verbs = ACTION_VERBS.get(level, "").split(", ")
    objective_lower = objective.lower()
    
    for verb in verbs:
        # Check for the verb as a word (not part of another word)
        if re.search(r'\b' + verb + r'\b', objective_lower):
            return True
    
    return False


def identify_blooms_level(objective: str) -> Optional[str]:
    """Identify the highest Bloom's taxonomy level in the objective.
    
    Args:
        objective: The learning objective text
        
    Returns:
        The highest Bloom's taxonomy level found, or None if no level is detected
    """
    # Check for verbs from highest to lowest level
    levels = ["Create", "Evaluate", "Analyze", "Apply", "Understand", "Remember"]
    
    for level in levels:
        if contains_action_verb(objective, level):
            return level
    
    return None


def basic_objective_analysis(objective: str) -> Tuple[List[str], List[str]]:
    """Perform a basic analysis of a learning objective.
    
    Args:
        objective: The learning objective text
        
    Returns:
        A tuple containing (strengths, suggestions)
    """
    strengths = []
    suggestions = []
    
    # Check length
    if len(objective) < 20:
        suggestions.append("The objective is too short. Consider adding more detail.")
    
    # Check format
    if "students will be able to" in objective.lower():
        strengths.append("Uses the recommended 'students will be able to' format")
    else:
        suggestions.append("Consider using the format: 'Students will be able to...'")
    
    # Check for time-bound element
    if "by the end of" in objective.lower():
        strengths.append("Includes a time-bound element")
    else:
        suggestions.append("Consider adding when the objective should be achieved (e.g., 'By the end of this course')")
    
    # Check for Bloom's level
    level = identify_blooms_level(objective)
    if level:
        strengths.append(f"Uses action verbs from Bloom's taxonomy level: {level}")
    else:
        suggestions.append("No clear Bloom's taxonomy action verb detected. Consider using a specific action verb.")
    
    return strengths, suggestions


def evaluate_objective_rubric(objective: str) -> Dict[str, int]:
    """Evaluate a learning objective against the rubric criteria.
    
    Args:
        objective: The learning objective text
        
    Returns:
        Dictionary with scores for each rubric criterion
    """
    # This is a placeholder for more advanced analysis
    # In a real implementation, this would use more sophisticated analysis
    
    scores = {}
    
    # Basic scoring logic (to be enhanced in future versions)
    # Specific
    scores["Specific"] = 3 if len(objective) > 30 else 2
    
    # Measurable
    measurable_words = ["demonstrate", "calculate", "solve", "identify", "analyze"]
    scores["Measurable"] = 4 if any(word in objective.lower() for word in measurable_words) else 2
    
    # Action-oriented
    level = identify_blooms_level(objective)
    scores["Action-oriented"] = 4 if level else 2
    
    # Realistic - assuming all objectives are realistic
    scores["Realistic"] = 3
    
    # Time-bound
    scores["Time-bound"] = 4 if "by the end of" in objective.lower() else 2
    
    # Aligned - hard to assess without context
    scores["Aligned"] = 3
    
    return scores


def analyze_objective_with_anthropic(objective: str) -> str:
    """Use Anthropic's Claude API to analyze a learning objective."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return "Anthropic API key not found. Please set ANTHROPIC_API_KEY in your environment."
    client = anthropic.Anthropic(api_key=api_key)
    prompt = (
        "You are an expert in educational assessment and Bloom's Taxonomy. "
        "Analyze the following learning objective for strengths, weaknesses, and Bloom's level. "
        "Provide suggestions for improvement and a rubric-based score (1-5) for Specific, Measurable, Action-oriented, Realistic, Time-bound, and Aligned. "
        "Respond in markdown with clear sections for Strengths, Suggestions, Detected Bloom's Level, and Rubric Evaluation.\n\n"
        f"Learning Objective: {objective}"
    )
    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",  # or another available model
            max_tokens=1024,
            temperature=0.2,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text if hasattr(response, 'content') else str(response)
    except Exception as e:
        return f"Error communicating with Anthropic API: {e}"


def objective_analyzer() -> None:
    """Create an interface for analyzing and improving learning objectives."""
    st.header("Learning Objective Analyzer")
    
    st.write("""
    Enter a learning objective below to analyze it against Bloom's Taxonomy and best practices.
    """)
    
    user_objective = st.text_area(
        "Enter your learning objective:",
        placeholder="e.g., By the end of this course, students will be able to implement sorting algorithms."
    )
    
    use_claude = st.checkbox("Use Anthropic Claude AI for analysis (requires API key)")
    
    if user_objective and st.button("Analyze Objective"):
        if use_claude:
            st.subheader("Anthropic Claude Analysis")
            with st.spinner("Contacting Anthropic Claude..."):
                result = analyze_objective_with_anthropic(user_objective)
            st.markdown(result)
        else:
            st.subheader("Analysis Results")
            
            # Basic analysis
            strengths, suggestions = basic_objective_analysis(user_objective)
            
            # Display strengths
            if strengths:
                st.success("Strengths")
                for strength in strengths:
                    st.markdown(f"✅ {strength}")
            
            # Display suggestions
            if suggestions:
                st.warning("Suggestions for Improvement")
                for suggestion in suggestions:
                    st.markdown(f"🔍 {suggestion}")
            
            # Bloom's level
            level = identify_blooms_level(user_objective)
            if level:
                st.info(f"Detected Bloom's Taxonomy Level: **{level}**")
                
                st.write(f"Other verbs at this level you might consider:")
                other_verbs = ACTION_VERBS[level].split(", ")
                cols = st.columns(4)
                for i, verb in enumerate(other_verbs[:8]):  # Show first 8 verbs
                    cols[i % 4].markdown(f"- {verb}")
            else:
                st.warning("No clear Bloom's Taxonomy level detected. Consider using specific action verbs.")
                
            # Rubric evaluation
            st.subheader("Rubric Evaluation")
            st.write("Preliminary scoring based on the rubric:")
            
            scores = evaluate_objective_rubric(user_objective)
            
            # Display scores as a bar chart
            chart_data = {
                "Criteria": list(scores.keys()),
                "Score": list(scores.values())
            }
            
            st.bar_chart(chart_data, x="Criteria")
            
            # Overall assessment
            avg_score = sum(scores.values()) / len(scores)
            if avg_score >= 4:
                st.success(f"Overall Assessment: Strong objective ({avg_score:.1f}/5)")
            elif avg_score >= 3:
                st.info(f"Overall Assessment: Good objective, with room for improvement ({avg_score:.1f}/5)")
            else:
                st.warning(f"Overall Assessment: Needs improvement ({avg_score:.1f}/5)")
                
            # Note about the analysis
            st.caption("""
            Note: This analysis is based on basic patterns and heuristics. 
            It's meant to provide guidance but cannot replace human judgment.
            """)