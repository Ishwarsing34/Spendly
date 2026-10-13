claude code 



1. claude -r  => to check the past conversation
2. /resume => in between to get into another session
3. for every feature create a new session
4. when u start a session rename it with the feature u r developing
5. rename [project-name]
6. commit frequently in a session
7. /btw => asking questions in between which is not link to your feature/session
8. export <file-name> = when u r adding a big change to       code then export u r past conversation
9. /logout and /login
10. /model => to switch between models
11. /usage => to track usage
12. /extra-usage ==> mid way recharge
13. /stats => gives statistics on the usage base
14. /insights => detailed report based on your usage
15. /config => changing the claude code config
16. /permissions => allows permission
17. /theme
18./voice 
19. /rewind => to go back in code and conversation




=========models====================

* Opus - most powerful but most expensive. Used for
complex programming tasks.

* Sonnet - the default for most users. Best balance of speed,
quality, and token cost. Good for everyday coding tasks.

* Haiku - fastest and cheapest. Use for simple, repetitive, or
exploratory tasks where you don't need deep reasoning.



==> A common power-user pattern is to use Opus for the
planning phase - where you're thinking through
architecture, writing specs, making decisions - then switch
to Sonnet for the implementation phase where the thinking
is done and you just need reliable code generation.





==========CONTEXT WINDOW MANAGEMENT========================


A context window is the amount of information (in tokens)
that a model like Claude Code can see and remember at
one time while generating a response. 
Think of it as the model's working memory.


sonnet context window ===> 200k tokens reality 150k bcz previously few tokens are occupied

each session creates a new context window

tokens are consumed by both ur msgs amd claude's replies

claude replies consume roughly 6x more tokens than your messages

every request sends the entire conversation history from scratch



subagents get their own isolated context window completely separate from main session

subagents return only a summary to the main context not their full working history







========= What is Claude.md file? =======================


1. why we need claude.md ?

=> LLMs don't have memory

Claude Code can't remember things from prev sessions

Need to repeat instructions across sessions

Repeating instructions is cumbersome & error prone

Leads to inconsistent code generation



===Solution===>claude.md

The claude.md file is a special project-level instruction file
used by Claude Code to guide how it behaves while
working on your codebase.

Think of it as a persistent system prompt for your project.


Instead of repeatedly telling Claude:

how your project is structured
coding conventions
how to run/build/test
what tools to use

we put all of that into claude.md, and Claude
automatically uses it as context every time.


======how to create====

1.manually
2.using /init




=====.claude folder====

The .claude folder is Claude Code's local configuration
directory that controls how Claude behaves - either for a
specific project or across all projects on your machine.

It stores all config related info about skills, custom slash
commands, sub-agents etc.


1.Project-level .claude/ - scoped to one project, committed
to the repo, shared with the team.


2.Global/User-level ~/.claude/ - scoped to your machine,
applies to every project, personal to you.


===TYPES of CLAUDE.md=====

Project Root -. /CLAUDE.md

Inside .claude folder - ./.claude/CLAUDE.md


Local (Personal, Gitignored) - ./CLAUDE.local.md

Create CLAUDE.local.md in your project root. Claude
reads it alongside the main CLAUDE.md, and it's
automatically gitignored so your personal tweaks never
land in the repo.



Global -~ /.claude/CLAUDE.md

Your personal preferences that apply across all projects.
Things like your coding style defaults, preferred tools, or
general working style go here. This user-level file is
available across all your projects.


Subdirectory -. /some/folder/CLAUDE.md

Starting in the current working directory, Claude Code
recurses up to / and reads any CLAUDE.md or
CLAUDE.local.md files it finds.

This is especially convenient in large repositories.


=======GOOD PRACTICES====


Start with /init, then prune aggressively

Commit it to git

Only put universally applicable things in it

Use emphasis sparingly for critical rules
if everything is IMPORTANT, nothing is.

Keep it short - under 200 lines

as instruction count increases, instruction-following quality decreases
uniformly

Rule - Would removing this cause Claude to make mistakes?" If not, cut
it.

===what if your claude.md file is greater than 200 line===
=>Split into .claude/rules/ files
=>Use @ imports to reference external docs
=>Use subdirectory CLAUDE.md files
=>Treat it like a living document. Build it organically, not
upfront
=>Correct once, then codify
=>Audit periodically - instructions drift  (review it periodically)




======AUTO MEMORY=======

Auto memory is a persistent directory where Claude
records learnings, patterns, and insights as it works.

When Claude discovers something about your project
("oh, this application uses INR instead of USD"), it saves
that to auto-memory. Next session, it already knows. No
more repeating yourself.


It lives in ~/.claude/projects/<project>/memory/:


Only the first 200 lines of MEMORY.md load
automatically.

To review or edit what Claude has saved, run /memory
during any session.










==========SPEC DRIVEN DEVELOPMENT IN CLAUDE CODE===================

Spec driven development (SDD) is a software
development approach where a detailed specification
document is written before any code is written.

