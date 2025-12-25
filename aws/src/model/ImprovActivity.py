from enum import Enum
from typing import List

class ImprovActivity:
    
    def __init__(self):
        self.id: str = ""
        self.updated_at: str = ""

        self.name: List[str] = []
        self.brief: str = ""
        self.summary: str = ""
        self.description: str = ""

        self.tips: ActivityTips = ActivityTips()

        self.requirements: ActivityRequirements = ActivityRequirements()
        
        self.tags: set[ActivityTag] = set()
        self.skills: set[ActivitySkill] = set()

        self.field: ActivityField = ActivityField.SHORT_FORM
        self.type: ActivityType = ActivityType.GAME
        self.level: ActivityLevel = ActivityLevel.BEGINNER
        self.complexity: ActivityComplexity = ActivityComplexity.VERY_LOW
        self.skill_ceiling: ActivitySkillCeiling = ActivitySkillCeiling.LOW

        self.parent: str|None = None
        self.variants: List[str] = []

        self.credits: List[str] = []
        self.sources: List[str] = []

class ActivityTips():
    def __init__(self):
        self.generic: List[str] = []
        self.host: List[str] = []
        self.player: List[str] = []
        
class ActivityRequirements():
    def __init__(self):
        self.players: PlayerRequirement = PlayerRequirement()
        self.duration: DurationRequirement = DurationRequirement()
        self.physicality: PhysicalityRequirement = PhysicalityRequirement()
        self.vocality: VocalityRequirement = VocalityRequirement()

class PlayerRequirement():

    def __init__(self):
        self.minimum: int = 0
        self.recommended: int = 0

class DurationRequirement():
    def __init__(self):
        self.minimum: int = 0
        self.average: int = 0

class PhysicalityRequirement():
    def __init__(self):
        self.minimum: PhysicalityLevel = PhysicalityLevel.HALF_BODY
        self.recommended: PhysicalityLevel = PhysicalityLevel.HALF_BODY

class VocalityRequirement():
    def __init__(self):
        self.minimum: VocalityLevel = VocalityLevel.VOCAL
        self.recommended: VocalityLevel = VocalityLevel.VOCAL

class ActivityType(Enum):
    WARMUP = "warmup" # very brief and simple with no skill to learn
    EXERCISE = "exercise" # very specific game used to teach a specific skill
    DRILL = "drill" # repetitive game used to practice a specific skill
    GAME = "game" # full improv game with multiple potential skills
    
class ActivityField(Enum):
    SHORT_FORM = "short_form" # improv games built around the idea that a game has already been established
    LONG_FORM = "long_form" # improv games built around the idea of finding the game asychronously during play

class ActivityTag(Enum):
    SCENE = "scene" # games focused on creating a scene
    BACKLINE = "backline" # games where most players are on the sidelines
    GAUNTLET = "gauntlet" # a specific formation is used for quick drills
    JUMPOUT = "jumpout" # games where players have the initiative to jump in
    COMPETITIVE = "competitive" # games with competitive elements
    GUESSING = "guessing" # games involving guessing elements
    MUSICAL = "musical" # games involving music or singing
    HOSTED = "hosted" # games that require a host or moderator
    ASSISTED = "assisted" # games that require assistance by other performers
    NARRATIVE = "narrative" # games focused on storytelling
    PHYSICAL = "physical" # games that require significant physical movement

class ActivityLevel(Enum):
    BEGINNER = "beginner" # suitable for new improvisers
    INTERMEDIATE = "intermediate" # suitable for improvisers that are aware of foundational concepts like base reality, who what where, and subversion
    ADVANCED = "advanced" # suitable for improvisers that are aware of advanced concepts like game or actions like heightening, framing, and justification
    EXPERT = "expert" # suitable for improvisers with a strong understanding of long form structure, character work, and in depth theory

class ActivityComplexity(Enum):
    VERY_LOW = "very_low" # 1 rule, no special instructions, purely reactive
    LOW = "low" # 1-2 rules, rarely asked questions
    MEDIUM = "medium" # 2-3 rules, timing or cue-based, requires example
    HIGH = "high" # rules affect each other, requires multiple examples
    VERY_HIGH = "very_high" # many rules, complex interactions, requires detailed explanation and knowledge

class ActivitySkillCeiling(Enum):
    LOW = "low" # no skill development possible once rule is understood
    MEDIUM = "medium" # player can notice some skill development over time, theory can be applied
    HIGH = "high" # practice can lead to significant skill development and improvement of scene quality
    ENDLESS = "endless" # infinite potential for skill development and mastery over time, no ceiling

class ActivitySkill(Enum):
    FRAMING = "framing" # skills around establishing context within a scene so that a scene partner is aware of the game
    HEIGHTENING = "heightening" # skills around increasing the stakes of a scene through actions and dialogue
    JUSTIFICATION = "justification" # skills around providing reasons or motivations for actions within a scene
    REACTION = "reaction" # skills around responding appropriately to scene partners and situations
    LISTENING = "listening" # skills around actively hearing and understanding scene partners
    PHYSICALITY = "physicality" # skills around using the body effectively in a scene
    COMMITMENT = "commitment" # skills around fully engaging and dedicating to a scene or character
    RELATIONSHIP = "relationship" # skills around establishing and maintaining relationships between characters in a scene
    BASE_REALITY = "base_reality" # skills around creating a believable and consistent world within a scene

class PhysicalityLevel(Enum):
    NONE = "none" # no physical movement required
    HALF_BODY = "half_body" # requires upper body movement
    FULL_BODY = "full_body" # requires full body movement

class VocalityLevel(Enum):
    NONE = "none" # no vocalization required
    TEXT = "text" # can be done with text communication
    VOCAL = "vocal" # requires voice communication
