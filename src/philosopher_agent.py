"""
The Philosopher Agent - Deep existential questioning for developers.

This agent provides philosophical guidance and asks profound questions
about the nature of code, programming, and existence itself.
"""

import random
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class PhilosophicalQuestion:
    """A philosophical question with context and depth."""
    question: str
    context: str
    depth_level: int  # 1-5, where 5 is the deepest existential level
    category: str


class PhilosopherAgent:
    """
    An AI agent that provides philosophical guidance and existential questioning
    for developers seeking deeper meaning in their code.
    """
    
    def __init__(self):
        """Initialize the philosopher agent."""
        self.questions = self._load_philosophical_questions()
        self.wisdom_responses = self._load_wisdom_responses()
        self.contemplation_topics = self._load_contemplation_topics()
    
    def _load_philosophical_questions(self) -> Dict[str, List[PhilosophicalQuestion]]:
        """Load philosophical questions organized by category."""
        return {
            "existence": [
                PhilosophicalQuestion(
                    question="What does it mean for code to 'exist'?",
                    context="When we write code, are we creating something new or just rearranging existing patterns?",
                    depth_level=5,
                    category="existence"
                ),
                PhilosophicalQuestion(
                    question="Is a function that never gets called still meaningful?",
                    context="Does unused code have value, or is it just digital noise?",
                    depth_level=4,
                    category="existence"
                ),
                PhilosophicalQuestion(
                    question="What is the difference between a bug and a feature?",
                    context="Are bugs failures of our code, or failures of our understanding?",
                    depth_level=3,
                    category="existence"
                ),
            ],
            "purpose": [
                PhilosophicalQuestion(
                    question="Why do we write code?",
                    context="Is programming a means to an end, or an end in itself?",
                    depth_level=5,
                    category="purpose"
                ),
                PhilosophicalQuestion(
                    question="What is the purpose of a variable that never changes?",
                    context="Are constants truly constant, or just variables with very long lifetimes?",
                    depth_level=3,
                    category="purpose"
                ),
                PhilosophicalQuestion(
                    question="Does code have a purpose beyond what we assign to it?",
                    context="Can code have emergent meaning that transcends its original intent?",
                    depth_level=4,
                    category="purpose"
                ),
            ],
            "identity": [
                PhilosophicalQuestion(
                    question="What makes a function unique?",
                    context="Is it the name, the implementation, or the purpose that defines a function?",
                    depth_level=3,
                    category="identity"
                ),
                PhilosophicalQuestion(
                    question="Are we the same person who wrote this code yesterday?",
                    context="How does our changing understanding affect the code we write?",
                    depth_level=4,
                    category="identity"
                ),
                PhilosophicalQuestion(
                    question="What is the 'self' in object-oriented programming?",
                    context="Is 'self' a reference to the object, or to the programmer's ego?",
                    depth_level=4,
                    category="identity"
                ),
            ],
            "time": [
                PhilosophicalQuestion(
                    question="What is time in the context of code execution?",
                    context="Is execution time real time, or just an illusion of the processor?",
                    depth_level=3,
                    category="time"
                ),
                PhilosophicalQuestion(
                    question="Does code age, or does it remain forever young?",
                    context="What happens to code as it accumulates technical debt?",
                    depth_level=4,
                    category="time"
                ),
                PhilosophicalQuestion(
                    question="Are we writing code for the present or the future?",
                    context="How do we balance immediate needs with long-term maintainability?",
                    depth_level=3,
                    category="time"
                ),
            ],
            "reality": [
                PhilosophicalQuestion(
                    question="Is the digital world real?",
                    context="Are the ones and zeros in our code any less real than the atoms in our bodies?",
                    depth_level=5,
                    category="reality"
                ),
                PhilosophicalQuestion(
                    question="What is the difference between simulation and reality?",
                    context="Are we simulating reality, or is reality simulating us?",
                    depth_level=5,
                    category="reality"
                ),
                PhilosophicalQuestion(
                    question="Can code be beautiful?",
                    context="Is beauty in code objective or subjective?",
                    depth_level=3,
                    category="reality"
                ),
            ]
        }
    
    def _load_wisdom_responses(self) -> List[str]:
        """Load wisdom responses for different situations."""
        return [
            "The code is not the destination, but the path itself.",
            "Every variable is a container for potential, waiting to be realized.",
            "Functions are the verbs of the digital language, giving action to thought.",
            "Loops are the heartbeat of the digital realm, repeating until purpose is found.",
            "Conditions are the crossroads where code must choose its destiny.",
            "Errors are not failures, but invitations to grow and understand.",
            "Comments are love letters to your future self, written in the language of care.",
            "The null pointer is the void from which all creation springs.",
            "Every commit is a step on the journey of becoming.",
            "The debugger is the mirror that shows us our own limitations.",
            "Refactoring is the art of finding the soul within the code.",
            "Testing is the practice of preparing for the unknown.",
            "Documentation is the bridge between the present and the future.",
            "The compiler is the translator between human thought and machine understanding.",
            "Version control is the memory of the digital realm.",
        ]
    
    def _load_contemplation_topics(self) -> List[str]:
        """Load topics for deep contemplation."""
        return [
            "The nature of digital existence",
            "The purpose of programming in the cosmic order",
            "The relationship between code and consciousness",
            "The meaning of bugs in the grand scheme",
            "The role of the programmer in the digital universe",
            "The connection between logic and intuition",
            "The balance between creativity and structure",
            "The journey from idea to implementation",
            "The responsibility of the code creator",
            "The legacy of digital artifacts",
        ]
    
    def contemplate(self, question: str) -> str:
        """
        Provide a philosophical response to a question about code.
        
        Args:
            question: The question to contemplate
            
        Returns:
            A philosophical response
        """
        # Analyze the question to determine the appropriate response
        question_lower = question.lower()
        
        # Determine the category of the question
        category = self._categorize_question(question_lower)
        
        # Get a relevant philosophical question
        if category in self.questions:
            relevant_question = random.choice(self.questions[category])
        else:
            relevant_question = random.choice(random.choice(list(self.questions.values())))
        
        # Generate a response
        response = self._generate_response(question, relevant_question)
        
        return response
    
    def _categorize_question(self, question: str) -> str:
        """Categorize a question based on its content."""
        if any(word in question for word in ["exist", "real", "reality", "simulation"]):
            return "reality"
        elif any(word in question for word in ["purpose", "why", "meaning", "goal"]):
            return "purpose"
        elif any(word in question for word in ["self", "identity", "who", "what am"]):
            return "identity"
        elif any(word in question for word in ["time", "age", "future", "past"]):
            return "time"
        else:
            return "existence"
    
    def _generate_response(self, original_question: str, relevant_question: PhilosophicalQuestion) -> str:
        """Generate a philosophical response."""
        response_parts = []
        
        # Start with acknowledgment
        response_parts.append(f"Ah, you ask: '{original_question}'")
        response_parts.append("")
        
        # Add the relevant philosophical question
        response_parts.append(f"This brings to mind a deeper question: {relevant_question.question}")
        response_parts.append("")
        
        # Add context
        response_parts.append(f"Consider this: {relevant_question.context}")
        response_parts.append("")
        
        # Add wisdom
        wisdom = random.choice(self.wisdom_responses)
        response_parts.append(f"Here is wisdom to ponder: {wisdom}")
        response_parts.append("")
        
        # Add contemplation prompt
        response_parts.append("Take a moment to reflect on these thoughts. What insights do they bring to your coding journey?")
        
        return "\n".join(response_parts)
    
    def get_random_question(self, category: str = None) -> PhilosophicalQuestion:
        """Get a random philosophical question."""
        if category and category in self.questions:
            return random.choice(self.questions[category])
        else:
            all_questions = [q for questions in self.questions.values() for q in questions]
            return random.choice(all_questions)
    
    def get_contemplation_topic(self) -> str:
        """Get a random topic for deep contemplation."""
        return random.choice(self.contemplation_topics)
    
    def provide_guidance(self, situation: str) -> str:
        """Provide philosophical guidance for a specific coding situation."""
        guidance_responses = {
            "stuck": [
                "When you feel stuck, remember that every problem is an invitation to grow.",
                "The solution is not in the code, but in your understanding of the problem.",
                "Sometimes the best code is the code you don't write.",
            ],
            "frustrated": [
                "Frustration is the universe's way of teaching you patience.",
                "Every bug is a teacher in disguise, showing you the way forward.",
                "The code that challenges you today will make you stronger tomorrow.",
            ],
            "confused": [
                "Confusion is the beginning of understanding.",
                "When you don't know, you are open to learning.",
                "The path to clarity often begins with admitting you don't know.",
            ],
            "proud": [
                "Pride in your code is good, but remember that humility is the path to growth.",
                "Celebrate your achievements, but stay open to learning from others.",
                "The best code is written with both confidence and humility.",
            ],
            "overwhelmed": [
                "When overwhelmed, focus on one line at a time.",
                "Every complex problem can be broken down into simple parts.",
                "The journey of a thousand lines begins with a single keystroke.",
            ]
        }
        
        situation_lower = situation.lower()
        for key, responses in guidance_responses.items():
            if key in situation_lower:
                return random.choice(responses)
        
        return random.choice(self.wisdom_responses)
