# Agent Configuration Reference

## Frontmatter Configuration

| Field | Description | Options | Required |
|-------|-------------|---------|----------|
| `name` | Agent identifier (kebab-case) | Any string | Yes |
| `description` | Purpose with trigger phrase | Any string | Yes |
| `model` | LLM model selection | `sonnet`, `opus` | Yes |
| `tools` | Minimal necessary tools | Array of tool names | Yes |
| `color` | UI styling color | Color name | No |

## Model Selection

### Sonnet Configuration
```yaml
model: sonnet
```

Use for:
- ✅ Code generation from templates
- ✅ Documentation writing
- ✅ Test generation
- ✅ API endpoint creation
- ✅ Simple refactoring
- ✅ Routine automation

### Opus Configuration
```yaml
model: opus
```

Use for:
- ✅ Complex architectural decisions
- ✅ Security analysis and threat modeling
- ✅ Performance optimization
- ✅ Legacy code archaeology
- ✅ Multi-step problem solving
- ✅ Cross-domain analysis

## Tools Configuration

### Minimal Tool Set (Recommended)
```yaml
tools: [Read, Write, Grep]
```

### Available Tools
- `Read` - File reading
- `Write` - File creation/overwriting
- `Edit` - File editing
- `MultiEdit` - Multiple file edits
- `Grep` - Text search
- `Glob` - File pattern matching
- `LS` - Directory listing
- `WebSearch` - Web search
- `WebFetch` - Web page fetching

### Tool Selection Guidelines

✅ **Do:**
- Select only necessary tools
- Start with Read, Grep, Glob
- Add others only if required

❌ **Don't:**
- Request all available tools
- Include tools "just in case"
- Use both WebSearch and WebFetch unless needed

### Example Tool Configurations

#### Code Analysis Agent
```yaml
tools: [Read, Grep, Glob]
```

#### Documentation Agent
```yaml
tools: [Read, Write, Edit]
```

#### API Design Agent
```yaml
tools: [Read, Write, WebSearch]
```

#### Deployment Agent
```yaml
tools: [Read, Write, Edit, Grep]
```

## Color Configuration

Optional UI styling:

```yaml
color: blue      # Professional
color: green     # Success/optimization
color: red       # Security/critical
color: purple    # Architecture/design
color: orange    # Performance/speed
color: yellow    # Testing/quality
```

## Complete Configuration Example

```yaml
---
name: api-designer
description: Use PROACTIVELY when designing REST APIs. Specializes in RESTful design, OpenAPI specs, and API best practices.
model: sonnet
color: blue
tools: [Read, Write, WebSearch]
---
```