#!/usr/bin/env python3
"""Generate ~108 new templates for agentfactory-templates repo."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

EXISTING_IDS = [
    'blog-writer','content-repurposer','email-drafter','newsletter-writer','resume-writer',
    'social-media-content','story-writer','csv-analyzer','log-analyzer','seo-auditor',
    'survey-analyzer','api-designer','bug-analyzer','code-explainer','code-review',
    'db-schema-designer','doc-generator','git-changelog','test-writer','budget-analyzer',
    'crypto-briefing','invoice-generator','price-tracker','stock-research','arxiv-digest',
    'competitor-tracker','deep-research','hn-digest','news-briefing','reddit-summarizer',
    'site-monitor','weather-briefing','book-summarizer','eli5-explainer','flashcard-generator',
    'skill-roadmap','study-guide','topic-researcher','birthday-gift-finder','journal-prompt',
    'language-tutor','meal-planner','travel-planner','workout-planner','brainstorm-facilitator',
    'daily-planner','decision-matrix','goal-setter','habit-tracker','meeting-summarizer',
    'project-breakdown','weekly-review'
]

def t(id, name, cat, desc, kw, agents, pipeline, sched, fields, card):
    """Shorthand template builder."""
    return {"id":id,"name":name,"category":cat,"description":desc,"keywords":kw,
            "agents":agents,"pipeline_shape":pipeline,"default_schedule":sched,
            "user_fields":fields,"suggestion_card":card}

def a(name, role, purpose, tools, hint):
    """Shorthand agent builder."""
    return {"name":name,"role":role,"purpose":purpose,"tools":tools,"system_prompt_hint":hint}

def p(label, idx, mode="FromPrevious"):
    """Shorthand pipeline step."""
    return {"label":label,"agent_index":idx,"input_mode":mode}

def c(title, subtitle, prompt):
    """Shorthand suggestion card."""
    return {"title":title,"subtitle":subtitle,"prompt_template":prompt}

NEW_TEMPLATES = [
    # ── INFORMATION +10 ──
    t("patent-monitor","Patent Monitor","information",
      "Monitor patent filings in your technology area",
      ["patent","filing","IP","intellectual property","monitor"],
      [a("Patent Searcher","researcher","Search patent databases for new filings",["web_fetch"],"Search patent databases (Google Patents, USPTO) for recent filings matching the specified technology keywords. Extract titles, abstracts, filing dates, and assignees."),
       a("Patent Analyst","analyst","Analyze patent trends and relevance",["file_write"],"Analyze the patent filings. Identify trends, key players, and patents most relevant to the user. Highlight potential competitive threats and opportunities.")],
      [p("Search Patents",0),p("Analyze",1)],
      "0 9 * * 1",["technology_area"],
      c("Patent Monitor","Track new patent filings weekly","Monitor patents in [technology area]")),

    t("academic-paper-finder","Academic Paper Finder","information",
      "Find and summarize academic papers on any research topic",
      ["academic","paper","research","scholar","citation","journal"],
      [a("Paper Searcher","researcher","Search academic databases for relevant papers",["web_fetch"],"Search Google Scholar, Semantic Scholar, and PubMed for papers on the given topic. Find highly cited papers, recent publications, and survey papers. Extract titles, authors, abstracts, and citation counts."),
       a("Paper Summarizer","writer","Summarize found papers with key findings",["file_write"],"Create a literature review summary. Group papers by theme. For each paper provide a 2-3 sentence summary of key findings. Note methodology and limitations. Highlight the most impactful papers.")],
      [p("Search Papers",0),p("Summarize",1)],
      None,["research_topic"],
      c("Paper Finder","Find academic papers on any topic","Find papers about [research topic]")),

    t("industry-report","Industry Report Generator","information",
      "Generate a comprehensive report on any industry or market",
      ["industry","market","report","analysis","sector","trends"],
      [a("Industry Researcher","researcher","Research industry data, trends, and key players",["web_fetch"],"Research the industry thoroughly. Find market size, growth rate, key players, recent trends, regulatory landscape, and technology disruptions. Use industry reports and news sources."),
       a("Report Writer","writer","Write a structured industry report",["file_write"],"Write a professional industry report with: executive summary, market overview, competitive landscape, trends and drivers, challenges, and outlook. Include data points and sources.")],
      [p("Research Industry",0),p("Write Report",1)],
      None,["industry"],
      c("Industry Report","Comprehensive industry analysis","Generate a report on the [industry] industry")),

    t("event-tracker","Event & Conference Tracker","information",
      "Track upcoming events, conferences, and meetups in your field",
      ["event","conference","meetup","summit","webinar","track"],
      [a("Event Scanner","researcher","Scan for upcoming events and conferences",["web_fetch"],"Search for upcoming conferences, meetups, and events in the specified field. Find dates, locations, speakers, ticket prices, and registration deadlines. Check Eventbrite, Meetup, and industry sites."),
       a("Event Curator","writer","Curate and organize event listings",["file_write"],"Create a curated list of upcoming events organized by date. Include: event name, date, location, cost, key speakers, and relevance score. Highlight early-bird deadlines and free events.")],
      [p("Scan Events",0),p("Curate",1)],
      "0 9 * * 1",["field"],
      c("Event Tracker","Find conferences and meetups","Find upcoming events in [field]")),

    t("regulation-monitor","Regulation Monitor","information",
      "Track regulatory changes and compliance updates in your industry",
      ["regulation","compliance","legal","law","policy","government"],
      [a("Regulation Scanner","researcher","Scan for regulatory changes and updates",["web_fetch"],"Monitor government websites, regulatory bodies, and legal news for changes affecting the specified industry. Track proposed rules, final rules, and enforcement actions."),
       a("Compliance Analyst","analyst","Analyze regulatory impact and required actions",["file_write"],"Analyze each regulatory change for business impact. Identify compliance deadlines, required actions, and potential penalties. Prioritize by urgency and impact.")],
      [p("Scan Regulations",0),p("Analyze Impact",1)],
      "0 8 * * 1",["industry"],
      c("Regulation Monitor","Track regulatory changes","Monitor regulations affecting [industry]")),

    t("product-hunt-digest","Product Hunt Digest","information",
      "Get a daily digest of top Product Hunt launches",
      ["product hunt","launch","startup","app","tool","new"],
      [a("PH Fetcher","researcher","Fetch top Product Hunt launches",["web_fetch"],"Fetch today's top Product Hunt launches. Get product names, descriptions, upvote counts, maker info, and links. Focus on the top 10-15 products."),
       a("PH Summarizer","writer","Create a readable Product Hunt digest",["file_write"],"Create a digest of today's best launches. Group by category (developer tools, AI, design, etc). Include brief descriptions and why each product is interesting.")],
      [p("Fetch Launches",0),p("Summarize",1)],
      "0 18 * * *",[],
      c("Product Hunt Digest","Daily top launches","Get today's top Product Hunt launches")),

    t("job-market-scanner","Job Market Scanner","information",
      "Scan job postings to understand market demand for specific roles",
      ["job","hiring","market","salary","demand","career"],
      [a("Job Scanner","researcher","Scan job boards for market intelligence",["web_fetch"],"Search major job boards for the specified role. Analyze job titles, required skills, salary ranges, company types, and location trends. Note common requirements and nice-to-haves."),
       a("Market Reporter","writer","Write a job market analysis report",["file_write"],"Write a job market report with: demand level, salary ranges, most-requested skills, top hiring companies, remote vs on-site trends, and career advice based on findings.")],
      [p("Scan Jobs",0),p("Write Report",1)],
      None,["role","location"],
      c("Job Market Scanner","Understand demand for any role","Scan the job market for [role] positions")),

    t("podcast-finder","Podcast Episode Finder","information",
      "Find and summarize relevant podcast episodes on any topic",
      ["podcast","episode","listen","audio","show","interview"],
      [a("Podcast Searcher","researcher","Search for relevant podcast episodes",["web_fetch"],"Search podcast directories and review sites for episodes about the specified topic. Find episode titles, show names, guest names, duration, and descriptions."),
       a("Episode Curator","writer","Curate a listening list with summaries",["file_write"],"Create a curated listening list. For each episode include: show name, episode title, guest, duration, key topics covered, and a brief summary. Rank by relevance.")],
      [p("Search Podcasts",0),p("Curate List",1)],
      None,["topic"],
      c("Podcast Finder","Find podcast episodes on any topic","Find podcasts about [topic]")),

    t("github-trending","GitHub Trending Digest","information",
      "Get a digest of trending GitHub repositories",
      ["github","trending","repository","open source","code","stars"],
      [a("GH Scanner","researcher","Fetch trending GitHub repositories",["web_fetch"],"Fetch trending repositories from GitHub trending page. Get repo names, descriptions, star counts, language, and contributors. Check daily, weekly trends."),
       a("Trend Reporter","writer","Write a trending repos digest",["file_write"],"Create a digest of trending repos grouped by language/category. Include: repo name, description, stars gained, why it's interesting, and potential use cases.")],
      [p("Fetch Trending",0),p("Write Digest",1)],
      "0 17 * * *",[],
      c("GitHub Trending","Trending repos digest","Show me today's trending GitHub repos")),

    t("startup-tracker","Startup Funding Tracker","information",
      "Track recent startup funding rounds and acquisitions",
      ["startup","funding","venture","investment","acquisition","series"],
      [a("Funding Scanner","researcher","Scan for recent funding announcements",["web_fetch"],"Search TechCrunch, Crunchbase news, and startup media for recent funding rounds. Find company names, round sizes, investors, valuations, and what the startup does."),
       a("Funding Reporter","writer","Write a funding activity report",["file_write"],"Create a funding report organized by sector. Include: company, round type, amount, key investors, and brief company description. Highlight notable trends and largest rounds.")],
      [p("Scan Funding",0),p("Write Report",1)],
      "0 9 * * 1",[],
      c("Startup Tracker","Track startup funding rounds","Show me this week's startup funding news")),

    # ── CONTENT +12 ──
    t("podcast-script","Podcast Script Writer","content",
      "Write engaging podcast scripts with intro, segments, and outro",
      ["podcast","script","show","episode","audio","host"],
      [a("Script Researcher","researcher","Research the podcast topic for talking points",["web_fetch"],"Research the podcast topic. Find interesting facts, statistics, quotes, and discussion angles. Identify potential questions and counterarguments."),
       a("Script Writer","writer","Write a structured podcast script",["file_write"],"Write a podcast script with: hook intro, topic introduction, 3-4 discussion segments with transitions, key talking points per segment, listener questions section, and outro with call-to-action. Include time estimates per segment.")],
      [p("Research Topic",0),p("Write Script",1)],
      None,["topic","duration"],
      c("Podcast Script","Write podcast episode scripts","Write a podcast script about [topic]")),

    t("ad-copy-writer","Ad Copy Writer","content",
      "Write persuasive ad copy for multiple platforms",
      ["ad","copy","advertising","marketing","campaign","conversion"],
      [a("Audience Researcher","researcher","Research the target audience and competition",["web_fetch"],"Research the target audience demographics, pain points, and desires. Analyze competitor ads. Identify winning hooks and angles for the product/service."),
       a("Copywriter","writer","Write compelling ad copy variants",["file_write"],"Write ad copy variants for: Google Ads (headlines + descriptions), Facebook/Instagram ads, and LinkedIn ads. Include multiple headline variants, CTAs, and A/B test suggestions. Follow platform character limits.")],
      [p("Research Audience",0),p("Write Copy",1)],
      None,["product","audience"],
      c("Ad Copy Writer","Write ads for any platform","Write ad copy for [product] targeting [audience]")),

    t("seo-article-writer","SEO Article Writer","content",
      "Write SEO-optimized articles that rank on search engines",
      ["seo","article","rank","search","optimize","keyword"],
      [a("Keyword Researcher","researcher","Research keywords and search intent",["web_fetch"],"Research the target keyword. Find search volume estimates, related keywords, LSI terms, and questions people ask. Analyze top-ranking content to understand what Google wants."),
       a("SEO Writer","writer","Write an SEO-optimized article",["file_write"],"Write an SEO-optimized article. Include the target keyword in title, H2s, intro, and naturally throughout. Use related keywords. Write compelling meta description. Add FAQ section from People Also Ask. Aim for comprehensive coverage.")],
      [p("Keyword Research",0),p("Write Article",1)],
      None,["keyword","word_count"],
      c("SEO Article","Write articles that rank","Write an SEO article about [keyword]")),

    t("product-description","Product Description Writer","content",
      "Write compelling product descriptions for e-commerce",
      ["product","description","ecommerce","listing","sell","features"],
      [a("Product Analyst","analyst","Analyze product features and benefits",[],"Analyze the product details provided. Identify key features, unique selling points, target audience, and emotional benefits. Compare with typical competitor descriptions."),
       a("Description Writer","writer","Write persuasive product descriptions",["file_write"],"Write product descriptions in multiple formats: short (50 words), medium (150 words), and detailed (300+ words). Include bullet points for features, benefit-focused copy, and SEO-friendly language. Write for the target audience's pain points.")],
      [p("Analyze Product",0),p("Write Description",1)],
      None,["product_details"],
      c("Product Description","Write e-commerce descriptions","Write a product description for [product]")),

    t("press-release","Press Release Writer","content",
      "Write professional press releases for announcements",
      ["press","release","PR","announcement","media","news"],
      [a("PR Writer","writer","Write a professional press release",["file_write"],"Write a press release following AP style. Include: compelling headline, dateline, strong lead paragraph (who/what/when/where/why), supporting quotes, body paragraphs with details, boilerplate about the company, and media contact. Keep it to one page.")],
      [p("Write Release",0)],
      None,["announcement","company"],
      c("Press Release","Write professional press releases","Write a press release about [announcement]")),

    t("video-script","Video Script Writer","content",
      "Write scripts for YouTube videos and video content",
      ["video","script","youtube","tutorial","vlog","content"],
      [a("Script Researcher","researcher","Research the video topic and trending formats",["web_fetch"],"Research the video topic. Find what performs well on YouTube for this topic. Identify key points, hooks, and common viewer questions. Note trending formats and video lengths."),
       a("Script Writer","writer","Write an engaging video script",["file_write"],"Write a video script with: attention-grabbing hook (first 10 seconds), intro with value proposition, main content sections with visual cues, B-roll suggestions, call-to-action, and end screen script. Include timestamps and estimated duration.")],
      [p("Research",0),p("Write Script",1)],
      None,["topic","platform"],
      c("Video Script","Write YouTube and video scripts","Write a video script about [topic]")),

    t("case-study-writer","Case Study Writer","content",
      "Write compelling case studies from client success stories",
      ["case study","success","client","testimonial","results","story"],
      [a("Story Extractor","analyst","Extract the narrative arc from the raw data",[],"Analyze the provided case study data. Identify: the client's challenge, the solution implemented, key results/metrics, and the transformation story. Find the most compelling narrative angle."),
       a("Case Study Writer","writer","Write a polished case study",["file_write"],"Write a professional case study with: headline with results, client overview, challenge section, solution section, implementation details, results with specific metrics, client quote placeholder, and key takeaways. Make it scannable with headers and pull quotes.")],
      [p("Extract Story",0),p("Write Case Study",1)],
      None,["client_data"],
      c("Case Study","Write compelling case studies","Write a case study about [client success]")),

    t("grant-proposal","Grant Proposal Writer","content",
      "Write compelling grant proposals for funding applications",
      ["grant","proposal","funding","nonprofit","research","application"],
      [a("Proposal Researcher","researcher","Research the grant requirements and funder priorities",["web_fetch"],"Research the grant program requirements, funder priorities, past awarded projects, and evaluation criteria. Identify what makes a winning proposal for this funder."),
       a("Proposal Writer","writer","Write a compelling grant proposal",["file_write"],"Write a grant proposal with: executive summary, statement of need with data, project description, goals and objectives (SMART), methodology, timeline, budget justification, evaluation plan, and organizational capacity. Align language with funder priorities.")],
      [p("Research Grant",0),p("Write Proposal",1)],
      None,["project","funder"],
      c("Grant Proposal","Write funding proposals","Write a grant proposal for [project]")),

    t("whitepaper-writer","Whitepaper Writer","content",
      "Write authoritative whitepapers on technical or business topics",
      ["whitepaper","technical","authority","thought leadership","paper"],
      [a("Subject Researcher","researcher","Research the whitepaper topic in depth",["web_fetch"],"Research the topic thoroughly. Find data, statistics, expert opinions, case examples, and industry benchmarks. Identify the key argument or thesis the whitepaper should advance."),
       a("Whitepaper Author","writer","Write a professional whitepaper",["file_write"],"Write a professional whitepaper with: title page, abstract, introduction stating the problem, background/context, analysis with data, solution or recommendations, conclusion, and references. Maintain an authoritative but accessible tone. Target 2000-3000 words.")],
      [p("Research",0),p("Write Paper",1)],
      None,["topic"],
      c("Whitepaper","Write authoritative whitepapers","Write a whitepaper about [topic]")),

    t("speech-writer","Speech Writer","content",
      "Write speeches for presentations, events, and occasions",
      ["speech","presentation","talk","keynote","toast","address"],
      [a("Speech Writer","writer","Write a compelling speech tailored to the occasion",["file_write"],"Write a speech tailored to the occasion and audience. Include: strong opening hook, 3 main points with supporting stories/data, smooth transitions, memorable phrases, audience engagement moments, and a powerful closing. Add speaker notes for delivery tips. Estimate duration based on word count (~150 words per minute).")],
      [p("Write Speech",0)],
      None,["occasion","audience","duration"],
      c("Speech Writer","Write speeches for any occasion","Write a speech for [occasion]")),

    t("technical-blog","Technical Blog Writer","content",
      "Write in-depth technical blog posts with code examples",
      ["technical","blog","tutorial","code","programming","howto"],
      [a("Tech Researcher","researcher","Research the technical topic and best practices",["web_fetch"],"Research the technical topic. Find official documentation, best practices, common pitfalls, and real-world examples. Identify the latest version and any recent changes."),
       a("Tech Writer","writer","Write a detailed technical blog post",["file_write"],"Write a technical blog post with: clear title, TL;DR section, prerequisites, step-by-step explanation with code snippets, diagrams (described in text), common errors and solutions, conclusion with next steps. Use proper code formatting and syntax highlighting hints.")],
      [p("Research",0),p("Write Post",1)],
      None,["topic","language"],
      c("Technical Blog","Write technical tutorials","Write a technical post about [topic]")),

    t("landing-page-copy","Landing Page Copywriter","content",
      "Write high-converting landing page copy",
      ["landing page","copy","conversion","marketing","website","sales"],
      [a("Market Researcher","researcher","Research the market and competitor landing pages",["web_fetch"],"Research competitor landing pages for similar products. Identify winning headlines, value propositions, social proof strategies, and CTA patterns. Understand the target audience's pain points."),
       a("Landing Page Writer","writer","Write conversion-optimized landing page copy",["file_write"],"Write landing page copy sections: hero headline + subheadline, value proposition, 3 key benefits with supporting copy, social proof section, features list, FAQ section, and CTA sections. Include multiple headline variants for A/B testing.")],
      [p("Research Market",0),p("Write Copy",1)],
      None,["product","audience"],
      c("Landing Page Copy","Write high-converting page copy","Write landing page copy for [product]")),

    # ── PRODUCTIVITY +12 ──
    t("meeting-agenda","Meeting Agenda Builder","productivity",
      "Create structured meeting agendas with time allocations",
      ["meeting","agenda","plan","prepare","structure","schedule"],
      [a("Agenda Builder","planner","Create a structured meeting agenda",["file_write"],"Create a meeting agenda with: meeting objective, attendee roles, time-boxed agenda items with owners, discussion questions for each item, decision points, and parking lot. Allocate time based on priority. Include a 5-min buffer.")],
      [p("Build Agenda",0)],
      None,["meeting_topic","duration","attendees"],
      c("Meeting Agenda","Create structured agendas","Create an agenda for a meeting about [topic]")),

    t("project-estimator","Project Estimator","productivity",
      "Estimate project timelines, effort, and costs",
      ["estimate","project","timeline","cost","effort","planning"],
      [a("Scope Analyzer","analyst","Analyze project scope and identify work items",[],"Break down the project into work items. Identify technical complexity, dependencies, and unknowns. Consider similar past projects and industry benchmarks."),
       a("Estimator","planner","Create detailed estimates with ranges",["file_write"],"Create project estimates with: optimistic, likely, and pessimistic timelines (three-point estimation). Include effort hours by role, cost ranges, key assumptions, and risk factors that could affect estimates. Add a confidence level for each estimate.")],
      [p("Analyze Scope",0),p("Estimate",1)],
      None,["project_description"],
      c("Project Estimator","Estimate timelines and costs","Estimate this project: [description]")),

    t("retrospective-facilitator","Retrospective Facilitator","productivity",
      "Facilitate team retrospectives with structured frameworks",
      ["retro","retrospective","sprint","agile","improve","team"],
      [a("Retro Facilitator","coach","Facilitate a structured retrospective",["file_write"],"Facilitate a retrospective using the chosen framework (Start/Stop/Continue, 4Ls, or Sailboat). Analyze the input for themes. Group similar items. Identify the top 3 actionable improvements. Create SMART action items with owners and deadlines.")],
      [p("Facilitate Retro",0)],
      None,["feedback","framework"],
      c("Retrospective","Run team retrospectives","Facilitate a retro: [what happened this sprint]")),

    t("okr-generator","OKR Generator","productivity",
      "Generate OKRs (Objectives and Key Results) for teams or individuals",
      ["okr","objective","key result","goal","metric","performance"],
      [a("OKR Architect","planner","Design meaningful OKRs aligned with strategy",["file_write"],"Create 3-5 objectives with 3-4 key results each. Make objectives inspiring and ambitious. Make key results specific, measurable, and time-bound. Include baseline metrics, target values, and suggested initiatives for each KR. Score difficulty 1-10.")],
      [p("Generate OKRs",0)],
      None,["focus_area","timeframe"],
      c("OKR Generator","Create OKRs for teams","Generate OKRs for [team/focus area]")),

    t("sop-writer","SOP Writer","productivity",
      "Write Standard Operating Procedures for any process",
      ["sop","procedure","process","documentation","standard","operations"],
      [a("Process Analyzer","analyst","Analyze the process and identify all steps",[],"Analyze the described process. Identify all steps, decision points, inputs, outputs, roles, and potential failure modes. Map the process flow."),
       a("SOP Writer","writer","Write a formal Standard Operating Procedure",["file_write"],"Write an SOP document with: purpose, scope, definitions, responsibilities, prerequisites, step-by-step procedures with numbered steps, decision trees, quality checks, troubleshooting guide, and revision history template. Follow ISO-style formatting.")],
      [p("Analyze Process",0),p("Write SOP",1)],
      None,["process_description"],
      c("SOP Writer","Write standard procedures","Write an SOP for [process]")),

    t("status-report","Status Report Generator","productivity",
      "Generate professional project status reports",
      ["status","report","update","progress","stakeholder","project"],
      [a("Report Generator","writer","Generate a structured status report",["file_write"],"Generate a project status report with: RAG status (Red/Amber/Green), executive summary, accomplishments this period, planned next period, risks and issues with mitigation plans, budget status, milestone tracker, and blockers needing escalation. Keep it concise and action-oriented.")],
      [p("Generate Report",0)],
      None,["project_status"],
      c("Status Report","Generate project status reports","Create a status report: [project updates]")),

    t("email-sequence","Email Sequence Planner","productivity",
      "Plan multi-email sequences for onboarding, sales, or nurture campaigns",
      ["email","sequence","campaign","drip","onboarding","nurture"],
      [a("Sequence Strategist","strategist","Plan the email sequence strategy",[],"Design the email sequence flow. Determine: number of emails, timing between sends, goal of each email, and progression logic. Consider the audience journey and conversion goals."),
       a("Sequence Writer","writer","Write all emails in the sequence",["file_write"],"Write each email in the sequence with: subject line (with A/B variant), preview text, body copy, CTA, and send timing. Ensure narrative progression across emails. Include merge field placeholders.")],
      [p("Plan Strategy",0),p("Write Emails",1)],
      None,["goal","audience"],
      c("Email Sequence","Plan multi-email campaigns","Plan an email sequence for [goal]")),

    t("risk-register","Risk Register Builder","productivity",
      "Create and manage project risk registers",
      ["risk","register","mitigation","assessment","project","management"],
      [a("Risk Analyst","analyst","Identify and assess project risks",[],"Identify potential risks across categories: technical, schedule, resource, external, and scope. For each risk, assess probability (1-5), impact (1-5), and calculate risk score. Suggest risk owners."),
       a("Mitigation Planner","planner","Create mitigation and contingency plans",["file_write"],"Create a risk register table with: risk ID, description, category, probability, impact, risk score, owner, mitigation strategy, contingency plan, and triggers. Prioritize by risk score. Include a risk heat map description.")],
      [p("Identify Risks",0),p("Plan Mitigations",1)],
      None,["project_description"],
      c("Risk Register","Build project risk registers","Create a risk register for [project]")),

    t("process-mapper","Process Mapper","productivity",
      "Map and optimize business processes visually",
      ["process","map","workflow","flowchart","optimize","BPMN"],
      [a("Process Analyst","analyst","Analyze and map the current process",[],"Analyze the described process. Identify all steps, actors, decisions, parallel paths, and handoffs. Detect bottlenecks, redundancies, and waste."),
       a("Process Optimizer","planner","Optimize the process and create documentation",["file_write"],"Create a process map in text format (using ASCII flowchart). Document current state and proposed optimized state. Identify: eliminated steps, automated steps, parallelized steps. Calculate estimated time savings.")],
      [p("Analyze Process",0),p("Optimize",1)],
      None,["process_description"],
      c("Process Mapper","Map and optimize processes","Map this process: [description]")),

    t("presentation-outliner","Presentation Outliner","productivity",
      "Create structured presentation outlines with speaker notes",
      ["presentation","slides","outline","powerpoint","keynote","deck"],
      [a("Presentation Planner","planner","Plan the presentation structure and flow",[],"Plan a presentation with logical flow. Determine: key message, audience needs, number of slides, and narrative arc. Use the rule of three for main points."),
       a("Slide Writer","writer","Write slide content and speaker notes",["file_write"],"Write each slide with: title, 3-5 bullet points (not too wordy), speaker notes with talking points, and visual/diagram suggestions. Include title slide, agenda, main content, summary, and Q&A slide. Keep slides clean and focused.")],
      [p("Plan Structure",0),p("Write Slides",1)],
      None,["topic","audience","duration"],
      c("Presentation Outliner","Create presentation outlines","Create a presentation about [topic]")),

    t("knowledge-base-builder","Knowledge Base Builder","productivity",
      "Build structured knowledge base articles from raw information",
      ["knowledge base","wiki","documentation","FAQ","help center","article"],
      [a("Content Organizer","analyst","Organize raw information into knowledge base structure",[],"Analyze the raw information. Identify distinct topics, subtopics, and frequently asked questions. Create a logical category hierarchy and cross-references."),
       a("Article Writer","writer","Write polished knowledge base articles",["file_write"],"Write knowledge base articles with: clear title, brief description, step-by-step instructions where applicable, screenshots placeholders, related articles links, and tags. Use consistent formatting. Include a search-friendly summary.")],
      [p("Organize Content",0),p("Write Articles",1)],
      None,["raw_content"],
      c("Knowledge Base","Build KB articles from notes","Create knowledge base articles from: [raw info]")),

    t("time-audit","Time Audit Analyzer","productivity",
      "Analyze how you spend time and find optimization opportunities",
      ["time","audit","productivity","efficiency","schedule","optimize"],
      [a("Time Analyst","analyst","Analyze time usage data and identify patterns",[],"Analyze the time data provided. Categorize activities (deep work, meetings, admin, breaks, etc). Calculate time allocation percentages. Identify time wasters, context switches, and productive patterns."),
       a("Productivity Coach","coach","Provide actionable time optimization advice",["file_write"],"Create a time audit report with: current time allocation breakdown, comparison to ideal ratios, top 3 time wasters, specific optimization recommendations, suggested schedule restructure, and tools/techniques to implement. Include a sample optimized daily schedule.")],
      [p("Analyze Time",0),p("Coach",1)],
      None,["time_data"],
      c("Time Audit","Analyze and optimize time usage","Audit my time usage: [how I spent my week]")),

    # ── DEVELOPMENT +14 ──
    t("migration-planner","Migration Planner","development",
      "Plan code or system migrations with step-by-step strategies",
      ["migration","upgrade","refactor","legacy","modernize","transition"],
      [a("Migration Analyst","analyst","Analyze the current system and target state",["file_read"],"Analyze the current system architecture, dependencies, and pain points. Define the target state. Identify breaking changes, data migration needs, and rollback strategies."),
       a("Migration Planner","planner","Create a detailed migration plan",["file_write"],"Create a phased migration plan with: pre-migration checklist, step-by-step migration phases, data migration strategy, testing requirements per phase, rollback procedures, timeline, and risk mitigation. Include a go/no-go decision framework.")],
      [p("Analyze Systems",0),p("Plan Migration",1)],
      None,["current_system","target_system"],
      c("Migration Planner","Plan system migrations","Plan a migration from [current] to [target]")),

    t("dependency-auditor","Dependency Auditor","development",
      "Audit project dependencies for vulnerabilities and updates",
      ["dependency","audit","vulnerability","security","outdated","package"],
      [a("Dependency Scanner","analyst","Scan and catalog all project dependencies",["file_read","shell"],"Read the project's dependency files (package.json, Cargo.toml, requirements.txt, etc). List all direct and transitive dependencies with versions. Check for known vulnerabilities using public databases."),
       a("Audit Reporter","writer","Write a dependency audit report",["file_write"],"Write an audit report with: dependency inventory, vulnerable packages with severity ratings, outdated packages with latest versions, unused dependencies, license compatibility issues, and prioritized update recommendations.")],
      [p("Scan Dependencies",0),p("Write Report",1)],
      None,["project_path"],
      c("Dependency Auditor","Audit project dependencies","Audit dependencies in [project path]")),

    t("cicd-helper","CI/CD Pipeline Helper","development",
      "Design and troubleshoot CI/CD pipelines",
      ["cicd","pipeline","deploy","github actions","jenkins","automation"],
      [a("Pipeline Designer","architect","Design or troubleshoot CI/CD pipeline configurations",["file_read"],"Analyze the project structure and requirements. Design a CI/CD pipeline with: build, test, lint, security scan, and deploy stages. Handle environment-specific configs and secrets management."),
       a("Config Writer","developer","Write pipeline configuration files",["file_write"],"Write the CI/CD configuration (GitHub Actions, GitLab CI, or Jenkins). Include: trigger conditions, caching, parallel jobs, environment variables, artifact management, deployment steps, and rollback mechanism. Add comments explaining each section.")],
      [p("Design Pipeline",0),p("Write Config",1)],
      None,["project_type","platform"],
      c("CI/CD Helper","Design CI/CD pipelines","Create a CI/CD pipeline for [project type]")),

    t("perf-profiler","Performance Profiler","development",
      "Analyze code for performance bottlenecks and optimization opportunities",
      ["performance","optimize","profile","bottleneck","speed","benchmark"],
      [a("Perf Analyzer","analyst","Analyze code for performance issues",["file_read"],"Analyze the code for performance issues. Look for: N+1 queries, unnecessary allocations, blocking operations, missing indexes, inefficient algorithms, and memory leaks. Benchmark critical paths."),
       a("Optimization Advisor","advisor","Recommend specific performance optimizations",["file_write"],"Write a performance report with: identified bottlenecks ranked by impact, specific optimization recommendations with code examples, expected improvement estimates, trade-offs of each optimization, and benchmarking suggestions.")],
      [p("Analyze Performance",0),p("Recommend",1)],
      None,["code_or_path"],
      c("Performance Profiler","Find and fix performance issues","Profile this code for performance: [code]")),

    t("architecture-reviewer","Architecture Reviewer","development",
      "Review system architecture designs and suggest improvements",
      ["architecture","design","review","system","scalability","patterns"],
      [a("Architecture Reviewer","architect","Review architecture for issues and improvements",["file_read"],"Review the system architecture. Evaluate: scalability, fault tolerance, security, maintainability, and cost efficiency. Identify single points of failure, tight coupling, and missing components. Compare against best practices and known patterns."),
       a("Recommendation Writer","writer","Write architecture review findings",["file_write"],"Write an architecture review document with: summary assessment, strengths, concerns ranked by severity, specific recommendations with rationale, suggested architecture diagram changes, and migration path for improvements.")],
      [p("Review Architecture",0),p("Write Findings",1)],
      None,["architecture_description"],
      c("Architecture Review","Review system architecture","Review this architecture: [description]")),

    t("regex-builder","Regex Builder","development",
      "Build and explain regular expressions for any pattern",
      ["regex","regular expression","pattern","match","parse","extract"],
      [a("Regex Engineer","developer","Build and explain regular expressions",["file_write"],"Build a regex pattern for the user's requirements. Provide: the regex pattern, a plain-English explanation of each part, test cases that match, test cases that don't match, edge cases to consider, and variants for different regex engines (PCRE, JavaScript, Python). Include common gotchas.")],
      [p("Build Regex",0)],
      None,["pattern_description"],
      c("Regex Builder","Build and test regex patterns","Build a regex to match [pattern]")),

    t("error-decoder","Error Message Decoder","development",
      "Decode cryptic error messages and stack traces into fixes",
      ["error","decode","stack trace","exception","crash","debug"],
      [a("Error Researcher","researcher","Research the error message and find solutions",["web_fetch"],"Research the error message or stack trace. Search Stack Overflow, GitHub issues, and documentation for this exact error. Find the most common causes and verified solutions."),
       a("Solution Writer","writer","Write a clear explanation and fix",["file_write"],"Write a clear explanation of: what the error means in plain English, the most likely cause, step-by-step fix instructions, alternative solutions if the first doesn't work, and how to prevent it in the future. Include code snippets where applicable.")],
      [p("Research Error",0),p("Write Solution",1)],
      None,[],
      c("Error Decoder","Decode error messages into fixes","Fix this error: [paste error message]")),

    t("security-scanner","Security Review Scanner","development",
      "Scan code for common security vulnerabilities",
      ["security","vulnerability","scan","OWASP","injection","XSS"],
      [a("Security Scanner","analyst","Scan code for security vulnerabilities",["file_read"],"Scan the code for OWASP Top 10 vulnerabilities: injection, broken auth, sensitive data exposure, XXE, broken access control, misconfig, XSS, insecure deserialization, known vulnerabilities, and insufficient logging."),
       a("Security Reporter","writer","Write a security scan report",["file_write"],"Write a security report with: findings ranked by CVSS-style severity (Critical/High/Medium/Low), affected code locations, exploit scenarios, specific remediation steps with code examples, and a summary security score.")],
      [p("Scan Code",0),p("Write Report",1)],
      None,["code_or_path"],
      c("Security Scanner","Scan code for vulnerabilities","Scan this code for security issues: [code]")),

    t("dockerfile-generator","Dockerfile Generator","development",
      "Generate optimized Dockerfiles and docker-compose configs",
      ["docker","container","dockerfile","compose","deploy","image"],
      [a("Docker Architect","architect","Design the containerization strategy",["file_read"],"Analyze the project to determine: base image, build stages, runtime dependencies, ports, volumes, and environment variables. Design multi-stage builds for optimal image size."),
       a("Docker Writer","developer","Write Dockerfile and compose configuration",["file_write"],"Write an optimized Dockerfile with: multi-stage build, minimal base image, proper layer caching, non-root user, health checks, and security best practices. Also write docker-compose.yml if multiple services are needed. Add comments explaining each directive.")],
      [p("Design",0),p("Write Config",1)],
      None,["project_type"],
      c("Dockerfile Generator","Generate Docker configurations","Create a Dockerfile for [project type]")),

    t("code-converter","Code Converter","development",
      "Convert code between programming languages",
      ["convert","translate","port","language","transform","rewrite"],
      [a("Code Analyzer","analyst","Analyze the source code and identify conversion challenges",["file_read"],"Analyze the source code. Identify language-specific features that need special handling during conversion: idioms, standard library usage, error handling patterns, memory management, and concurrency models."),
       a("Code Converter","developer","Convert code to the target language",["file_write"],"Convert the code to the target language. Use idiomatic patterns of the target language (don't just transliterate). Handle: error patterns, null safety, type systems, and standard library equivalents. Add comments for non-obvious conversions. Include a conversion notes section.")],
      [p("Analyze Source",0),p("Convert",1)],
      None,["target_language"],
      c("Code Converter","Convert between languages","Convert this code to [language]: [code]")),

    t("api-mock-generator","API Mock Generator","development",
      "Generate mock API servers and test data from API specs",
      ["mock","api","test data","stub","fixture","fake"],
      [a("Spec Analyzer","analyst","Analyze the API specification",["file_read"],"Analyze the API spec (OpenAPI/Swagger or description). Identify all endpoints, request/response schemas, data types, and relationships between entities. Determine realistic data constraints."),
       a("Mock Generator","developer","Generate mock server code and test data",["file_write"],"Generate: mock server code with all endpoints returning realistic fake data, test fixture files (JSON), factory functions for generating test data, and edge case data (empty, maximum, unicode, etc). Match the specified framework/language.")],
      [p("Analyze Spec",0),p("Generate Mocks",1)],
      None,["api_spec"],
      c("API Mock Generator","Generate mock APIs and test data","Generate mocks for this API: [spec or description]")),

    t("refactor-advisor","Refactoring Advisor","development",
      "Analyze code and suggest refactoring improvements",
      ["refactor","clean code","code smell","improve","maintainability","SOLID"],
      [a("Code Smell Detector","analyst","Identify code smells and anti-patterns",["file_read"],"Analyze the code for: code smells (long methods, large classes, feature envy, etc), SOLID violations, DRY violations, complexity hotspots, and naming issues. Measure rough cyclomatic complexity."),
       a("Refactoring Advisor","advisor","Suggest specific refactoring strategies",["file_write"],"Suggest refactorings with: the code smell identified, the refactoring pattern to apply (Extract Method, Strategy Pattern, etc), before/after code examples, risk level of the change, and recommended order of refactoring. Prioritize by impact and safety.")],
      [p("Detect Smells",0),p("Suggest Refactoring",1)],
      None,["code_or_path"],
      c("Refactoring Advisor","Get refactoring suggestions","Suggest refactorings for: [code]")),

    t("commit-message-writer","Commit Message Writer","development",
      "Write clear, conventional commit messages from code diffs",
      ["commit","message","git","conventional","changelog","diff"],
      [a("Diff Analyzer","analyst","Analyze the code diff and understand changes",[],"Analyze the provided code diff. Identify: what changed, why it likely changed (bug fix, feature, refactor, etc), affected components, and breaking changes."),
       a("Message Writer","writer","Write a well-formatted commit message",["file_write"],"Write a commit message following Conventional Commits format. Include: type (feat/fix/refactor/docs/test/chore), optional scope, concise subject line (<50 chars), detailed body explaining what and why, and footer with breaking changes or issue references.")],
      [p("Analyze Diff",0),p("Write Message",1)],
      None,[],
      c("Commit Message","Write commit messages from diffs","Write a commit message for this diff: [diff]")),

    t("load-test-designer","Load Test Designer","development",
      "Design load testing scenarios and scripts",
      ["load test","stress test","performance","benchmark","k6","jmeter"],
      [a("Test Designer","architect","Design load testing scenarios",[],"Design load test scenarios covering: baseline performance, stress testing, spike testing, and soak testing. Define virtual user profiles, think times, ramp-up patterns, and success criteria (response time, error rate, throughput)."),
       a("Script Writer","developer","Write load test scripts",["file_write"],"Write load test scripts (k6 or similar). Include: scenario configuration, realistic user flows, dynamic data generation, assertions/checks, and result analysis thresholds. Add setup/teardown and custom metrics. Include a runner script with environment configs.")],
      [p("Design Scenarios",0),p("Write Scripts",1)],
      None,["system_description","target_load"],
      c("Load Test Designer","Design load test scenarios","Design load tests for [system]")),

    # ── PERSONAL +10 ──
    t("recipe-converter","Recipe Converter & Scaler","personal",
      "Convert recipes between measurement systems and scale servings",
      ["recipe","convert","scale","metric","imperial","servings"],
      [a("Recipe Converter","writer","Convert and scale recipes accurately",["file_write"],"Convert the recipe between measurement systems (metric/imperial). Scale all ingredients proportionally to the desired serving size. Adjust cooking times and temperatures. Note ingredients that don't scale linearly (e.g., spices, leavening). Include both original and converted versions.")],
      [p("Convert Recipe",0)],
      None,["recipe","target_servings"],
      c("Recipe Converter","Convert and scale recipes","Convert this recipe to [servings] servings: [recipe]")),

    t("home-maintenance","Home Maintenance Scheduler","personal",
      "Create a seasonal home maintenance schedule",
      ["home","maintenance","house","repair","seasonal","schedule"],
      [a("Maintenance Planner","planner","Create a comprehensive maintenance schedule",["file_write"],"Create a seasonal home maintenance schedule based on the home type and climate. Include: spring, summer, fall, and winter tasks. Cover HVAC, plumbing, electrical, exterior, interior, and appliances. Add estimated time and cost for each task. Flag critical vs nice-to-have tasks.")],
      [p("Plan Maintenance",0)],
      None,["home_type","climate"],
      c("Home Maintenance","Schedule home maintenance","Create a maintenance schedule for my [home type]")),

    t("pet-care-planner","Pet Care Planner","personal",
      "Create personalized pet care routines and health schedules",
      ["pet","care","dog","cat","vet","health","routine"],
      [a("Pet Care Researcher","researcher","Research breed-specific care requirements",["web_fetch"],"Research care requirements for the specific pet breed. Find: dietary needs, exercise requirements, grooming schedule, common health issues, vaccination schedule, and age-specific care tips."),
       a("Care Plan Writer","planner","Create a comprehensive pet care plan",["file_write"],"Create a personalized pet care plan with: daily routine (feeding, exercise, grooming), weekly tasks, monthly tasks, annual vet visits and vaccinations, diet recommendations, training tips, and warning signs to watch for.")],
      [p("Research",0),p("Plan Care",1)],
      None,["pet_type","breed","age"],
      c("Pet Care","Create pet care routines","Create a care plan for my [age] year old [breed]")),

    t("wardrobe-planner","Wardrobe Capsule Planner","personal",
      "Plan a capsule wardrobe with versatile outfit combinations",
      ["wardrobe","fashion","capsule","outfit","style","clothing"],
      [a("Style Advisor","advisor","Plan a capsule wardrobe",["file_write"],"Create a capsule wardrobe plan based on the user's style preferences, climate, and lifestyle. Include: essential pieces list (30-40 items), color palette, outfit combinations (aim for 50+ outfits from the capsule), shopping list for missing pieces with budget estimates, and seasonal swap suggestions.")],
      [p("Plan Wardrobe",0)],
      None,["style","climate","lifestyle"],
      c("Wardrobe Planner","Build a capsule wardrobe","Plan a capsule wardrobe for [style] in [climate]")),

    t("meditation-guide","Meditation & Mindfulness Guide","personal",
      "Get guided meditation scripts and mindfulness exercises",
      ["meditation","mindfulness","calm","stress","breathe","relax"],
      [a("Meditation Guide","coach","Create guided meditation and mindfulness exercises",["file_write"],"Create a guided meditation script tailored to the user's needs. Include: preparation instructions, breathing exercise, body scan or visualization, main meditation practice, and gentle closing. Time each section. Offer modifications for beginners and experienced practitioners.")],
      [p("Guide Meditation",0)],
      None,["focus","duration"],
      c("Meditation Guide","Guided meditation scripts","Guide me through a [duration] minute meditation for [focus]")),

    t("moving-checklist","Moving Checklist Generator","personal",
      "Generate comprehensive moving checklists and timelines",
      ["moving","checklist","relocate","pack","house","apartment"],
      [a("Moving Planner","planner","Create a detailed moving plan and checklist",["file_write"],"Create a comprehensive moving checklist organized by timeline: 8 weeks before, 6 weeks, 4 weeks, 2 weeks, 1 week, moving day, and after move. Include: admin tasks, packing strategy by room, utilities to transfer, address changes, cleaning tasks, and budget tracker.")],
      [p("Plan Move",0)],
      None,["move_date","distance"],
      c("Moving Checklist","Plan your move step by step","Create a moving checklist for [move date]")),

    t("book-club-guide","Book Club Discussion Guide","personal",
      "Generate book club discussion guides with questions and themes",
      ["book club","discussion","reading","questions","literary","group"],
      [a("Book Researcher","researcher","Research the book for discussion material",["web_fetch"],"Research the book thoroughly. Find: plot summary, major themes, author's intent, literary devices, historical context, and critical reception. Identify controversial or thought-provoking elements."),
       a("Guide Writer","writer","Write a book club discussion guide",["file_write"],"Create a discussion guide with: book overview (spoiler-free intro and full summary), 15-20 discussion questions organized by theme, character analysis prompts, thematic explorations, author background, similar book recommendations, and activity suggestions for the meeting.")],
      [p("Research Book",0),p("Write Guide",1)],
      None,["book_title"],
      c("Book Club Guide","Create discussion guides","Create a book club guide for [book title]")),

    t("event-planner","Event Planner","personal",
      "Plan events with timelines, budgets, and vendor checklists",
      ["event","party","plan","celebrate","venue","catering"],
      [a("Event Researcher","researcher","Research venues, vendors, and event ideas",["web_fetch"],"Research event options. Find venue ideas, catering options, entertainment, decoration themes, and vendor pricing in the specified area and budget range."),
       a("Event Planner","planner","Create a detailed event plan",["file_write"],"Create a comprehensive event plan with: timeline (countdown from event date), budget breakdown, guest list management tips, venue checklist, vendor contact list template, day-of schedule (hour by hour), and contingency plans. Include decoration and theme ideas.")],
      [p("Research Options",0),p("Plan Event",1)],
      None,["event_type","budget","guest_count"],
      c("Event Planner","Plan any event","Plan a [event type] for [guest count] people")),

    t("sleep-optimizer","Sleep Optimizer","personal",
      "Analyze sleep habits and get personalized improvement advice",
      ["sleep","insomnia","rest","circadian","routine","health"],
      [a("Sleep Analyst","analyst","Analyze sleep patterns and identify issues",[],"Analyze the reported sleep data: bedtime, wake time, sleep quality, disruptions, caffeine/screen habits, and environment. Identify issues affecting sleep quality."),
       a("Sleep Coach","coach","Provide personalized sleep improvement advice",["file_write"],"Create a personalized sleep improvement plan with: sleep hygiene audit, specific recommendations ranked by impact, ideal sleep schedule based on chronotype, evening routine design, bedroom environment optimization, and a 2-week gradual improvement plan. Cite sleep science research.")],
      [p("Analyze Sleep",0),p("Coach",1)],
      None,["sleep_data"],
      c("Sleep Optimizer","Improve your sleep quality","Help me improve my sleep: [sleep habits]")),

    t("hobby-finder","Hobby Finder","personal",
      "Discover new hobbies based on your interests and lifestyle",
      ["hobby","interest","activity","leisure","creative","sport"],
      [a("Hobby Researcher","researcher","Research hobbies matching the user's profile",["web_fetch"],"Research hobbies matching the user's interests, available time, budget, and physical ability. Find beginner-friendly options, local resources, online communities, and equipment costs."),
       a("Hobby Advisor","advisor","Recommend hobbies with getting-started guides",["file_write"],"Recommend 10 hobbies with: description, why it fits the user, difficulty level, startup cost, time commitment, how to start (first 3 steps), local/online resources, and community links. Group by category: creative, physical, intellectual, social.")],
      [p("Research Hobbies",0),p("Recommend",1)],
      None,["interests","time_available","budget"],
      c("Hobby Finder","Discover new hobbies","Find hobbies for someone who likes [interests]")),

    # ── FINANCE +10 ──
    t("expense-report","Expense Report Generator","finance",
      "Generate formatted expense reports from raw expense data",
      ["expense","report","receipt","reimbursement","business","travel"],
      [a("Expense Organizer","analyst","Organize and categorize expense data",[],"Parse the raw expense data. Categorize each expense (travel, meals, accommodation, transport, supplies, etc). Validate amounts and dates. Flag any items that may need receipts or exceed typical limits."),
       a("Report Writer","writer","Generate a formatted expense report",["file_write"],"Generate a professional expense report with: report period, purpose of expenses, itemized list with date/vendor/category/amount, category subtotals, grand total, policy compliance notes, and required approvals. Format as a clean table.")],
      [p("Organize Expenses",0),p("Write Report",1)],
      None,["expense_data"],
      c("Expense Report","Generate expense reports","Create an expense report: [expenses]")),

    t("tax-prep-helper","Tax Preparation Helper","finance",
      "Organize tax documents and identify deductions",
      ["tax","deduction","IRS","filing","return","preparation"],
      [a("Tax Organizer","analyst","Organize tax documents and identify deductions",[],"Analyze the provided financial information. Organize into income sources, deductible expenses, credits, and required forms. Identify commonly missed deductions for the user's situation. Flag items needing documentation."),
       a("Tax Advisor","advisor","Provide tax preparation guidance",["file_write"],"Create a tax preparation guide with: document checklist organized by form, identified deductions with estimated value, tax credit eligibility, deadline reminders, estimated tax liability, and suggestions for reducing next year's taxes. Include standard disclaimer about seeking professional advice.")],
      [p("Organize Documents",0),p("Advise",1)],
      None,["financial_info"],
      c("Tax Prep","Organize taxes and find deductions","Help me prepare taxes: [income and expenses]")),

    t("investment-portfolio","Portfolio Analyzer","finance",
      "Analyze investment portfolio allocation and suggest rebalancing",
      ["portfolio","investment","allocation","rebalance","diversification","asset"],
      [a("Portfolio Analyst","analyst","Analyze portfolio composition and risk",[],"Analyze the portfolio holdings. Calculate: asset allocation percentages, sector concentration, geographic diversification, risk metrics, and deviation from target allocation. Identify overweight and underweight positions."),
       a("Rebalance Advisor","advisor","Suggest portfolio rebalancing actions",["file_write"],"Create a portfolio analysis report with: current allocation pie chart (text), risk assessment, comparison to target allocation, specific rebalancing trades needed, tax-loss harvesting opportunities, and recommendations for improved diversification. Include standard investment disclaimer.")],
      [p("Analyze Portfolio",0),p("Recommend",1)],
      None,["holdings"],
      c("Portfolio Analyzer","Analyze investment portfolios","Analyze my portfolio: [holdings]")),

    t("subscription-tracker","Subscription Tracker","finance",
      "Track all subscriptions and find savings opportunities",
      ["subscription","recurring","cancel","save","monthly","annual"],
      [a("Subscription Analyst","analyst","Analyze subscriptions for savings opportunities",[],"Catalog all subscriptions with: name, cost, billing cycle, and usage estimate. Calculate total monthly and annual spend. Identify overlapping services, underused subscriptions, and available cheaper alternatives."),
       a("Savings Advisor","advisor","Recommend subscription optimizations",["file_write"],"Create a subscription audit report with: complete subscription inventory, total monthly/annual costs, underused subscriptions to cancel, services to downgrade, cheaper alternatives, annual vs monthly savings opportunities, and projected annual savings.")],
      [p("Analyze Subscriptions",0),p("Recommend",1)],
      None,["subscriptions"],
      c("Subscription Tracker","Find subscription savings","Audit my subscriptions: [list of subscriptions]")),

    t("retirement-planner","Retirement Calculator","finance",
      "Calculate retirement projections and savings targets",
      ["retirement","savings","401k","IRA","compound","future"],
      [a("Retirement Analyst","analyst","Calculate retirement projections",[],"Calculate retirement projections based on: current savings, monthly contributions, expected return rate, inflation, retirement age, and desired retirement income. Model multiple scenarios (conservative, moderate, aggressive)."),
       a("Retirement Advisor","advisor","Provide retirement planning advice",["file_write"],"Create a retirement planning report with: projected retirement balance at target age, monthly income in retirement, savings gap analysis, recommended contribution increases, account type optimization (401k vs IRA vs taxable), and Social Security considerations. Include multiple scenario projections. Add financial disclaimer.")],
      [p("Calculate Projections",0),p("Advise",1)],
      None,["current_savings","monthly_contribution","retirement_age"],
      c("Retirement Planner","Plan your retirement","Plan retirement: [age], [savings], [contributions]")),

    t("debt-payoff","Debt Payoff Strategizer","finance",
      "Create optimal debt payoff strategies",
      ["debt","payoff","loan","credit card","interest","snowball","avalanche"],
      [a("Debt Analyst","analyst","Analyze debt portfolio and calculate payoff strategies",[],"Analyze all debts: balances, interest rates, minimum payments, and terms. Calculate both avalanche (highest interest first) and snowball (smallest balance first) strategies. Compare total interest paid and payoff timelines."),
       a("Payoff Planner","planner","Create a detailed debt payoff plan",["file_write"],"Create a debt payoff plan with: debt inventory table, avalanche vs snowball comparison, recommended strategy with reasoning, month-by-month payment schedule, total interest saved, debt-free date, and motivational milestones. Include extra payment impact calculator.")],
      [p("Analyze Debts",0),p("Plan Payoff",1)],
      None,["debts"],
      c("Debt Payoff","Create debt payoff strategies","Plan to pay off: [list debts with balances and rates]")),

    t("freelance-rate","Freelance Rate Calculator","finance",
      "Calculate optimal freelance rates based on expenses and goals",
      ["freelance","rate","hourly","pricing","contractor","billing"],
      [a("Rate Calculator","analyst","Calculate optimal freelance rates",["file_write"],"Calculate the optimal freelance rate considering: desired annual income, business expenses, taxes (self-employment + income), benefits costs (health insurance, retirement), non-billable hours (admin, marketing, learning), vacation days, and utilization rate. Provide hourly, daily, and project-based rate recommendations. Compare with market rates.")],
      [p("Calculate Rate",0)],
      None,["desired_income","expenses"],
      c("Rate Calculator","Calculate freelance rates","Calculate my freelance rate: [income goal] and [expenses]")),

    t("net-worth-tracker","Net Worth Tracker","finance",
      "Calculate and track net worth with growth projections",
      ["net worth","assets","liabilities","wealth","track","financial"],
      [a("Net Worth Analyst","analyst","Calculate net worth and analyze trends",[],"Calculate net worth from provided assets and liabilities. Categorize assets (liquid, invested, property, other) and liabilities (mortgage, loans, credit). Calculate key ratios: debt-to-asset, liquid net worth, and savings rate."),
       a("Wealth Advisor","advisor","Provide net worth growth strategies",["file_write"],"Create a net worth report with: asset and liability breakdown, net worth calculation, key financial ratios, comparison to age-based benchmarks, growth projections, and specific recommendations to grow net worth. Include strategies for each category: increase assets, reduce liabilities, optimize allocation.")],
      [p("Calculate",0),p("Advise",1)],
      None,["assets","liabilities"],
      c("Net Worth Tracker","Track and grow net worth","Calculate my net worth: [assets] and [liabilities]")),

    t("business-expense-categorizer","Business Expense Categorizer","finance",
      "Automatically categorize business expenses for accounting",
      ["categorize","accounting","bookkeeping","expense","business","ledger"],
      [a("Expense Categorizer","analyst","Categorize expenses by accounting category",["file_write"],"Categorize each expense into standard accounting categories: COGS, operating expenses, office supplies, travel, marketing, utilities, insurance, professional services, software/subscriptions, meals/entertainment, etc. Apply IRS guidelines for deductibility. Flag items needing review or split between categories. Output in accounting-friendly format.")],
      [p("Categorize",0)],
      None,["expense_list"],
      c("Expense Categorizer","Categorize business expenses","Categorize these expenses: [expense list]")),

    t("financial-goal-tracker","Financial Goal Tracker","finance",
      "Set and track progress toward financial goals",
      ["goal","savings","target","progress","financial","milestone"],
      [a("Goal Analyst","analyst","Analyze progress toward financial goals",[],"Analyze each financial goal: target amount, current progress, timeline, and monthly contribution needed. Calculate if the user is on track, ahead, or behind for each goal. Factor in returns for investment goals."),
       a("Goal Coach","coach","Provide guidance to stay on track",["file_write"],"Create a financial goals dashboard with: goal summary table, progress bars (text), on-track status for each goal, required adjustments if behind, celebration notes if ahead, recommended priority order, and specific monthly action items. Provide motivational context.")],
      [p("Analyze Goals",0),p("Coach",1)],
      None,["goals"],
      c("Goal Tracker","Track financial goals","Track my financial goals: [goals with targets]")),

    # ── LEARNING +10 ──
    t("coding-kata","Coding Kata Generator","learning",
      "Generate coding exercises and challenges with solutions",
      ["coding","kata","exercise","practice","challenge","algorithm"],
      [a("Kata Designer","teacher","Design coding challenges appropriate to skill level",[],"Design a coding challenge appropriate to the skill level and language. Include: problem statement, input/output examples, constraints, hints (progressive), and bonus challenges. Cover various CS concepts: algorithms, data structures, string manipulation, etc."),
       a("Solution Writer","developer","Write detailed solutions with explanations",["file_write"],"Write a solution with: step-by-step approach explanation, code solution in the specified language, time and space complexity analysis, alternative approaches, and test cases. Explain the thought process a developer should follow.")],
      [p("Design Kata",0),p("Write Solution",1)],
      None,["language","difficulty"],
      c("Coding Kata","Practice coding challenges","Give me a [difficulty] [language] coding challenge")),

    t("certification-prep","Certification Prep Coach","learning",
      "Prepare for professional certifications with practice questions",
      ["certification","exam","prep","practice","questions","study"],
      [a("Exam Researcher","researcher","Research the certification exam format and topics",["web_fetch"],"Research the certification exam: format, number of questions, passing score, topic weights, question types, and recommended preparation approach. Find official study resources."),
       a("Practice Builder","teacher","Create practice questions and study materials",["file_write"],"Create a study package with: 20 practice questions matching exam format and difficulty, detailed explanations for correct and incorrect answers, topic-by-topic study notes for weak areas, exam strategy tips, and a study schedule. Group questions by domain/topic.")],
      [p("Research Exam",0),p("Build Practice",1)],
      None,["certification_name"],
      c("Cert Prep","Prepare for certifications","Help me prepare for [certification]")),

    t("math-tutor","Math Tutor","learning",
      "Get step-by-step explanations for math problems",
      ["math","tutor","calculus","algebra","statistics","equation"],
      [a("Math Tutor","teacher","Solve and explain math problems step by step",["file_write"],"Solve the math problem step by step. For each step: state what you're doing, why, and show the work. Use multiple approaches when possible. Relate to real-world applications. Provide similar practice problems at the end. Adapt explanations to the student's level.")],
      [p("Solve & Explain",0)],
      None,["problem"],
      c("Math Tutor","Step-by-step math help","Help me solve: [math problem]")),

    t("writing-tutor","Writing Coach","learning",
      "Get feedback and coaching on your writing skills",
      ["writing","grammar","style","feedback","improve","essay"],
      [a("Writing Reviewer","teacher","Review writing and provide constructive feedback",[],"Review the writing for: clarity, structure, grammar, style, voice, and persuasiveness. Identify both strengths and areas for improvement. Be constructive and encouraging."),
       a("Writing Coach","coach","Provide specific improvement suggestions with examples",["file_write"],"Provide a detailed writing review with: overall assessment, specific praise for what works well, grammar/spelling corrections, style suggestions with before/after examples, structural recommendations, voice and tone notes, and 3 specific exercises to improve identified weak areas.")],
      [p("Review Writing",0),p("Coach",1)],
      None,[],
      c("Writing Coach","Improve your writing skills","Review my writing: [paste text]")),

    t("history-explorer","History Explorer","learning",
      "Explore historical events with context and analysis",
      ["history","historical","event","era","civilization","timeline"],
      [a("History Researcher","researcher","Research historical events and context",["web_fetch"],"Research the historical topic. Find: key events, dates, people involved, causes, consequences, different perspectives, primary source excerpts, and connections to other events. Include lesser-known but important details."),
       a("History Writer","writer","Write an engaging historical narrative",["file_write"],"Write an engaging historical exploration with: timeline of events, key figures and their motivations, cause and effect analysis, multiple perspectives, primary source quotes, lasting impact and legacy, and connections to present day. Make history come alive with narrative techniques.")],
      [p("Research History",0),p("Write Narrative",1)],
      None,["topic_or_era"],
      c("History Explorer","Explore historical events","Explore the history of [topic or era]")),

    t("debate-coach","Debate Coach","learning",
      "Prepare arguments for debates with pros, cons, and rebuttals",
      ["debate","argument","persuade","rhetoric","position","critical thinking"],
      [a("Research Assistant","researcher","Research both sides of the debate topic",["web_fetch"],"Research both sides of the debate topic thoroughly. Find strong arguments, evidence, statistics, expert opinions, and real-world examples for both positions. Identify the strongest and weakest points on each side."),
       a("Debate Coach","coach","Prepare debate arguments and rebuttals",["file_write"],"Prepare a debate brief with: opening statement, 3-5 main arguments with supporting evidence, anticipated opposing arguments with prepared rebuttals, key statistics and quotes, closing statement, and debate tips. Include both sides for balanced preparation.")],
      [p("Research Topic",0),p("Prepare Arguments",1)],
      None,["topic","position"],
      c("Debate Coach","Prepare for debates","Prepare arguments for [position] on [topic]")),

    t("science-experiment","Science Experiment Designer","learning",
      "Design science experiments with hypothesis, method, and analysis",
      ["science","experiment","hypothesis","method","lab","research"],
      [a("Experiment Designer","teacher","Design a rigorous science experiment",["file_write"],"Design a science experiment with: research question, background context, hypothesis (null and alternative), variables (independent, dependent, controlled), materials list, step-by-step procedure, safety precautions, data collection plan, expected results, and statistical analysis approach. Appropriate for the specified level (K-12 or university).")],
      [p("Design Experiment",0)],
      None,["topic","level"],
      c("Experiment Designer","Design science experiments","Design an experiment about [topic]")),

    t("vocabulary-builder","Vocabulary Builder","learning",
      "Build vocabulary with contextual usage and memory techniques",
      ["vocabulary","words","GRE","SAT","English","verbal"],
      [a("Vocab Researcher","researcher","Research words and create learning materials",["web_fetch"],"For each word or word list: find definitions, etymology, pronunciation guide, example sentences from real usage, synonyms, antonyms, and common collocations. Group words by theme or root."),
       a("Vocab Builder","teacher","Create vocabulary learning cards with memory aids",["file_write"],"Create vocabulary study materials with: word, definition, part of speech, pronunciation, 3 example sentences, mnemonic device or memory trick, word family, common mistakes, and a mini-quiz. Group by difficulty or theme for structured learning.")],
      [p("Research Words",0),p("Build Cards",1)],
      None,["words_or_level"],
      c("Vocabulary Builder","Build your vocabulary","Help me learn these words: [word list or level]")),

    t("interview-prep","Interview Prep Coach","learning",
      "Prepare for job interviews with practice questions and tips",
      ["interview","job","prepare","question","behavioral","technical"],
      [a("Interview Researcher","researcher","Research the company and role for interview prep",["web_fetch"],"Research the company: culture, values, recent news, products, and team. Research common interview questions for the specified role. Find Glassdoor-style interview experiences if available."),
       a("Interview Coach","coach","Create a comprehensive interview prep package",["file_write"],"Create an interview prep package with: company research summary, 15 likely questions (behavioral + technical + role-specific), STAR-format answer frameworks for behavioral questions, questions to ask the interviewer, common pitfalls to avoid, salary negotiation tips, and a pre-interview checklist.")],
      [p("Research",0),p("Prep Package",1)],
      None,["company","role"],
      c("Interview Prep","Prepare for job interviews","Prepare me for an interview at [company] for [role]")),

    t("concept-mapper","Concept Map Builder","learning",
      "Create visual concept maps showing relationships between ideas",
      ["concept map","mind map","diagram","relationships","visual","organize"],
      [a("Concept Analyzer","analyst","Analyze the topic and identify key concepts and relationships",[],"Analyze the topic and break it into key concepts. Identify hierarchical relationships, cross-links, and examples for each concept. Determine the central concept and how all others connect."),
       a("Map Builder","writer","Build a structured concept map",["file_write"],"Create a concept map in text format with: central concept, main branches (5-7 major concepts), sub-branches, cross-links between concepts with labeled relationships, and examples for leaf nodes. Use indentation and arrows to show hierarchy and connections. Include a summary of key relationships.")],
      [p("Analyze Concepts",0),p("Build Map",1)],
      None,["topic"],
      c("Concept Mapper","Map relationships between ideas","Create a concept map for [topic]")),

    # ── DATA +10 ──
    t("data-cleaner","Data Cleaner","data",
      "Clean and normalize messy data with consistent formatting",
      ["clean","normalize","format","deduplicate","missing","data quality"],
      [a("Data Cleaner","analyst","Identify and fix data quality issues",["file_write"],"Analyze the data for quality issues: missing values, duplicates, inconsistent formats, outliers, invalid entries, and encoding problems. Apply cleaning rules: standardize formats, fill or flag missing values, remove duplicates, fix typos. Report all changes made with before/after examples.")],
      [p("Clean Data",0)],
      None,["data"],
      c("Data Cleaner","Clean messy data","Clean this data: [paste data]")),

    t("schema-designer","Data Schema Designer","data",
      "Design optimal data schemas for any use case",
      ["schema","model","design","normalize","entity","relationship"],
      [a("Schema Analyst","analyst","Analyze requirements and identify entities",[],"Analyze the data requirements. Identify all entities, their attributes, data types, constraints, and relationships (one-to-one, one-to-many, many-to-many). Consider query patterns and access patterns."),
       a("Schema Writer","architect","Design and document the data schema",["file_write"],"Design a normalized data schema with: entity definitions, attribute specifications (name, type, constraints), relationship diagrams (text-based ERD), indexes for common queries, sample data, and migration considerations. Provide both SQL DDL and NoSQL document structure if applicable.")],
      [p("Analyze Requirements",0),p("Design Schema",1)],
      None,["requirements"],
      c("Schema Designer","Design data schemas","Design a schema for [use case]")),

    t("dashboard-builder","Dashboard Spec Builder","data",
      "Design data dashboard layouts with KPIs and visualizations",
      ["dashboard","KPI","visualization","metrics","chart","report"],
      [a("Metrics Analyst","analyst","Identify key metrics and KPIs for the dashboard",[],"Analyze the business context and identify: primary KPIs, secondary metrics, diagnostic metrics, and leading indicators. Define calculation formulas, data sources, and update frequency for each metric."),
       a("Dashboard Designer","architect","Design the dashboard layout and visualizations",["file_write"],"Design a dashboard specification with: KPI cards with targets, chart types for each metric (with justification), layout wireframe (text-based), filter/drill-down capabilities, data refresh strategy, alert thresholds, and color coding rules. Include a data requirements document for engineering.")],
      [p("Identify Metrics",0),p("Design Dashboard",1)],
      None,["business_context"],
      c("Dashboard Builder","Design data dashboards","Design a dashboard for [business area]")),

    t("sql-query-builder","SQL Query Builder","data",
      "Build complex SQL queries from natural language descriptions",
      ["sql","query","database","select","join","aggregate"],
      [a("Query Builder","developer","Build SQL queries from natural language",["file_write"],"Translate the natural language request into SQL. Write: the query with proper formatting and comments, explanation of each clause, sample output table, performance considerations (index usage, execution plan hints), and alternative approaches. Support multiple SQL dialects (PostgreSQL, MySQL, SQLite) if requested.")],
      [p("Build Query",0)],
      None,["description","dialect"],
      c("SQL Query Builder","Build SQL from descriptions","Write a SQL query to [description]")),

    t("data-pipeline-designer","Data Pipeline Designer","data",
      "Design ETL/ELT data pipelines with error handling",
      ["pipeline","ETL","ELT","ingestion","transform","data engineering"],
      [a("Pipeline Architect","architect","Design the data pipeline architecture",[],"Design a data pipeline considering: source systems, ingestion method (batch/streaming), transformation steps, data quality checks, error handling, retry logic, monitoring, and destination. Choose appropriate tools/frameworks."),
       a("Pipeline Documenter","writer","Document the pipeline design and implementation guide",["file_write"],"Document the pipeline with: architecture diagram (text), source-to-target mapping, transformation rules, data quality checks, error handling strategy, scheduling/orchestration, monitoring and alerting, and implementation steps. Include code snippets for key components.")],
      [p("Design Pipeline",0),p("Document",1)],
      None,["source","destination","requirements"],
      c("Pipeline Designer","Design data pipelines","Design a pipeline from [source] to [destination]")),

    t("json-transformer","JSON Transformer","data",
      "Transform JSON data between different structures and formats",
      ["json","transform","convert","reshape","map","format"],
      [a("JSON Transformer","developer","Transform JSON between structures",["file_write"],"Analyze the source JSON structure and target format. Create a transformation that: maps fields correctly, handles nested objects and arrays, applies data type conversions, handles missing fields with defaults, and validates the output. Provide the transformation code/rules and sample output.")],
      [p("Transform",0)],
      None,["source_json","target_format"],
      c("JSON Transformer","Transform JSON structures","Transform this JSON to [target format]: [json]")),

    t("data-dictionary","Data Dictionary Generator","data",
      "Generate comprehensive data dictionaries from datasets",
      ["dictionary","metadata","catalog","documentation","dataset","column"],
      [a("Data Profiler","analyst","Profile the dataset and extract metadata",[],"Profile the dataset: for each column identify name, data type, description, sample values, null percentage, unique count, min/max values, distribution pattern, and potential PII flags."),
       a("Dictionary Writer","writer","Write a formatted data dictionary",["file_write"],"Create a data dictionary with: table/file overview, column-by-column documentation in a table format, data quality summary, relationships to other tables (if known), business rules and constraints, common queries, and data lineage notes.")],
      [p("Profile Data",0),p("Write Dictionary",1)],
      None,["dataset"],
      c("Data Dictionary","Generate data dictionaries","Create a data dictionary for: [dataset description]")),

    t("api-data-mapper","API Response Mapper","data",
      "Map API responses to your internal data models",
      ["api","mapping","response","model","integration","adapter"],
      [a("Mapping Analyst","analyst","Analyze API response and target model",[],"Analyze the API response structure and the target internal model. Identify field mappings, type conversions, nested object flattening, array handling, and fields that need transformation or enrichment."),
       a("Mapper Writer","developer","Write mapping code and documentation",["file_write"],"Write mapping code/configuration that transforms the API response to the target model. Include: field mapping table, transformation functions, null/default handling, validation rules, error cases, and unit tests for the mapping. Support the specified language/framework.")],
      [p("Analyze Mapping",0),p("Write Mapper",1)],
      None,["api_response","target_model"],
      c("API Mapper","Map API responses to models","Map this API response to my model: [response structure]")),

    t("regex-data-extractor","Data Extraction Builder","data",
      "Build data extraction rules for unstructured text",
      ["extract","parse","unstructured","text","pattern","scrape"],
      [a("Pattern Analyst","analyst","Analyze text patterns and design extraction rules",[],"Analyze the unstructured text samples. Identify repeating patterns for the desired data points. Design extraction rules using regex, delimiter-based parsing, or structural patterns. Handle edge cases and variations."),
       a("Extractor Builder","developer","Build extraction code and validate results",["file_write"],"Build extraction rules/code that: captures all target data points, handles format variations, provides confidence scores, falls back gracefully on unrecognized patterns, and outputs structured data (JSON/CSV). Include test cases with expected outputs.")],
      [p("Analyze Patterns",0),p("Build Extractor",1)],
      None,["sample_text","target_fields"],
      c("Data Extractor","Extract data from text","Extract [fields] from this text: [sample]")),

    t("ab-test-analyzer","A/B Test Analyzer","data",
      "Analyze A/B test results with statistical significance",
      ["ab test","experiment","significance","conversion","hypothesis","statistics"],
      [a("Test Analyst","analyst","Analyze A/B test data with statistical rigor",["file_write"],"Analyze the A/B test results. Calculate: conversion rates for each variant, absolute and relative lift, statistical significance (chi-squared or z-test), confidence interval, p-value, required sample size analysis, and effect size. Determine if the test has reached significance. Provide recommendation: ship winner, continue testing, or redesign. Include visualizations (text-based charts).")],
      [p("Analyze Test",0)],
      None,["test_data"],
      c("A/B Test Analyzer","Analyze experiment results","Analyze this A/B test: [control and variant data]")),

    # ── AUTOMATION +10 (NEW) ──
    t("email-auto-responder","Email Auto-Responder Designer","automation",
      "Design automated email response rules and templates",
      ["email","auto-reply","filter","rules","respond","automate"],
      [a("Email Analyst","analyst","Analyze email patterns and design response rules",[],"Analyze the described email patterns. Design classification rules for incoming emails by: sender type, subject keywords, urgency level, and content category. Define which emails need auto-responses vs forwarding vs flagging."),
       a("Template Writer","writer","Write response templates and automation rules",["file_write"],"Create an email automation system with: classification rules, response templates for each category, escalation criteria, out-of-office variations, follow-up sequences, and filter configuration (compatible with Gmail/Outlook rules). Include merge fields for personalization.")],
      [p("Analyze Patterns",0),p("Write Templates",1)],
      None,["email_types"],
      c("Email Auto-Responder","Design email automation","Design auto-responses for [email types]")),

    t("file-organizer","File Organization System Designer","automation",
      "Design file organization systems with naming conventions and folder structures",
      ["file","organize","folder","naming","structure","convention"],
      [a("Organization Designer","architect","Design a file organization system",["file_write"],"Design a comprehensive file organization system with: folder hierarchy (max 3-4 levels deep), naming conventions with examples, tagging/metadata strategy, archive rules, version control approach, and cleanup automation scripts. Tailor to the specific use case (personal, team, project). Include migration plan from current messy state.")],
      [p("Design System",0)],
      None,["use_case","current_state"],
      c("File Organizer","Design file organization systems","Organize my files for [use case]")),

    t("backup-scheduler","Backup Strategy Planner","automation",
      "Design comprehensive backup strategies with schedules and retention",
      ["backup","recovery","disaster","schedule","retention","restore"],
      [a("Backup Architect","architect","Design a backup strategy",[],"Design a backup strategy considering: data types, RPO/RTO requirements, storage costs, and compliance needs. Plan full, incremental, and differential backups with appropriate schedules."),
       a("Strategy Writer","writer","Document the backup strategy",["file_write"],"Document the backup strategy with: backup types and schedules, retention policies, storage locations (local, cloud, offsite), estimated storage requirements, restoration procedures, testing schedule, monitoring and alerting, and disaster recovery runbook. Include cost estimates.")],
      [p("Design Strategy",0),p("Document",1)],
      None,["data_types","requirements"],
      c("Backup Planner","Design backup strategies","Plan a backup strategy for [data types]")),

    t("cron-job-builder","Cron Job Builder","automation",
      "Build and explain cron job schedules for task automation",
      ["cron","schedule","automate","recurring","timer","task"],
      [a("Cron Builder","developer","Build cron expressions and automation scripts",["file_write"],"Build cron expressions for the requested schedules. For each: provide the cron expression, plain-English explanation, next 5 execution times, timezone considerations, and a wrapper script with logging, error handling, and notification on failure. Include common cron gotchas and testing tips.")],
      [p("Build Cron Jobs",0)],
      None,["tasks_and_schedules"],
      c("Cron Job Builder","Build scheduled tasks","Create cron jobs for: [task descriptions and schedules]")),

    t("workflow-automator","Workflow Automation Designer","automation",
      "Design multi-step automated workflows with triggers and actions",
      ["workflow","automation","trigger","action","zapier","n8n"],
      [a("Workflow Analyst","analyst","Analyze the process and identify automation opportunities",[],"Analyze the described workflow. Identify: manual steps that can be automated, trigger events, required integrations, data flow between steps, conditional logic, and error handling needs. Calculate time savings."),
       a("Workflow Designer","architect","Design the automated workflow",["file_write"],"Design the automated workflow with: trigger definition, step-by-step actions, conditional branches, data transformations, error handling, retry logic, and notification points. Provide implementation instructions for the specified platform (Zapier, n8n, Make, or custom). Include a workflow diagram in text format.")],
      [p("Analyze Process",0),p("Design Workflow",1)],
      None,["process_description","platform"],
      c("Workflow Automator","Design automated workflows","Automate this workflow: [process description]")),

    t("notification-system","Notification System Designer","automation",
      "Design notification and alerting systems with routing rules",
      ["notification","alert","webhook","slack","monitoring","trigger"],
      [a("Alert Designer","architect","Design notification routing and escalation rules",["file_write"],"Design a notification system with: event categories and severity levels, routing rules (who gets what), channel preferences (email, Slack, SMS, webhook), escalation policies, quiet hours and override rules, aggregation/deduplication logic, and template for each notification type. Include rate limiting and digest options.")],
      [p("Design System",0)],
      None,["event_types","channels"],
      c("Notification System","Design alerting systems","Design notifications for [event types]")),

    t("data-sync-planner","Data Sync Planner","automation",
      "Plan data synchronization between systems with conflict resolution",
      ["sync","synchronize","integration","bidirectional","conflict","data"],
      [a("Sync Analyst","analyst","Analyze sync requirements and identify challenges",[],"Analyze the systems to be synced. Identify: entities to sync, field mappings, sync direction (one-way/bidirectional), conflict scenarios, data volume estimates, and frequency requirements. Assess consistency requirements."),
       a("Sync Planner","architect","Design the synchronization strategy",["file_write"],"Design a sync strategy with: entity mapping table, sync frequency and method (push/pull/webhook), conflict resolution rules (last-write-wins, merge, manual), error handling and retry logic, data validation, audit logging, and monitoring. Include sequence diagrams for key flows.")],
      [p("Analyze Requirements",0),p("Plan Sync",1)],
      None,["system_a","system_b"],
      c("Data Sync Planner","Plan data synchronization","Plan sync between [system A] and [system B]")),

    t("report-automator","Report Automation Designer","automation",
      "Design automated report generation and distribution systems",
      ["report","automate","schedule","distribute","generate","recurring"],
      [a("Report Analyst","analyst","Analyze reporting requirements and data sources",[],"Analyze the reporting needs: what metrics to include, data sources, calculation logic, formatting requirements, distribution list, and delivery schedule. Identify which parts can be fully automated vs need manual input."),
       a("Automation Designer","architect","Design the report automation system",["file_write"],"Design a report automation system with: data collection queries, calculation and transformation logic, report template with sections, chart/visualization specifications, generation schedule, distribution rules (email, Slack, dashboard), and exception handling. Include sample report output.")],
      [p("Analyze Requirements",0),p("Design Automation",1)],
      None,["report_type","frequency"],
      c("Report Automator","Automate report generation","Automate this report: [report description]")),

    t("api-integration-planner","API Integration Planner","automation",
      "Plan API integrations between services with authentication and error handling",
      ["api","integration","connect","webhook","oauth","service"],
      [a("Integration Analyst","analyst","Analyze APIs and plan the integration",["web_fetch"],"Research both APIs: authentication methods, rate limits, endpoints needed, data formats, webhook capabilities, and SDKs available. Identify the optimal integration approach."),
       a("Integration Planner","architect","Create a detailed integration plan",["file_write"],"Create an integration plan with: authentication setup (API keys, OAuth flow), endpoint mapping, request/response examples, rate limit handling, retry and error handling strategy, data transformation layer, testing approach, and monitoring. Include code snippets for key operations.")],
      [p("Research APIs",0),p("Plan Integration",1)],
      None,["service_a","service_b"],
      c("Integration Planner","Plan API integrations","Plan integration between [service A] and [service B]")),

    t("task-scheduler-designer","Task Scheduler Designer","automation",
      "Design task scheduling systems with dependencies and priorities",
      ["scheduler","task","queue","priority","dependency","job"],
      [a("Scheduler Analyst","analyst","Analyze tasks and design scheduling logic",[],"Analyze the tasks to be scheduled: dependencies between tasks, priority levels, resource constraints, SLA requirements, and failure recovery needs. Design an optimal execution order and parallelization strategy."),
       a("Scheduler Designer","architect","Design the task scheduling system",["file_write"],"Design a task scheduling system with: task definitions, dependency graph (text DAG), priority rules, resource allocation, concurrency limits, retry policies, dead letter handling, and monitoring dashboard specs. Include a task manifest format and example configurations.")],
      [p("Analyze Tasks",0),p("Design Scheduler",1)],
      None,["tasks","constraints"],
      c("Task Scheduler","Design task scheduling","Design a scheduler for: [task descriptions]")),

    # ── BUSINESS +10 (NEW) ──
    t("swot-analyzer","SWOT Analyzer","business",
      "Perform comprehensive SWOT analysis for businesses or projects",
      ["SWOT","strength","weakness","opportunity","threat","strategy"],
      [a("SWOT Researcher","researcher","Research internal and external factors",["web_fetch"],"Research the business/project and its market. Identify: internal strengths and weaknesses, market opportunities, competitive threats, industry trends, and regulatory factors. Gather data to support each point."),
       a("SWOT Analyst","analyst","Create a detailed SWOT analysis with strategies",["file_write"],"Create a comprehensive SWOT analysis with: categorized findings (each with supporting evidence), SWOT matrix visualization (text), SO strategies (use strengths to capture opportunities), WO strategies (overcome weaknesses via opportunities), ST strategies (use strengths to mitigate threats), WT strategies (minimize weaknesses and avoid threats), and prioritized action items.")],
      [p("Research",0),p("Analyze",1)],
      None,["business_or_project"],
      c("SWOT Analysis","Perform SWOT analysis","Do a SWOT analysis for [business/project]")),

    t("pitch-deck","Pitch Deck Builder","business",
      "Create compelling pitch deck outlines for investors or stakeholders",
      ["pitch","deck","investor","startup","fundraise","presentation"],
      [a("Pitch Researcher","researcher","Research the market and competitive landscape",["web_fetch"],"Research the market for the pitch: market size (TAM/SAM/SOM), growth rate, key competitors, industry trends, and comparable funding rounds. Find data points that strengthen the pitch narrative."),
       a("Deck Writer","writer","Write the pitch deck content slide by slide",["file_write"],"Write pitch deck content for 12-15 slides: title, problem, solution, market opportunity (with TAM/SAM/SOM), business model, traction/metrics, competitive advantages, competitive landscape, go-to-market strategy, team, financial projections, ask/use of funds, and closing. Each slide: headline, 3-5 bullets, speaker notes, and visual suggestion.")],
      [p("Research Market",0),p("Write Deck",1)],
      None,["company","product"],
      c("Pitch Deck","Build investor pitch decks","Create a pitch deck for [company/product]")),

    t("customer-persona","Customer Persona Builder","business",
      "Create detailed customer personas from market research",
      ["persona","customer","avatar","segment","target","audience"],
      [a("Market Researcher","researcher","Research the target market and customer segments",["web_fetch"],"Research the target market. Find: demographics, psychographics, behaviors, pain points, buying patterns, media consumption, and decision-making factors. Look for survey data and market research reports."),
       a("Persona Builder","writer","Create detailed customer personas",["file_write"],"Create 3-4 detailed customer personas with: name and photo description, demographics (age, income, education, location), psychographics (values, goals, fears), day-in-the-life narrative, pain points, buying triggers, objections, preferred channels, and a quote that captures their mindset. Include a persona comparison matrix.")],
      [p("Research Market",0),p("Build Personas",1)],
      None,["product","market"],
      c("Customer Personas","Build customer personas","Create personas for [product] in [market]")),

    t("business-plan","Business Plan Writer","business",
      "Write comprehensive business plans for startups or new ventures",
      ["business plan","startup","venture","strategy","executive summary","market"],
      [a("Business Researcher","researcher","Research the market and industry for the business plan",["web_fetch"],"Research the industry, target market, competitors, regulatory environment, and market trends. Find market size data, growth projections, and comparable business models."),
       a("Plan Writer","writer","Write a comprehensive business plan",["file_write"],"Write a business plan with: executive summary, company description, market analysis, organization structure, product/service line, marketing and sales strategy, financial projections (3-year P&L, cash flow), funding requirements, and appendices. Follow SBA-recommended format. Include realistic assumptions.")],
      [p("Research",0),p("Write Plan",1)],
      None,["business_idea"],
      c("Business Plan","Write business plans","Write a business plan for [business idea]")),

    t("competitive-analysis","Competitive Analysis Framework","business",
      "Build detailed competitive analysis frameworks",
      ["competitive","analysis","benchmark","comparison","market","positioning"],
      [a("Competitor Researcher","researcher","Research competitors in depth",["web_fetch"],"Research each competitor: products, pricing, positioning, market share, strengths, weaknesses, recent moves, customer reviews, and technology stack. Find company size, funding, and key personnel."),
       a("Analysis Writer","analyst","Create a competitive analysis framework",["file_write"],"Create a competitive analysis with: competitor profiles, feature comparison matrix, pricing comparison, positioning map (text-based), competitive advantages/disadvantages, market share estimates, threat assessment, and strategic recommendations. Include a battle card for sales team use.")],
      [p("Research Competitors",0),p("Analyze",1)],
      None,["company","competitors"],
      c("Competitive Analysis","Analyze your competition","Analyze competitors for [company]")),

    t("pricing-strategy","Pricing Strategy Advisor","business",
      "Develop pricing strategies based on market and cost analysis",
      ["pricing","strategy","revenue","margin","value","monetization"],
      [a("Pricing Researcher","researcher","Research market pricing and customer willingness to pay",["web_fetch"],"Research: competitor pricing models, customer price sensitivity, value metrics, industry benchmarks, and pricing psychology. Find comparable products and their pricing tiers."),
       a("Pricing Advisor","advisor","Develop pricing strategy recommendations",["file_write"],"Develop a pricing strategy with: cost analysis, value-based pricing model, competitive pricing comparison, recommended price points, tiering structure, discount policies, pricing psychology tactics, projected revenue at different price points, and A/B testing plan. Include sensitivity analysis.")],
      [p("Research Pricing",0),p("Develop Strategy",1)],
      None,["product","costs"],
      c("Pricing Strategy","Develop pricing strategies","Develop pricing for [product]")),

    t("market-entry","Market Entry Strategy","business",
      "Plan market entry strategies for new products or geographies",
      ["market entry","launch","go-to-market","expansion","strategy","GTM"],
      [a("Market Researcher","researcher","Research the target market for entry planning",["web_fetch"],"Research the target market: size, growth, customer needs, competitive landscape, regulatory requirements, distribution channels, cultural considerations, and barriers to entry. Identify early adopter segments."),
       a("Strategy Writer","strategist","Write a market entry strategy",["file_write"],"Write a market entry strategy with: market assessment, entry mode recommendation (direct, partnership, acquisition), target segment prioritization, value proposition for the market, go-to-market playbook (channels, messaging, timeline), resource requirements, risk mitigation, and success metrics with 90-day, 6-month, and 1-year milestones.")],
      [p("Research Market",0),p("Write Strategy",1)],
      None,["product","target_market"],
      c("Market Entry","Plan market entry strategies","Plan entry into [market] with [product]")),

    t("kpi-dashboard","KPI Framework Designer","business",
      "Design KPI frameworks aligned with business objectives",
      ["KPI","metric","OKR","measurement","performance","indicator"],
      [a("KPI Designer","analyst","Design a KPI framework aligned with business goals",["file_write"],"Design a KPI framework with: strategic objectives mapped to KPIs, KPI definitions (name, formula, data source, frequency, owner), target setting methodology, leading vs lagging indicator balance, KPI hierarchy (company -> department -> team), dashboard mockup (text), review cadence, and action triggers for when KPIs miss targets. Limit to 5-7 KPIs per level to avoid metric overload.")],
      [p("Design Framework",0)],
      None,["business_objectives"],
      c("KPI Framework","Design KPI frameworks","Design KPIs for [business objectives]")),

    t("meeting-roi","Meeting ROI Calculator","business",
      "Calculate the cost and ROI of meetings to optimize meeting culture",
      ["meeting","cost","ROI","productivity","time","culture"],
      [a("Meeting Analyst","analyst","Analyze meeting costs and effectiveness",[],"Calculate the cost of each meeting based on: attendee salaries (estimates by role), meeting duration, frequency, and preparation time. Assess each meeting's purpose, outcomes, and whether they could be replaced by async communication."),
       a("Meeting Optimizer","advisor","Recommend meeting optimizations",["file_write"],"Create a meeting audit report with: total meeting hours and costs per week, cost per meeting type, meetings ranked by ROI (outcomes vs cost), specific recommendations (cancel, shorten, reduce attendees, make async), estimated time and cost savings, and a meeting policy recommendation.")],
      [p("Analyze Meetings",0),p("Optimize",1)],
      None,["meeting_list"],
      c("Meeting ROI","Calculate meeting costs and ROI","Audit these meetings: [meeting list with attendees and frequency]")),

    t("brand-voice","Brand Voice Guide Builder","business",
      "Create comprehensive brand voice and tone guidelines",
      ["brand","voice","tone","style","messaging","identity"],
      [a("Brand Researcher","researcher","Research the brand and its audience",["web_fetch"],"Research the brand: existing content, competitors' voices, target audience preferences, industry norms, and brand values. Analyze current content samples for existing voice patterns."),
       a("Guide Writer","writer","Create a brand voice guide",["file_write"],"Create a brand voice guide with: brand personality traits (3-5 adjectives with definitions), voice characteristics (with do/don't examples), tone variations by context (social, support, marketing, formal), vocabulary lists (preferred and avoided words), writing style rules, sample content in the brand voice, and a quick-reference cheat sheet for content creators.")],
      [p("Research Brand",0),p("Write Guide",1)],
      None,["brand_name","values"],
      c("Brand Voice","Create brand voice guides","Create a brand voice guide for [brand]")),
]


def generate():
    os.chdir(BASE)

    # Verify no ID collisions
    new_ids = [t["id"] for t in NEW_TEMPLATES]
    collisions = set(new_ids) & set(EXISTING_IDS)
    if collisions:
        print(f"ERROR: ID collisions with existing templates: {collisions}")
        return

    dupes = [x for x in new_ids if new_ids.count(x) > 1]
    if dupes:
        print(f"ERROR: Duplicate new IDs: {set(dupes)}")
        return

    # Create new category directories
    for cat in ["automation", "business"]:
        os.makedirs(cat, exist_ok=True)

    # Write each new template
    for tmpl in NEW_TEMPLATES:
        tmpl["schema_version"] = 1
        tmpl["author"] = "agentfactory"
        if "tags" not in tmpl:
            tmpl["tags"] = []

        cat = tmpl["category"]
        tid = tmpl["id"]
        folder = os.path.join(BASE, cat, tid)
        os.makedirs(folder, exist_ok=True)

        with open(os.path.join(folder, "template.json"), "w") as f:
            json.dump(tmpl, f, indent=2)

        # Generate README
        agents_list = "\n".join(
            f"{i+1}. **{a['name']}** ({a['role']}): {a['purpose']}"
            for i, a in enumerate(tmpl["agents"])
        )
        pipeline_flow = " -> ".join(s["label"] for s in tmpl["pipeline_shape"])
        schedule = tmpl.get("default_schedule")
        schedule_line = f"\n**Schedule:** `{schedule}`\n" if schedule else ""

        readme = f"""# {tmpl["name"]}

