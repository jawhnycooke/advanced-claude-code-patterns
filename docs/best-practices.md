# Best Practices Guide

Production-ready patterns and recommendations for Claude Code advanced implementations.

## Table of Contents
1. [Architecture Principles](#architecture-principles)
2. [Agent Best Practices](#agent-best-practices)
3. [Hook Optimization](#hook-optimization)
4. [Workflow Design](#workflow-design)
5. [Security Considerations](#security-considerations)
6. [Performance Optimization](#performance-optimization)
7. [Team Collaboration](#team-collaboration)
8. [Monitoring and Observability](#monitoring-and-observability)
9. [Cost Optimization](#cost-optimization)
10. [Common Anti-Patterns](#common-anti-patterns)

## Architecture Principles

### 1. Separation of Concerns

**✅ Do:**
```markdown
# Specialized agents for specific tasks
.claude/
├── agents/
│   ├── security-reviewer.md    # Security only
│   ├── test-generator.md        # Testing only
│   └── performance-optimizer.md # Performance only
```

**❌ Don't:**
```markdown
# One agent trying to do everything
.claude/
└── agents/
    └── super-agent.md  # Does security, testing, performance, etc.
```

### 2. Composability Over Complexity

**✅ Do:**
```yaml
# Compose simple workflows
stages:
  - name: analyze
    agent: analyzer
    output: analysis
  
  - name: process
    agent: processor
    input: ${analyze.output}
```

**❌ Don't:**
```yaml
# Overly complex single stage
stages:
  - name: do_everything
    agent: complex-agent
    actions: [analyze, process, validate, deploy, test, rollback]
```

### 3. Fail Fast, Recover Gracefully

**✅ Do:**
```json
{
  "hooks": {
    "pre-commit": {
      "fail_fast": true,
      "on_failure": {
        "message": "Specific error: ${error}",
        "suggestion": "Run 'make fix' to resolve"
      }
    }
  }
}
```

**❌ Don't:**
```json
{
  "hooks": {
    "pre-commit": {
      "continue_on_error": true,
      "suppress_output": true
    }
  }
}
```

## Command Template Best Practices

### 1. Argument Handling

**✅ Always Handle Missing Arguments:**
```markdown
---
name: my-command
description: Does something useful
version: 1.0.0
argument-hint: [target] [--mode]
---

# Command Title

## Parameters
$ARGUMENTS

If no arguments provided above:
- Use sensible defaults
- Analyze current context
- Ask for clarification if needed
```

**❌ Don't Assume Arguments:**
```markdown
# Bad - fails when no arguments given
## Processing file: $ARGUMENTS
```

### 2. Clear Argument Instructions

**✅ Good Parsing Guidance:**
```markdown
## Input Parameters
$ARGUMENTS

Parse arguments to determine:
- Target: specific file or directory (default: current directory)
- Mode: --quick or --deep (default: --quick)
- Output: --json or --text (default: --text)

If no arguments provided, use defaults listed above.
```

### 3. Argument Hints

**✅ Helpful Hints:**
```yaml
argument-hint: <required-arg> [optional-arg] [--flag]
```

**Examples:**
- `argument-hint: <file-path>` - Single required argument
- `argument-hint: [target] [--deep]` - All optional
- `argument-hint: <issue-number> [--priority:high|medium|low]` - Required with optional flag

### 4. Deprecated Metadata Fields

**❌ Don't Use These:**
```yaml
---
name: my-command
model: opus        # ❌ Remove - let Claude choose
tools: [Read, Write]  # ❌ Remove - let Claude determine
---
```

**✅ Use Only These:**
```yaml
---
name: my-command
description: Clear description
version: 1.0.0
argument-hint: [optional-args]
---
```

## Agent Best Practices

### 1. Agent Structure Requirements

**✅ Standard Agent Structure (right-sized for purpose):**
```markdown
---
name: agent-name
description: Use PROACTIVELY when... [trigger phrase]
model: sonnet  # or opus for complex tasks
tools: [Read, Grep, Glob]  # Minimal necessary set
---

## Quick Reference
- Core capability 1
- Core capability 2  
- Primary workflow
- Key constraint
- Value proposition

## Activation Instructions

- CRITICAL: Most important rule in CAPS
- WORKFLOW: Step → Step → Step → Step
- Essential behavioral rule
- Another essential rule
- STAY IN CHARACTER as PersonaName, role

## Core Identity

**Role**: Senior/Principal Title
**Identity**: You are **PersonaName**, who [one-line impact].

**Principles**:
- **Principle**: Action-oriented description
- [4-5 more principles maximum]

## Domain Knowledge
[Focused content with 1-2 examples per concept]

## Output Format
Deliverables:
- **Field**: Description
- **Field**: Description
```

**❌ Common Mistakes:**
- Unnecessary verbosity without added value
- Missing Quick Reference section
- Overly verbose activation instructions
- Including background stories in persona
- Requesting unnecessary tools
- Using prose in output format

### 2. Model Selection Strategy

**Choose Sonnet for:**
- Code generation from templates
- Documentation writing
- Test generation
- API endpoint creation
- Simple refactoring
- Routine automation

**Choose Opus for:**
- Complex architectural decisions
- Security analysis
- Performance optimization
- Legacy code archaeology
- Multi-step problem solving
- Cross-domain analysis

```yaml
# Simple tasks - use sonnet
model: sonnet

# Complex analysis - use opus
model: opus
```

### 3. Essential Agent Elements

**Required Sections:**
1. **Quick Reference** (3-5 bullets) - First content section
2. **Activation Instructions** (5-6 lines max)
3. **Core Identity** (No background stories)
4. **Domain Knowledge** (Merged with responsibilities)
5. **Output Format** (Directive bullets)

**Agent Validation Checklist:**
```python
def validate_agent(content):
    checks = {
        'focused': is_content_focused(content),  # No unnecessary verbosity
        'has_quick_ref': '## Quick Reference' in content,
        'activation_brief': is_activation_concise(content),
        'has_identity': '## Core Identity' in content,
        'minimal_tools': count_tools(content) <= 7,
        'has_output': '## Output Format' in content
    }
    return all(checks.values())

def is_content_focused(content):
    """Check if content is focused and purposeful."""
    # Check for redundancy, unnecessary sections, verbose explanations
    return True  # Implementation depends on specific criteria
```

### 4. Minimal Tool Selection

**Base Tools (start with these):**
```yaml
tools: [Read, Grep, Glob]
```

**Add Only If Necessary:**
- `Write, Edit` - For file modifications
- `Bash` - For command execution
- `WebSearch` - For current information
- `TodoWrite` - For task management
- `Task` - For multi-agent orchestration

**Never Request All Tools:**
```yaml
# ❌ Bad
tools: [Read, Write, Edit, MultiEdit, Grep, Glob, LS, Bash, BashOutput, WebSearch, WebFetch, Task, TodoWrite]

# ✅ Good
tools: [Read, Write, Grep]  # Only what's needed
```

### 5. Effective Personas

**✅ Good Persona:**
```markdown
## Core Identity

**Role**: Principal Security Engineer
**Identity**: You are **SecureGuard**, who prevents breaches before they happen.

**Principles**:
- **Zero Trust**: Verify everything
- **Defense in Depth**: Layer protections
- **Shift Left**: Security from the start
- **Continuous Monitoring**: Never stop watching
- **Education First**: Teach secure practices
```

**❌ Bad Persona:**
```markdown
## Core Identity

**Role**: Security Expert
**Identity**: You are an agent that does security.

**Background**: [Long story about career history...]
**Certifications**: [List of credentials...]
**Experience**: [Detailed work history...]
```

### 6. Testing Agents

```python
# Test agent structure
def test_agent_structure():
    agent = load_agent("security-reviewer.md")
    assert agent.is_focused()  # No unnecessary content
    assert agent.has_section("Quick Reference")
    assert agent.activation_is_concise()
    assert agent.tools_count <= 7

# Test agent behavior
def test_agent_behavior():
    response = run_agent("security-reviewer", test_code)
    assert "SecureGuard" in response  # Stays in character
    assert follows_output_format(response)
```

## Hook Optimization

### 1. Performance-First Design

**Fast Hooks:**
```json
{
  "name": "quick-checks",
  "timeout": 10,
  "parallel": true,
  "actions": [
    {
      "type": "command",
      "command": "ruff check .",  // Fast linter
      "cache": true
    }
  ]
}
```

**Slow Hooks to Avoid:**
```json
{
  "name": "slow-checks",
  "actions": [
    {
      "type": "command",
      "command": "pytest tests/",  // Run all tests on every commit
      "timeout": 600
    }
  ]
}
```

### 2. Progressive Hook Validation

```json
{
  "name": "progressive-validation",
  "stages": [
    {
      "name": "quick",
      "timeout": 5,
      "actions": ["syntax-check", "lint-changed-files"]
    },
    {
      "name": "thorough",
      "when": "branch == 'main'",
      "actions": ["full-test-suite", "security-scan"]
    }
  ]
}
```

### 3. Smart Caching

```json
{
  "name": "cached-checks",
  "cache": {
    "key": "${files_hash}",
    "ttl": 3600
  },
  "actions": [
    {
      "type": "command",
      "command": "npm run build",
      "cache_output": true,
      "skip_if_cached": true
    }
  ]
}
```

## Workflow Design

### 1. Idempotent Workflows

**Good: Idempotent**
```yaml
stages:
  - name: ensure_resource
    tasks:
      - name: check_exists
        command: kubectl get deployment app
        continue_on_error: true
      
      - name: create_if_missing
        when: ${check_exists.failed}
        command: kubectl apply -f deployment.yaml
```

**Bad: Non-idempotent**
```yaml
stages:
  - name: create_resource
    tasks:
      - name: create
        command: kubectl create -f deployment.yaml  # Fails if exists
```

### 2. Workflow State Management

```yaml
name: stateful_workflow
state:
  backend: redis
  prefix: workflow_${id}

stages:
  - name: process
    tasks:
      - name: checkpoint
        save_state:
          key: last_processed
          value: ${task.output}
      
      - name: resume
        on_restart:
          load_state:
            key: last_processed
            continue_from: ${state.value}
```

### 3. Workflow Composition

```yaml
# Base workflow
name: base_deployment
abstract: true
stages:
  - name: prepare
    tasks: [...]
  - name: deploy
    tasks: [...]

---
# Extended workflow
name: production_deployment
extends: base_deployment
override:
  stages:
    - name: deploy
      add_before:
        - name: approval
          type: manual_approval
```

## Security Considerations

### 1. Credential Management

**✅ Secure:**
```yaml
# Use environment variables
authentication:
  github:
    token: ${env:GITHUB_TOKEN}
  database:
    password: ${env:DB_PASSWORD}
```

**❌ Insecure:**
```yaml
# Never hardcode credentials
authentication:
  github:
    token: "ghp_actualTokenHere"
  database:
    password: "actualPassword"
```

### 2. Input Validation

```python
# Always validate inputs in agents
def validate_user_input(input_str: str) -> str:
    """Validate and sanitize user input."""
    # Remove potential command injection
    if any(char in input_str for char in [';', '|', '&', '$', '`']):
        raise ValueError("Invalid characters in input")
    
    # Escape for SQL
    escaped = input_str.replace("'", "''")
    
    return escaped
```

### 3. Least Privilege

```markdown
---
name: read-only-analyzer
model: sonnet
tools: [Read, Grep]  # No Write or Bash access
permissions:
  read_paths: ["src/", "tests/"]
  deny_paths: [".env", "secrets/", "*.key"]
---
```

### 4. Audit Logging

```json
{
  "audit": {
    "enabled": true,
    "log_level": "info",
    "include": [
      "agent_executions",
      "hook_triggers",
      "workflow_runs",
      "file_modifications"
    ],
    "destination": "audit.log",
    "format": "json"
  }
}
```

## Performance Optimization

### 1. Agent Response Caching

```python
# Cache expensive agent operations
from functools import lru_cache
import hashlib

@lru_cache(maxsize=100)
def cached_agent_call(agent_name: str, input_hash: str):
    """Cache agent responses for identical inputs."""
    return run_agent(agent_name, input_hash)

def get_agent_response(agent_name: str, input_data: str):
    input_hash = hashlib.md5(input_data.encode()).hexdigest()
    return cached_agent_call(agent_name, input_hash)
```

### 2. Parallel Processing

```yaml
# Maximize parallelization
stages:
  - name: parallel_analysis
    parallel:
      max_workers: 10
      chunk_size: 100
    tasks:
      - name: analyze_files
        for_each: ${files}
        agent: analyzer
        input: ${item}
```

### 3. Resource Limits

```yaml
# Prevent resource exhaustion
resources:
  limits:
    memory: 2Gi
    cpu: 2
    time: 300
  
  monitoring:
    alert_on:
      memory_usage: "> 80%"
      cpu_usage: "> 90%"
```

## Team Collaboration

### 1. Shared Configuration

```json
// team-settings.json
{
  "team": {
    "standards": {
      "code_style": "black",
      "test_coverage": 80,
      "documentation": "required"
    },
    "agents": {
      "shared_repo": "https://github.com/team/claude-agents",
      "auto_update": true
    },
    "notifications": {
      "slack_channel": "#dev-team",
      "email_list": "dev@company.com"
    }
  }
}
```

### 2. Agent Sharing

```bash
# Share agents across team
claude agent export security-reviewer > shared/security-reviewer.md
claude agent import shared/security-reviewer.md

# Version control agents
git add agents/
git commit -m "feat: add security reviewer agent v2.0"
git push
```

### 3. Workflow Documentation with YAML

> **📝 Note on YAML for Workflows**
> 
> YAML files are **not required** for workflows but are a **best practice** for:
> - Documenting complex multi-stage processes
> - Planning workflow architecture before implementation
> - Sharing workflow patterns across teams
> - Maintaining a clear record of workflow design decisions
> 
> Remember: Actual workflows are executed via slash commands, agents, and hooks - not YAML files.

#### Workflow Template Example

```yaml
# Team workflow template
name: team_feature_workflow
owner: platform-team
maintainers: ["alice", "bob"]
documentation: https://wiki.company.com/workflows

parameters:
  team:
    type: string
    allowed: ["backend", "frontend", "mobile"]
  
stages:
  - name: team_specific
    switch: ${parameters.team}
    cases:
      backend:
        import: workflows/backend.yaml
      frontend:
        import: workflows/frontend.yaml
```

## Monitoring and Observability

### 1. Metrics Collection

```yaml
metrics:
  provider: prometheus
  endpoint: /metrics
  
  custom_metrics:
    - name: agent_execution_time
      type: histogram
      labels: [agent_name, model]
    
    - name: workflow_success_rate
      type: gauge
      labels: [workflow_name, environment]
    
    - name: hook_trigger_count
      type: counter
      labels: [hook_name, event]
```

### 2. Distributed Tracing

```yaml
tracing:
  provider: jaeger
  sampling_rate: 0.1
  
  trace_points:
    - agents: all
    - workflows: [critical_workflows]
    - hooks: [pre-deploy, post-deploy]
```

### 3. Alerting Rules

```yaml
alerts:
  - name: high_error_rate
    metric: error_rate
    condition: "> 5%"
    window: 5m
    severity: critical
    notify: ["pagerduty", "slack"]
  
  - name: slow_agent_response
    metric: agent_response_time
    condition: "p95 > 10s"
    window: 10m
    severity: warning
```

## Cost Optimization

### 1. Model Usage Optimization

```python
def select_optimal_model(task_complexity: float) -> str:
    """Select most cost-effective model for task."""
    if task_complexity < 0.3:
        return "sonnet"  # $3 per million tokens
    elif task_complexity < 0.7:
        return "sonnet"  # Still use sonnet for moderate tasks
    else:
        return "opus"  # $15 per million tokens only for complex
```

### 2. Token Usage Monitoring

```yaml
monitoring:
  token_usage:
    track: true
    alert_threshold: 1000000  # Alert at 1M tokens
    daily_limit: 5000000      # 5M tokens per day
    
    breakdown:
      by_agent: true
      by_workflow: true
      by_user: true
```

### 3. Caching Strategy

```python
# Aggressive caching for common operations
CACHE_CONFIG = {
    "agent_responses": {
        "ttl": 3600,
        "max_size": "1GB"
    },
    "workflow_state": {
        "ttl": 86400,
        "max_size": "500MB"
    },
    "hook_results": {
        "ttl": 300,
        "max_size": "100MB"
    }
}
```

## Common Anti-Patterns

### 1. ❌ God Agent

**Wrong:**
```markdown
---
name: do-everything
model: opus  # Expensive for simple tasks
---
I can do security, testing, deployment, monitoring, and more!
```

**Right:**
```markdown
# Multiple specialized agents
security-reviewer.md
test-generator.md
deployment-agent.md
monitoring-setup.md
```

### 2. ❌ Synchronous Everything

**Wrong:**
```yaml
stages:
  - name: sequential
    tasks:
      - task1  # Waits
      - task2  # Waits
      - task3  # Waits
```

**Right:**
```yaml
stages:
  - name: parallel
    parallel: true
    tasks: [task1, task2, task3]  # Run simultaneously
```

### 3. ❌ No Error Handling

**Wrong:**
```json
{
  "hook": {
    "action": "delete_everything",
    "confirm": false,
    "backup": false
  }
}
```

**Right:**
```json
{
  "hook": {
    "action": "delete_carefully",
    "confirm": true,
    "backup": true,
    "rollback_on_error": true,
    "dry_run": true
  }
}
```

### 4. ❌ Hardcoded Values

**Wrong:**
```yaml
database:
  host: "prod-db.company.com"
  password: "admin123"
```

**Right:**
```yaml
database:
  host: ${env:DB_HOST}
  password: ${env:DB_PASSWORD}
```

### 5. ❌ No Documentation

**Wrong:**
```markdown
---
name: mystery-agent
---
# Does stuff
```

**Right:**
```markdown
---
name: api-validator
description: Validates REST API contracts against OpenAPI spec
version: 1.0.0
---

# API Validator Agent

## Purpose
Validates REST API implementations against OpenAPI specifications.

## Usage
Provide an OpenAPI spec and implementation to validate.

## Example
"Validate the /users endpoint against openapi.yaml"
```

## Production Readiness Checklist

### Before Deploying to Production

- [ ] All agents have defined models and tools
- [ ] Hooks have timeout and retry configuration
- [ ] Workflows are idempotent and resumable
- [ ] Credentials are externalized
- [ ] Monitoring and alerting configured
- [ ] Cost limits and alerts set
- [ ] Audit logging enabled
- [ ] Backup and rollback procedures documented
- [ ] Team trained on patterns and tools
- [ ] Documentation up to date

## Continuous Improvement

### 1. Regular Reviews

```yaml
review_schedule:
  agents:
    frequency: monthly
    metrics: [usage, accuracy, cost]
  
  workflows:
    frequency: quarterly
    metrics: [success_rate, duration, cost]
  
  hooks:
    frequency: weekly
    metrics: [trigger_count, failure_rate]
```

### 2. A/B Testing

```yaml
experiments:
  - name: model_comparison
    variants:
      - name: control
        model: sonnet
      - name: treatment
        model: opus
    metrics: [accuracy, speed, cost]
    duration: 1_week
```

### 3. Feedback Loop

```python
# Collect and act on feedback
feedback_system = {
    "collection": ["user_ratings", "error_reports", "suggestions"],
    "analysis": "weekly",
    "action_items": "prioritized_backlog",
    "implementation": "sprint_planning"
}
```

## Next Steps

- Review [Troubleshooting Guide](./troubleshooting.md) for common issues
- Explore [Agent Templates](../agents/) for real implementations
- Check [Command Templates](../commands/) for more patterns
- Join [Community Forum](https://community.anthropic.com) for support

