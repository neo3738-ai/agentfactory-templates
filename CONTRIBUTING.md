# Contributing Templates to Agentfactory

Thanks for sharing your template with the community!

## How to Submit

1. Fork this repository
2. Create a folder: `<category>/<your-template-id>/`
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
| custom | Everything else |

## Guidelines

- Templates should be useful to others, not just yourself
- Include a clear README with usage examples
- Don't include API keys or personal data
- Test your template in Agentfactory before submitting
- One template per pull request for easier review
