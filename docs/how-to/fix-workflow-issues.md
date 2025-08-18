# How to Fix Workflow Issues

Task-focused solutions for workflow failures and execution problems.

## Prerequisites
- Workflow files exist in `.claude/workflows/`
- Basic understanding of YAML workflow syntax
- Access to workflow execution logs

## Fix: Workflow Stuck in Pending

**Quick Diagnosis:**
```bash
claude workflow status [workflow-id]
claude workflow logs [workflow-id]
```

**Steps:**
1. **Identify the blocking stage:**
   ```bash
   # Check current status
   claude workflow status workflow-id --verbose
   ```

2. **Add timeout to problematic stage:**
   ```yaml
   stages:
     - name: stuck_stage
       timeout: 300  # 5 minutes
       on_timeout: skip  # Options: skip, fail, retry
   ```

3. **Force workflow progression:**
   ```bash
   # Skip current stage
   claude workflow continue [workflow-id] --skip-current
   
   # Or restart from specific stage
   claude workflow restart [workflow-id] --from-stage [stage-name]
   ```

## Fix: Dependency Failures Blocking Workflow

**Problem:** Stage dependencies not met, workflow can't progress.

**Error Example:**
```
Error: Stage 'deploy' depends on 'test' which failed
```

**Steps:**
1. **Add conditional dependencies:**
   ```yaml
   stages:
     - name: deploy
       depends_on: 
         - stage: test
           condition: success  # Options: success, complete, skipped
   ```

2. **Allow partial success:**
   ```yaml
   stages:
     - name: deploy
       depends_on: [test]
       continue_on_dependency_failure: true
       when: ${test.success_rate} > 0.8
   ```

3. **Add fallback path:**
   ```yaml
   stages:
     - name: deploy
       depends_on: [test]
       on_dependency_failure:
         - name: manual_review
           type: approval
           message: "Tests failed. Approve manual deployment?"
   ```

## Fix: Lost Workflow State

**Problem:** Workflow restarts from beginning, previous progress lost.

**Steps:**
1. **Enable state persistence:**
   ```yaml
   # Add to workflow config
   state:
     backend: redis  # Options: redis, file, database
     ttl: 86400      # 24 hours
     checkpoint_frequency: after_each_task
   ```

2. **Recover from checkpoint:**
   ```bash
   claude workflow recover [workflow-id] --from-checkpoint
   ```

3. **Manual state recovery:**
   ```python
   # Recover workflow state
   import json
   
   state_file = ".claude/workflow-state.json"
   with open(state_file, 'r') as f:
       state = json.load(f)
   
   # Update state
   state["current_stage"] = "deployment"
   state["completed_tasks"] = ["test", "build"]
   
   with open(state_file, 'w') as f:
       json.dump(state, f)
   ```

## Fix: Circular Dependencies

**Problem:** Workflow stages have circular dependencies.

**Error Example:**
```
Error: Workflow cycle detected: stage_a -> stage_b -> stage_a
```

**Steps:**
1. **Map dependency graph:**
   ```bash
   # Visualize dependencies
   claude workflow graph [workflow-id]
   ```

2. **Break circular dependencies:**
   ```yaml
   # Before (circular)
   stages:
     - name: stage_a
       depends_on: [stage_b]
     - name: stage_b
       depends_on: [stage_a]
   
   # After (fixed)
   stages:
     - name: stage_setup
       # No dependencies
     - name: stage_a
       depends_on: [stage_setup]
     - name: stage_b
       depends_on: [stage_setup]
   ```

3. **Use conditional execution instead:**
   ```yaml
   stages:
     - name: conditional_stage
       when: ${previous_stage.status} == 'success'
       # Instead of depends_on
   ```

## Fix: Workflow Resource Exhaustion

**Problem:** Workflow consuming too much memory/CPU.

**Steps:**
1. **Set resource limits:**
   ```yaml
   resources:
     limits:
       memory: 2Gi
       cpu: 2
       timeout: 3600  # 1 hour
   ```

