"""
The Zen Master - Mindfulness and balance for developers.

This module provides zen wisdom and mindfulness guidance for developers
seeking balance and peace in their coding journey.
"""

import random
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum


class ZenLevel(Enum):
    """Levels of zen mastery."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    MASTER = "master"


@dataclass
class ZenWisdom:
    """A piece of zen wisdom with context."""
    wisdom: str
    context: str
    level: ZenLevel
    category: str


class ZenMaster:
    """
    A zen master that provides mindfulness guidance and wisdom
    for developers seeking balance and peace in their coding journey.
    """
    
    def __init__(self, level: ZenLevel = ZenLevel.INTERMEDIATE):
        """Initialize the zen master."""
        self.level = level
        self.wisdom_collection = self._load_zen_wisdom()
        self.meditation_guidance = self._load_meditation_guidance()
        self.breathing_exercises = self._load_breathing_exercises()
    
    def _load_zen_wisdom(self) -> Dict[str, List[ZenWisdom]]:
        """Load zen wisdom organized by category."""
        return {
            "patience": [
                ZenWisdom(
                    wisdom="The bug that cannot be fixed today will teach you tomorrow.",
                    context="Patience is not the ability to wait, but how you behave while waiting.",
                    level=ZenLevel.BEGINNER,
                    category="patience"
                ),
                ZenWisdom(
                    wisdom="A thousand lines of code begin with a single keystroke.",
                    context="Every journey starts with a single step, every program with a single line.",
                    level=ZenLevel.INTERMEDIATE,
                    category="patience"
                ),
                ZenWisdom(
                    wisdom="The compiler that runs slowly is teaching you to breathe.",
                    context="Speed is not always the goal; sometimes the process is the teacher.",
                    level=ZenLevel.ADVANCED,
                    category="patience"
                ),
            ],
            "acceptance": [
                ZenWisdom(
                    wisdom="Accept the code as it is, then improve it.",
                    context="Acceptance is not resignation; it's the foundation of change.",
                    level=ZenLevel.BEGINNER,
                    category="acceptance"
                ),
                ZenWisdom(
                    wisdom="The error message is not your enemy, but your teacher.",
                    context="Resistance to what is creates suffering; acceptance creates peace.",
                    level=ZenLevel.INTERMEDIATE,
                    category="acceptance"
                ),
                ZenWisdom(
                    wisdom="Perfect code is an illusion; beautiful code is reality.",
                    context="Perfection is the enemy of progress; beauty is the goal.",
                    level=ZenLevel.ADVANCED,
                    category="acceptance"
                ),
            ],
            "mindfulness": [
                ZenWisdom(
                    wisdom="Code with awareness, not just intention.",
                    context="Mindfulness is being present with your code, not just writing it.",
                    level=ZenLevel.BEGINNER,
                    category="mindfulness"
                ),
                ZenWisdom(
                    wisdom="The present moment is the only time you can write code.",
                    context="Past code is memory, future code is imagination, present code is reality.",
                    level=ZenLevel.INTERMEDIATE,
                    category="mindfulness"
                ),
                ZenWisdom(
                    wisdom="When you are fully present, the code writes itself.",
                    context="True mastery comes when the doer disappears and only the doing remains.",
                    level=ZenLevel.MASTER,
                    category="mindfulness"
                ),
            ],
            "balance": [
                ZenWisdom(
                    wisdom="Balance is not about equal time, but about equal presence.",
                    context="Quality of attention matters more than quantity of time.",
                    level=ZenLevel.BEGINNER,
                    category="balance"
                ),
                ZenWisdom(
                    wisdom="The best code is written in the space between work and rest.",
                    context="Balance is not a destination, but a way of traveling.",
                    level=ZenLevel.INTERMEDIATE,
                    category="balance"
                ),
                ZenWisdom(
                    wisdom="When you find balance, the code finds you.",
                    context="Balance is not something you achieve, but something you become.",
                    level=ZenLevel.ADVANCED,
                    category="balance"
                ),
            ],
            "simplicity": [
                ZenWisdom(
                    wisdom="The simplest code is often the most profound.",
                    context="Simplicity is the ultimate sophistication in the digital realm.",
                    level=ZenLevel.BEGINNER,
                    category="simplicity"
                ),
                ZenWisdom(
                    wisdom="Remove everything that is not essential, and what remains is truth.",
                    context="In code, as in life, less is often more.",
                    level=ZenLevel.INTERMEDIATE,
                    category="simplicity"
                ),
                ZenWisdom(
                    wisdom="The empty function is full of potential.",
                    context="Sometimes the most powerful code is the code that does nothing.",
                    level=ZenLevel.ADVANCED,
                    category="simplicity"
                ),
            ]
        }
    
    def _load_meditation_guidance(self) -> List[str]:
        """Load meditation guidance for developers."""
        return [
            "Sit comfortably and focus on your breath. With each inhale, imagine drawing in clarity. With each exhale, release the tension of debugging.",
            "Close your eyes and visualize your code as a flowing river. Watch the data flow through your functions like water over stones.",
            "Take a moment to appreciate the silence between keystrokes. In this silence, wisdom speaks.",
            "Imagine each line of code as a step on a path. Where does this path lead? What is your destination?",
            "Focus on the present moment. You are here, now, writing code. Nothing else exists in this moment.",
            "Visualize your bugs as teachers. What are they trying to teach you? Listen with an open heart.",
            "Breathe in the possibility of perfect code. Breathe out the reality of imperfect code. Both are true.",
            "Imagine your code as a garden. What seeds are you planting? What will grow from your efforts?",
            "Focus on the rhythm of your typing. Let it become a meditation, a prayer to the digital gods.",
            "Take a moment to appreciate the miracle of code. From nothing, you create something that can think, act, and transform the world.",
        ]
    
    def _load_breathing_exercises(self) -> List[Dict[str, Any]]:
        """Load breathing exercises for developers."""
        return [
            {
                "name": "The Debugger's Breath",
                "description": "A breathing exercise for when you're stuck debugging",
                "steps": [
                    "Inhale for 4 counts while thinking 'I am calm'",
                    "Hold for 4 counts while thinking 'I am focused'",
                    "Exhale for 4 counts while thinking 'I will find the solution'",
                    "Hold for 4 counts while thinking 'I am patient'"
                ],
                "duration": "2-3 minutes"
            },
            {
                "name": "The Coder's Flow",
                "description": "A breathing exercise for entering flow state",
                "steps": [
                    "Inhale deeply and slowly",
                    "Exhale completely and slowly",
                    "Repeat 5 times",
                    "On the 6th breath, begin coding"
                ],
                "duration": "1-2 minutes"
            },
            {
                "name": "The Refactor's Rest",
                "description": "A breathing exercise for when refactoring becomes overwhelming",
                "steps": [
                    "Inhale while thinking 'I accept what is'",
                    "Exhale while thinking 'I can improve it'",
                    "Inhale while thinking 'I am capable'",
                    "Exhale while thinking 'I will succeed'"
                ],
                "duration": "3-5 minutes"
            }
        ]
    
    def provide_wisdom(self, situation: str = None) -> str:
        """
        Provide zen wisdom for a specific situation or general guidance.
        
        Args:
            situation: The situation to provide wisdom for
            
        Returns:
            A piece of zen wisdom
        """
        if situation:
            category = self._categorize_situation(situation)
            if category in self.wisdom_collection:
                wisdom = random.choice(self.wisdom_collection[category])
                return f"{wisdom.wisdom}\n\n{wisdom.context}"
        
        # Return random wisdom
        all_wisdom = [w for wisdom_list in self.wisdom_collection.values() for w in wisdom_list]
        wisdom = random.choice(all_wisdom)
        return f"{wisdom.wisdom}\n\n{wisdom.context}"
    
    def _categorize_situation(self, situation: str) -> str:
        """Categorize a situation to provide appropriate wisdom."""
        situation_lower = situation.lower()
        
        if any(word in situation_lower for word in ["stuck", "blocked", "can't", "unable"]):
            return "patience"
        elif any(word in situation_lower for word in ["error", "bug", "broken", "failed"]):
            return "acceptance"
        elif any(word in situation_lower for word in ["distracted", "unfocused", "scattered"]):
            return "mindfulness"
        elif any(word in situation_lower for word in ["tired", "overwhelmed", "stressed"]):
            return "balance"
        elif any(word in situation_lower for word in ["complex", "complicated", "messy"]):
            return "simplicity"
        else:
            return "mindfulness"
    
    def guide_meditation(self, duration: int = 5) -> str:
        """
        Guide a meditation session for developers.
        
        Args:
            duration: Duration of meditation in minutes
            
        Returns:
            Meditation guidance
        """
        guidance = random.choice(self.meditation_guidance)
        
        return f"""