The spec acts as the single source of truth for what the
system should do, and all development flows from it.



===> FORMAT OF SPEC DOCUMENT


Problem Statement

Functional Requirements

API contracts (inputs, outputs, data shapes)

Constraints

Edge cases and error handling

Acceptance criteria


spec => review => design => review => tasks => build => validate



plan mode =>

1. OPUS FOR COMPLEX PLANNING
2. EXTENDED THINKING => /CONFIG => THINKING MODE => ON
3. EFFORT LEVEL  => LOW MEDIUM HIGH MAX  =? /effort
4. ULTRAPLAN => TO COMPLEX PLANS => /Ultraplan




=====How to make our custom slash commands=======

TWO TYPES

1.Project-scoped - stored in .claude/commands/,
available only within that project

2.er-scoped - stored in ~/.claude/commands/,
available across all your projects


Examples:

/review - runs a code review checklist on the current file

/commit - generates a git commit message based on staged
changes

/test - runs the test suite and analyzes any failures

/security-scan - scans the codebase for common vulnerabilities
like SQL injection or exposed credentials




============CLAUDE SKILLS=======================

Skills are reusable, file-based resources
that provide Claude with domain-specific
expertise such as workflows, context, and
best practices that transform
general-purpose agents into specialists.


Progressive Disclosure => process of loading skills in context 

Core idea - don't present information until the moment
it's needed.

Level 1: The description (always visible)

Level 2: The SKILL.md body (loaded on demand)

Level 3: Referenced resources (loaded if needed)



========TYPES OF SKILLS==============


Based on scope:

1. Personal Skills - ~/.claude/skills/
Personal skills are available across all your projects.

2. Project Skills - .claude/skills/
Project skills are available across your current project.
Shared with your teammates


==========ways to create skills======

1.create manually =>not recommended for beginners
2. use claude chatbot => skill-creator
3. Install skills from community sources



=========steps to create a skill===================

Identify the need

Create dir and Write the skill.md file

Add supporting files(if needed)

Test the skills

Iterate and refine




==========SUB-AGENTS================


==TYPES OF SUB - AGENTS===

1.Built in subagents => 1. explore subagent 2. plan subagent 3. general - purpose subagent
2. custom subagents =? 1. use level  2. project level

===how subagents get triggered==

1.implicit
2.explicit 


use /Agents to create agents







=====================CLAUDE + MCP==================

/mcp => to check the list of mcp servers u have

===RECOMMENDED MCP SERVERS=====

1.CONTEXT7 => Context7 is an MCP server that pulls  live, up-to-date
documentation for any library or framework directly
into Claude's context while you're coding.

2.JIRA  => Jira is a project management tool made by Atlassian,
widely used by software development teams to plan,
track, and manage work - from bug fixes to full feature
development.

3.NOTION => Notion is an all-in-one workspace tool used by teams
and individuals to write docs, manage knowledge, plan
projects, and collaborate - all in one place.

Read the product requirements doc for the Analytics module in
Notion and implement the feature in my Flask app

Read the API design document in Notion and scaffold all
the endpoints in app.py

4.SLACK => Slack is a business communication platform used by
teams to send messages, share files, and collaborate -
organized into channels, direct messages, and threads.

Push this fix to GitHub, open a PR, and post the PR link in
#code-reviews with a summary of what was changed


5.AWS => AWS (Amazon Web Services) is the world's largest cloud
platform offering 200+ services - from servers and
databases to AI and networking

Deploy the latest build of Spendly to the EC2 instance and verify
it's running

Check CloudWatch logs for the Spendly app from the last 2 hours and find what's causing the 500 errors

6. DOCKER => Docker is a platform that packages your application and
all its dependencies into a container - a lightweight,
portable, self-contained unit that runs the same way on
any machine.

Read my Spendly Flask app and generate an optimized
Dockerfile for it

My Docker image is 2GB, analyze the Dockerfile and reduce
the image size
 

NOTE :- use MCP servers which are essentials otherwise it will ended up taking extra space in your context



=============HOOKS===========



Hooks are custom scripts written by the programmer that the harness
automatically executes at specific events during a session's lifecycle.


USE-CASES

1. Auto-formatting & Linting
2. Blocking dangerous shell commands
3. Protecting sensitive files
4. Notification
5. Telemetry
6. Generating summary


HOW HOOKS WORK? created in .claude/settings.json

1. You ask Claude to "clean up the Spendly project"
2. Claude enters the agent loop and decides:"Bash: rm spendly.db "
3. The harness sees a Bash tool call and checks - is there a PreToolUse hook with a matcher
that matches "Bash"? Yes
4. The harness runs your script, piping in JSON that contains the command rm spendly.db
5. Your script reads the JSON, sees rm targeting spendly.db , prints "Cannot delete the
database file" to stderr, and exits with code 2
6. The harness reads exit code 2- block. It does not run the command
7. The harness sends the error message "Cannot delete the database file" back to the model
8. The model reads the error, understands, and moves on to something else
9. The agent loop continues. Your database is safe




===========PLUGINS================


