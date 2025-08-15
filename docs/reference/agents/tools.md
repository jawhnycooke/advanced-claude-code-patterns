# Agent Tools Reference

## Available Tools

### File Operations

#### Read
Read file contents.
```yaml
tools: [Read]
```
Use for: Analyzing existing code, configuration files, documentation

#### Write
Create or overwrite files.
```yaml
tools: [Write]
```
Use for: Creating new files, templates, documentation

#### Edit
Edit existing files with find-and-replace.
```yaml
tools: [Edit]
```
Use for: Making targeted changes to existing code

#### MultiEdit
Perform multiple edits on a single file.
```yaml
tools: [MultiEdit]
```
Use for: Complex refactoring with multiple changes

### Search Operations

#### Grep
Search text within files using regex patterns.
```yaml
tools: [Grep]
```
Use for: Finding code patterns, analyzing codebases, searching content

#### Glob
Find files by name patterns.
```yaml
tools: [Glob]
```
Use for: Discovering files, analyzing project structure

#### LS
List directory contents.
```yaml
tools: [LS]
```
Use for: Exploring project structure, finding files

### Web Operations

#### WebSearch
Search the web for information.
```yaml
tools: [WebSearch]
```
Use for: Finding documentation, best practices, library information

#### WebFetch
Fetch content from web pages.
```yaml
tools: [WebFetch]
```
Use for: Retrieving specific documentation, API specs

## Tool Selection by Agent Type

### Code Analysis Agents
```yaml
tools: [Read, Grep, Glob]
```
- `Read`: Examine source files
- `Grep`: Search for patterns
- `Glob`: Find relevant files

### Documentation Agents
```yaml
tools: [Read, Write, Edit]
```
- `Read`: Analyze existing code
- `Write`: Create documentation
- `Edit`: Update existing docs

### Refactoring Agents
```yaml
tools: [Read, Edit, MultiEdit, Grep]
```
- `Read`: Understand current code
- `Edit/MultiEdit`: Make changes
- `Grep`: Find all occurrences

### API Design Agents
```yaml
tools: [Read, Write, WebSearch]
```
- `Read`: Analyze requirements
- `Write`: Create specifications
- `WebSearch`: Research best practices

### Security Agents
```yaml
tools: [Read, Grep, Glob]
```
- `Read`: Examine code for vulnerabilities
- `Grep`: Search for security patterns
- `Glob`: Find security-relevant files

### Testing Agents
```yaml
tools: [Read, Write, Edit, Grep]
```
- `Read`: Understand code to test
- `Write`: Create test files
- `Edit`: Update existing tests
- `Grep`: Find test patterns

### Deployment Agents
```yaml
tools: [Read, Write, Edit, Grep, Glob]
```
- `Read`: Examine configuration
- `Write`: Create deployment files
- `Edit`: Update configurations
- `Grep`: Find deployment patterns
- `Glob`: Locate config files

## Tool Usage Guidelines

### Performance Considerations
- More tools = slower initialization
- Only include tools the agent will use
- Prefer specific tools over general ones

### Security Considerations
- Web tools can introduce risks
- File write tools need careful validation
- Limit tools to minimum necessary set

### Best Practices
1. Start with Read + Grep + Glob for analysis
2. Add Write/Edit only if agent creates/modifies files
3. Include Web tools only for research-based agents
4. Never include tools "just in case"
5. Test agent behavior with minimal tool set first

## Common Tool Combinations

### Read-Only Analysis
```yaml
tools: [Read, Grep, Glob]
```

### Basic Development
```yaml
tools: [Read, Write, Edit]
```

### Advanced Development
```yaml
tools: [Read, Write, Edit, MultiEdit, Grep]
```

### Research and Development
```yaml
tools: [Read, Write, WebSearch, Grep]
```

### Full Development Suite
```yaml
tools: [Read, Write, Edit, MultiEdit, Grep, Glob, LS]
```

## Tool Limitations

### File Operations
- Write overwrites entire files
- Edit requires exact string matches
- MultiEdit applies changes sequentially

### Search Operations
- Grep uses regex syntax
- Glob supports standard patterns
- LS only lists immediate directory contents

### Web Operations
- WebSearch returns limited results
- WebFetch may fail on protected content
- Both require internet connectivity