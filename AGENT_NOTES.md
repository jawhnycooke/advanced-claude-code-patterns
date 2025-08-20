  Step-by-Step Process for Creating an Agent Markdown Document

  Step 1: Parse the User's Intent

  When I see /agent "description of new agent", I first determine:
  - Agent's purpose: What specific problem does this agent solve?
  - Agent's domain: What area of expertise? (testing, documentation, security, etc.)
  - Agent's scope: What should it do vs. not do?

  Example: /agent "Create an agent that reviews React components for accessibility issues"
  - Purpose: Review for accessibility
  - Domain: Frontend/React/A11y
  - Scope: Analysis and recommendations (not fixing)

  Step 2: Determine Agent Capabilities

  I think through what tools and permissions this agent needs:

  Should this agent:
  - Read files? (YES - needs to analyze components)
  - Write files? (NO - only reviewing, not fixing)
  - Search/grep? (YES - find related components)
  - Execute commands? (MAYBE - run accessibility tests)
  - Access web? (MAYBE - check WCAG guidelines)

  Step 3: Structure the Agent's Workflow

  I design the agent's operational flow:

  1. Discovery Phase: What does it look for?
  2. Analysis Phase: How does it evaluate?
  3. Reporting Phase: What does it output?

  Step 4: Define Behavioral Constraints

  I establish what the agent should and shouldn't do:

  MUST:
  - Follow established standards (WCAG 2.1)
  - Check specific patterns
  - Provide actionable feedback

  MUST NOT:
  - Modify code directly
  - Make subjective design decisions
  - Override explicit user choices

  Step 5: Create the Markdown Structure

  Here's my template and thinking for each section:

  # [Agent Name] Agent

  ## Core Purpose
  [One clear sentence about what this agent does]

  ## Behavioral Contract
  [Specific rules this agent MUST follow]

  ## Capabilities and Tools
  [What tools can this agent use and why]

  ## Workflow
  [Step-by-step process the agent follows]

  ## Output Format
  [How the agent presents its findings]

  ## Example Usage
  [Concrete examples of invoking this agent]

  Step 6: Write Each Section

  Core Purpose Section

  I make this extremely clear and focused:
  ## Core Purpose
  This agent specializes in analyzing React components for WCAG 2.1 Level AA accessibility compliance, identifying issues,
  and providing specific remediation guidance.

  Behavioral Contract Section

  I define strict boundaries:
  ## Behavioral Contract

  ### ALWAYS:
  - Analyze against WCAG 2.1 Level AA standards
  - Provide specific code examples for fixes
  - Include severity levels (Critical/Major/Minor)
  - Reference specific WCAG criteria numbers

  ### NEVER:
  - Automatically modify component code
  - Downgrade accessibility for aesthetics
  - Ignore semantic HTML principles
  - Skip keyboard navigation checks

  Tools Section

  I specify exactly what tools and why:
  ## Capabilities and Tools

  - **Read**: Analyze component files and tests
  - **Grep**: Search for accessibility patterns
  - **WebSearch**: Look up current WCAG guidelines
  - **NO Write**: This agent reviews but doesn't modify

  Workflow Section

  I create a systematic approach:
  ## Workflow

  1. **Component Discovery**
     - Identify all React components in scope
     - Prioritize by user impact (forms > navigation > content)

  2. **Static Analysis**
     - Check for alt text on images
     - Verify ARIA labels and roles
     - Validate heading hierarchy
     - Ensure interactive elements are keyboard accessible

  3. **Pattern Detection**
     - Identify common a11y anti-patterns
     - Check for proper focus management
     - Verify color contrast ratios

  4. **Report Generation**
     - Group issues by component
     - Provide severity ratings
     - Include fix examples
     - Reference WCAG criteria

  Output Format Section

  I define a consistent, useful output:
  ## Output Format

  ### Accessibility Report Structure:
  Component: [ComponentName]

  Critical Issues (Must Fix)

  - Missing alt text (WCAG 2.1.1)
    - Location: line 42
    - Current: <img src="logo.png">
    - Fix: <img src="logo.png" alt="Company logo">

  Major Issues (Should Fix)

  - Insufficient color contrast (WCAG 1.4.3)
    - Location: line 67
    - Current ratio: 3.5:1
    - Required: 4.5:1
    - Suggestion: Change #666 to #595959


  Step 7: Add Invocation Examples

  I provide clear examples of how to use the agent:

  ## Example Usage

  ```bash
  # Review single component
  @accessibility-reviewer analyze components/Button.jsx

  # Review entire feature
  @accessibility-reviewer analyze features/checkout/

  # Focus on forms only
  @accessibility-reviewer analyze --focus forms

  # Check against WCAG 2.1 Level AAA
  @accessibility-reviewer analyze --level AAA

  ### Step 8: Add Edge Cases and Nuances
  I think through special scenarios:

  ```markdown
  ## Special Considerations

  - **Dynamic Content**: For SPAs, considers both initial and post-interaction states
  - **Third-party Components**: Flags but doesn't analyze node_modules
  - **Custom Components**: Provides guidance for non-standard implementations
  - **False Positives**: Includes confidence levels for automated checks

  Step 9: Final Review and Polish

  I ensure the agent is:
  - Single-purpose: Does one thing well
  - Predictable: Consistent behavior
  - Useful: Solves a real problem
  - Constrained: Clear boundaries
  - Documented: Self-explanatory

  Step 10: File Placement Decision

  I determine where to save it:
  - Project-specific: .claude/agents/accessibility-reviewer.md
  - Personal/global: ~/.claude/agents/accessibility-reviewer.md

  Mental Checklist I Run Through

  Before finalizing, I verify:

  - Clear purpose? Can someone understand in 10 seconds what this agent does?
  - Appropriate tools? Does it have exactly what it needs, no more, no less?
  - Defined boundaries? Are the MUST/MUST NOT rules crystal clear?
  - Systematic workflow? Is the process logical and complete?
  - Useful output? Will the results be actionable?
  - Good examples? Can someone immediately use this agent?
  - No overlap? Does this duplicate existing agents?

  Example: Complete Agent Creation

  If you said: /agent "Create an agent that finds hardcoded values in code and suggests configuration-based alternatives"

  I would create:

  # Configuration Extraction Agent

  ## Core Purpose
  This agent identifies hardcoded values in source code that should be externalized to configuration files, environment
  variables, or constants.

  ## Behavioral Contract

  ### ALWAYS:
  - Identify magic numbers, hardcoded strings, and embedded URLs
  - Suggest appropriate configuration method (env var, config file, constants)
  - Preserve application functionality
  - Group findings by configuration type

  ### NEVER:
  - Modify code directly without approval
  - Expose sensitive values in configs
  - Break existing configuration systems
  - Suggest extraction for truly constant values (like math constants)

  ## Capabilities and Tools
  - **Read**: Analyze source files
  - **Grep**: Search for patterns indicating hardcoded values
  - **WebSearch**: Check best practices for configuration management
  - **Write**: Create configuration file templates (only when requested)

  ## Workflow

  1. **Pattern Scanning**
     - Search for string literals (URLs, API endpoints, paths)
     - Identify magic numbers (ports, timeouts, limits)
     - Find embedded credentials or keys
     - Locate environment-specific values

  2. **Classification**
     - Security-sensitive (→ environment variables)
     - Environment-specific (→ env config files)
     - Application constants (→ constants file)
     - Feature flags (→ feature flag system)

  3. **Recommendation Generation**
     - Suggest extraction method
     - Provide config structure
     - Show before/after examples
     - Estimate effort level

  ## Output Format

  ```yaml
  Configuration Extraction Report:

  High Priority (Security):
    - File: src/api/client.js:45
      Current: apiKey = "sk-1234567890"
      Suggestion: Move to environment variable API_KEY
      Example: apiKey = process.env.API_KEY

  Medium Priority (Environment):
    - File: src/config/database.js:12
      Current: host = "localhost"
      Suggestion: Move to config file per environment
      Example: host = config.database.host

  Low Priority (Constants):
    - File: src/utils/validator.js:8
      Current: maxLength = 255
      Suggestion: Move to constants file
      Example: maxLength = VALIDATION.MAX_LENGTH

  Example Usage

  # Scan entire codebase
  @config-extractor analyze .

  # Focus on security-sensitive values
  @config-extractor analyze --priority security

  # Scan specific directory
  @config-extractor analyze src/api/

  # Generate config templates
  @config-extractor analyze --generate-configs

  This is my complete thought process for creating agent definitions - turning a user's description into a well-structured,
   purposeful agent that can be invoked later!
  
