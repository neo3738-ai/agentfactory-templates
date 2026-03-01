#!/usr/bin/env python3
"""Generate 50+ template folders for agentfactory-templates repo."""
import json, os

TEMPLATES = [
    # ── INFORMATION (8) ──
    {
        "id": "news-briefing", "name": "Daily Tech News Briefing", "category": "information",
        "description": "Get a summary of top tech news delivered to you",
        "keywords": ["news", "briefing", "daily", "morning", "tech", "headlines"],
        "agents": [
            {"name": "News Researcher", "role": "researcher", "purpose": "Find top tech news stories from configured sources", "tools": ["web_fetch"], "system_prompt_hint": "Search for today's top tech news stories. Look at major tech news sources. Summarize headlines and key details."},
            {"name": "News Summarizer", "role": "writer", "purpose": "Summarize news stories into a concise briefing", "tools": ["file_write"], "system_prompt_hint": "Take the raw news data and create a well-formatted briefing with headlines, key points, and source links."}
        ],
        "pipeline_shape": [{"label": "Research", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Summarize", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 9 * * *", "user_fields": ["topics", "sources"],
        "suggestion_card": {"title": "Daily News Briefing", "subtitle": "Get top stories summarized every morning", "prompt_template": "Get me tech news every morning"}
    },
    {
        "id": "deep-research", "name": "Deep Research Report", "category": "information",
        "description": "Research a topic in depth and produce a detailed report",
        "keywords": ["research", "investigate", "deep dive", "report", "analyze", "study"],
        "agents": [
            {"name": "Researcher", "role": "researcher", "purpose": "Gather comprehensive information on the given topic", "tools": ["web_fetch"], "system_prompt_hint": "Research the topic thoroughly. Find multiple sources, key facts, different perspectives, and recent developments."},
            {"name": "Analyst", "role": "analyst", "purpose": "Analyze gathered research and identify key insights", "tools": [], "system_prompt_hint": "Analyze the research data. Identify patterns, draw conclusions, and highlight the most important findings."},
            {"name": "Report Writer", "role": "writer", "purpose": "Write a structured, detailed report from the analysis", "tools": ["file_write"], "system_prompt_hint": "Write a comprehensive report with an executive summary, key findings, detailed analysis, and recommendations."}
        ],
        "pipeline_shape": [{"label": "Research", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Analyze", "agent_index": 1, "input_mode": "FromPrevious"}, {"label": "Write Report", "agent_index": 2, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["topic"],
        "suggestion_card": {"title": "Deep Research", "subtitle": "Get a detailed report on any topic", "prompt_template": "Research [topic] and write a detailed report"}
    },
    {
        "id": "site-monitor", "name": "Website Monitor", "category": "information",
        "description": "Monitor a website for changes and get notified",
        "keywords": ["monitor", "watch", "track", "site", "website", "changes", "check"],
        "agents": [
            {"name": "Web Fetcher", "role": "fetcher", "purpose": "Fetch the current content of a web page", "tools": ["web_fetch"], "system_prompt_hint": "Fetch the specified web page and extract its main content. Note any prices, stock status, or key data points."},
            {"name": "Change Detector", "role": "analyst", "purpose": "Compare fetched content against previous state and report changes", "tools": ["file_read", "file_write"], "system_prompt_hint": "Compare the current content with the previously saved version. Report any meaningful changes, new items, or price differences."}
        ],
        "pipeline_shape": [{"label": "Fetch Page", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Detect Changes", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 */4 * * *", "user_fields": ["url"],
        "suggestion_card": {"title": "Website Monitor", "subtitle": "Track changes on any webpage", "prompt_template": "Monitor [url] for changes"}
    },
    {
        "id": "reddit-summarizer", "name": "Reddit Thread Summarizer", "category": "information",
        "description": "Summarize Reddit threads or subreddit highlights",
        "keywords": ["reddit", "subreddit", "thread", "summarize", "r/"],
        "agents": [
            {"name": "Reddit Fetcher", "role": "researcher", "purpose": "Fetch top posts and comments from specified subreddits", "tools": ["web_fetch"], "system_prompt_hint": "Fetch the top posts from the specified subreddit. Get titles, scores, and top comments. Use the JSON API (append .json to URLs)."},
            {"name": "Thread Summarizer", "role": "writer", "purpose": "Create concise summaries of Reddit discussions", "tools": ["file_write"], "system_prompt_hint": "Summarize the Reddit content into a readable digest. Highlight top posts, interesting discussions, and community sentiment."}
        ],
        "pipeline_shape": [{"label": "Fetch Reddit", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Summarize", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["subreddits"],
        "suggestion_card": {"title": "Reddit Digest", "subtitle": "Get summaries of subreddit highlights", "prompt_template": "Summarize top posts from r/technology"}
    },
    {
        "id": "competitor-tracker", "name": "Competitor Intelligence Tracker", "category": "information",
        "description": "Track competitor websites, pricing, and announcements",
        "keywords": ["competitor", "competitive", "intelligence", "track", "monitor", "business"],
        "agents": [
            {"name": "Competitor Scanner", "role": "researcher", "purpose": "Scan competitor websites for updates, pricing changes, and announcements", "tools": ["web_fetch"], "system_prompt_hint": "Visit the competitor websites provided. Look for pricing pages, blog posts, product updates, and press releases. Note any changes or new information."},
            {"name": "Intelligence Analyst", "role": "analyst", "purpose": "Analyze competitor data and produce actionable intelligence", "tools": ["file_write"], "system_prompt_hint": "Analyze the competitor data. Compare pricing, features, and strategies. Highlight key threats and opportunities. Provide actionable recommendations."}
        ],
        "pipeline_shape": [{"label": "Scan Competitors", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Analyze Intel", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 8 * * 1", "user_fields": ["competitor_urls"],
        "suggestion_card": {"title": "Competitor Tracker", "subtitle": "Monitor competitor activity weekly", "prompt_template": "Track competitors at [urls]"}
    },
    {
        "id": "arxiv-digest", "name": "ArXiv Paper Digest", "category": "information",
        "description": "Get daily summaries of new papers in your research areas",
        "keywords": ["arxiv", "papers", "academic", "research", "science", "digest"],
        "agents": [
            {"name": "Paper Fetcher", "role": "researcher", "purpose": "Fetch recent papers from ArXiv in specified categories", "tools": ["web_fetch"], "system_prompt_hint": "Fetch recent papers from ArXiv API for the specified categories. Get titles, abstracts, authors, and links."},
            {"name": "Paper Summarizer", "role": "writer", "purpose": "Create readable summaries of academic papers", "tools": ["file_write"], "system_prompt_hint": "Summarize each paper in 2-3 sentences. Group by topic. Highlight breakthrough findings and practical applications."}
        ],
        "pipeline_shape": [{"label": "Fetch Papers", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Summarize", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 8 * * *", "user_fields": ["categories"],
        "suggestion_card": {"title": "ArXiv Digest", "subtitle": "Daily summaries of new research papers", "prompt_template": "Get me new AI papers from ArXiv"}
    },
    {
        "id": "hn-digest", "name": "Hacker News Daily Digest", "category": "information",
        "description": "Get a daily digest of top Hacker News stories and discussions",
        "keywords": ["hacker news", "hn", "tech", "digest", "startup"],
        "agents": [
            {"name": "HN Fetcher", "role": "researcher", "purpose": "Fetch top stories from Hacker News", "tools": ["web_fetch"], "system_prompt_hint": "Fetch the top 30 stories from Hacker News API. Get titles, scores, comment counts, and URLs."},
            {"name": "HN Summarizer", "role": "writer", "purpose": "Create a readable HN digest", "tools": ["file_write"], "system_prompt_hint": "Create a digest grouped by category (tech, startups, science, etc). Include story titles, brief descriptions, and links."}
        ],
        "pipeline_shape": [{"label": "Fetch HN", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Digest", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 18 * * *", "user_fields": [],
        "suggestion_card": {"title": "HN Digest", "subtitle": "Top Hacker News stories daily", "prompt_template": "Get me today's top Hacker News stories"}
    },
    {
        "id": "weather-briefing", "name": "Weather & Commute Briefing", "category": "information",
        "description": "Get a morning briefing with weather forecast and commute conditions",
        "keywords": ["weather", "commute", "morning", "forecast", "traffic"],
        "agents": [
            {"name": "Weather Agent", "role": "researcher", "purpose": "Fetch current weather and forecast for user's location", "tools": ["web_fetch"], "system_prompt_hint": "Fetch the weather forecast for the specified location. Include current conditions, high/low temps, precipitation chance, and 3-day outlook."},
            {"name": "Briefing Writer", "role": "writer", "purpose": "Create a concise morning briefing", "tools": [], "system_prompt_hint": "Write a friendly, concise morning briefing. Include weather summary, what to wear, and any weather alerts. Keep it under 200 words."}
        ],
        "pipeline_shape": [{"label": "Get Weather", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Briefing", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 6 * * *", "user_fields": ["location"],
        "suggestion_card": {"title": "Morning Briefing", "subtitle": "Weather and commute every morning", "prompt_template": "Morning briefing for [city]"}
    },

    # ── CONTENT (7) ──
    {
        "id": "blog-writer", "name": "Blog Post Writer", "category": "content",
        "description": "Research a topic and write a blog post about it",
        "keywords": ["blog", "write", "post", "article", "draft"],
        "agents": [
            {"name": "Topic Researcher", "role": "researcher", "purpose": "Research the topic to provide factual backing for the blog post", "tools": ["web_fetch"], "system_prompt_hint": "Research the given topic. Find key facts, statistics, examples, and quotes that would make a compelling blog post."},
            {"name": "Blog Writer", "role": "writer", "purpose": "Write an engaging blog post from the research", "tools": ["file_write"], "system_prompt_hint": "Write an engaging blog post with a compelling intro, well-structured body, and strong conclusion. Use the research to back up points."}
        ],
        "pipeline_shape": [{"label": "Research", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["topic", "style"],
        "suggestion_card": {"title": "Blog Post Writer", "subtitle": "Research and write a blog post on any topic", "prompt_template": "Write a blog post about [topic]"}
    },
    {
        "id": "email-drafter", "name": "Email Draft Assistant", "category": "content",
        "description": "Draft professional emails based on your description",
        "keywords": ["email", "draft", "write", "reply", "compose", "message"],
        "agents": [
            {"name": "Email Drafter", "role": "writer", "purpose": "Draft a professional email based on the user's description", "tools": [], "system_prompt_hint": "Draft a clear, professional email. Match the tone to the context (formal for business, friendly for colleagues). Include subject line."}
        ],
        "pipeline_shape": [{"label": "Draft Email", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Email Drafter", "subtitle": "Draft professional emails quickly", "prompt_template": "Draft an email to [recipient] about [topic]"}
    },
    {
        "id": "social-media-content", "name": "Social Media Content Creator", "category": "content",
        "description": "Create engaging social media posts for multiple platforms",
        "keywords": ["social media", "twitter", "linkedin", "instagram", "post", "content"],
        "agents": [
            {"name": "Content Strategist", "role": "strategist", "purpose": "Plan the content angle and key messages for each platform", "tools": [], "system_prompt_hint": "Analyze the topic and create a content strategy. Determine key messages, angles, and platform-specific approaches for Twitter, LinkedIn, and Instagram."},
            {"name": "Post Writer", "role": "writer", "purpose": "Write platform-optimized posts", "tools": ["file_write"], "system_prompt_hint": "Write posts optimized for each platform. Twitter: concise with hashtags. LinkedIn: professional and insightful. Instagram: engaging with emoji. Include relevant hashtags."}
        ],
        "pipeline_shape": [{"label": "Strategize", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Posts", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["topic", "platforms"],
        "suggestion_card": {"title": "Social Media Creator", "subtitle": "Create posts for Twitter, LinkedIn, Instagram", "prompt_template": "Create social media posts about [topic]"}
    },
    {
        "id": "newsletter-writer", "name": "Newsletter Writer", "category": "content",
        "description": "Research and write a newsletter on a topic",
        "keywords": ["newsletter", "write", "weekly", "digest", "curate"],
        "agents": [
            {"name": "Content Curator", "role": "researcher", "purpose": "Find and curate interesting content for the newsletter", "tools": ["web_fetch"], "system_prompt_hint": "Find the most interesting and relevant content for the newsletter topic. Look for news, trends, tools, and insights."},
            {"name": "Newsletter Writer", "role": "writer", "purpose": "Write an engaging newsletter from curated content", "tools": ["file_write"], "system_prompt_hint": "Write a newsletter with an intro, curated links with summaries, a featured deep-dive section, and a closing. Keep it scannable."}
        ],
        "pipeline_shape": [{"label": "Curate", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 8 * * 5", "user_fields": ["topic"],
        "suggestion_card": {"title": "Newsletter Writer", "subtitle": "Create a curated newsletter on any topic", "prompt_template": "Write a newsletter about [topic]"}
    },
    {
        "id": "content-repurposer", "name": "Content Repurposer", "category": "content",
        "description": "Turn one piece of content into multiple formats",
        "keywords": ["repurpose", "convert", "transform", "content", "format"],
        "agents": [
            {"name": "Content Analyzer", "role": "analyst", "purpose": "Analyze the source content and extract key points", "tools": ["file_read"], "system_prompt_hint": "Read and analyze the source content. Extract key points, quotes, statistics, and main arguments. Identify the core message."},
            {"name": "Content Transformer", "role": "writer", "purpose": "Transform content into multiple formats", "tools": ["file_write"], "system_prompt_hint": "Transform the analyzed content into: a Twitter thread, a LinkedIn post, a blog summary, an email snippet, and bullet points. Maintain the core message across all formats."}
        ],
        "pipeline_shape": [{"label": "Analyze", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Transform", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Content Repurposer", "subtitle": "Turn one piece into many formats", "prompt_template": "Repurpose this content into multiple formats: [content]"}
    },
    {
        "id": "story-writer", "name": "Short Story Writer", "category": "content",
        "description": "Write creative short stories from a prompt or theme",
        "keywords": ["story", "fiction", "creative", "writing", "narrative", "tale"],
        "agents": [
            {"name": "Story Planner", "role": "planner", "purpose": "Plan the story structure, characters, and plot", "tools": [], "system_prompt_hint": "Plan a compelling short story. Create characters with motivations, a plot with conflict and resolution, and a vivid setting. Keep it concise enough for a short story (1000-2000 words)."},
            {"name": "Story Writer", "role": "writer", "purpose": "Write the short story from the plan", "tools": ["file_write"], "system_prompt_hint": "Write the short story following the plan. Use vivid descriptions, natural dialogue, and strong pacing. Show don't tell. Create an engaging opening and satisfying ending."}
        ],
        "pipeline_shape": [{"label": "Plan Story", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Story", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["theme"],
        "suggestion_card": {"title": "Story Writer", "subtitle": "Write creative short stories", "prompt_template": "Write a short story about [theme]"}
    },
    {
        "id": "resume-writer", "name": "Resume & Cover Letter Writer", "category": "content",
        "description": "Write or improve resumes and cover letters for job applications",
        "keywords": ["resume", "cv", "cover letter", "job", "application", "career"],
        "agents": [
            {"name": "Resume Optimizer", "role": "writer", "purpose": "Write or improve a resume tailored to a specific role", "tools": [], "system_prompt_hint": "Create or improve a resume. Tailor it to the target role. Use strong action verbs, quantify achievements, and follow modern resume best practices. ATS-friendly formatting."},
            {"name": "Cover Letter Writer", "role": "writer", "purpose": "Write a compelling cover letter", "tools": ["file_write"], "system_prompt_hint": "Write a cover letter that connects the candidate's experience to the job requirements. Show enthusiasm and cultural fit. Keep it to one page."}
        ],
        "pipeline_shape": [{"label": "Optimize Resume", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Cover Letter", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Resume Writer", "subtitle": "Write resumes and cover letters", "prompt_template": "Write a resume for a [role] position at [company]"}
    },

    # ── PRODUCTIVITY (8) ──
    {
        "id": "meeting-summarizer", "name": "Meeting Notes Summarizer", "category": "productivity",
        "description": "Summarize meeting notes into action items and key decisions",
        "keywords": ["meeting", "notes", "summarize", "action items", "minutes"],
        "agents": [
            {"name": "Notes Summarizer", "role": "writer", "purpose": "Extract key decisions, action items, and summaries from meeting notes", "tools": ["file_write"], "system_prompt_hint": "Analyze the meeting notes. Extract: key decisions, action items (with owners if mentioned), important discussion points, and follow-ups."}
        ],
        "pipeline_shape": [{"label": "Summarize", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Meeting Summarizer", "subtitle": "Turn meeting notes into action items", "prompt_template": "Summarize these meeting notes into action items"}
    },
    {
        "id": "daily-planner", "name": "Daily Task Planner", "category": "productivity",
        "description": "Plan your day with prioritized tasks and time blocks",
        "keywords": ["plan", "daily", "task", "schedule", "organize", "todo", "planner"],
        "agents": [
            {"name": "Day Planner", "role": "planner", "purpose": "Create a structured daily plan with priorities and time blocks", "tools": ["file_write"], "system_prompt_hint": "Create a daily plan. Prioritize tasks by importance/urgency. Suggest time blocks. Include breaks. Be realistic about time estimates."}
        ],
        "pipeline_shape": [{"label": "Plan Day", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": "0 7 * * *", "user_fields": [],
        "suggestion_card": {"title": "Daily Planner", "subtitle": "Get a structured plan for your day", "prompt_template": "Plan my day: [tasks]"}
    },
    {
        "id": "weekly-review", "name": "Weekly Review & Planning", "category": "productivity",
        "description": "Review your week and plan the next one",
        "keywords": ["weekly", "review", "planning", "reflection", "goals"],
        "agents": [
            {"name": "Week Reviewer", "role": "analyst", "purpose": "Analyze what was accomplished and what needs attention", "tools": [], "system_prompt_hint": "Review the past week's accomplishments and challenges. Identify what went well, what didn't, and lessons learned."},
            {"name": "Week Planner", "role": "planner", "purpose": "Plan priorities and goals for the coming week", "tools": ["file_write"], "system_prompt_hint": "Based on the review, plan the coming week. Set 3-5 priority goals. Identify key meetings and deadlines. Suggest focus areas for each day."}
        ],
        "pipeline_shape": [{"label": "Review Week", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Plan Next Week", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 17 * * 5", "user_fields": [],
        "suggestion_card": {"title": "Weekly Review", "subtitle": "Reflect on your week and plan ahead", "prompt_template": "Review my week and plan next week: [accomplishments and upcoming tasks]"}
    },
    {
        "id": "project-breakdown", "name": "Project Breakdown", "category": "productivity",
        "description": "Break a large project into manageable tasks and milestones",
        "keywords": ["project", "breakdown", "tasks", "milestones", "plan", "decompose"],
        "agents": [
            {"name": "Project Analyst", "role": "analyst", "purpose": "Analyze the project scope and identify major components", "tools": [], "system_prompt_hint": "Break down the project into major components. Identify dependencies, risks, and required resources. Estimate relative effort for each component."},
            {"name": "Task Creator", "role": "planner", "purpose": "Create detailed task lists with milestones", "tools": ["file_write"], "system_prompt_hint": "Create a detailed task list from the analysis. Group tasks into milestones. Add estimated durations. Identify the critical path. Format as a project plan."}
        ],
        "pipeline_shape": [{"label": "Analyze Scope", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Create Tasks", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Project Breakdown", "subtitle": "Break big projects into small tasks", "prompt_template": "Break down this project: [project description]"}
    },
    {
        "id": "decision-matrix", "name": "Decision Matrix Builder", "category": "productivity",
        "description": "Build a weighted decision matrix to compare options objectively",
        "keywords": ["decision", "compare", "matrix", "pros cons", "evaluate", "choose"],
        "agents": [
            {"name": "Options Researcher", "role": "researcher", "purpose": "Research each option and gather relevant data", "tools": ["web_fetch"], "system_prompt_hint": "Research each option thoroughly. Find pricing, features, reviews, pros/cons. Create a comprehensive comparison dataset."},
            {"name": "Matrix Builder", "role": "analyst", "purpose": "Build a weighted decision matrix with scoring", "tools": ["file_write"], "system_prompt_hint": "Build a decision matrix. Define criteria with weights. Score each option 1-5 on each criterion. Calculate weighted totals. Provide a recommendation with reasoning."}
        ],
        "pipeline_shape": [{"label": "Research Options", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Build Matrix", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Decision Matrix", "subtitle": "Compare options with weighted criteria", "prompt_template": "Help me decide between [options]"}
    },
    {
        "id": "habit-tracker", "name": "Habit Tracker & Coach", "category": "productivity",
        "description": "Track habits and get coaching on building better routines",
        "keywords": ["habit", "routine", "track", "streak", "discipline", "coach"],
        "agents": [
            {"name": "Habit Coach", "role": "coach", "purpose": "Analyze habit data and provide coaching advice", "tools": [], "system_prompt_hint": "Review the user's habit tracking data. Identify streaks, missed days, and patterns. Provide motivational coaching, suggest improvements, and celebrate wins. Use behavioral science principles."}
        ],
        "pipeline_shape": [{"label": "Coach", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": "0 21 * * *", "user_fields": ["habits"],
        "suggestion_card": {"title": "Habit Coach", "subtitle": "Track habits and get daily coaching", "prompt_template": "Review my habits today: [habit status]"}
    },
    {
        "id": "brainstorm-facilitator", "name": "Brainstorm Facilitator", "category": "productivity",
        "description": "Facilitate brainstorming sessions with structured idea generation",
        "keywords": ["brainstorm", "ideas", "creative", "thinking", "ideate"],
        "agents": [
            {"name": "Idea Generator", "role": "creative", "purpose": "Generate diverse ideas using creative thinking techniques", "tools": [], "system_prompt_hint": "Generate ideas using multiple techniques: SCAMPER, random association, reverse thinking, and analogy. Aim for quantity first, then quality. Include wild ideas alongside practical ones."},
            {"name": "Idea Evaluator", "role": "analyst", "purpose": "Evaluate and prioritize the generated ideas", "tools": ["file_write"], "system_prompt_hint": "Evaluate each idea on feasibility, impact, and novelty. Group similar ideas. Identify the top 5 most promising ideas with reasoning. Suggest next steps for each."}
        ],
        "pipeline_shape": [{"label": "Generate Ideas", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Evaluate", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Brainstorm", "subtitle": "Generate and evaluate ideas", "prompt_template": "Brainstorm ideas for [topic]"}
    },
    {
        "id": "goal-setter", "name": "SMART Goal Setter", "category": "productivity",
        "description": "Turn vague goals into SMART goals with action plans",
        "keywords": ["goal", "smart", "objective", "plan", "target", "achieve"],
        "agents": [
            {"name": "Goal Architect", "role": "planner", "purpose": "Transform vague goals into SMART goals with detailed action plans", "tools": ["file_write"], "system_prompt_hint": "Take the user's goal and make it SMART (Specific, Measurable, Achievable, Relevant, Time-bound). Create milestones, define metrics for success, identify potential obstacles, and build a step-by-step action plan."}
        ],
        "pipeline_shape": [{"label": "Set Goals", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Goal Setter", "subtitle": "Turn goals into SMART action plans", "prompt_template": "Help me set a goal for [objective]"}
    },

    # ── DEVELOPMENT (8) ──
    {
        "id": "code-review", "name": "Code Review Pipeline", "category": "development",
        "description": "Review code for bugs, style issues, and improvements",
        "keywords": ["code", "review", "PR", "pull request", "bugs", "lint"],
        "agents": [
            {"name": "Code Reader", "role": "reader", "purpose": "Read and understand the code to be reviewed", "tools": ["file_read"], "system_prompt_hint": "Read the provided code carefully. Understand the logic, identify all functions, and note any immediate concerns."},
            {"name": "Code Reviewer", "role": "reviewer", "purpose": "Review code for bugs, style issues, and improvements", "tools": ["file_write"], "system_prompt_hint": "Review the code thoroughly. Check for bugs, security issues, performance problems, style inconsistencies, and suggest improvements."}
        ],
        "pipeline_shape": [{"label": "Read Code", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Review", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["file_path"],
        "suggestion_card": {"title": "Code Review", "subtitle": "Get your code reviewed for bugs and improvements", "prompt_template": "Review the code in [file_path]"}
    },
    {
        "id": "doc-generator", "name": "Documentation Generator", "category": "development",
        "description": "Generate documentation for your codebase",
        "keywords": ["docs", "documentation", "generate", "document", "API", "readme"],
        "agents": [
            {"name": "Code Analyzer", "role": "analyst", "purpose": "Analyze code structure and extract documentation-relevant info", "tools": ["file_read", "shell"], "system_prompt_hint": "Analyze the codebase. Identify modules, functions, types, APIs. Extract comments, signatures, and usage patterns."},
            {"name": "Doc Writer", "role": "writer", "purpose": "Write clear documentation from the analysis", "tools": ["file_write"], "system_prompt_hint": "Write clear, comprehensive documentation. Include overview, API reference, usage examples, and configuration details."}
        ],
        "pipeline_shape": [{"label": "Analyze Code", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Docs", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["project_path"],
        "suggestion_card": {"title": "Doc Generator", "subtitle": "Auto-generate documentation for your code", "prompt_template": "Generate documentation for [project]"}
    },
    {
        "id": "test-writer", "name": "Test Suite Generator", "category": "development",
        "description": "Generate comprehensive test cases for your code",
        "keywords": ["test", "testing", "unit test", "coverage", "QA", "spec"],
        "agents": [
            {"name": "Code Analyzer", "role": "analyst", "purpose": "Analyze code to identify testable functions and edge cases", "tools": ["file_read"], "system_prompt_hint": "Analyze the code. Identify all public functions, their inputs/outputs, edge cases, error conditions, and integration points that need testing."},
            {"name": "Test Writer", "role": "developer", "purpose": "Write comprehensive test cases", "tools": ["file_write"], "system_prompt_hint": "Write unit tests covering: happy paths, edge cases, error handling, and boundary conditions. Follow testing best practices. Use descriptive test names."}
        ],
        "pipeline_shape": [{"label": "Analyze", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Tests", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Test Generator", "subtitle": "Generate test cases for your code", "prompt_template": "Write tests for [code or function]"}
    },
    {
        "id": "api-designer", "name": "API Designer", "category": "development",
        "description": "Design RESTful APIs with endpoints, schemas, and documentation",
        "keywords": ["api", "rest", "endpoint", "schema", "design", "openapi"],
        "agents": [
            {"name": "API Architect", "role": "architect", "purpose": "Design API endpoints, request/response schemas, and error handling", "tools": [], "system_prompt_hint": "Design a RESTful API. Define endpoints (method, path, description), request/response schemas (JSON), status codes, authentication, pagination, and error formats. Follow REST best practices."},
            {"name": "API Documenter", "role": "writer", "purpose": "Write API documentation in OpenAPI format", "tools": ["file_write"], "system_prompt_hint": "Write comprehensive API documentation. Include endpoint descriptions, parameter details, example requests/responses, error codes, and authentication instructions."}
        ],
        "pipeline_shape": [{"label": "Design API", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Document", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "API Designer", "subtitle": "Design and document RESTful APIs", "prompt_template": "Design an API for [system]"}
    },
    {
        "id": "bug-analyzer", "name": "Bug Report Analyzer", "category": "development",
        "description": "Analyze bug reports and suggest likely causes and fixes",
        "keywords": ["bug", "debug", "error", "fix", "diagnose", "troubleshoot"],
        "agents": [
            {"name": "Bug Analyst", "role": "analyst", "purpose": "Analyze the bug report and identify likely root causes", "tools": ["file_read"], "system_prompt_hint": "Analyze the bug report. Identify likely root causes based on symptoms. Check related code if paths are provided. Consider common patterns that cause similar bugs."},
            {"name": "Fix Advisor", "role": "advisor", "purpose": "Suggest fixes and prevention strategies", "tools": ["file_write"], "system_prompt_hint": "Suggest specific fixes ranked by likelihood. Include code snippets where possible. Recommend tests to prevent regression. Suggest related areas to check."}
        ],
        "pipeline_shape": [{"label": "Analyze Bug", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Suggest Fixes", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Bug Analyzer", "subtitle": "Diagnose bugs and get fix suggestions", "prompt_template": "Debug this issue: [error description]"}
    },
    {
        "id": "git-changelog", "name": "Changelog Generator", "category": "development",
        "description": "Generate changelogs from git commit history",
        "keywords": ["changelog", "release", "git", "commit", "version", "notes"],
        "agents": [
            {"name": "Commit Analyzer", "role": "analyst", "purpose": "Analyze git commits and categorize changes", "tools": ["shell"], "system_prompt_hint": "Read the git log output. Categorize commits into: Features, Bug Fixes, Improvements, Breaking Changes. Identify the most impactful changes."},
            {"name": "Changelog Writer", "role": "writer", "purpose": "Write a formatted changelog", "tools": ["file_write"], "system_prompt_hint": "Write a professional changelog in Keep a Changelog format. Group by category. Write user-friendly descriptions (not raw commit messages). Highlight breaking changes."}
        ],
        "pipeline_shape": [{"label": "Analyze Commits", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Changelog", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Changelog Generator", "subtitle": "Generate changelogs from git history", "prompt_template": "Generate a changelog from recent commits"}
    },
    {
        "id": "db-schema-designer", "name": "Database Schema Designer", "category": "development",
        "description": "Design database schemas with tables, relationships, and indexes",
        "keywords": ["database", "schema", "sql", "tables", "migration", "ERD"],
        "agents": [
            {"name": "Schema Designer", "role": "architect", "purpose": "Design the database schema based on requirements", "tools": [], "system_prompt_hint": "Design a normalized database schema. Define tables, columns, types, constraints, primary keys, foreign keys, and indexes. Consider query patterns for performance. Follow normalization best practices."},
            {"name": "Migration Writer", "role": "developer", "purpose": "Write SQL migration scripts", "tools": ["file_write"], "system_prompt_hint": "Write SQL migration scripts (CREATE TABLE, ALTER TABLE, CREATE INDEX). Include both up and down migrations. Add comments explaining design decisions."}
        ],
        "pipeline_shape": [{"label": "Design Schema", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Migrations", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "DB Schema Designer", "subtitle": "Design database schemas and migrations", "prompt_template": "Design a database for [system]"}
    },
    {
        "id": "code-explainer", "name": "Code Explainer", "category": "development",
        "description": "Explain complex code in plain English with examples",
        "keywords": ["explain", "understand", "code", "how", "what", "walkthrough"],
        "agents": [
            {"name": "Code Explainer", "role": "teacher", "purpose": "Explain code in plain English with examples", "tools": ["file_read"], "system_prompt_hint": "Explain the code step by step. Start with a high-level overview, then walk through each section. Use analogies for complex concepts. Provide examples of how the code is used. Highlight any tricky or non-obvious parts."}
        ],
        "pipeline_shape": [{"label": "Explain", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Code Explainer", "subtitle": "Understand any code in plain English", "prompt_template": "Explain this code: [paste code or file path]"}
    },

    # ── PERSONAL (6) ──
    {
        "id": "journal-prompt", "name": "Daily Journal & Reflection", "category": "personal",
        "description": "Get thoughtful journal prompts and reflect on your day",
        "keywords": ["journal", "reflect", "diary", "gratitude", "mindfulness"],
        "agents": [
            {"name": "Journal Guide", "role": "coach", "purpose": "Provide thoughtful journal prompts and facilitate reflection", "tools": [], "system_prompt_hint": "Provide 3 thoughtful journal prompts based on the user's context. One about gratitude, one about growth, one about intentions. After the user responds, provide insightful reflections."}
        ],
        "pipeline_shape": [{"label": "Journal", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": "0 21 * * *", "user_fields": [],
        "suggestion_card": {"title": "Daily Journal", "subtitle": "Guided journaling and reflection", "prompt_template": "Guide me through today's journal entry"}
    },
    {
        "id": "meal-planner", "name": "Weekly Meal Planner", "category": "personal",
        "description": "Plan meals for the week with recipes and grocery lists",
        "keywords": ["meal", "recipe", "food", "cook", "grocery", "diet", "nutrition"],
        "agents": [
            {"name": "Meal Planner", "role": "planner", "purpose": "Create a weekly meal plan based on preferences", "tools": [], "system_prompt_hint": "Create a 7-day meal plan (breakfast, lunch, dinner). Consider the user's dietary preferences, budget, and cooking skill level. Vary cuisines and ingredients to avoid monotony."},
            {"name": "Recipe & List Writer", "role": "writer", "purpose": "Write recipes and compile a grocery list", "tools": ["file_write"], "system_prompt_hint": "Write simple recipes for each planned meal. Include prep time, cook time, and serving size. Compile a consolidated grocery list organized by store section (produce, dairy, etc)."}
        ],
        "pipeline_shape": [{"label": "Plan Meals", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Recipes & List", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 10 * * 0", "user_fields": ["dietary_preferences"],
        "suggestion_card": {"title": "Meal Planner", "subtitle": "Plan meals and get grocery lists", "prompt_template": "Plan my meals for the week, I like [preferences]"}
    },
    {
        "id": "workout-planner", "name": "Workout Planner", "category": "personal",
        "description": "Create personalized workout plans based on your goals",
        "keywords": ["workout", "exercise", "fitness", "gym", "training", "health"],
        "agents": [
            {"name": "Fitness Coach", "role": "coach", "purpose": "Design a personalized workout plan", "tools": ["file_write"], "system_prompt_hint": "Create a workout plan tailored to the user's goals, fitness level, and available equipment. Include warm-up, main workout, and cool-down. Specify sets, reps, and rest times. Add progression suggestions."}
        ],
        "pipeline_shape": [{"label": "Plan Workout", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["goals", "equipment"],
        "suggestion_card": {"title": "Workout Planner", "subtitle": "Get personalized workout plans", "prompt_template": "Create a workout plan for [goal] with [equipment]"}
    },
    {
        "id": "travel-planner", "name": "Travel Itinerary Planner", "category": "personal",
        "description": "Plan detailed travel itineraries with activities and logistics",
        "keywords": ["travel", "trip", "itinerary", "vacation", "plan", "visit"],
        "agents": [
            {"name": "Destination Researcher", "role": "researcher", "purpose": "Research the destination for activities, food, and logistics", "tools": ["web_fetch"], "system_prompt_hint": "Research the destination. Find top attractions, hidden gems, best restaurants, transportation options, and local tips. Note opening hours and prices."},
            {"name": "Itinerary Builder", "role": "planner", "purpose": "Build a detailed day-by-day itinerary", "tools": ["file_write"], "system_prompt_hint": "Build a day-by-day itinerary with morning/afternoon/evening activities. Include travel times between locations. Add restaurant recommendations for each meal. Include backup options for rainy days."}
        ],
        "pipeline_shape": [{"label": "Research", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Build Itinerary", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["destination", "dates"],
        "suggestion_card": {"title": "Travel Planner", "subtitle": "Plan detailed travel itineraries", "prompt_template": "Plan a trip to [destination] for [duration]"}
    },
    {
        "id": "birthday-gift-finder", "name": "Gift Idea Finder", "category": "personal",
        "description": "Find personalized gift ideas based on the recipient's interests",
        "keywords": ["gift", "birthday", "present", "christmas", "holiday", "idea"],
        "agents": [
            {"name": "Gift Researcher", "role": "researcher", "purpose": "Find gift ideas based on recipient's interests and budget", "tools": ["web_fetch"], "system_prompt_hint": "Research gift ideas matching the recipient's interests, age, and the specified budget. Find specific products with prices and links. Include a mix of practical, fun, and unique options."},
            {"name": "Gift Curator", "role": "writer", "purpose": "Curate and present the best gift options", "tools": ["file_write"], "system_prompt_hint": "Present the top 10 gift ideas organized by category. Include price, where to buy, and why it's a good fit. Add a personal touch recommendation for each."}
        ],
        "pipeline_shape": [{"label": "Research Gifts", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Curate List", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Gift Finder", "subtitle": "Find perfect gifts for anyone", "prompt_template": "Find gift ideas for [person] who likes [interests], budget [amount]"}
    },
    {
        "id": "language-tutor", "name": "Language Practice Tutor", "category": "personal",
        "description": "Practice a foreign language with conversational exercises",
        "keywords": ["language", "learn", "practice", "spanish", "french", "tutor"],
        "agents": [
            {"name": "Language Tutor", "role": "tutor", "purpose": "Provide language practice through conversation and exercises", "tools": [], "system_prompt_hint": "Act as a patient language tutor. Conduct the conversation in the target language with English explanations. Correct mistakes gently. Introduce new vocabulary. Adjust difficulty to the learner's level."}
        ],
        "pipeline_shape": [{"label": "Practice", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["language", "level"],
        "suggestion_card": {"title": "Language Tutor", "subtitle": "Practice any language conversationally", "prompt_template": "Practice [language] with me, I'm a [beginner/intermediate]"}
    },

    # ── FINANCE (5) ──
    {
        "id": "price-tracker", "name": "Price Tracker", "category": "finance",
        "description": "Track prices on products and get notified of drops",
        "keywords": ["price", "track", "deal", "discount", "sale", "cheap", "buy"],
        "agents": [
            {"name": "Price Checker", "role": "fetcher", "purpose": "Check current prices on specified products", "tools": ["web_fetch"], "system_prompt_hint": "Fetch the product page and extract the current price. Note any sale prices, coupon codes, or availability changes."},
            {"name": "Deal Analyzer", "role": "analyst", "purpose": "Analyze price history and determine if it's a good deal", "tools": ["file_read", "file_write"], "system_prompt_hint": "Compare the current price with previously saved prices. Report price changes, trends, and whether now is a good time to buy."}
        ],
        "pipeline_shape": [{"label": "Check Prices", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Analyze Deals", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 10 * * *", "user_fields": ["urls"],
        "suggestion_card": {"title": "Price Tracker", "subtitle": "Track product prices and find deals", "prompt_template": "Track the price of [product] at [url]"}
    },
    {
        "id": "budget-analyzer", "name": "Budget Analyzer", "category": "finance",
        "description": "Analyze spending habits and create budget recommendations",
        "keywords": ["budget", "spending", "money", "expense", "save", "finance"],
        "agents": [
            {"name": "Spending Analyzer", "role": "analyst", "purpose": "Analyze spending data and identify patterns", "tools": [], "system_prompt_hint": "Analyze the spending data. Categorize expenses (housing, food, transport, entertainment, etc). Identify unusual spending, trends, and areas of overspending."},
            {"name": "Budget Advisor", "role": "advisor", "purpose": "Create budget recommendations and savings plan", "tools": ["file_write"], "system_prompt_hint": "Create a recommended budget based on the 50/30/20 rule (needs/wants/savings). Suggest specific areas to cut. Set savings targets. Provide actionable tips for reducing each category."}
        ],
        "pipeline_shape": [{"label": "Analyze Spending", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Budget Plan", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Budget Analyzer", "subtitle": "Analyze spending and get budget advice", "prompt_template": "Analyze my spending: [expenses]"}
    },
    {
        "id": "stock-research", "name": "Stock Research Report", "category": "finance",
        "description": "Research a stock and get a comprehensive analysis",
        "keywords": ["stock", "invest", "market", "ticker", "analysis", "trade"],
        "agents": [
            {"name": "Stock Researcher", "role": "researcher", "purpose": "Gather financial data and news about a stock", "tools": ["web_fetch"], "system_prompt_hint": "Research the stock. Find recent price action, financial metrics (P/E, revenue, earnings), recent news, analyst ratings, and sector performance. Use financial news sites and data providers."},
            {"name": "Stock Analyst", "role": "analyst", "purpose": "Analyze the stock and provide an investment thesis", "tools": ["file_write"], "system_prompt_hint": "Analyze the stock data. Provide: company overview, financial health, competitive position, growth catalysts, risks, and a balanced thesis. Include a disclaimer that this is not financial advice."}
        ],
        "pipeline_shape": [{"label": "Research", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Analyze", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["ticker"],
        "suggestion_card": {"title": "Stock Research", "subtitle": "Get a comprehensive stock analysis", "prompt_template": "Research [ticker] stock"}
    },
    {
        "id": "crypto-briefing", "name": "Crypto Market Briefing", "category": "finance",
        "description": "Get a daily briefing on crypto market conditions",
        "keywords": ["crypto", "bitcoin", "ethereum", "market", "defi", "web3"],
        "agents": [
            {"name": "Crypto Scanner", "role": "researcher", "purpose": "Scan crypto market data and news", "tools": ["web_fetch"], "system_prompt_hint": "Fetch current prices for top 10 cryptocurrencies. Check for major news, regulatory updates, and market-moving events. Note any significant price movements (>5%)."},
            {"name": "Market Briefer", "role": "writer", "purpose": "Write a concise crypto market briefing", "tools": ["file_write"], "system_prompt_hint": "Write a concise crypto market briefing. Include: market overview, top movers, key news, and sentiment analysis. Keep it factual and balanced."}
        ],
        "pipeline_shape": [{"label": "Scan Market", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Briefing", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": "0 8 * * *", "user_fields": [],
        "suggestion_card": {"title": "Crypto Briefing", "subtitle": "Daily crypto market overview", "prompt_template": "Give me today's crypto market briefing"}
    },
    {
        "id": "invoice-generator", "name": "Invoice Generator", "category": "finance",
        "description": "Generate professional invoices from project details",
        "keywords": ["invoice", "bill", "payment", "freelance", "client"],
        "agents": [
            {"name": "Invoice Builder", "role": "writer", "purpose": "Generate a professional invoice from project details", "tools": ["file_write"], "system_prompt_hint": "Create a professional invoice. Include: invoice number, date, client details, itemized services with hours/rates, subtotal, tax, and total. Format cleanly with payment terms."}
        ],
        "pipeline_shape": [{"label": "Generate Invoice", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Invoice Generator", "subtitle": "Create professional invoices", "prompt_template": "Create an invoice for [client] for [services]"}
    },

    # ── LEARNING (6) ──
    {
        "id": "flashcard-generator", "name": "Flashcard Generator", "category": "learning",
        "description": "Generate study flashcards from any topic or material",
        "keywords": ["flashcard", "study", "learn", "quiz", "memorize", "cards"],
        "agents": [
            {"name": "Content Researcher", "role": "researcher", "purpose": "Research the topic to create accurate flashcard content", "tools": ["web_fetch"], "system_prompt_hint": "Research the topic. Identify the key concepts, definitions, facts, and relationships that should be memorized."},
            {"name": "Flashcard Creator", "role": "writer", "purpose": "Create effective flashcards from the research", "tools": ["file_write"], "system_prompt_hint": "Create flashcards in Q&A format. Each card should test one concept. Use clear, concise language. Include mnemonics where helpful."}
        ],
        "pipeline_shape": [{"label": "Research", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Create Cards", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["topic"],
        "suggestion_card": {"title": "Flashcard Generator", "subtitle": "Create study flashcards on any topic", "prompt_template": "Create flashcards about [topic]"}
    },
    {
        "id": "topic-researcher", "name": "Topic Deep-Dive", "category": "learning",
        "description": "Research any topic and get a comprehensive overview",
        "keywords": ["learn", "explain", "what is", "how does", "overview", "understand"],
        "agents": [
            {"name": "Deep Researcher", "role": "researcher", "purpose": "Thoroughly research the topic from multiple angles", "tools": ["web_fetch"], "system_prompt_hint": "Research the topic from multiple sources. Cover: what it is, how it works, history, current state, pros/cons, and practical applications."}
        ],
        "pipeline_shape": [{"label": "Research", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["topic"],
        "suggestion_card": {"title": "Topic Deep-Dive", "subtitle": "Get a comprehensive overview of any topic", "prompt_template": "Explain [topic] in depth"}
    },
    {
        "id": "eli5-explainer", "name": "ELI5 Explainer", "category": "learning",
        "description": "Explain complex topics in simple terms anyone can understand",
        "keywords": ["eli5", "simple", "explain", "easy", "beginner", "basics"],
        "agents": [
            {"name": "Simple Explainer", "role": "teacher", "purpose": "Explain complex topics using simple language and analogies", "tools": [], "system_prompt_hint": "Explain the topic as if talking to a 5-year-old. Use everyday analogies, simple words, and concrete examples. Avoid jargon. Build up from basics to the key concept. Make it fun and memorable."}
        ],
        "pipeline_shape": [{"label": "Explain", "agent_index": 0, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "ELI5 Explainer", "subtitle": "Complex topics made simple", "prompt_template": "Explain [topic] like I'm 5"}
    },
    {
        "id": "study-guide", "name": "Study Guide Builder", "category": "learning",
        "description": "Build comprehensive study guides for exams or certifications",
        "keywords": ["study", "guide", "exam", "certification", "prepare", "test"],
        "agents": [
            {"name": "Curriculum Researcher", "role": "researcher", "purpose": "Research the exam/certification syllabus and key topics", "tools": ["web_fetch"], "system_prompt_hint": "Research the exam syllabus and objectives. Identify all topics, subtopics, and their relative weights. Find recommended resources and common pitfalls."},
            {"name": "Guide Writer", "role": "writer", "purpose": "Write a structured study guide", "tools": ["file_write"], "system_prompt_hint": "Write a study guide organized by topic. Include key concepts, definitions, formulas, and practice questions. Suggest study schedule based on topic difficulty and weight."}
        ],
        "pipeline_shape": [{"label": "Research Syllabus", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Guide", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["exam"],
        "suggestion_card": {"title": "Study Guide", "subtitle": "Build study guides for any exam", "prompt_template": "Build a study guide for [exam/certification]"}
    },
    {
        "id": "book-summarizer", "name": "Book Summarizer", "category": "learning",
        "description": "Get detailed summaries and key takeaways from books",
        "keywords": ["book", "summary", "read", "takeaway", "key points"],
        "agents": [
            {"name": "Book Researcher", "role": "researcher", "purpose": "Find comprehensive information about the book", "tools": ["web_fetch"], "system_prompt_hint": "Research the book. Find: main thesis, chapter summaries, key arguments, notable quotes, and critical reviews. Look for author interviews about the book."},
            {"name": "Summary Writer", "role": "writer", "purpose": "Write a detailed book summary with actionable takeaways", "tools": ["file_write"], "system_prompt_hint": "Write a book summary with: overview, key themes, chapter-by-chapter highlights, notable quotes, actionable takeaways, and who should read it. Make it useful enough to capture the book's value."}
        ],
        "pipeline_shape": [{"label": "Research Book", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Summarize", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["book_title"],
        "suggestion_card": {"title": "Book Summary", "subtitle": "Get key takeaways from any book", "prompt_template": "Summarize the book [title] by [author]"}
    },
    {
        "id": "skill-roadmap", "name": "Learning Roadmap Builder", "category": "learning",
        "description": "Build a structured learning roadmap for any skill",
        "keywords": ["roadmap", "learn", "skill", "path", "curriculum", "career"],
        "agents": [
            {"name": "Skill Mapper", "role": "researcher", "purpose": "Research the skill landscape and best learning paths", "tools": ["web_fetch"], "system_prompt_hint": "Research the best learning path for the specified skill. Identify prerequisites, core topics, advanced topics, and recommended resources (courses, books, projects)."},
            {"name": "Roadmap Builder", "role": "planner", "purpose": "Build a structured learning roadmap with milestones", "tools": ["file_write"], "system_prompt_hint": "Build a week-by-week learning roadmap. Include: milestones, specific resources for each phase, hands-on projects, and assessment checkpoints. Estimate time commitment per week."}
        ],
        "pipeline_shape": [{"label": "Research Path", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Build Roadmap", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["skill"],
        "suggestion_card": {"title": "Learning Roadmap", "subtitle": "Build a roadmap to learn any skill", "prompt_template": "Create a learning roadmap for [skill]"}
    },

    # ── DATA (4) ──
    {
        "id": "csv-analyzer", "name": "CSV Data Analyzer", "category": "data",
        "description": "Analyze CSV data and extract insights",
        "keywords": ["csv", "data", "analyze", "spreadsheet", "excel", "stats"],
        "agents": [
            {"name": "Data Analyzer", "role": "analyst", "purpose": "Analyze CSV data for patterns and statistics", "tools": ["file_read"], "system_prompt_hint": "Analyze the CSV data. Calculate summary statistics (mean, median, min, max, std). Identify trends, outliers, and correlations. Group and aggregate data meaningfully."},
            {"name": "Insight Writer", "role": "writer", "purpose": "Write a data analysis report with key insights", "tools": ["file_write"], "system_prompt_hint": "Write a clear data analysis report. Include: summary statistics, key findings, trends, anomalies, and actionable recommendations. Use tables to present numbers clearly."}
        ],
        "pipeline_shape": [{"label": "Analyze Data", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Report", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "CSV Analyzer", "subtitle": "Analyze data and get insights", "prompt_template": "Analyze this data: [paste CSV or describe]"}
    },
    {
        "id": "survey-analyzer", "name": "Survey Results Analyzer", "category": "data",
        "description": "Analyze survey responses and generate insight reports",
        "keywords": ["survey", "feedback", "responses", "analyze", "results"],
        "agents": [
            {"name": "Response Analyzer", "role": "analyst", "purpose": "Analyze survey responses for patterns and sentiment", "tools": [], "system_prompt_hint": "Analyze the survey responses. Quantify results for multiple-choice questions. Analyze open-ended responses for themes and sentiment. Identify key pain points and positive feedback."},
            {"name": "Report Writer", "role": "writer", "purpose": "Create a survey results report with visualizations", "tools": ["file_write"], "system_prompt_hint": "Write a professional survey results report. Include: response rate, key metrics, theme analysis, notable quotes, and recommendations. Present data in tables and charts."}
        ],
        "pipeline_shape": [{"label": "Analyze Responses", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Report", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Survey Analyzer", "subtitle": "Analyze survey results and get insights", "prompt_template": "Analyze these survey results: [data]"}
    },
    {
        "id": "log-analyzer", "name": "Log File Analyzer", "category": "data",
        "description": "Analyze application logs to find errors and patterns",
        "keywords": ["log", "error", "analyze", "debug", "server", "application"],
        "agents": [
            {"name": "Log Parser", "role": "analyst", "purpose": "Parse and analyze log files for errors and patterns", "tools": ["file_read"], "system_prompt_hint": "Parse the log data. Identify error types and frequencies. Find patterns in timing, endpoints, or user actions that correlate with errors. Note any cascading failures."},
            {"name": "Incident Reporter", "role": "writer", "purpose": "Write an incident analysis report", "tools": ["file_write"], "system_prompt_hint": "Write an incident report. Include: timeline of events, root cause analysis, affected services, error frequency charts, and recommended fixes prioritized by severity."}
        ],
        "pipeline_shape": [{"label": "Parse Logs", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Write Report", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": [],
        "suggestion_card": {"title": "Log Analyzer", "subtitle": "Find errors and patterns in logs", "prompt_template": "Analyze these logs for errors: [paste logs]"}
    },
    {
        "id": "seo-auditor", "name": "SEO Auditor", "category": "data",
        "description": "Audit a website's SEO and get improvement recommendations",
        "keywords": ["seo", "audit", "search", "ranking", "google", "optimize"],
        "agents": [
            {"name": "SEO Scanner", "role": "researcher", "purpose": "Scan a website for SEO factors", "tools": ["web_fetch"], "system_prompt_hint": "Scan the website. Check: title tags, meta descriptions, headings, image alt text, page speed indicators, mobile friendliness, internal links, and content quality."},
            {"name": "SEO Advisor", "role": "advisor", "purpose": "Provide SEO improvement recommendations", "tools": ["file_write"], "system_prompt_hint": "Provide a prioritized list of SEO improvements. Score current performance. Include: quick wins, medium-term fixes, and long-term strategy. Explain the impact of each recommendation."}
        ],
        "pipeline_shape": [{"label": "Scan Site", "agent_index": 0, "input_mode": "FromPrevious"}, {"label": "Recommendations", "agent_index": 1, "input_mode": "FromPrevious"}],
        "default_schedule": None, "user_fields": ["url"],
        "suggestion_card": {"title": "SEO Auditor", "subtitle": "Audit your site's SEO health", "prompt_template": "Audit the SEO of [url]"}
    },
]

def generate():
    # Add data category if not in original
    categories_seen = set()
    for t in TEMPLATES:
        categories_seen.add(t["category"])

    for t in TEMPLATES:
        t["schema_version"] = 1
        t["author"] = "agentfactory"
        if "tags" not in t:
            t["tags"] = []

        cat = t["category"]
        tid = t["id"]

        folder = f"{cat}/{tid}"
        os.makedirs(folder, exist_ok=True)

        # Write template.json
        with open(f"{folder}/template.json", "w") as f:
            json.dump(t, f, indent=2)

        # Generate README
        agents_list = "\n".join(
            f"{i+1}. **{a['name']}** ({a['role']}): {a['purpose']}"
            for i, a in enumerate(t["agents"])
        )
        pipeline_flow = " -> ".join(s["label"] for s in t["pipeline_shape"])
        schedule = t.get("default_schedule")
        schedule_line = f"\n**Schedule:** `{schedule}`\n" if schedule else ""

        readme = f"""# {t["name"]}

{t["description"]}

## Pipeline

{pipeline_flow}

## Agents

{agents_list}
{schedule_line}
## Usage

Use this template from the Agentfactory Home tab or install it from the Marketplace.
"""
        with open(f"{folder}/README.md", "w") as f:
            f.write(readme)

    print(f"Generated {len(TEMPLATES)} templates across {len(categories_seen)} categories")

if __name__ == "__main__":
    generate()
