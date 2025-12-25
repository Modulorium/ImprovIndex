export enum ActivityType {
  WARMUP = 'warmup', // very brief and simple with no skill to learn
  EXERCISE = 'exercise', // very specific game used to teach a specific skill
  DRILL = 'drill', // repetitive game used to practice a specific skill
  GAME = 'game', // full improv game with multiple potential skills
}

export enum ActivityField {
  SHORT_FORM = 'short_form', // improv games built around the idea that a game has already been established
  LONG_FORM = 'long_form', // improv games built around the idea of finding the game asynchronously during play
}

export enum ActivityTag {
  SCENE = 'scene', // games focused on creating a scene
  BACKLINE = 'backline', // games where most players are on the sidelines
  GAUNTLET = 'gauntlet', // a specific formation is used for quick drills
  JUMPOUT = 'jumpout', // games where players have the initiative to jump in
  COMPETITIVE = 'competitive', // games with competitive elements
  GUESSING = 'guessing', // games involving guessing elements
  MUSICAL = 'musical', // games involving music or singing
  HOSTED = 'hosted', // games that require a host or moderator
  ASSISTED = 'assisted', // games that require assistance by other performers
  NARRATIVE = 'narrative', // games focused on storytelling
  PHYSICAL = 'physical', // games that require significant physical movement
}

export enum ActivityLevel {
  BEGINNER = 'beginner', // suitable for new improvisers
  INTERMEDIATE = 'intermediate', // suitable for improvisers that are aware of foundational concepts like base reality, who what where, and subversion
  ADVANCED = 'advanced', // suitable for improvisers that are aware of advanced concepts like game or actions like heightening, framing, and justification
  EXPERT = 'expert', // suitable for improvisers with a strong understanding of long form structure, character work, and in depth theory
}

export enum ActivityComplexity {
  VERY_LOW = 'very_low', // 1 rule, no special instructions, purely reactive
  LOW = 'low', // 1-2 rules, rarely asked questions
  MEDIUM = 'medium', // 2-3 rules, timing or cue-based, requires example
  HIGH = 'high', // rules affect each other, requires multiple examples
  VERY_HIGH = 'very_high', // many rules, complex interactions, requires detailed explanation and knowledge
}

export enum ActivitySkillCeiling {
  LOW = 'low', // minimal skill development possible once rule is understood
  MEDIUM = 'medium', // player can notice some skill development over time, theory can be applied
  HIGH = 'high', // practice can lead to significant skill development and improvement of scene quality
  ENDLESS = 'endless', // infinite potential for skill development and mastery over time, no ceiling
}

export enum ActivitySkill {
  FRAMING = 'framing', // skills around establishing context within a scene so that a scene partner is aware of the game
  HEIGHTENING = 'heightening', // skills around increasing the stakes of a scene through actions and dialogue
  JUSTIFICATION = 'justification', // skills around providing reasons or motivations for actions within a scene
  REACTION = 'reaction', // skills around responding appropriately to scene partners and situations
  LISTENING = 'listening', // skills around actively hearing and understanding scene partners
  PHYSICALITY = 'physicality', // skills around using the body effectively in a scene
  COMMITMENT = 'commitment', // skills around fully engaging and dedicating to a scene or character
  RELATIONSHIP = 'relationship', // skills around establishing and maintaining relationships between characters in a scene
  BASE_REALITY = 'base_reality', // skills around creating a believable and consistent world within a scene
}

export enum PhysicalityLevel {
  NONE = 'none', // no physical movement required
  HALF_BODY = 'half_body', // requires upper body movement
  FULL_BODY = 'full_body', // requires full body movement
}

export enum VocalityLevel {
  NONE = 'none', // no vocalization required
  TEXT = 'text', // can be done with text communication
  VOCAL = 'vocal', // requires voice communication
}

export class PlayerRequirement {
  minimum: number = 0;
  recommended: number = 0;
}

export class DurationRequirement {
  minimum: number = 0; // seconds
  average: number = 0; // seconds
}

export class PhysicalityRequirement {
  minimum: PhysicalityLevel = PhysicalityLevel.HALF_BODY;
  recommended: PhysicalityLevel = PhysicalityLevel.HALF_BODY;
}

export class VocalityRequirement {
  minimum: VocalityLevel = VocalityLevel.VOCAL;
  recommended: VocalityLevel = VocalityLevel.VOCAL;
}

export class ActivityTips {
  generic: string[] = [];
  host: string[] = [];
  player: string[] = [];
}

export class ActivityRequirements {
  players: PlayerRequirement = new PlayerRequirement();
  duration: DurationRequirement = new DurationRequirement();
  physicality: PhysicalityRequirement = new PhysicalityRequirement();
  vocality: VocalityRequirement = new VocalityRequirement();
}

export class ImprovActivity {
  id: string = '';
  updated_at: string = '';

  name: string[] = [];
  brief: string = ''; // 50 character limit
  summary: string = ''; // 200 character limit
  description: string = ''; // 500 character limit

  tips: ActivityTips = new ActivityTips();
  requirements: ActivityRequirements = new ActivityRequirements();

  tags: Set<ActivityTag> = new Set();
  skills: Set<ActivitySkill> = new Set();

  field: ActivityField = ActivityField.SHORT_FORM;
  type: ActivityType = ActivityType.GAME;
  level: ActivityLevel = ActivityLevel.BEGINNER;
  complexity: ActivityComplexity = ActivityComplexity.VERY_LOW;
  skill_ceiling: ActivitySkillCeiling = ActivitySkillCeiling.LOW;

  parent: string | null = null;
  variants: string[] = [];

  credits: string[] = [];
  sources: string[] = [];
}
