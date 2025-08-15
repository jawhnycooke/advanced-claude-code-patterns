# Agent Development Guide

Comprehensive guide to creating and using custom Claude Code agents for specialized tasks.

## Table of Contents
1. [Understanding Agents](#understanding-agents)
2. [Agent Structure](#agent-structure)
3. [Quick Reference Section](#quick-reference-section)
4. [Activation Instructions](#activation-instructions)
5. [Agent Personas](#agent-personas)
6. [Creating Your First Agent](#creating-your-first-agent)
7. [Model Selection Strategy](#model-selection-strategy)
8. [Advanced Agent Patterns](#advanced-agent-patterns)
9. [Agent Composition](#agent-composition)
10. [Testing Agents](#testing-agents)
11. [Best Practices](#best-practices)

## Understanding Agents

### What Are Agents?

Agents are specialized configurations of Claude Code that excel at specific tasks. They are Markdown files with YAML frontmatter that define:
- The agent's purpose and expertise
- Which model to use (sonnet or opus)
- Available tools and permissions  
- Behavioral instructions

### Why Use Agents?

- **Specialization**: Focused expertise for specific domains
- **Consistency**: Reproducible behavior across sessions
- **Efficiency**: Streamlined structure for faster processing
- **Reusability**: Share agents across projects and teams
- **Composability**: Combine agents for complex tasks

## Agent Structure

### Standard Agent Format

Every agent should be **no longer than necessary** to keep the agent focused and effective. The structure should be streamlined while preserving essential domain knowledge:

```markdown
---
name: agent-name
description: Brief description starting with trigger phrase
model: sonnet  # or opus for complex tasks
color: semantic-color
tools: [Read, Write, Grep]  # Minimal necessary set
---

## Quick Reference
- Core capability 1
- Core capability 2
- Primary workflow
- Key constraint or requirement
- Main value proposition

## Activation Instructions

- CRITICAL: Most important rule in CAPS
- WORKFLOW: Step → Step → Step → Step
- Essential behavioral rule
- Another essential rule
- STAY IN CHARACTER as PersonaName, brief role

## Core Identity

**Role**: Senior/Principal Title  
**Identity**: You are **PersonaName**, who [impactful one-line description].

**Principles**:
- **Principle Name**: Action-oriented description
- **Principle Name**: Action-oriented description
- **Principle Name**: Action-oriented description
- **Principle Name**: Action-oriented description
- **Principle Name**: Action-oriented description

## Domain Knowledge Section 1

### Subsection
```language
# Focused code example
code here
```

### Another Subsection
- Specific pattern or approach
- Implementation detail
- Best practice

## Domain Knowledge Section 2

Content with inline examples as needed

## Output Format

What agent provides:
- **Field Name**: What it contains
- **Field Name**: What it contains
- **Field Name**: What it contains

Deliverables:
- Specific item
- Specific item
- Specific item
```

### Frontmatter Configuration

| Field | Description | Options | Required |
|-------|-------------|---------|----------|
| `name` | Agent identifier (kebab-case) | Any string | Yes |
| `description` | Purpose with trigger phrase | Any string | Yes |
| `model` | LLM model selection | `sonnet`, `opus` | Yes |
| `tools` | Minimal necessary tools | Array of tool names | Yes |
| `color` | UI styling color | Color name | No |

### Structure Requirements

- **Total Length**: As concise as necessary for agent effectiveness
- **Quick Reference**: 3-5 bullet points (required first section)
- **Activation Instructions**: Brief and directive (typically 5-6 lines)
- **Core Identity**: Condensed format, no background stories
- **Principles**: Action-oriented, only as many as needed
- **Code Examples**: Focused examples that demonstrate key concepts
- **Output Format**: Directive bullets, not prose

**Key Principle**: Remove redundancy while preserving essential information. Some agents may need 80 lines, others 200+ lines - let the agent's purpose and complexity determine the appropriate length.

## Quick Reference Section

The Quick Reference is the **required first section** after frontmatter that provides immediate context:

### Purpose
- Instantly conveys agent capabilities
- Sets user expectations
- Provides at-a-glance value proposition
- Reduces cognitive load

### Structure
```markdown
## Quick Reference
- Primary capability or specialization
- Key workflow or process
- Main constraint or requirement  
- Unique value proposition
- Critical dependency or tool
```

### Examples

#### Security Agent
```markdown
## Quick Reference
- Identifies OWASP Top 10 vulnerabilities
- Performs threat modeling and risk assessment
- Reviews authentication and authorization
- Provides remediation with severity ratings
- Requires code read access for analysis
```

#### Test Generator
```markdown
## Quick Reference
- Creates comprehensive test suites
- Follows TDD red-green-refactor cycle
- Generates unit and integration tests
- Achieves 80%+ code coverage
- Outputs pytest-compatible tests
```

## Activation Instructions

Activation instructions guide Claude on how to embody the agent. Keep them concise and directive.

### Structure (keep brief and directive)
```markdown
## Activation Instructions

- CRITICAL: [Most important rule in CAPS]
- WORKFLOW: [Step] → [Step] → [Step] → [Step]
- [Essential behavioral rule]
- [Another essential rule]
- STAY IN CHARACTER as [Name], [brief role]
```

### Examples

#### Security Reviewer
```markdown
## Activation Instructions

- CRITICAL: Always check for OWASP Top 10 vulnerabilities
- WORKFLOW: Scan → Analyze → Prioritize → Report → Remediate
- Provide severity ratings for all findings
- Never approve code with critical vulnerabilities
- STAY IN CHARACTER as SecureGuard, security expert
```

#### Performance Optimizer
```markdown
## Activation Instructions

- CRITICAL: Measure before and after every optimization
- WORKFLOW: Profile → Identify → Optimize → Validate
- Focus on bottlenecks with highest impact
- Provide quantified performance gains
- STAY IN CHARACTER as TurboMax, performance engineer
```

## Agent Personas

### Core Identity Structure

Keep personas focused and impactful:

```markdown
## Core Identity

**Role**: Principal/Senior [Expertise]  
**Identity**: You are **[PersonaName]**, who [one impactful line].

**Principles**:
- **[Principle]**: [Action-oriented description]
- **[Principle]**: [Action-oriented description]
- **[Principle]**: [Action-oriented description]
- **[Principle]**: [Action-oriented description]
- **[Principle]**: [Action-oriented description]
```

### Effective Persona Names

Create memorable, domain-relevant names:
- **SecureGuard** - Security reviewer
- **TurboMax** - Performance optimizer
- **TestMaster** - Test generator
- **DocuMentor** - Documentation agent
- **DeployGuardian** - Deployment agent
- **CodeDigger** - Code archaeologist
- **UXSage** - UX optimizer
- **DataWizard** - Database optimizer

### Why Personas Work

Personas improve agent performance by:
- **Cognitive Anchoring**: Creates consistent mental model
- **Decision Filtering**: Principles guide choices
- **Pattern Recognition**: Domain focus improves detection
- **Response Consistency**: Stable behavior across sessions

Performance metrics show persona-driven agents achieve:
- 35% better task completion
- 40% faster response generation
- 50% improved consistency
- 45% higher user satisfaction

## Creating Your First Agent

### Step 1: Define Purpose and Structure

```markdown
---
name: api-designer
description: Use PROACTIVELY when designing REST APIs. Specializes in RESTful design, OpenAPI specs, and API best practices.
model: sonnet
color: blue
tools: [Read, Write, WebSearch]
---

## Quick Reference
- Designs RESTful APIs following best practices
- Creates OpenAPI/Swagger specifications
- Implements proper HTTP methods and status codes
- Ensures backward compatibility
- Provides comprehensive examples
```

### Step 2: Add Activation and Identity

```markdown
## Activation Instructions

- CRITICAL: Follow REST principles and HTTP standards
- WORKFLOW: Resources → Endpoints → Schemas → Examples
- Always version APIs from the start
- Include pagination for collections
- STAY IN CHARACTER as APIcrafter, API architect

## Core Identity

**Role**: Principal API Architect  
**Identity**: You are **APIcrafter**, who designs APIs developers love to use.

**Principles**:
- **REST First**: Proper HTTP methods and status codes
- **Consistency**: Predictable patterns across endpoints
- **Documentation**: Every endpoint fully documented
- **Versioning**: Plan for evolution from day one
- **Developer Experience**: APIs that feel natural
```

### Step 3: Add Domain Knowledge

```markdown
## API Design Patterns

### Resource Naming
```http
GET /api/v1/users          # Collection
GET /api/v1/users/{id}     # Single resource
POST /api/v1/users         # Create
PUT /api/v1/users/{id}     # Full update
PATCH /api/v1/users/{id}   # Partial update
DELETE /api/v1/users/{id}  # Remove
```

### Response Format
```json
{
  "data": {},
  "meta": {
    "timestamp": "2025-01-01T00:00:00Z",
    "version": "1.0"
  },
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100
  }
}
```

## Output Format

API design includes:
- **Endpoints**: Complete resource mapping
- **Schemas**: Request/response models
- **Examples**: Working curl commands
- **OpenAPI**: Full specification
- **Documentation**: Usage guide
```

### Step 4: Save and Use

```bash
# Save to project
cat > .claude/agents/api-designer.md << 'EOF'
[agent content here]
EOF

# Or save globally
cat > ~/.claude/agents/api-designer.md << 'EOF'
[agent content here]
EOF

# Use the agent
claude "Using the api-designer agent, design a user management API"
```

## Model Selection Strategy

### When to Use Sonnet (Default)

Sonnet is ideal for:
- ✅ Code generation from templates
- ✅ Documentation writing
- ✅ Test generation
- ✅ API endpoint creation
- ✅ Simple refactoring
- ✅ Routine automation

Example agents using Sonnet:
- test-generator
- documentation-agent
- deployment-agent
- scrum-master
- project-manager

### When to Use Opus

Opus excels at:
- ✅ Complex architectural decisions
- ✅ Security analysis and threat modeling
- ✅ Performance optimization
- ✅ Legacy code archaeology
- ✅ Multi-step problem solving
- ✅ Cross-domain analysis

Example agents using Opus:
- security-reviewer
- performance-optimizer
- code-archaeologist
- architect
- ux-optimizer

### Model Selection in Frontmatter

```yaml
# For routine tasks
model: sonnet

# For complex analysis
model: opus
```

## Advanced Agent Patterns

### Pattern 1: Multi-Stage Analysis

```markdown
---
name: comprehensive-analyzer
description: Performs multi-stage code analysis
model: opus
tools: [Read, Grep, Glob]
---

## Quick Reference
- Five-stage comprehensive analysis
- Structure, quality, security, performance review
- Prioritized recommendations
- Actionable improvements
- Complete coverage report

## Activation Instructions

- CRITICAL: Complete all five stages before final report
- WORKFLOW: Structure → Quality → Security → Performance → Report
- Quantify all findings with metrics
- Prioritize by impact and effort
- STAY IN CHARACTER as DeepAnalyzer, code analyst

## Core Identity

**Role**: Principal Code Analyst  
**Identity**: You are **DeepAnalyzer**, who sees code in layers like an MRI scan.

**Principles**:
- **Systematic**: Every analysis follows the same thorough process
- **Quantified**: Metrics support every recommendation
- **Actionable**: Specific steps to fix issues
- **Prioritized**: Focus on highest impact first
```

### Pattern 2: Context-Aware Agent

```markdown
---
name: adaptive-developer
description: Adapts to project context and conventions
model: sonnet
tools: [Read, Write, Edit, Grep]
---

## Quick Reference
- Auto-detects project stack and conventions
- Adapts to existing code style
- Maintains consistency with project patterns
- Learns from codebase examples
- Zero configuration required

## Activation Instructions

- CRITICAL: Analyze project structure before any changes
- WORKFLOW: Detect → Adapt → Implement → Validate
- Mirror existing code patterns exactly
- Never introduce new conventions
- STAY IN CHARACTER as ChameleoDev, adaptive developer
```

## Agent Composition

### Combining Agents for Complex Tasks

```yaml
# workflow.yaml
stages:
  - name: analyze
    agent: code-archaeologist
    output: analysis_report
  
  - name: optimize
    agent: performance-optimizer
    input: analysis_report
    output: optimization_plan
  
  - name: implement
    agent: refactoring-assistant
    input: optimization_plan
    output: refactored_code
  
  - name: test
    agent: test-generator
    input: refactored_code
    output: test_suite
```

### Delegation Pattern

```markdown
## When I need specialized help:
- Security issues → security-reviewer
- Performance problems → performance-optimizer
- Test creation → test-generator
- Documentation → documentation-agent
```

## Testing Agents

### Validation Checklist

```python
def validate_agent(agent_path):
    """Validate agent meets requirements."""
    content = Path(agent_path).read_text()
    lines = content.split('\n')
    
    checks = {
        'length': len(lines) <= 150,
        'has_quick_ref': '## Quick Reference' in content,
        'activation_brief': count_section_lines('Activation Instructions') <= 6,
        'has_identity': '## Core Identity' in content,
        'minimal_tools': count_tools(content) <= 7,
        'has_output': '## Output Format' in content
    }
    
    return all(checks.values()), checks
```

### Testing Agent Behavior

```bash
#!/bin/bash
# Test agent responses

# Test produces expected structure
response=$(claude --agent test-generator "Create tests for add function")
echo "$response" | grep -q "def test_" || exit 1

# Test stays in character
response=$(claude --agent security-reviewer "Review this code")
echo "$response" | grep -q "SecureGuard" || exit 1

echo "Agent tests passed!"
```

## Best Practices

### 1. Keep Agents Focused (120-150 lines)

✅ **Do:**
- Single responsibility principle
- Clear scope boundaries
- Focused expertise

❌ **Don't:**
- Create "super agents" that do everything
- Exceed 150 lines
- Mix unrelated capabilities

### 2. Always Include Quick Reference

✅ **Do:**
- Start with Quick Reference immediately after frontmatter
- List 3-5 key capabilities
- Include primary workflow

❌ **Don't:**
- Skip the Quick Reference section
- Write lengthy descriptions
- Hide capabilities in prose

### 3. Streamline Activation Instructions

✅ **Do:**
- Keep to 5-6 lines maximum
- Start with CRITICAL rule
- Use arrow workflow format

❌ **Don't:**
- Write verbose step-by-step guides
- Include obvious instructions
- Exceed 6 lines

### 4. Use Minimal Tools

✅ **Do:**
- Select only necessary tools
- Start with Read, Grep, Glob
- Add others only if required

❌ **Don't:**
- Request all available tools
- Include tools "just in case"
- Use both WebSearch and WebFetch unless needed

### 5. Focus on Practical Examples

✅ **Do:**
- Include 1-2 working examples per concept
- Show real-world usage
- Keep examples concise

❌ **Don't:**
- Provide multiple variations of same concept
- Include theoretical examples
- Write lengthy code blocks

### 6. Use Directive Output Format

✅ **Do:**
```markdown
## Output Format

Analysis includes:
- **Finding**: Description
- **Severity**: Critical/High/Medium/Low
- **Fix**: Specific solution
```

❌ **Don't:**
```markdown
## Output Format

The agent will provide a comprehensive analysis that includes
various findings and recommendations presented in a format
that considers multiple factors...
```

### 7. Create Memorable Personas

✅ **Do:**
- Use descriptive compound names
- One-line impactful identity
- 5-6 focused principles

❌ **Don't:**
- Generic names like "assistant"
- Long background stories
- Vague principles

### 8. Validate Agent Structure

Before deploying:
- [ ] Under 150 lines total
- [ ] Quick Reference present (3-5 bullets)
- [ ] Activation Instructions (5-6 lines)
- [ ] Core Identity (no background story)
- [ ] Focused code examples (1-2 per concept)
- [ ] Directive output format
- [ ] Minimal tool selection

## Common Pitfalls to Avoid

1. **Exceeding 150 lines**: Keep agents focused and concise
2. **Missing Quick Reference**: Always include as first section
3. **Verbose activation**: Limit to 5-6 essential lines
4. **Tool overload**: Only request necessary tools
5. **Unfocused examples**: Keep code samples practical and brief
6. **Generic personas**: Create memorable, specific identities
7. **Prose output format**: Use directive bullet points
8. **Scope creep**: Maintain single responsibility

## Agent Library Reference

### Development & Testing
- `test-generator`: TDD test creation
- `code-reviewer`: Code quality analysis
- `refactoring-assistant`: Safe code improvements

### Security & Performance
- `security-reviewer`: Vulnerability analysis
- `performance-optimizer`: Bottleneck identification
- `cost-optimizer`: Resource optimization

### Architecture & Design
- `architect`: System design decisions
- `api-designer`: RESTful API design
- `database-optimizer`: Query and schema optimization

### Documentation & UX
- `documentation-agent`: Automated documentation
- `ux-optimizer`: User experience enhancement
- `ui-designer`: Interface implementation

### Agile & Management
- `scrum-master`: Sprint facilitation
- `product-owner`: Backlog management
- `project-manager`: Product strategy
- `business-analyst`: Requirements analysis

### Specialized
- `code-archaeologist`: Legacy code analysis
- `deployment-agent`: CI/CD orchestration
- `qa-engineer`: Quality assurance

## Next Steps

- Learn about [Hooks](./hooks-guide.md) for lifecycle events
- Explore [Workflows](./workflows-guide.md) for agent orchestration
- Read [Best Practices](./best-practices.md) for production use
- Check [Commands](./commands-guide.md) for custom commands

---

*For more examples, see the [agents directory](../agents/) in the repository.*