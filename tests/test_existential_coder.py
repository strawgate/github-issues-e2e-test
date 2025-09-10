"""
Tests for the ExistentialCoder class.

These tests verify that the existential coder provides meaningful
philosophical insights about code.
"""

import pytest
from src.existential_coder import ExistentialCoder, ContemplationLevel, CodeInsight


class TestExistentialCoder:
    """Test cases for the ExistentialCoder class."""
    
    def test_init(self):
        """Test that ExistentialCoder initializes correctly."""
        coder = ExistentialCoder()
        assert coder.contemplation_level == ContemplationLevel.DEEP
        assert len(coder.philosophical_questions) > 0
        assert len(coder.wisdom_quotes) > 0
    
    def test_init_with_level(self):
        """Test initialization with specific contemplation level."""
        coder = ExistentialCoder(ContemplationLevel.COSMIC)
        assert coder.contemplation_level == ContemplationLevel.COSMIC
    
    def test_analyze_code_function(self):
        """Test analysis of function definitions."""
        coder = ExistentialCoder()
        code = "def hello_world():\n    print('Hello, World!')"
        
        insights = coder.analyze_code(code)
        
        assert len(insights) > 0
        assert any(insight.line_number == 1 for insight in insights)
        assert any("function" in insight.question.lower() for insight in insights)
    
    def test_analyze_code_condition(self):
        """Test analysis of conditional statements."""
        coder = ExistentialCoder()
        code = "if x > 0:\n    print('Positive')"
        
        insights = coder.analyze_code(code)
        
        assert len(insights) > 0
        assert any(insight.line_number == 1 for insight in insights)
        assert any("condition" in insight.question.lower() for insight in insights)
    
    def test_analyze_code_loop(self):
        """Test analysis of loop statements."""
        coder = ExistentialCoder()
        code = "for i in range(10):\n    print(i)"
        
        insights = coder.analyze_code(code)
        
        assert len(insights) > 0
        assert any(insight.line_number == 1 for insight in insights)
        assert any("loop" in insight.question.lower() for insight in insights)
    
    def test_analyze_code_variable(self):
        """Test analysis of variable assignments."""
        coder = ExistentialCoder()
        code = "x = 42"
        
        insights = coder.analyze_code(code)
        
        assert len(insights) > 0
        assert any(insight.line_number == 1 for insight in insights)
        assert any("variable" in insight.question.lower() for insight in insights)
    
    def test_analyze_code_error_handling(self):
        """Test analysis of error handling."""
        coder = ExistentialCoder()
        code = "try:\n    risky_operation()\nexcept Exception as e:\n    print(e)"
        
        insights = coder.analyze_code(code)
        
        assert len(insights) > 0
        assert any(insight.line_number == 3 for insight in insights)
        assert any("error" in insight.question.lower() for insight in insights)
    
    def test_analyze_code_empty(self):
        """Test analysis of empty code."""
        coder = ExistentialCoder()
        code = ""
        
        insights = coder.analyze_code(code)
        
        assert len(insights) == 0
    
    def test_analyze_code_comments_only(self):
        """Test analysis of code with only comments."""
        coder = ExistentialCoder()
        code = "# This is a comment\n# Another comment"
        
        insights = coder.analyze_code(code)
        
        assert len(insights) == 0
    
    def test_generate_commit_message_refactor(self):
        """Test commit message generation for refactoring."""
        coder = ExistentialCoder()
        changes = ["refactored user authentication", "restructured database layer"]
        
        message = coder.generate_commit_message(changes)
        
        assert "refactor" in message.lower()
        assert "?" in message  # Should be philosophical
    
    def test_generate_commit_message_fix(self):
        """Test commit message generation for bug fixes."""
        coder = ExistentialCoder()
        changes = ["fixed null pointer exception", "resolved memory leak"]
        
        message = coder.generate_commit_message(changes)
        
        assert "fix" in message.lower() or "bug" in message.lower()
        assert "?" in message  # Should be philosophical
    
    def test_generate_commit_message_feature(self):
        """Test commit message generation for new features."""
        coder = ExistentialCoder()
        changes = ["added new user interface", "implemented search functionality"]
        
        message = coder.generate_commit_message(changes)
        
        assert "add" in message.lower() or "new" in message.lower() or "implement" in message.lower()
        assert "?" in message  # Should be philosophical
    
    def test_generate_commit_message_docs(self):
        """Test commit message generation for documentation."""
        coder = ExistentialCoder()
        changes = ["updated README", "added code comments"]
        
        message = coder.generate_commit_message(changes)
        
        assert "doc" in message.lower() or "readme" in message.lower()
        assert "?" in message  # Should be philosophical
    
    def test_generate_commit_message_test(self):
        """Test commit message generation for tests."""
        coder = ExistentialCoder()
        changes = ["added unit tests", "verified functionality"]
        
        message = coder.generate_commit_message(changes)
        
        assert "test" in message.lower() or "verify" in message.lower()
        assert "?" in message  # Should be philosophical
    
    def test_generate_commit_message_general(self):
        """Test commit message generation for general changes."""
        coder = ExistentialCoder()
        changes = ["made some changes"]
        
        message = coder.generate_commit_message(changes)
        
        assert "?" in message  # Should be philosophical
        assert len(message) > 0
    
    def test_classify_changes_refactor(self):
        """Test change classification for refactoring."""
        coder = ExistentialCoder()
        changes = ["refactored the code", "restructured modules"]
        
        result = coder._classify_changes(changes)
        assert result == "refactor"
    
    def test_classify_changes_fix(self):
        """Test change classification for bug fixes."""
        coder = ExistentialCoder()
        changes = ["fixed the bug", "resolved the issue"]
        
        result = coder._classify_changes(changes)
        assert result == "fix"
    
    def test_classify_changes_feature(self):
        """Test change classification for new features."""
        coder = ExistentialCoder()
        changes = ["added new feature", "implemented functionality"]
        
        result = coder._classify_changes(changes)
        assert result == "feature"
    
    def test_classify_changes_docs(self):
        """Test change classification for documentation."""
        coder = ExistentialCoder()
        changes = ["updated documentation", "added comments"]
        
        result = coder._classify_changes(changes)
        assert result == "docs"
    
    def test_classify_changes_test(self):
        """Test change classification for tests."""
        coder = ExistentialCoder()
        changes = ["added tests", "verified behavior"]
        
        result = coder._classify_changes(changes)
        assert result == "test"
    
    def test_classify_changes_general(self):
        """Test change classification for general changes."""
        coder = ExistentialCoder()
        changes = ["made some changes"]
        
        result = coder._classify_changes(changes)
        assert result == "general"
