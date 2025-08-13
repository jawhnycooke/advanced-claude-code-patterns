# Model Selection Guide for Claude Code Agents

## Overview

Claude Code agents now support model selection, allowing developers to optimize for performance and cost. Each agent can be configured to use either "sonnet" (default) or "opus" based on task complexity.

## Available Models

### Sonnet (Default)
- **Best for**: Standard tasks, quick operations, routine automation
- **Performance**: Fast response times
- **Cost**: Standard pricing
- **Token Limits**: Standard context window

### Opus
- **Best for**: Complex analysis, deep reasoning, critical decisions
- **Performance**: Highest quality outputs
- **Cost**: Premium pricing
- **Token Limits**: Extended context window

## Usage Guidelines

### When to Use Sonnet (Default)

Use Sonnet for most agent tasks, including:

1. **Simple Operations**
   - Running tests
   - Executing commands
   - File operations
   - Basic validation

2. **Routine Automation**
   - Pre-commit hooks
   - Formatting checks
   - Dependency updates
   - Build processes

3. **Standard Analysis**
   - Basic code review
   - Simple refactoring
   - Documentation updates
   - Log parsing

### When to Use Opus

Reserve Opus for demanding tasks that require:

1. **Complex Analysis**
   - Security vulnerability assessment
   - Performance optimization
   - Architecture decisions
   - Code quality deep dives

2. **Critical Operations**
   - Production deployments
   - Database migrations
   - Breaking change analysis
   - Incident response

3. **Advanced Reasoning**
   - Legacy code understanding
   - Complex refactoring
   - Algorithm optimization
   - Design pattern selection

## Configuration Examples

### Basic Agent with Sonnet (Default)

```yaml
agents:
  test-runner:
    name: "test-runner"
    description: "Run test suites"
    model: "sonnet"  # Can be omitted as it's the default
    tools: ["Bash"]
    system_prompt: "You are a test execution specialist."
```

### Complex Agent with Opus

```yaml
agents:
  security-reviewer:
    name: "security-reviewer"
    description: "Comprehensive security analysis"
    model: "opus"  # Explicitly use Opus for complex analysis
    tools: ["Read", "Grep", "WebSearch"]
    system_prompt: |
      You are a security expert performing comprehensive vulnerability analysis.
      Consider OWASP Top 10, CVE databases, and industry best practices.
```

## Agent-Specific Recommendations

### Use Sonnet for These Agents
- **test-generator**: Basic test creation
- **doc-updater**: README maintenance
- **format-checker**: Code style validation
- **dependency-checker**: Version updates
- **build-runner**: CI/CD execution

### Use Opus for These Agents
- **security-reviewer**: Vulnerability analysis
- **performance-optimizer**: Bottleneck identification
- **code-archaeologist**: Legacy code analysis
- **architecture-advisor**: Design decisions
- **incident-responder**: Production issues

## Dynamic Model Selection

Agents can dynamically select models based on context:

```python
from base import AgentConfig, BaseAgent

class AdaptiveAgent(BaseAgent):
    def __init__(self):
        # Start with Sonnet for initial analysis
        config = AgentConfig(
            name="adaptive-agent",
            description="Adapts model based on complexity",
            model="sonnet"
        )
        super().__init__(config)
    
    async def execute(self, context):
        # Assess task complexity
        if self._is_complex_task(context):
            # Switch to Opus for complex tasks
            self.config.model = "opus"
            logger.info("Switching to Opus for complex analysis")
        
        # Execute task with selected model
        return await self._run_analysis(context)
```

## Cost Optimization Strategies

1. **Default to Sonnet**: Always start with Sonnet unless you know the task requires Opus

2. **Progressive Enhancement**: Use Sonnet for initial analysis, then Opus only for deep dives

3. **Task-Based Selection**: Map specific task types to appropriate models

4. **Batch Processing**: Group simple tasks for Sonnet, reserve Opus for critical paths

5. **Caching Results**: Store Opus results to avoid repeated expensive calls

## Performance Metrics

### Typical Response Times
- **Sonnet**: 1-3 seconds for most operations
- **Opus**: 3-8 seconds for complex analysis

### Context Window Usage
- **Sonnet**: Efficient for files under 10K lines
- **Opus**: Can handle entire codebases effectively

### Quality Differences
- **Sonnet**: 95% accuracy for standard tasks
- **Opus**: 99% accuracy for complex reasoning

## Best Practices

1. **Document Model Choice**: Always comment why Opus is chosen
   ```yaml
   model: "opus"  # Required for multi-file security analysis
   ```

2. **Monitor Usage**: Track which agents use Opus most frequently

3. **Regular Review**: Periodically assess if Opus is still needed

4. **User Configuration**: Allow users to override model selection
   ```bash
   claude-agent run security-check --model sonnet  # Override to save costs
   ```

5. **Fallback Strategy**: Implement graceful degradation
   ```python
   try:
       result = await run_with_opus()
   except RateLimitError:
       result = await run_with_sonnet()  # Fallback to Sonnet
   ```

## Migration Guide

### Updating Existing Agents

1. **Review Current Agents**: Identify which agents would benefit from Opus

2. **Add Model Parameter**: Update agent configurations
   ```yaml
   # Before
   agents:
     reviewer:
       name: "reviewer"
       description: "Code review"
   
   # After
   agents:
     reviewer:
       name: "reviewer"
       description: "Code review"
       model: "opus"  # Explicitly set for complex reviews
   ```

3. **Test Performance**: Compare outputs between models

4. **Measure Impact**: Track improvements in accuracy and completeness

## Conclusion

The model parameter provides fine-grained control over agent performance and cost. Use Sonnet by default and reserve Opus for tasks where the additional capabilities justify the increased cost. Regular monitoring and adjustment ensure optimal resource utilization.