"""
Utility functions for G.I.T.H.U.B.

This module contains utility functions that support the existential
coding experience and provide helpful tools for developers.
"""

import random
import re
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class CodePattern:
    """A pattern found in code with its philosophical meaning."""
    pattern: str
    meaning: str
    wisdom: str
    category: str


def contemplate_code(code: str) -> List[str]:
    """
    Contemplate the deeper meaning of code.
    
    Args:
        code: The code to contemplate
        
    Returns:
        List of contemplative thoughts about the code
    """
    thoughts = []
    
    # Look for patterns and their meanings
    patterns = [
        CodePattern(
            pattern=r"def\s+\w+\s*\(",
            meaning="Function definitions are the verbs of the digital language",
            wisdom="Every function is a microcosm of purpose in the digital universe",
            category="functions"
        ),
        CodePattern(
            pattern=r"if\s+.*:",
            meaning="Conditional statements are the crossroads where code must choose",
            wisdom="Every condition is a choice between two realities",
            category="conditions"
        ),
        CodePattern(
            pattern=r"for\s+.*in\s+.*:",
            meaning="Loops are the heartbeat of the digital realm",
            wisdom="Repetition is the mother of learning, and loops are the mother of repetition",
            category="loops"
        ),
        CodePattern(
            pattern=r"try:",
            meaning="Error handling is the art of accepting imperfection",
            wisdom="Every try block is a prayer for success in the face of uncertainty",
            category="error_handling"
        ),
        CodePattern(
            pattern=r"class\s+\w+",
            meaning="Classes are the blueprints of digital reality",
            wisdom="Every class is a universe with its own laws and possibilities",
            category="classes"
        ),
        CodePattern(
            pattern=r"import\s+",
            meaning="Imports are the bridges between different realms of knowledge",
            wisdom="Every import is a connection to the collective wisdom of developers",
            category="imports"
        ),
        CodePattern(
            pattern=r"#.*",
            meaning="Comments are love letters to your future self",
            wisdom="Comments are the soul of the code, explaining not just what, but why",
            category="comments"
        ),
    ]
    
    for pattern in patterns:
        if re.search(pattern.pattern, code):
            thoughts.append(f"**{pattern.category.title()}:** {pattern.meaning}")
            thoughts.append(f"*Wisdom:* {pattern.wisdom}")
            thoughts.append("")
    
    # Add general contemplations
    general_thoughts = [
        "What is the purpose of this code in the grand scheme of things?",
        "How does this code serve the greater good?",
        "What would happen if this code never existed?",
        "What is the soul of this code trying to express?",
        "How does this code reflect the human condition?",
        "What lessons does this code have to teach us?",
        "How does this code connect to the cosmic order?",
        "What is the deeper meaning behind this implementation?",
    ]
    
    thoughts.extend(random.sample(general_thoughts, 3))
    
    return thoughts


def find_meaning_in_bugs(bug_description: str) -> str:
    """
    Find the deeper meaning in bugs and errors.
    
    Args:
        bug_description: Description of the bug or error
        
    Returns:
        The deeper meaning and wisdom from the bug
    """
    bug_meanings = {
        "null": "The null pointer is the void from which all creation springs. It teaches us about the nature of emptiness and potential.",
        "undefined": "Undefined is not a state of nothingness, but a state of infinite possibility waiting to be defined.",
        "error": "Errors are not failures, but invitations to grow and understand. Every error is a teacher in disguise.",
        "exception": "Exceptions are the universe's way of saying 'pay attention' - they point us toward what we need to learn.",
        "timeout": "Timeouts remind us that not everything can be rushed, and that patience is a virtue in the digital realm.",
        "memory": "Memory errors teach us about the finite nature of resources and the importance of efficiency.",
        "syntax": "Syntax errors are the grammar police of the digital realm, teaching us the importance of clear communication.",
        "logic": "Logic errors reveal the gap between what we think we know and what we actually know.",
        "type": "Type errors remind us that everything has its place and purpose in the cosmic order.",
        "permission": "Permission errors teach us about boundaries and respect in the digital realm.",
    }
    
    bug_lower = bug_description.lower()
    
    for keyword, meaning in bug_meanings.items():
        if keyword in bug_lower:
            return meaning
    
    # Default meaning for unknown bugs
    return "This bug is a mystery waiting to be solved, a puzzle that will teach you something new about yourself and your code."