2. **Limit concurrent operations:**
   ```yaml
   parallel:
     max_workers: 4        # Reduce from default
     chunk_size: 10        # Process in smaller batches
     memory_limit: 1Gi     # Per worker
   ```

3. **Optimize stage execution:**
   ```yaml
   stages:
     - name: optimized_stage
       cache: true         # Cache results
       incremental: true   # Only process changes
       batch_size: 50      # Process in batches
   ```

## Fix: Workflow Validation Errors

**Problem:** Workflow YAML has syntax or logic errors.

**Steps:**
1. **Validate YAML syntax:**
   ```bash
   # Check syntax
   yamllint .claude/workflows/my-workflow.yaml
   
   # Validate workflow logic
   claude workflow validate my-workflow.yaml
   ```

2. **Common YAML fixes:**
   ```yaml
   # ✅ Correct indentation
   stages:
     - name: test
       commands:
         - pytest
   
   # ❌ Wrong indentation
   stages:
   - name: test
     commands:
     - pytest
   ```

3. **Fix logic errors:**
   ```yaml
   # ✅ Valid stage reference
   stages:
     - name: test
     - name: deploy
       depends_on: [test]  # Reference existing stage
   
   # ❌ Invalid reference
   stages:
     - name: test
     - name: deploy
       depends_on: [build]  # 'build' stage doesn't exist
   ```

## Fix: Environment Variable Issues

**Problem:** Workflow can't access required environment variables.

**Steps:**
1. **Check variable availability:**
   ```bash
   # Test in workflow context
   claude workflow env [workflow-id]
   ```

2. **Set variables in workflow:**
   ```yaml
   environment:
     GITHUB_TOKEN: ${env:GITHUB_TOKEN}
     DATABASE_URL: ${secret:db_url}
     NODE_ENV: production
   ```

3. **Use fallback values:**
   ```yaml
   environment:
     API_URL: ${env:API_URL:https://api.default.com}
     TIMEOUT: ${env:TIMEOUT:30}
   ```

## Fix: Workflow Performance Issues

**Problem:** Workflow running slowly or timing out.

**Steps:**
1. **Profile workflow execution:**
   ```bash
   claude workflow profile [workflow-id]
   ```

2. **Optimize stage ordering:**
   ```yaml
   # Run independent stages in parallel
   stages:
     - name: lint
       parallel: true
     - name: type_check
       parallel: true
     - name: test
       depends_on: [lint, type_check]
   ```

3. **Use caching:**
   ```yaml
   stages:
     - name: build
       cache:
         key: ${checksum:package.json}
         paths: [node_modules/]
   ```

## Emergency Recovery

**Complete workflow reset:**
```bash
# Stop all workflows
claude workflow stop --all

# Clear workflow state
claude workflow clear-state

# Restart critical workflows
claude workflow start critical-workflow
```

**Backup and restore:**
```bash
# Backup workflow definitions
cp -r .claude/workflows/ .claude/workflows.backup/

# Restore from backup
cp .claude/workflows.backup/working-workflow.yaml .claude/workflows/
```

## Troubleshooting Commands

**Status and logs:**
```bash
# Check all workflows
claude workflow list

# Detailed status
claude workflow status [workflow-id] --verbose

# View logs
claude workflow logs [workflow-id] --tail -f

# Debug mode
claude workflow run [workflow-id] --debug
```

**Validation and testing:**
```bash
# Validate workflow file
claude workflow validate workflow-file.yaml

# Dry run
claude workflow run [workflow-id] --dry-run

# Test single stage
claude workflow test-stage [workflow-id] [stage-name]
```

## When to Get Help

Contact support if:
- Workflow validation passes but execution fails
- State corruption occurs repeatedly
- Performance issues persist after optimization
- Dependencies resolve correctly but workflow still fails

Include in your report:
- Workflow YAML file
- Execution logs
- Output of `claude workflow status --verbose`
- Environment details where workflow runs