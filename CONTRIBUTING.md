# Contributing Templates to Agentfactory

Thanks for sharing your template with the community!

## Easiest Way: Share from the App

Starting in v0.4.6, you can share templates directly from Agentfactory:

1. Open the template you want to share (pipeline, agent, or council)
2. Click the **Share** button
3. Set up your GitHub token (one-time, stored locally in the vault)
4. Preview and submit — a pull request is created automatically

Community uploads go to `community/<category>/` and are tagged with a "Community" badge in the marketplace.

## Manual Submit (via GitHub)

1. Fork this repository
2. Create a folder: `community/<category>/<your-template-id>/`
3. Add your `template.json` and `README.md`
4. Open a Pull Request

## Template Format

Your `template.json` must follow this structure:

```json
{
  "schema_version": 1,
  "id": "my-template-id",
  "name": "My Template Name",
  "description": "One sentence describing what it does",
  "author": "your-name",
  "category": "productivity",
  "tags": ["tag1", "tag2"],
  "keywords": ["keyword1", "keyword2"],
  "template_type": "pipeline",
  "agents": [
    {
      "name": "Agent Name",
      "role": "role",
      "purpose": "What this agent does",
      "tools": ["web_fetch"],
      "system_prompt_hint": "Key instructions for this agent"
    }
  ],
  "pipeline_shape": [
    { "label": "Step Name", "agent_index": 0, "input_mode": "FromPrevious" }
  ],
  "default_schedule": null,
  "user_fields": [],
  "suggestion_card": {
    "title": "Card Title",
    "subtitle": "Short subtitle",
    "prompt_template": "What the user types to use this"
  }
}
```

See any existing template for a complete example.

## Template Types

| Type | What it packages |
|------|-----------------|
| `pipeline` | Multi-agent workflow with steps |
| `agent` | Single agent blueprint |
| `council` | Council with voting rules and member agents |

## Categories

| Category | For |
|----------|-----|
| information | News, research, monitoring |
| content | Writing, editing, drafting |
| productivity | Planning, organizing, summarizing |
| development | Code review, docs, testing |
| personal | Health, journaling, self-improvement |
| finance | Budgets, price tracking, investing |
| learning | Study aids, flashcards, deep dives |
| data | Analysis, auditing, log parsing |
| automation | Workflows, scheduling, integrations |
| business | Strategy, analysis, planning |
| custom | Everything else |

## Folder Structure

```
agentfactory-templates/
├── information/         # Official templates
│   └── template-id/
├── content/
├── community/           # Community uploads
│   ├── productivity/
│   │   └── my-template/
│   └── development/
└── index.json
```

## Guidelines

- Templates should be useful to others, not just yourself
- Include a clear README with usage examples
- Don't include API keys or personal data
- Test your template in Agentfactory before submitting
- One template per pull request for easier review
