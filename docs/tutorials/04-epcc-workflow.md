# Tutorial 4: Master the EPCC Workflow
Learn to use the Explore-Plan-Code-Commit methodology for systematic development.

## What You'll Learn
By the end of this tutorial, you'll understand how to use the EPCC (Explore-Plan-Code-Commit) workflow to develop features systematically with Claude Code. You'll implement a complete feature from exploration to deployment.

## What You'll Build
We'll add a user authentication feature to a sample project using the full EPCC workflow, creating documentation at each phase and learning the command patterns.

## Prerequisites
- Completed [Tutorial 1: Your First Agent](01-first-agent.md)
- Completed [Tutorial 2: Your First Hook](02-first-hook.md)
- Completed [Tutorial 3: Your First Workflow](03-first-workflow.md)
- A project ready for feature development

## Step 1: Understanding EPCC Phases

The EPCC workflow has four distinct phases, each with its own purpose and output:

```
🔍 EXPLORE → 📋 PLAN → 💻 CODE → ✅ COMMIT
```

Each phase creates a documentation file that feeds into the next phase:

| Phase | Command | Output File | Purpose |
|-------|---------|-------------|---------|
| Explore | `/epcc/epcc-explore` | `EPCC_EXPLORE.md` | Understand the codebase |
| Plan | `/epcc/epcc-plan` | `EPCC_PLAN.md` | Design the approach |
| Code | `/epcc/epcc-code` | `EPCC_CODE.md` | Track implementation |
| Commit | `/epcc/epcc-commit` | `EPCC_COMMIT.md` | Finalize changes |

## Step 2: Phase 1 - EXPLORE

Start by exploring your codebase to understand the current authentication system:

```
/epcc/epcc-explore "user authentication system"
```

Claude will generate `EPCC_EXPLORE.md` with:
- Project structure analysis
- Current authentication patterns
- Dependencies and constraints
- Security considerations
- Recommendations for improvement

**What to look for in the output:**
- How the current system handles users
- What libraries are being used
- Where authentication logic lives
- Performance and security gaps

## Step 3: Phase 2 - PLAN

Now plan your authentication enhancement based on the exploration findings:

```
/epcc/epcc-plan "implement JWT authentication with refresh tokens"
```

Claude will generate `EPCC_PLAN.md` containing:
- Clear implementation objectives
- Technical approach and architecture
- Task breakdown with time estimates
- Risk assessment and mitigation strategies
- Testing strategy
- Success criteria

**Review the plan carefully:**
- Are the tasks granular enough?
- Do the time estimates seem realistic?
- Are all risks identified?
- Is the testing strategy comprehensive?

## Step 4: Phase 3 - CODE

Implement the first task from your plan using Test-Driven Development:

```
/epcc/epcc-code --tdd "implement JWT token generation service"
```

Claude will:
1. Write tests for the JWT service
2. Implement the minimal code to pass tests
3. Refactor for quality
4. Update `EPCC_CODE.md` with progress

**Follow this pattern for each task:**
```bash
# Check what's next in the plan
cat EPCC_PLAN.md

# Implement the next task
/epcc/epcc-code "implement JWT validation middleware"

# Check progress
cat EPCC_CODE.md
```

**Key principles during coding:**
- Complete one task fully before moving to the next
- Keep tests green at all times
- Update documentation as you go
- Ask for clarification if tasks are unclear

## Step 5: Phase 4 - COMMIT

When all planned tasks are complete, finalize your changes:

```
/epcc/epcc-commit "feat: Add JWT authentication with refresh tokens"
```

Claude will generate `EPCC_COMMIT.md` with:
- Complete change summary
- Testing validation results
- Security scan results
- Properly formatted commit message
- Pull request description

**The commit phase ensures:**
- All tests pass
- Code quality standards met
- Security requirements satisfied
- Documentation is updated
- Commit message follows conventions

## Step 6: Review Your Documentation Trail

You now have four files documenting your entire development process:

```bash
# Review the complete journey
ls EPCC_*.md

# See the exploration findings
cat EPCC_EXPLORE.md

# Review the implementation plan
cat EPCC_PLAN.md

# Check implementation progress
cat EPCC_CODE.md

# See the final summary
cat EPCC_COMMIT.md
```

## Step 7: Understanding Command Options

Each EPCC command supports different options for various scenarios:

### Exploration Options
```bash
# Quick overview for small changes
/epcc/epcc-explore "bug fix" --quick

# Deep analysis for complex features
/epcc/epcc-explore "payment system" --deep

# Focus on specific area
/epcc/epcc-explore "database layer" --focus performance
```

### Planning Options
```bash
# Include detailed risk assessment
/epcc/epcc-plan "payment integration" --with-risks

# Quick planning for minor changes
/epcc/epcc-plan "update validation" --quick

# Detailed planning with estimates
/epcc/epcc-plan "major refactor" --detailed
```

### Coding Options
```bash
# Continue with the current plan
/epcc/epcc-code

# Implement a specific task
/epcc/epcc-code "add password validation"

# Use test-driven development
/epcc/epcc-code --tdd "implement user registration"
```

### Commit Options
```bash
# Standard commit process
/epcc/epcc-commit "feat: Add new feature"

# Squash multiple commits
/epcc/epcc-commit --squash "Combine related changes"

# Amend the last commit
/epcc/epcc-commit --amend
```

## What You Learned

✅ **EPCC Workflow Structure**: The four phases and their purposes  
✅ **Command Usage**: How to use each `/epcc/` command effectively  
✅ **Documentation Trail**: How each phase creates permanent records  
✅ **Quality Gates**: How EPCC ensures code quality at each step  
✅ **Command Options**: Different approaches for different scenarios  
✅ **Integration**: How EPCC works with TDD and security practices  

## Next Steps

- **Practice**: Apply EPCC to your next feature development
- **Customize**: Adapt the workflow to your team's specific needs
- **Integrate**: Set up git hooks to enforce EPCC practices
- **Measure**: Track how EPCC improves your development quality

## Common Patterns

### New Feature Development
```bash
/epcc/epcc-explore "shopping cart" --deep
/epcc/epcc-plan "enhanced shopping cart with persistence"
/epcc/epcc-code --tdd "implement cart persistence"
/epcc/epcc-commit "feat: Add persistent shopping cart"
```

### Bug Fixes
```bash
/epcc/epcc-explore "login issue #456" --focus authentication
/epcc/epcc-plan "fix session timeout bug"
/epcc/epcc-code --tdd "fix session handling"
/epcc/epcc-commit "fix: Resolve login session timeout"
```

### Refactoring
```bash
/epcc/epcc-explore "payment module" --deep
/epcc/epcc-plan "refactor to strategy pattern"
/epcc/epcc-code "implement payment strategy abstraction"
/epcc/epcc-commit "refactor: Implement strategy pattern for payments"
```

The EPCC workflow provides a systematic approach that reduces errors, improves code quality, and creates comprehensive documentation of your development process.