def generate_philosophical_variable_name(original_name: str) -> str:
    """
    Generate a more philosophical version of a variable name.
    
    Args:
        original_name: The original variable name
        
    Returns:
        A more philosophical variable name
    """
    philosophical_mappings = {
        "user": "digital_soul",
        "data": "cosmic_information",
        "result": "manifestation",
        "temp": "temporary_reality",
        "count": "quantum_measurement",
        "index": "dimensional_position",
        "value": "essence",
        "flag": "cosmic_signal",
        "config": "universal_parameters",
        "state": "existential_condition",
        "list": "collection_of_truths",
        "dict": "mapping_of_meaning",
        "string": "sequence_of_symbols",
        "number": "mathematical_essence",
        "boolean": "binary_truth",
        "object": "digital_entity",
        "function": "purposeful_action",
        "class": "blueprint_of_existence",
        "method": "way_of_being",
        "property": "inherent_quality",
    }
    
    original_lower = original_name.lower()
    
    for key, value in philosophical_mappings.items():
        if key in original_lower:
            return original_lower.replace(key, value)
    
    # If no mapping found, add philosophical prefix
    philosophical_prefixes = [
        "cosmic_",
        "digital_",
        "eternal_",
        "infinite_",
        "universal_",
        "divine_",
        "sacred_",
        "mystical_",
    ]
    
    prefix = random.choice(philosophical_prefixes)
    return f"{prefix}{original_name}"


def analyze_code_complexity(code: str) -> Dict[str, Any]:
    """
    Analyze the complexity of code from a philosophical perspective.
    
    Args:
        code: The code to analyze
        
    Returns:
        A dictionary containing complexity analysis and wisdom
    """
    lines = code.split('\n')
    non_empty_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
    
    # Basic metrics
    total_lines = len(lines)
    code_lines = len(non_empty_lines)
    comment_lines = len([line for line in lines if line.strip().startswith('#')])
    
    # Complexity indicators
    function_count = len(re.findall(r'def\s+\w+', code))
    class_count = len(re.findall(r'class\s+\w+', code))
    loop_count = len(re.findall(r'for\s+|while\s+', code))
    condition_count = len(re.findall(r'if\s+|elif\s+', code))
    
    # Philosophical analysis
    complexity_level = "simple"
    wisdom = ""
    
    if function_count > 10:
        complexity_level = "complex"
        wisdom = "Many functions create many possibilities, but also many responsibilities. Remember: with great power comes great complexity."
    elif loop_count > 5:
        complexity_level = "cyclical"
        wisdom = "Many loops suggest a cyclical nature. Are you repeating patterns that could be simplified? Life is about learning, not repeating."
    elif condition_count > 8:
        complexity_level = "conditional"
        wisdom = "Many conditions create many paths. Each path is a choice, and every choice has consequences. Choose wisely."
    elif code_lines > 100:
        complexity_level = "extensive"
        wisdom = "Extensive code suggests extensive thinking. But remember: the best code is often the simplest code."
    else:
        complexity_level = "simple"
        wisdom = "Simple code is beautiful code. In simplicity lies elegance, and in elegance lies truth."
    
    return {
        "total_lines": total_lines,
        "code_lines": code_lines,
        "comment_lines": comment_lines,
        "function_count": function_count,
        "class_count": class_count,
        "loop_count": loop_count,
        "condition_count": condition_count,
        "complexity_level": complexity_level,
        "wisdom": wisdom,
        "philosophical_insight": f"This code has {complexity_level} complexity, which reflects the {complexity_level} nature of the problem it solves."
    }


