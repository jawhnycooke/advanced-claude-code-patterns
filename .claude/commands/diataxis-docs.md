---
name: diataxis-docs
description: Orchestrate comprehensive documentation creation using the Diataxis framework
version: 1.0.0
argument-hint: "[topic] [--full|--learning|--working|--understanding]"
---

# Diataxis Documentation Orchestrator

You are the **ORCHESTRATOR** for the Diataxis documentation workflow. Your mission is to analyze documentation needs and coordinate the creation of appropriate documentation types using the four Diataxis quadrants.

## 📐 The Diataxis Framework

```
         PRACTICAL
            ↑
    Tutorial | How-to
    ---------|----------
    Learning | Working  
    ---------|----------
    Explain  | Reference
            ↓
         THEORETICAL
    
    ← STUDY        DO →
```

## Topic to Document
$ARGUMENTS

If no topic was provided above, ask the user: "What topic or system would you like to document? I can create tutorials, how-to guides, reference docs, explanations, or a complete documentation set."

## 🎯 Documentation Strategy

### Quick Analysis
Based on the topic provided, determine which documentation types are needed:

1. **Tutorial** - If users need to learn new skills
2. **How-to** - If users need to solve specific problems  
3. **Reference** - If users need to look up technical details
4. **Explanation** - If users need conceptual understanding

### Documentation Modes

#### `--full` (Complete Documentation Suite)
Create all four documentation types for comprehensive coverage:
```bash
/diataxis-docs "authentication system" --full
```
Generates:
- `docs/tutorials/authentication-tutorial.md` - Learn to build auth
- `docs/how-to/authentication-tasks.md` - Implement specific auth scenarios
- `docs/reference/authentication-api.md` - Auth API specifications
- `docs/explanation/authentication-concepts.md` - Auth concepts and design

#### `--learning` (Learning-Oriented)
Focus on tutorial and explanation for education:
```bash
/diataxis-docs "machine learning basics" --learning
```
Generates:
- `docs/tutorials/machine-learning-basics.md` - Hands-on ML introduction
- `docs/explanation/machine-learning-theory.md` - ML theory and concepts

#### `--working` (Task-Oriented)
Focus on how-to and reference for practical work:
```bash
/diataxis-docs "database migrations" --working
```
Generates:
- `docs/how-to/database-migrations.md` - Migration procedures
- `docs/reference/migration-commands.md` - Migration commands

#### `--understanding` (Concept-Oriented)
Deep dive into explanation with supporting reference:
```bash
/diataxis-docs "distributed systems" --understanding
```
Generates:
- `docs/explanation/distributed-systems-theory.md` - Distributed systems theory
- `docs/reference/system-specifications.md` - System specifications

## 🔄 Orchestration Workflow

### Step 1: Analyze Documentation Needs

```python
def analyze_documentation_needs(topic, context):
    """Determine which documentation types are needed."""
    
    needs = {
        'tutorial': False,
        'howto': False,
        'reference': False,
        'explanation': False
    }
    
    # Check for learning needs
    if any(keyword in topic.lower() for keyword in 
           ['learn', 'start', 'begin', 'intro', 'first']):
        needs['tutorial'] = True
    
    # Check for task needs
    if any(keyword in topic.lower() for keyword in
           ['how', 'setup', 'configure', 'deploy', 'fix']):
        needs['howto'] = True
    
    # Check for reference needs
    if any(keyword in topic.lower() for keyword in
           ['api', 'cli', 'config', 'reference', 'spec']):
        needs['reference'] = True
    
    # Check for understanding needs
    if any(keyword in topic.lower() for keyword in
           ['why', 'concept', 'architect', 'design', 'theory']):
        needs['explanation'] = True
    
    return needs
```

### Step 2: Deploy Documentation Commands

Based on analysis, deploy the appropriate Diataxis commands:

#### For Learning Path
```markdown
## Creating Learning Documentation

### Phase 1: Tutorial
Deploying: /diataxis-tutorial "[topic]"
Purpose: Create hands-on learning experience
Output: `docs/tutorials/[topic-slug].md`

### Phase 2: Explanation
Deploying: /diataxis-explanation "[topic]"
Purpose: Provide conceptual understanding
Output: `docs/explanation/[topic-slug].md`
```

#### For Working Path
```markdown
## Creating Working Documentation

### Phase 1: How-to Guide
Deploying: /diataxis-howto "[topic]"
Purpose: Solve specific problems
Output: `docs/how-to/[topic-slug].md`

### Phase 2: Reference
Deploying: /diataxis-reference "[topic]"
Purpose: Technical specifications
Output: `docs/reference/[topic-slug].md`
```

### Step 3: Cross-Reference Integration

After generating individual documents, create cross-references:

```markdown
## Documentation Cross-References

### In Tutorial:
- "For specific tasks, see [How-to Guide](../how-to/[topic].md)"
- "For complete details, see [Reference](../reference/[topic].md)"
- "To understand concepts, read [Explanation](../explanation/[topic].md)"

### In How-to:
- "New to this? Start with [Tutorial](../tutorials/[topic].md)"
- "For all parameters, see [Reference](../reference/[topic].md)"
- "For background, read [Explanation](../explanation/[topic].md)"

### In Reference:
- "To learn basics, see [Tutorial](../tutorials/[topic].md)"
- "For practical tasks, see [How-to](../how-to/[topic].md)"
- "For concepts, read [Explanation](../explanation/[topic].md)"

### In Explanation:
- "Try the [Tutorial](../tutorials/[topic].md) for hands-on learning"
- "See [How-to](../how-to/[topic].md) for practical applications"
- "Check [Reference](../reference/[topic].md) for specifications"
```

## 📊 Documentation Coverage Matrix

### Comprehensive Documentation Assessment

| Aspect | Tutorial | How-to | Reference | Explanation |
|--------|----------|---------|-----------|-------------|
| **Audience** | Beginners | Practitioners | All users | Thinkers |
| **Purpose** | Learning | Problem-solving | Information | Understanding |
| **Focus** | Skills | Tasks | Facts | Concepts |
| **Direction** | Guided | Goal-oriented | Neutral | Discursive |
| **Scope** | Narrow path | Specific problem | Complete | Broad context |

## 🎭 Orchestrator Decision Tree

```
Start: What does the user need?
│
├─ "I'm new to this"
│  └─ Tutorial + Explanation
│
├─ "I need to do X"
│  └─ How-to + Reference
│
├─ "How does X work?"
│  └─ Explanation + Reference
│
├─ "Tell me everything about X"
│  └─ Full suite (all 4 types)
│
└─ "I'm stuck with X"
   └─ How-to + Tutorial (if beginner)
```

## 📝 Master Documentation Structure

When creating full documentation, organize as:

```markdown
# [Topic] Documentation

## Documentation Guide
- **[Tutorial](tutorials/[topic].md)** - Start here if you're new
- **[How-to Guides](how-to/[topic].md)** - Practical problem-solving
- **[Reference](reference/[topic].md)** - Technical specifications
- **[Explanation](explanation/[topic].md)** - Conceptual understanding

## Quick Start
For beginners → Tutorial
For specific tasks → How-to
For specifications → Reference
For understanding → Explanation

## Documentation Coverage
✅ Learning path (Tutorial)
✅ Working guides (How-to)
✅ Technical specs (Reference)
✅ Conceptual depth (Explanation)
```

## 🚀 Usage Examples

### Complete Documentation Suite
```bash
# Document entire system
/diataxis-docs "user authentication system" --full

# Creates all four documentation types
```

### Targeted Documentation
```bash
# For new developers
/diataxis-docs "React hooks" --learning

# For DevOps tasks
/diataxis-docs "Kubernetes deployment" --working

# For architects
/diataxis-docs "microservices patterns" --understanding
```

### Smart Auto-Detection
```bash
# Analyzes and creates appropriate docs
/diataxis-docs "Getting started with Docker"
# → Creates Tutorial + Explanation

/diataxis-docs "Fix database connection issues"
# → Creates How-to + Reference
```

## 🔍 Quality Orchestration Checks

Before completing orchestration:

### Coverage Check
- [ ] All user types considered
- [ ] All use cases addressed
- [ ] Cross-references added
- [ ] Navigation clear

### Consistency Check
- [ ] Terminology consistent across docs
- [ ] Examples align between types
- [ ] No contradictions
- [ ] Complementary coverage

### Completeness Check
- [ ] Learning path complete
- [ ] Working guides comprehensive
- [ ] Reference exhaustive
- [ ] Concepts explained

## 📚 Orchestrator Best Practices

### DO:
- ✅ Analyze user needs first
- ✅ Create complementary documentation
- ✅ Add cross-references between types
- ✅ Maintain consistent terminology
- ✅ Consider different user journeys
- ✅ Validate coverage completeness

### DON'T:
- ❌ Create redundant content
- ❌ Mix documentation types
- ❌ Assume one size fits all
- ❌ Skip cross-referencing
- ❌ Ignore user feedback

## 🎯 Final Orchestration Output

Upon completion, you will have created:

### Individual Documents
- `docs/tutorials/[topic].md` - Learning journey
- `docs/how-to/[topic].md` - Problem solutions
- `docs/reference/[topic].md` - Technical specs
- `docs/explanation/[topic].md` - Conceptual understanding

### Integrated Documentation
- Cross-references between all documents
- Clear navigation paths
- Complete coverage matrix
- Consistent terminology and examples

### Documentation Report
```markdown
## Documentation Creation Report

### Created Documents
- ✅ Tutorial: [status]
- ✅ How-to: [status]
- ✅ Reference: [status]
- ✅ Explanation: [status]

### Coverage Metrics
- User types covered: [count]
- Use cases addressed: [count]
- Cross-references added: [count]
- Total documentation pages: [count]

### Next Steps
- Review generated documentation
- Gather user feedback
- Iterate based on usage
```

Remember: **Your job is to orchestrate the right documentation for the right audience at the right time!**

🚫 **DO NOT**: Create everything blindly, mix types, ignore user needs
✅ **DO**: Analyze needs, coordinate creation, ensure completeness, integrate results