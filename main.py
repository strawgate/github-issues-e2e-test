"""
G.I.T.H.U.B. - The Existential Code Companion

Generally Introspective Text Handler for Unrealized Brilliance

This is the main entry point for the G.I.T.H.U.B. application.
"""

from src.existential_coder import ExistentialCoder
from src.philosopher_agent import PhilosopherAgent
from src.zen_master import ZenMaster
from src.oracle import Oracle
from src.utils import contemplate_code, find_meaning_in_bugs


def main():
    """
    The main function that demonstrates the power of G.I.T.H.U.B.
    
    This function showcases the existential coding companion's abilities
    to provide philosophical insights and wisdom to developers.
    """
    print("🧘 Welcome to G.I.T.H.U.B. - The Existential Code Companion")
    print("=" * 60)
    print("Generally Introspective Text Handler for Unrealized Brilliance")
    print("=" * 60)
    print()
    
    # Initialize the existential coder
    coder = ExistentialCoder()
    
    # Sample code to analyze
    sample_code = '''
def hello_world():
    """A simple function that greets the world."""
    print("Hello, World!")
    return "greeting_complete"

if __name__ == "__main__":
    result = hello_world()
    print(f"The result is: {result}")
'''
    
    print("🔍 Analyzing sample code for existential meaning...")
    print("-" * 50)
    print(sample_code)
    print("-" * 50)
    print()
    
    # Analyze the code
    insights = coder.analyze_code(sample_code, "sample.py")
    
    print("🤔 Philosophical Insights:")
    print("=" * 30)
    for i, insight in enumerate(insights, 1):
        if insight.line_number:
            print(f"Line {insight.line_number}: {insight.question}")
        else:
            print(f"General: {insight.question}")
        print(f"Wisdom: {insight.wisdom}")
        print()
    
    # Demonstrate other components
    print("🧘 Zen Master's Wisdom:")
    print("=" * 25)
    zen_master = ZenMaster()
    wisdom = zen_master.provide_wisdom("stuck debugging")
    print(wisdom)
    print()
    
    print("🔮 Oracle's Prophecy:")
    print("=" * 20)
    oracle = Oracle()
    prophecy = oracle.consult("What does the future hold for my code?")
    print(prophecy)
    print()
    
    print("💭 Philosopher's Contemplation:")
    print("=" * 30)
    philosopher = PhilosopherAgent()
    contemplation = philosopher.contemplate("Why do we write code?")
    print(contemplation)
    print()
    
    print("✨ The journey of digital enlightenment continues...")
    print("Remember: Every line of code is a step on the path to wisdom.")


if __name__ == "__main__":
    main()