def suggest_meditation_break(complexity_analysis: Dict[str, Any]) -> Optional[str]:
    """
    Suggest a meditation break based on code complexity.
    
    Args:
        complexity_analysis: The complexity analysis results
        
    Returns:
        A meditation suggestion or None
    """
    complexity_level = complexity_analysis["complexity_level"]
    
    if complexity_level in ["complex", "extensive"]:
        return "Your code shows signs of complexity. Consider taking a meditation break to clear your mind and return with fresh perspective."
    elif complexity_level == "cyclical":
        return "Many loops detected. Take a moment to breathe and consider if there's a simpler way to express your intent."
    elif complexity_level == "conditional":
        return "Many conditions found. Pause and reflect: are all these paths necessary, or can you simplify your logic?"
    
    return None


def generate_commit_philosophy(changes: List[str]) -> str:
    """
    Generate a philosophical reflection on the changes made.
    
    Args:
        changes: List of changes made
        
    Returns:
        A philosophical reflection on the changes
    """
    change_text = " ".join(changes).lower()
    
    if "refactor" in change_text:
        return "Refactoring is the art of finding the soul within the code. You have not just changed the structure, but revealed the essence."
    elif "fix" in change_text or "bug" in change_text:
        return "In fixing this bug, you have not just solved a problem, but learned a lesson. Every fix is a step toward mastery."
    elif "add" in change_text or "new" in change_text:
        return "You have added something new to the digital realm. Every addition is a contribution to the collective wisdom of developers."
    elif "remove" in change_text or "delete" in change_text:
        return "In removing code, you have not just deleted lines, but simplified reality. Sometimes less is more, and more is less."
    elif "update" in change_text or "modify" in change_text:
        return "You have updated the code, and in doing so, you have updated your understanding. Every change is a step toward enlightenment."
    else:
        return "You have made changes to the code, and in doing so, you have changed yourself. Every modification is a moment of growth."


def calculate_code_karma(code: str) -> int:
    """
    Calculate the karma of code based on its positive and negative aspects.
    
    Args:
        code: The code to analyze
        
    Returns:
        A karma score (positive is good, negative is bad)
    """
    karma = 0
    
    # Positive karma factors
    if "def " in code:
        karma += 5  # Functions are good
    if "class " in code:
        karma += 3  # Classes are good
    if "try:" in code:
        karma += 2  # Error handling is good
    if "if __name__ == '__main__':" in code:
        karma += 1  # Main guard is good
    if "import " in code:
        karma += 1  # Imports are good
    
    # Negative karma factors
    if "eval(" in code:
        karma -= 10  # eval is dangerous
    if "exec(" in code:
        karma -= 10  # exec is dangerous
    if "global " in code:
        karma -= 2  # globals are generally bad
    if "pass" in code:
        karma -= 1  # pass statements are often placeholders
    
    # Comment karma
    comment_ratio = len([line for line in code.split('\n') if line.strip().startswith('#')]) / len(code.split('\n'))
    if comment_ratio > 0.1:
        karma += 3  # Good commenting
    elif comment_ratio < 0.05:
        karma -= 2  # Poor commenting
    
    return karma


def get_karma_interpretation(karma: int) -> str:
    """
    Get an interpretation of the karma score.
    
    Args:
        karma: The karma score
        
    Returns:
        An interpretation of the karma
    """
    if karma >= 10:
        return "Your code radiates positive energy. You are on the path of digital enlightenment."
    elif karma >= 5:
        return "Your code shows good intentions. Continue on your journey with confidence."
    elif karma >= 0:
        return "Your code is neutral. Consider adding more positive elements to improve your karma."
    elif karma >= -5:
        return "Your code shows some negative patterns. Reflect on your choices and seek improvement."
    else:
        return "Your code has accumulated negative karma. Consider refactoring and following better practices."