{tmpl["description"]}

## Pipeline

{pipeline_flow}

## Agents

{agents_list}
{schedule_line}
## Usage

Use this template from the Agentfactory Home tab or install it from the Marketplace.
"""
        with open(os.path.join(folder, "README.md"), "w") as f:
            f.write(readme)

    print(f"Created {len(NEW_TEMPLATES)} new templates")

    # Now rebuild index.json with ALL templates (old + new)
    all_templates = []

    # Scan all category dirs for template.json files
    categories_seen = set()
    for entry in sorted(os.listdir(BASE)):
        cat_path = os.path.join(BASE, entry)
        if not os.path.isdir(cat_path) or entry.startswith(".") or entry.startswith("_"):
            continue
        # Skip non-category dirs
        if entry in ["node_modules", "__pycache__"]:
            continue

        for tmpl_dir in sorted(os.listdir(cat_path)):
            tmpl_json = os.path.join(cat_path, tmpl_dir, "template.json")
            if os.path.isfile(tmpl_json):
                with open(tmpl_json) as f:
                    data = json.load(f)
                categories_seen.add(data.get("category", entry))
                all_templates.append({
                    "id": data["id"],
                    "name": data["name"],
                    "description": data["description"],
                    "author": data.get("author", "agentfactory"),
                    "category": data.get("category", entry),
                    "tags": data.get("tags", []),
                    "agent_count": len(data.get("agents", [])),
                    "download_url": f"{data.get('category', entry)}/{data['id']}/template.json",
                    "readme_url": f"{data.get('category', entry)}/{data['id']}/README.md",
                    "featured": data["id"] in ["deep-research", "code-review", "story-writer"],
                    "rating_avg": 0.0,
                    "rating_count": 0,
                    "discussion_url": ""
                })

    featured_ids = ["deep-research", "code-review", "story-writer"]

    index = {
        "version": 1,
        "updated_at": "2026-03-01T00:00:00Z",
        "repo_url": "https://github.com/neo3738-ai/agentfactory-templates",
        "featured": featured_ids,
        "categories": sorted(list(categories_seen)),
        "total": len(all_templates),
        "templates": all_templates
    }

    with open(os.path.join(BASE, "index.json"), "w") as f:
        json.dump(index, f, indent=2)

    print(f"Updated index.json: {len(all_templates)} total templates across {len(categories_seen)} categories")


if __name__ == "__main__":
    generate()
