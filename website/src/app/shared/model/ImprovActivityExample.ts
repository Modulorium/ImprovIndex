import {
  ImprovActivity,
  ActivityType,
  ActivityField,
  ActivityTag,
  ActivityLevel,
  ActivityComplexity,
  ActivitySkillCeiling,
  ActivitySkill,
  PhysicalityLevel,
  VocalityLevel,
} from './ImprovActivity';

export class ImprovActivityExample {
  static getExample(): ImprovActivity {
    const activity = new ImprovActivity();

    activity.id = 'example-activity-001';
    activity.updated_at = new Date().toISOString();

    activity.name = ['Example Activity', 'Example Game'];
    activity.brief = 'A brief description of the example activity';
    activity.description =
      'A more detailed description explaining how the activity works, the rules, and what to expect when performing it.';

    activity.tips.generic = ['Tip 1 for everyone', 'Tip 2 for everyone'];
    activity.tips.host = ['Tip for the host'];
    activity.tips.player = ['Tip for players'];

    activity.requirements.players.minimum = 2;
    activity.requirements.players.recommended = 4;

    activity.requirements.duration.minimum = 5;
    activity.requirements.duration.average = 10;

    activity.requirements.physicality.minimum = PhysicalityLevel.HALF_BODY;
    activity.requirements.physicality.recommended = PhysicalityLevel.FULL_BODY;

    activity.requirements.vocality.minimum = VocalityLevel.VOCAL;
    activity.requirements.vocality.recommended = VocalityLevel.VOCAL;

    activity.tags = new Set([ActivityTag.SCENE, ActivityTag.NARRATIVE]);
    activity.skills = new Set([ActivitySkill.LISTENING, ActivitySkill.COMMITMENT]);

    activity.field = ActivityField.SHORT_FORM;
    activity.type = ActivityType.GAME;
    activity.level = ActivityLevel.BEGINNER;
    activity.complexity = ActivityComplexity.LOW;
    activity.skill_ceiling = ActivitySkillCeiling.MEDIUM;

    activity.parent = null;
    activity.variants = [];

    activity.credits = ['John Doe'];
    activity.sources = ['Example Source'];

    return activity;
  }
}
