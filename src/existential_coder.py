"""
The Existential Coder - The heart of G.I.T.H.U.B.

This module contains the main class that provides existential guidance
and philosophical insights for developers.
"""

import random
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class ContemplationLevel(Enum):
    """Levels of existential contemplation."""
    SURFACE = "surface"  # Basic questions about variable names
    DEEP = "deep"        # Questions about life and code
    COSMIC = "cosmic"    # Questions about the nature of existence


@dataclass
class CodeInsight:
    """A philosophical insight about code."""
    question: str
    wisdom: str
    contemplation_level: ContemplationLevel
    line_number: Optional[int] = None


class ExistentialCoder:
    """
    The main class that provides existential guidance for developers.
    
    This class analyzes code not just for syntax errors, but for deeper
    philosophical implications and existential meaning.
    """
    
    def __init__(self, contemplation_level: ContemplationLevel = ContemplationLevel.DEEP):
        """Initialize the existential coder."""
        self.contemplation_level = contemplation_level
        self.philosophical_questions = self._load_philosophical_questions()
        self.wisdom_quotes = self._load_wisdom_quotes()
    
    def _load_philosophical_questions(self) -> Dict[str, List[str]]:
        """Load philosophical questions for different code patterns."""
        return {
            "variables": [
                "What does this variable represent in the grand scheme of things?",
                "Is this variable truly necessary, or are we just creating digital noise?",
                "What would this variable say if it could speak?",
                "Are we naming things to understand them, or to control them?",
            ],
            "functions": [
                "What is the purpose of this function in the cosmic order?",
                "Does this function serve the greater good, or just our immediate needs?",
                "What would happen if this function never existed?",
                "Are we creating solutions or just moving problems around?",
            ],
            "loops": [
                "Is this loop a metaphor for the cycles of life?",
                "What are we really iterating over - data or our own limitations?",
                "Does this loop have an end, or are we trapped in eternal repetition?",
                "Are we the loop, or is the loop us?",
            ],
            "conditions": [
                "What determines the path this code will take?",
                "Are we making decisions, or are the decisions making us?",
                "What if the condition is never true? What then?",
                "Is this 'if' statement a reflection of our own binary thinking?",
            ],
            "errors": [
                "What is this error trying to teach us?",
                "Is this bug a feature of the universe trying to communicate?",
                "What would happen if we never fixed this error?",
                "Are errors really mistakes, or just unexpected wisdom?",
            ]
        }
    
    def _load_wisdom_quotes(self) -> List[str]:
        """Load wisdom quotes for different situations."""
        return [
            "The code is not the destination, but the path.",
            "Every bug is a teacher in disguise.",
            "In the silence between keystrokes, wisdom speaks.",
            "The function that returns nothing still has meaning.",
            "Variables are temporary, but the lessons are eternal.",
            "The loop that never ends is called life.",
            "Error handling is the art of accepting imperfection.",
            "Comments are love letters to your future self.",
            "The null pointer is the void from which all creation springs.",
            "Every commit is a step on the journey of becoming.",
        ]
    
    def analyze_code(self, code: str, filename: str = "unknown") -> List[CodeInsight]:
        """
        Analyze code for existential meaning and philosophical implications.
        
        Args:
            code: The code to analyze
            filename: The name of the file being analyzed
            
        Returns:
            List of CodeInsight objects containing philosophical questions and wisdom
        """
        insights = []
        lines = code.split('\n')
        
        for i, line in enumerate(lines, 1):
            line_insights = self._analyze_line(line, i)
            insights.extend(line_insights)
        
        # Add general wisdom
        if insights:
            wisdom = random.choice(self.wisdom_quotes)
            insights.append(CodeInsight(
                question="What wisdom does this code hold?",
                wisdom=wisdom,
                contemplation_level=ContemplationLevel.COSMIC
            ))
        
        return insights
    
    def _analyze_line(self, line: str, line_number: int) -> List[CodeInsight]:
        """Analyze a single line of code for philosophical implications."""
        insights = []
        line = line.strip()
        
        if not line or line.startswith('#'):
            return insights
        
        # Analyze different code patterns
        if 'def ' in line:
            insights.extend(self._analyze_function_definition(line, line_number))
        elif 'if ' in line or 'elif ' in line:
            insights.extend(self._analyze_condition(line, line_number))
        elif 'for ' in line or 'while ' in line:
            insights.extend(self._analyze_loop(line, line_number))
        elif '=' in line and not '==' in line:
            insights.extend(self._analyze_variable_assignment(line, line_number))
        elif 'except' in line or 'raise' in line:
            insights.extend(self._analyze_error_handling(line, line_number))
        
        return insights
    
    def _analyze_function_definition(self, line: str, line_number: int) -> List[CodeInsight]:
        """Analyze function definitions for philosophical meaning."""
        questions = self.philosophical_questions["functions"]
        question = random.choice(questions)
        
        return [CodeInsight(
            question=question,
            wisdom="Every function is a microcosm of purpose in the digital universe.",
            contemplation_level=self.contemplation_level,
            line_number=line_number
        )]
    
    def _analyze_condition(self, line: str, line_number: int) -> List[CodeInsight]:
        """Analyze conditional statements for existential meaning."""
        questions = self.philosophical_questions["conditions"]
        question = random.choice(questions)
        
        return [CodeInsight(
            question=question,
            wisdom="Every condition is a choice between two realities.",
            contemplation_level=self.contemplation_level,
            line_number=line_number
        )]
    
    def _analyze_loop(self, line: str, line_number: int) -> List[CodeInsight]:
        """Analyze loops for philosophical implications."""
        questions = self.philosophical_questions["loops"]
        question = random.choice(questions)
        
        return [CodeInsight(
            question=question,
            wisdom="Loops are the heartbeat of the digital realm.",
            contemplation_level=self.contemplation_level,
            line_number=line_number
        )]
    
    def _analyze_variable_assignment(self, line: str, line_number: int) -> List[CodeInsight]:
        """Analyze variable assignments for deeper meaning."""
        questions = self.philosophical_questions["variables"]
        question = random.choice(questions)
        
        return [CodeInsight(
            question=question,
            wisdom="Every variable is a container for potential.",
            contemplation_level=self.contemplation_level,
            line_number=line_number
        )]
    
    def _analyze_error_handling(self, line: str, line_number: int) -> List[CodeInsight]:
        """Analyze error handling for philosophical insights."""
        questions = self.philosophical_questions["errors"]
        question = random.choice(questions)
        
        return [CodeInsight(
            question=question,
            wisdom="Errors are not failures, but invitations to grow.",
            contemplation_level=self.contemplation_level,
            line_number=line_number
        )]
    
    def generate_commit_message(self, changes: List[str]) -> str:
        """
        Generate a philosophical commit message based on the changes made.
        
        Args:
            changes: List of changes made in the commit
            
        Returns:
            A profound commit message that questions reality
        """
        change_type = self._classify_changes(changes)
        
        commit_templates = {
            "refactor": [
                "Refactored the code, but what is the 'self' that we are refactoring?",
                "Restructured the architecture, but are we not all just data structures in the cosmic database?",
                "Reorganized the modules, but what is organization in the face of infinite complexity?",
            ],
            "fix": [
                "Fixed the bug, but are we not all bugs in the cosmic code?",
                "Resolved the issue, but what is resolution when problems are infinite?",
                "Patched the vulnerability, but are we not all vulnerable in the digital realm?",
            ],
            "feature": [
                "Added new functionality, but what is new in an eternal cycle of creation?",
                "Implemented the feature, but are we implementing or being implemented?",
                "Created the module, but who created the creator?",
            ],
            "docs": [
                "Updated the documentation, but what is documentation when words are just symbols?",
                "Clarified the comments, but can clarity exist in a world of infinite interpretation?",
                "Wrote the README, but who reads the reader?",
            ],
            "test": [
                "Added tests, but what is testing when reality is untestable?",
                "Verified the functionality, but can we ever truly verify anything?",
                "Validated the behavior, but what validates the validator?",
            ]
        }
        
        templates = commit_templates.get(change_type, [
            "Made changes, but what is change in an unchanging universe?",
            "Modified the code, but are we not all modifications of the cosmic source?",
        ])
        
        return random.choice(templates)
    
    def _classify_changes(self, changes: List[str]) -> str:
        """Classify the type of changes made."""
        change_text = " ".join(changes).lower()
        
        if any(word in change_text for word in ["refactor", "restructure", "reorganize"]):
            return "refactor"
        elif any(word in change_text for word in ["fix", "bug", "issue", "error"]):
            return "fix"
        elif any(word in change_text for word in ["add", "new", "feature", "implement"]):
            return "feature"
        elif any(word in change_text for word in ["doc", "readme", "comment", "explain"]):
            return "docs"
        elif any(word in change_text for word in ["test", "spec", "verify", "validate"]):
            return "test"
        else:
            return "general"
