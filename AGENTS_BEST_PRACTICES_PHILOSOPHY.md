# Agents Best Practices and Philosophy

A comprehensive guide to understanding, creating, and managing agents in Claude Code.

## Table of Contents

1. [Agent Design Philosophy](#agent-design-philosophy)
2. [Technical Implementation](#technical-implementation)
3. [Agent Orchestration](#agent-orchestration)
4. [Context and State Management](#context-and-state-management)
5. [Best Practices](#best-practices)
6. [Advanced Patterns](#advanced-patterns)
7. [Specific Scenarios](#specific-scenarios)
8. [Decision Framework](#decision-framework)
9. [Agent Ecosystem Philosophy](#agent-ecosystem-philosophy)

---

## Agent Design Philosophy

### 1. When Something Should Be an Agent vs. Regular Task

**Create an agent when:**
- The task requires **specialized domain expertise** (e.g., security analysis, performance optimization)
- The work involves **multiple coordinated steps** that benefit from autonomous execution
- The task will be **repeated frequently** with similar patterns
- You need **consistent methodology** across different contexts
- The work requires **specific tool constraints** (e.g., read-only analysis)
- There's value in **encapsulating complexity** from the user

**Handle as a regular task when:**
- It's a **one-off operation** with unique requirements
- The task is **simple and straightforward** (< 3 steps)
- User needs **direct control** over each step
- The work is **highly context-specific** to current conversation
- Real-time **user feedback** is required during execution

**Example Decision:**
```
Task: "Review this code for security issues"
→ Agent (specialized expertise, repeatable pattern)

Task: "Add a console.log here to debug this specific issue"
→ Regular task (one-off, simple, context-specific)
```

### 2. Handling Agent Conflicts and Overlapping Responsibilities

**Design Principles:**
- **Single Responsibility**: Each agent should have ONE clear primary purpose
- **Clear Boundaries**: Use explicit MUST/MUST NOT rules
- **Hierarchical Specialization**: More specific agents override general ones
- **Composition Over Duplication**: Agents can invoke each other

**Conflict Resolution Strategy:**
```markdown
Priority Order:
1. Most specific agent (e.g., react-accessibility-reviewer)
2. Domain-specific agent (e.g., accessibility-reviewer)  
3. General-purpose agent (e.g., code-reviewer)
4. Base agent (e.g., general-purpose)
```

**Boundary Definition Example:**
```markdown
## security-reviewer
MUST: Analyze for vulnerabilities
MUST NOT: Fix issues (only report)

## security-fixer
MUST: Implement security fixes
MUST NOT: Analyze (assumes analysis complete)
```

### 3. Good Agent vs. Bad Agent Design

**Good Agent Characteristics:**
- **Focused**: Does one thing exceptionally well
- **Predictable**: Consistent behavior across invocations
- **Self-contained**: Minimal external dependencies
- **Well-documented**: Clear purpose and usage examples
- **Fail-safe**: Graceful degradation and clear error messages
- **Composable**: Works well with other agents

**Bad Agent Anti-patterns:**
- **Kitchen Sink**: Tries to do everything
- **Hidden Behavior**: Unclear or surprising actions
- **Overly Complex**: Difficult to understand or maintain
- **Rigid**: No flexibility for edge cases
- **Chatty**: Requires constant user interaction
- **Destructive**: Makes irreversible changes without confirmation

**Example Comparison:**

```markdown
# Bad: Kitchen Sink Agent
"An agent that reviews code, fixes bugs, writes tests, updates docs, and deploys"

# Good: Focused Agent
"An agent that identifies missing test coverage in JavaScript code"
```

---

## Technical Implementation

### 4. Determining Optimal Tool Permissions

**Principle of Least Privilege:**
Grant only the minimum permissions necessary for the agent's core function.

**Permission Decision Tree:**
```
1. What is the agent's primary action?
   - Analyze/Review → Read, Grep, Glob
   - Create/Generate → Write, Edit
   - Fix/Modify → Edit, MultiEdit
   - Test/Validate → Read, Bash (limited)
   - Deploy/Execute → Bash, BashOutput (careful!)

2. What could go wrong?
   - Data loss? → Remove Write
   - Security risk? → Remove Bash
   - Performance impact? → Add timeouts
   - Incorrect analysis? → Read-only safer

3. Can the task be done with less?
   - Always prefer Read over Edit
   - Always prefer Edit over Write
   - Always prefer specific over general
```

**Permission Templates:**

```markdown
## Analysis Agent
- Read: ✅ (examine files)
- Grep: ✅ (search patterns)
- Glob: ✅ (find files)
- Write: ❌ (no modifications)
- Bash: ❌ (no execution)

## Generator Agent
- Read: ✅ (understand context)
- Write: ✅ (create new files)
- Edit: ❌ (don't modify existing)
- Bash: ❌ (no execution)

## Fixer Agent
- Read: ✅ (understand current state)
- Edit: ✅ (modify existing files)
- Write: ⚠️ (only if creating new files)
- Bash: ⚠️ (only for validation)
```

### 5. Agent Versioning and Updates

**Versioning Strategy:**

```markdown
## Agent Version Format: v[MAJOR].[MINOR].[PATCH]

MAJOR: Breaking changes to behavior or interface
MINOR: New capabilities, backward compatible
PATCH: Bug fixes, documentation updates

Example:
v1.0.0 → Initial release
v1.1.0 → Added new analysis patterns
v1.1.1 → Fixed false positive in pattern detection
v2.0.0 → Changed output format (breaking)
```

**Update Management:**

```markdown
## Compatibility Matrix
Agent: security-reviewer
- v2.x: Current, recommended
- v1.x: Deprecated, supported until 2024-12
- v0.x: Unsupported, do not use

## Migration Path
From v1.x to v2.x:
1. Update output parsers to handle new format
2. Adjust tool permissions (Bash removed)
3. Update invocation examples
```

**Deprecation Process:**
1. Mark as deprecated with timeline
2. Provide migration guide
3. Maintain compatibility period
4. Log warnings when used
5. Final removal after notice period

### 6. Agent Types and subagent_type Parameter

**Agent Type Hierarchy:**

```
general-purpose
├── Capabilities: All tools
├── Use case: Undefined/broad tasks
└── Flexibility: Maximum

domain-specific (e.g., security-reviewer)
├── Capabilities: Domain-relevant tools
├── Use case: Specialized tasks
└── Flexibility: Constrained to domain

task-specific (e.g., test-generator)
├── Capabilities: Minimal required tools
├── Use case: Single specific task
└── Flexibility: Highly constrained
```

**Selection Criteria:**

```python
def select_subagent_type(task_description):
    if "security" in task_description:
        return "security-reviewer"
    elif "test" in task_description:
        return "test-generator"
    elif "performance" in task_description:
        return "performance-profiler"
    elif task_is_complex and not domain_specific:
        return "general-purpose"
    else:
        return most_specific_match(task_description)
```

---

## Agent Orchestration

### 7. Designing Agents for Pipeline Collaboration

**Pipeline Patterns:**

```markdown
## Sequential Pipeline
analyzer → planner → implementer → validator

## Parallel Analysis
┌→ security-reviewer ─┐
│→ performance-analyzer ├→ report-aggregator
└→ accessibility-checker ┘

## Conditional Flow
detector → (if issues) → fixer → validator
        ↘ (if clean) → reporter
```

**Data Passing Strategies:**

```markdown
## File-based Communication
Agent A writes: analysis_report.json
Agent B reads: analysis_report.json

## Context Preservation
Agent A output: "Found 3 security issues in auth.js"
Main context: Stores finding
Agent B input: "Fix the 3 security issues found in auth.js"

## Structured Handoff
{
  "from": "analyzer",
  "to": "fixer",
  "data": {
    "issues": [...],
    "priority": "high",
    "context": {...}
  }
}
```

**Best Practices:**
- Define clear **interface contracts** between agents
- Use **structured data formats** (JSON, YAML)
- Include **metadata** for traceability
- Implement **validation** at handoff points
- Design for **partial failure** recovery

### 8. Debugging Agent Behavior

**Common Failure Modes:**

```markdown
## 1. Silent Failure
Symptom: Agent completes but produces no output
Causes: 
- Missing permissions
- Empty search results
- Unhandled edge cases

Debug:
- Add verbose logging
- Check permission requirements
- Test with minimal input

## 2. Infinite Loops
Symptom: Agent never completes
Causes:
- Recursive file traversal
- Waiting for user input
- API rate limiting

Debug:
- Add iteration counters
- Set timeout limits
- Log progress indicators

## 3. Wrong Output Format
Symptom: Output doesn't match expected structure
Causes:
- Prompt ambiguity
- Version mismatch
- Edge case handling

Debug:
- Validate output schema
- Add format examples
- Test edge cases
```

**Debugging Strategy:**

```python
# Add debug wrapper
def debug_agent(agent_name, task):
    print(f"Starting {agent_name}")
    print(f"Input: {task}")
    
    start_time = time.time()
    result = run_agent(agent_name, task)
    duration = time.time() - start_time
    
    print(f"Duration: {duration}s")
    print(f"Output length: {len(result)}")
    print(f"Output preview: {result[:200]}")
    
    validate_output(result)
    return result
```

---

## Context and State Management

### 9. Maintaining Context Across Invocations

**Context Preservation Strategies:**

```markdown
## Stateless Design (Preferred)
Each invocation is independent:
- Context passed explicitly
- No hidden dependencies
- Reproducible results

## Conversation Context
Main assistant maintains context:
- Agent receives relevant history
- Returns results to main context
- Main coordinates multiple agents

## File-based State
State persisted to filesystem:
- .claude/agent_state/[agent_name].json
- Enables resumption
- Requires cleanup strategy
```

**Context Window Management:**

```markdown
## Priority Order for Context
1. Current task description
2. Recent relevant outputs
3. File contents being analyzed
4. Historical patterns/decisions
5. General project context

## Truncation Strategy
When approaching limits:
1. Summarize older findings
2. Drop redundant information
3. Focus on actionable items
4. Preserve error states
```

### 10. Scope Hierarchy: User vs. Project vs. Global

**Scope Resolution Order:**

```
1. Project-specific (.claude/agents/)
   ↓ Overrides
2. User-specific (~/.claude/agents/)
   ↓ Overrides
3. Global agents (built-in)
```

**Configuration Precedence:**

```markdown
## Example: code-reviewer agent

### Global (built-in)
- Basic code review functionality
- Generic best practices

### User (~/.claude/agents/)
- Personal style preferences
- Custom review checklist
- Preferred tools/linters

### Project (.claude/agents/)
- Project-specific standards
- Team conventions
- Required review criteria
```

**Discovery Mechanism:**

```python
def find_agent(agent_name):
    # Check project-specific first
    if exists(f".claude/agents/{agent_name}.md"):
        return load_project_agent(agent_name)
    
    # Check user-specific
    elif exists(f"~/.claude/agents/{agent_name}.md"):
        return load_user_agent(agent_name)
    
    # Fall back to global
    elif agent_name in GLOBAL_AGENTS:
        return load_global_agent(agent_name)
    
    else:
        raise AgentNotFound(agent_name)
```

---

## Best Practices

### 11. Common Mistakes When Creating Custom Agents

**Top 10 Mistakes:**

```markdown
## 1. Over-Engineering
❌ Creating complex multi-phase agents for simple tasks
✅ Start simple, add complexity only when needed

## 2. Unclear Purpose
❌ "An agent that helps with code"
✅ "An agent that identifies dead code in Python projects"

## 3. Permission Overreach
❌ Granting Write access for analysis tasks
✅ Minimum necessary permissions

## 4. Missing Error Handling
❌ Assuming happy path only
✅ Define behavior for edge cases and failures

## 5. Poor Output Format
❌ Unstructured text dumps
✅ Consistent, parseable output format

## 6. Ignoring Context Limits
❌ Trying to analyze entire large codebases
✅ Intelligent filtering and prioritization

## 7. No Usage Examples
❌ Just describing what agent does
✅ Concrete invocation examples

## 8. Tight Coupling
❌ Agent depends on specific project structure
✅ Flexible, configurable behavior

## 9. Verbose Output
❌ Printing every detail of analysis
✅ Summarized, actionable findings

## 10. No Testing Strategy
❌ Assuming agent will work correctly
✅ Test cases and validation criteria
```

### 12. Documenting Agents for Team Collaboration

**Documentation Template:**

```markdown
# [Agent Name] Agent

## Quick Reference
- **Purpose**: One-line description
- **Author**: @username
- **Version**: v1.0.0
- **Last Updated**: 2024-01-15

## Overview
Brief paragraph explaining why this agent exists and what problem it solves.

## Usage

### Basic Invocation
\`\`\`bash
@agent-name "analyze src/"
\`\`\`

### Advanced Options
\`\`\`bash
@agent-name "analyze src/" --verbose --format=json
\`\`\`

## Input Requirements
- Required: Target directory or file
- Optional: Configuration flags
- Context: Any necessary setup

## Output Format
\`\`\`json
{
  "status": "success",
  "findings": [...],
  "summary": "..."
}
\`\`\`

## Examples

### Example 1: Basic Analysis
[Show real input/output]

### Example 2: Complex Scenario
[Show edge case handling]

## Limitations
- Cannot analyze binary files
- Maximum 1000 files per run
- Requires Python 3.8+

## Troubleshooting
| Problem | Solution |
|---------|----------|
| No output | Check file permissions |
| Timeout | Reduce scope of analysis |

## Related Agents
- `dependency-analyzer`: For dependency analysis
- `security-scanner`: For security focus

## Changelog
- v1.0.0: Initial release
- v0.9.0: Beta testing
```

### 13. Ideal Size and Complexity for a Single Agent

**Complexity Metrics:**

```markdown
## Size Guidelines

### Small Agent (Preferred)
- 1-3 primary functions
- < 200 lines of logic
- Single responsibility
- 5-10 minute execution

### Medium Agent (Acceptable)
- 4-6 related functions
- 200-500 lines of logic
- Coordinated workflow
- 10-30 minute execution

### Large Agent (Avoid)
- 7+ functions
- > 500 lines of logic
- Multiple responsibilities
- > 30 minute execution
→ Consider splitting into multiple agents
```

**When to Split:**

```markdown
## Split Indicators
1. Multiple distinct phases with different tools
2. Parts could be useful independently
3. Different expertise domains
4. Significantly different execution times
5. Different permission requirements

## Example Split
❌ "test-and-deploy" agent
✅ "test-runner" + "deployment" agents

❌ "full-stack-reviewer" agent
✅ "frontend-reviewer" + "backend-reviewer" + "db-reviewer"
```

---

## Advanced Patterns

### 14. Creating Adaptive Agents

**Learning Patterns:**

```markdown
## Pattern Recognition
Agent tracks common issues:
\`\`\`json
{
  "patterns_detected": {
    "missing_error_handling": 45,
    "hardcoded_values": 23,
    "no_input_validation": 67
  },
  "suggestions": [
    "Consider project-wide error handling middleware",
    "Create configuration module for constants"
  ]
}
\`\`\`

## Feedback Incorporation
1. Agent provides initial analysis
2. User corrects/adjusts findings
3. Agent stores corrections
4. Future runs incorporate learning

## Adaptive Thresholds
- Start with strict thresholds
- Track false positive rate
- Adjust based on user acceptance
- Maintain per-project settings
```

**Implementation Strategy:**

```python
class AdaptiveAgent:
    def __init__(self):
        self.history = load_history()
        self.thresholds = load_thresholds()
    
    def analyze(self, code):
        findings = self.detect_issues(code)
        
        # Adjust based on history
        if self.history.false_positive_rate > 0.3:
            findings = self.apply_stricter_filter(findings)
        
        # Learn from patterns
        if self.detect_pattern_cluster(findings):
            self.suggest_systematic_fix()
        
        return findings
    
    def incorporate_feedback(self, feedback):
        self.history.add(feedback)
        self.adjust_thresholds()
        self.save_state()
```

### 15. Meta-Agents That Create or Modify Other Agents

**Meta-Agent Patterns:**

```markdown
## Agent Generator
Purpose: Creates specialized agents based on requirements

Input: "I need an agent that reviews SQL queries for performance"
Output: Complete agent definition with appropriate tools and workflow

## Agent Optimizer
Purpose: Analyzes agent performance and suggests improvements

Input: Existing agent + execution metrics
Output: Optimized agent configuration

## Agent Composer
Purpose: Combines multiple agents into pipelines

Input: List of agents + desired workflow
Output: Orchestration configuration
```

**Safety Constraints:**

```markdown
## Meta-Agent Rules
MUST:
- Validate generated agents before activation
- Preserve audit trail of modifications
- Require approval for permission changes
- Test in sandbox before deployment

MUST NOT:
- Grant permissions beyond original request
- Modify global/system agents
- Create recursive meta-agents
- Override security constraints
```

---

## Specific Scenarios

### 16. Complex Domain Example: Database Migration Agent

**Multi-Phase Operation Design:**

```markdown
# Database Migration Agent

## Phase 1: Analysis
Tools: Read, Grep
Actions:
- Inventory current schema
- Identify dependencies
- Assess data volumes
- Estimate migration time

## Phase 2: Planning
Tools: Write
Actions:
- Generate migration plan
- Create rollback procedures
- Define validation criteria
- Set checkpoint strategy

## Phase 3: Pre-Migration
Tools: Bash (limited)
Actions:
- Backup current state
- Validate target availability
- Check space requirements
- Verify permissions

## Phase 4: Migration
Tools: Bash, BashOutput
Actions:
- Execute migration scripts
- Monitor progress
- Validate checkpoints
- Handle errors

## Phase 5: Validation
Tools: Read, Bash
Actions:
- Compare schemas
- Verify data integrity
- Run test queries
- Check performance

## Rollback Mechanism
Triggered when:
- Validation fails
- Error threshold exceeded
- User cancellation
- Timeout reached

Actions:
1. Stop migration
2. Restore from backup
3. Verify restoration
4. Report failure details
```

### 17. External Service Integration Agent

**API Integration Pattern:**

```markdown
# External API Agent

## Authentication Handling
\`\`\`python
def setup_auth(self):
    # Check for credentials
    if not self.env.get('API_KEY'):
        return self.prompt_for_key()
    
    # Validate credentials
    if not self.validate_key():
        return self.handle_auth_error()
    
    # Setup session
    self.session = self.create_authenticated_session()
\`\`\`

## Rate Limiting Strategy
\`\`\`python
class RateLimiter:
    def __init__(self, max_per_minute=60):
        self.max = max_per_minute
        self.calls = []
    
    def wait_if_needed(self):
        now = time.time()
        self.calls = [c for c in self.calls if now - c < 60]
        
        if len(self.calls) >= self.max:
            sleep_time = 61 - (now - self.calls[0])
            time.sleep(sleep_time)
        
        self.calls.append(now)
\`\`\`

## Error Recovery
\`\`\`python
def call_api_with_retry(self, endpoint, data):
    for attempt in range(3):
        try:
            response = self.session.post(endpoint, json=data)
            if response.status_code == 429:  # Rate limited
                self.handle_rate_limit(response)
                continue
            elif response.status_code == 503:  # Service unavailable
                self.exponential_backoff(attempt)
                continue
            return response
        except NetworkError as e:
            if attempt == 2:
                raise
            self.log_retry(attempt, e)
\`\`\`
```

---

## Decision Framework

### 18. When to Suggest Creating an Agent vs. Direct Handling

**Decision Tree:**

```markdown
## Primary Decision Factors

1. Frequency of Task
   - Once → Direct handling
   - Occasionally → Consider agent
   - Frequently → Create agent

2. Complexity Level
   - Simple (1-3 steps) → Direct handling
   - Moderate (4-10 steps) → Consider agent
   - Complex (10+ steps) → Create agent

3. Expertise Required
   - General knowledge → Direct handling
   - Domain-specific → Consider agent
   - Specialized expertise → Create agent

4. Risk Level
   - Low risk → Direct handling
   - Moderate risk → Consider agent
   - High risk → Create agent (with constraints)

5. Reproducibility Need
   - One-off → Direct handling
   - Might repeat → Consider agent
   - Definitely repeat → Create agent
```

**Cost-Benefit Analysis:**

```python
def should_create_agent(task):
    score = 0
    
    # Frequency (0-3 points)
    if task.frequency == "daily":
        score += 3
    elif task.frequency == "weekly":
        score += 2
    elif task.frequency == "monthly":
        score += 1
    
    # Complexity (0-3 points)
    if task.steps > 10:
        score += 3
    elif task.steps > 5:
        score += 2
    elif task.steps > 3:
        score += 1
    
    # Expertise (0-3 points)
    if task.requires_specialized_knowledge:
        score += 3
    elif task.requires_domain_knowledge:
        score += 2
    elif task.requires_best_practices:
        score += 1
    
    # Decision
    if score >= 7:
        return "Definitely create agent"
    elif score >= 4:
        return "Consider creating agent"
    else:
        return "Handle directly"
```

---

## Agent Ecosystem Philosophy

### How Agents Should Complement Each Other

**Ecosystem Design Principles:**

```markdown
## 1. Hierarchical Specialization
General → Domain → Specific → Task
Each level adds constraints and expertise

## 2. Composability
Agents should work as:
- Independent units
- Pipeline components
- Orchestrated systems

## 3. Non-Overlapping Responsibilities
Each agent owns its domain completely
Clear handoff points between agents

## 4. Shared Conventions
- Common output formats
- Consistent error handling
- Standardized metadata

## 5. Progressive Enhancement
- Basic agents provide foundation
- Specialized agents add depth
- Meta-agents enable automation
```

**Ecosystem Evolution:**

```markdown
## Stage 1: Individual Agents
Independent tools for specific tasks

## Stage 2: Agent Pipelines
Agents working in sequence

## Stage 3: Agent Networks
Complex orchestration and dependencies

## Stage 4: Self-Organizing Systems
Agents that create and modify other agents

## Stage 5: Autonomous Ecosystems
Self-maintaining, self-improving agent networks
```

**Philosophy of Agent-Based Development:**

```markdown
## Core Beliefs

1. **Specialization Over Generalization**
   Expert agents outperform generalists in their domain

2. **Composition Over Monoliths**
   Small, focused agents combined > large, complex agents

3. **Explicit Over Implicit**
   Clear boundaries and contracts > assumed behavior

4. **Safety Over Capability**
   Constrained agents > powerful but risky agents

5. **Evolution Over Revolution**
   Incremental improvements > complete rewrites

6. **Community Over Isolation**
   Agents that work together > standalone tools

7. **Transparency Over Magic**
   Understandable behavior > black box automation
```

**Future Vision:**

```markdown
## The Ideal Agent Ecosystem

Imagine a development environment where:

1. **Agents handle routine tasks automatically**
   - Code review on every commit
   - Test generation for new functions
   - Documentation updates in sync

2. **Specialized experts available instantly**
   - Security agent catches vulnerabilities
   - Performance agent optimizes bottlenecks
   - Accessibility agent ensures compliance

3. **Intelligent orchestration**
   - Agents coordinate without manual pipeline
   - Right agent activated for each context
   - Seamless handoffs between specialists

4. **Continuous improvement**
   - Agents learn from usage patterns
   - Community shares agent improvements
   - Ecosystem evolves with needs

5. **Developer augmentation, not replacement**
   - Agents handle tedious work
   - Developers focus on creative problems
   - Human judgment guides agent actions
```

---

## Conclusion

The agent ecosystem represents a paradigm shift in how we approach software development tasks. By following these principles and best practices, we can create agents that:

- **Enhance productivity** without adding complexity
- **Maintain quality** through consistent methodology
- **Preserve safety** through careful constraints
- **Enable innovation** through composable building blocks

The key is to think of agents not as standalone tools, but as members of a collaborative ecosystem, each contributing their specialized expertise toward common goals.

Remember: **The best agent is one that does one thing so well that you forget it's an agent at all.**