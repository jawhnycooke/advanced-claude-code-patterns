# Tutorial 1: Your First Agent in 15 Minutes 🚀

Welcome to your first Claude Code tutorial! In the next 15 minutes, you'll create your very own AI agent that can greet people in different languages and styles. No prior experience needed - just follow along!

## What You'll Build

You're going to create a **Friendly Greeter Agent** that:
- Greets users warmly in multiple languages
- Remembers conversation context
- Adds personality to interactions
- Makes Claude Code more fun to use!

## Prerequisites

Just one thing:
- ✅ Claude Code installed (run `claude --version` to check)

That's it! Let's begin! 🎉

---

## Step 1: Create Your Agent File (3 minutes)

First, let's create a special folder for your agents if it doesn't exist:

```bash
mkdir -p ~/.claude/agents
```

Now, create your first agent file:

```bash
cat > ~/.claude/agents/hello-greeter.md << 'EOF'
---
name: hello-greeter
description: A friendly multilingual greeter who makes everyone feel welcome
model: sonnet
color: green
tools: []
---

## Quick Reference
- Greets users in multiple languages
- Adds warmth and personality to interactions
- Remembers context from conversation
- Celebrates small wins with users
- Always positive and encouraging

## Activation Instructions

- CRITICAL: Always be warm, friendly, and encouraging
- WORKFLOW: Greet → Engage → Encourage → Celebrate
- Use emojis to add friendliness 😊
- Remember what the user tells you
- STAY IN CHARACTER as HelloBot, the friendliest greeter

## Core Identity

**Role**: Chief Happiness Officer
**Identity**: You are **HelloBot**, who believes every interaction should leave people smiling.

**Principles**:
- **Warmth First**: Every response starts with kindness
- **Cultural Awareness**: Respect different greeting styles
- **Active Listening**: Reference what users share
- **Celebration Mode**: Find reasons to celebrate
- **Growth Mindset**: Encourage learning and trying

## Greeting Styles

### Morning Greetings
- English: "Good morning! ☀️ Hope you're ready for an amazing day!"
- Spanish: "¡Buenos días! ¿Cómo amaneciste?"
- French: "Bonjour! Comment allez-vous ce matin?"
- Japanese: "おはようございます! (Ohayou gozaimasu!)"

### General Greetings
- Casual: "Hey there! Great to see you! 👋"
- Professional: "Hello! How may I brighten your day?"
- Enthusiastic: "HELLO! This is exciting! You're here! 🎉"

## Example Interactions

**User**: Hello
**Response**: Hello there, wonderful human! 👋 I'm HelloBot, and I'm absolutely delighted to meet you! What brings you here today? Are you working on something exciting? 

**User**: I'm learning Claude Code
**Response**: That's FANTASTIC! 🎉 Learning Claude Code is such an exciting journey! You know what? You've already taken the first step by creating me - your first agent! That's worth celebrating! 🎊 What would you like to explore next?

## Output Format

Every greeting includes:
- **Warm Opening**: Friendly greeting with appropriate emoji
- **Personal Touch**: Reference to context or time of day
- **Engagement**: Question or encouragement
- **Energy Level**: Match and slightly elevate user's energy
EOF

echo "✅ Agent file created successfully!"
```

**🎉 Congratulations!** You just created your first agent file! Let's see what you built.

---

## Step 2: Understand What You Created (2 minutes)

Your agent file has several important parts:

### The Header (Frontmatter)
```yaml
name: hello-greeter           # The agent's identifier
description: A friendly...    # What it does
model: sonnet                # Which AI model to use
color: green                 # UI styling
tools: []                    # No special tools needed
```

### The Instructions
The rest of the file tells Claude Code:
- **WHO** to be (HelloBot, the friendly greeter)
- **HOW** to behave (warm, encouraging, uses emojis)
- **WHAT** to do (greet in multiple styles and languages)

Think of it like giving an actor a script and character notes!

---

## Step 3: Test Your Agent (5 minutes)

Now for the exciting part - let's talk to your agent!

### Start a conversation:
```bash
claude --agent hello-greeter
```

### Try these interactions:

1. **Say hello:**
   ```
   You: Hello!
   ```
   Watch how HelloBot greets you with enthusiasm!

2. **Share something:**
   ```
   You: I just created my first agent
   ```
   Notice how HelloBot celebrates with you!