🧘 Meditation Guidance ({duration} minutes)

{guidance}

Take {duration} minutes to practice this meditation. 
When you return, your code will be waiting for you with fresh eyes and an open heart.

Remember: The best code is written from a place of inner peace.
"""
    
    def suggest_breathing_exercise(self, situation: str = None) -> Dict[str, Any]:
        """
        Suggest a breathing exercise for a specific situation.
        
        Args:
            situation: The situation to suggest an exercise for
            
        Returns:
            A breathing exercise recommendation
        """
        if situation:
            situation_lower = situation.lower()
            if "debug" in situation_lower or "stuck" in situation_lower:
                return self.breathing_exercises[0]  # Debugger's Breath
            elif "flow" in situation_lower or "focus" in situation_lower:
                return self.breathing_exercises[1]  # Coder's Flow
            elif "refactor" in situation_lower or "overwhelmed" in situation_lower:
                return self.breathing_exercises[2]  # Refactor's Rest
        
        return random.choice(self.breathing_exercises)
    
    def provide_daily_affirmation(self) -> str:
        """Provide a daily affirmation for developers."""
        affirmations = [
            "I am a creator in the digital realm, bringing ideas to life through code.",
            "Every bug I encounter is an opportunity to grow and learn.",
            "My code is a reflection of my inner state; I write with peace and clarity.",
            "I am patient with my code and patient with myself.",
            "I trust in the process of creation, knowing that every line serves a purpose.",
            "I am grateful for the ability to create and solve problems through code.",
            "My code is beautiful because it comes from a place of love and intention.",
            "I am constantly learning and growing as a developer and as a person.",
            "I write code not just for functionality, but for the joy of creation.",
            "I am at peace with the unknown, knowing that solutions will reveal themselves.",
        ]
        
        return random.choice(affirmations)
    
    def assess_zen_level(self, responses: List[str]) -> ZenLevel:
        """
        Assess the user's zen level based on their responses.
        
        Args:
            responses: List of user responses to zen questions
            
        Returns:
            The assessed zen level
        """
        # This is a simplified assessment - in reality, this would be more complex
        zen_indicators = {
            "patience": ["wait", "time", "slow", "patient"],
            "acceptance": ["accept", "okay", "fine", "understand"],
            "mindfulness": ["present", "now", "aware", "focused"],
            "balance": ["balance", "harmony", "peace", "calm"],
            "simplicity": ["simple", "clear", "minimal", "essential"]
        }
        
        score = 0
        for response in responses:
            response_lower = response.lower()
            for category, indicators in zen_indicators.items():
                if any(indicator in response_lower for indicator in indicators):
                    score += 1
        
        if score >= 15:
            return ZenLevel.MASTER
        elif score >= 10:
            return ZenLevel.ADVANCED
        elif score >= 5:
            return ZenLevel.INTERMEDIATE
        else:
            return ZenLevel.BEGINNER