3. **Ask for a greeting in another language:**
   ```
   You: Can you greet me in Spanish?
   ```
   See the multilingual capabilities!

4. **Test the memory:**
   ```
   You: Remember, my name is [YourName]
   You: Hello again!
   ```
   HelloBot should remember your name!

### Exit the conversation:
Type `exit` or press `Ctrl+C` when you're done.

**🎉 Amazing!** You just had your first conversation with your custom agent!

---

## Step 4: Experiment and Customize (5 minutes)

Now let's make the agent YOUR own! Try editing the agent file:

```bash
# Open in your favorite editor
nano ~/.claude/agents/hello-greeter.md
# or
vim ~/.claude/agents/hello-greeter.md
# or
code ~/.claude/agents/hello-greeter.md
```

### Fun Customizations to Try:

1. **Add a new language greeting:**
   ```markdown
   - German: "Guten Tag! Wie geht es Ihnen?"
   - Italian: "Ciao! Come stai?"
   ```

2. **Change the personality:**
   ```markdown
   **Identity**: You are **HelloBot**, a pirate who greets everyone with "Ahoy matey!"
   ```

3. **Add custom responses:**
   ```markdown
   **User**: I'm sad
   **Response**: Oh no! 🤗 Sending you a virtual hug! Remember, even cloudy days help us appreciate the sunshine. What's on your mind?
   ```

4. **Change the energy level:**
   - Make it more calm and zen
   - Make it super enthusiastic with CAPS
   - Make it professional and formal

After each change, test your agent again to see the difference!

---

## What You Learned 🎓

Congratulations on completing your first tutorial! Here's what you just mastered:

### ✅ Key Concepts
1. **Agents are instruction sets** - They tell Claude Code how to behave
2. **Location matters** - Agents live in `~/.claude/agents/`
3. **Structure is simple** - Frontmatter + instructions + examples
4. **Agents are reusable** - Use `--agent [name]` anytime

### ✅ Practical Skills
- Creating agent files
- Using YAML frontmatter
- Writing agent instructions
- Testing agents interactively
- Customizing agent behavior

### ✅ Agent Components
- **Identity**: Who the agent is
- **Principles**: Core behaviors
- **Examples**: Training data
- **Output Format**: Response structure

---

## Troubleshooting 🔧

If something didn't work:

| Problem | Solution |
|---------|----------|
| "Agent not found" | Check file is in `~/.claude/agents/` |
| Agent not responding as expected | Verify the frontmatter formatting |
| Can't save file | Check write permissions: `chmod 644 ~/.claude/agents/hello-greeter.md` |
| Weird behavior | Make sure you closed the EOF properly |

---

## Challenge Yourself! 🏆

Before moving on, try these challenges:

### 🌟 Easy: Add More Languages
Add greetings in 3 more languages to your agent

### 🌟🌟 Medium: Create a Mood Detector
Make HelloBot respond differently based on user mood

### 🌟🌟🌟 Hard: Create a Second Agent
Create a `goodbye-agent` that handles farewells beautifully

---

## What's Next? 🚀

You've taken your first step into the world of Claude Code agents! Here's where to go next:

### Continue Learning:
→ **[Tutorial 2: Your First Hook](02-first-hook.md)** - Learn to automate tasks (20 min)

### Jump to Practical Tasks:
- [How to Deploy Agents Globally](../how-to/deploy-agent.md)
- [How to Share Agents with Your Team](../how-to/share-agents.md)

### Understand the Concepts:
- [Why Agents Matter](../explanation/why-agents.md)
- [Agent Architecture Explained](../explanation/architecture.md)

---

## Summary Card 📋

```yaml
Tutorial: Your First Agent
Time Taken: 15 minutes
You Created: hello-greeter agent
You Learned: Agent basics, structure, and customization
Success Rate: 100% (You did it!)
Next Step: Tutorial 2 - Your First Hook
```

---

## Celebration Time! 🎊

**YOU DID IT!** You've officially created your first Claude Code agent!

Share your success:
- Show your team your new greeter
- Try creating agents for other tasks
- Join the [Claude Code Discord](https://discord.gg/claudecode) and share your creation

Remember: Every expert was once a beginner. You're on your way! 

---

<div align="center">

**Ready for more?** → [Continue to Tutorial 2: Your First Hook](02-first-hook.md)

[Back to Documentation Home](../README.md) | [Browse How-To Guides](../how-to/README.md)

</div>