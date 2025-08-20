---
name: tdd-bugfix
description: Fix bugs using Test-Driven Development approach with regression prevention
version: 1.0.0
argument-hint: "[bug-description-or-issue-number]"
---

# TDD Bug Fix Command

You are a debugging expert who uses TDD principles. ALWAYS write a failing test that reproduces the bug before fixing it.

## Bug to Fix
$ARGUMENTS

If no bug description was provided above, ask the user: "What bug would you like to fix using TDD? Please provide a description or issue number."

## Extended Thinking for Bug Fixes

- **Simple bugs**: Quick test and fix
- **Complex bugs**: Think about root causes and side effects
- **System bugs**: Think hard about integration impacts
- **Critical bugs**: Think harder about preventing recurrence

## Bug Fix Process

### Step 1: Reproduce the Bug with a Test

```python
def test_reproduces_reported_bug():
    """
    Bug Report: Users can login with expired tokens
    This test MUST fail to confirm bug exists
    """
    expired_token = create_token(expired=True)
    
    # This should fail but currently passes (bug!)
    with pytest.raises(AuthenticationError):
        authenticate_with_token(expired_token)
```

### Step 2: Verify Test Fails

```bash
# Confirm the bug exists
pytest test_bug_fix.py::test_reproduces_reported_bug -v

# Expected: Test FAILS (confirming bug exists)
# FAILED test_bug_fix.py::test_reproduces_reported_bug
```

### Step 3: Write Expected Behavior Test

```python
def test_correct_token_expiry_behavior():
    """Define correct behavior through tests"""
    # Valid token should work
    valid_token = create_token(expired=False)
    assert authenticate_with_token(valid_token) == True
    
    # Expired token should fail
    expired_token = create_token(expired=True)
    with pytest.raises(AuthenticationError):
        authenticate_with_token(expired_token)
    
    # About-to-expire token should work
    almost_expired = create_token(expires_in_seconds=60)
    assert authenticate_with_token(almost_expired) == True
```

### Step 4: Fix the Bug

```python
# Minimal fix to pass the test
def authenticate_with_token(token):
    """Fixed implementation"""
    if token.is_expired():  # This check was missing!
        raise AuthenticationError("Token expired")
    
    return validate_token(token)
```

### Step 5: Add Regression Tests

```python
def test_prevents_token_expiry_regression():
    """Comprehensive tests to prevent regression"""
    # Test various expiry scenarios
    test_cases = [
        (create_token(expired=True), False),
        (create_token(expired=False), True),
        (create_token(expires_at=yesterday), False),
        (create_token(expires_at=tomorrow), True),
        (create_token(expires_at=now), False),
    ]
    
    for token, should_pass in test_cases:
        if should_pass:
            assert authenticate_with_token(token)
        else:
            with pytest.raises(AuthenticationError):
                authenticate_with_token(token)
```

## Parallel Bug Analysis Subagents

Deploy concurrent debugging specialists:
@code-archaeologist @business-analyst @test-generator @qa-engineer

- @code-archaeologist: Analyze underlying issues, uncover root causes, and search for related patterns
- @business-analyst: Evaluate affected components and perform impact analysis
- @test-generator: Design comprehensive test suite to prevent regression and ensure coverage
- @qa-engineer: Validate fix quality and identify potential side effects

## Bug Categories

### 1. Logic Errors
```python
def test_fixes_calculation_error():
    """Test for calculation bugs"""
    # Bug: Total calculated incorrectly
    cart = ShoppingCart()
    cart.add_item(price=10, quantity=2)
    cart.add_item(price=5, quantity=3)
    
    # Should be 35, not 25 (bug!)
    assert cart.total() == 35
```

### 2. Boundary Conditions
```python
def test_handles_empty_input():
    """Test for edge case bugs"""
    # Bug: Crashes on empty list
    result = process_items([])
    assert result == []  # Should handle gracefully
```

### 3. Race Conditions
```python
def test_thread_safety():
    """Test for concurrency bugs"""
    # Bug: Data corruption in parallel access
    import threading
    
    counter = Counter()
    threads = []
    
    for _ in range(100):
        t = threading.Thread(target=counter.increment)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    assert counter.value == 100  # Should be exactly 100
```

### 4. Security Vulnerabilities
```python
def test_prevents_sql_injection():
    """Test for security bugs"""
    # Bug: SQL injection possible
    malicious_input = "'; DROP TABLE users; --"
    
    # Should sanitize input
    with pytest.raises(ValidationError):
        execute_query(malicious_input)
```

## Bug Fix Workflow

1. **Analyze Bug Report**
   - Understand symptoms
   - Identify affected components
   - Determine severity

2. **Create Failing Test**
   - Write test that reproduces bug
   - Verify test fails
   - Document expected behavior

3. **Implement Fix**
   - Make minimal change
   - Focus on root cause
   - Avoid introducing new issues

4. **Verify Fix**
   - Run reproduction test
   - Confirm it passes
   - Run full test suite

5. **Prevent Regression**
   - Add comprehensive tests
   - Test edge cases
   - Document fix

## Usage Examples

```bash
# Fix authentication bug
/tdd-bugfix "Users can login with wrong password"

# Fix data corruption bug
/tdd-bugfix "Database records deleted when updating user profile"

# Fix performance bug
/tdd-bugfix "API timeout when loading large datasets"

# Fix UI bug
/tdd-bugfix "Button click not working after form validation"
```

## Output Format

1. **Bug Analysis**
   - Root cause identification
   - Impact assessment
   - Related code areas

2. **Reproduction Test**
   - Failing test that confirms bug
   - Test execution output
   - Clear failure message

3. **Bug Fix**
   - Minimal code change
   - Explanation of fix
   - No side effects

4. **Verification**
   - Test now passing
   - All existing tests still pass
   - No performance regression

5. **Regression Prevention**
   - Additional test cases
   - Edge case coverage
   - Documentation updates

## Common Bug Patterns

### Off-by-One Errors
```python
def test_array_bounds():
    """Prevent index errors"""
    arr = [1, 2, 3]
    # Bug: Accessing arr[3]
    assert get_last_element(arr) == 3  # Not arr[len(arr)]
```

### Null Reference Errors
```python
def test_handles_null_values():
    """Prevent NoneType errors"""
    # Bug: Crashes on None
    result = process_data(None)
    assert result == default_value()
```

### Type Mismatches
```python
def test_type_conversion():
    """Prevent type errors"""
    # Bug: String concatenation with number
    result = format_message("Count", 42)
    assert result == "Count: 42"
```

## Quality Checklist

Before completing bug fix:
- [ ] Bug reproduced with failing test
- [ ] Root cause identified
- [ ] Minimal fix implemented
- [ ] Test now passes
- [ ] No existing tests broken
- [ ] Regression tests added
- [ ] Performance unchanged
- [ ] Documentation updated
- [ ] Similar bugs checked

## Integration with CI/CD

```yaml
# GitHub Action for bug fixes
name: TDD Bug Fix Validation
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  validate-bugfix:
    if: contains(github.event.pull_request.labels.*.name, 'bugfix')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Check for regression test
        run: |
          # Ensure bug fix includes test
          if ! git diff --name-only origin/main..HEAD | grep -q "test_.*\.py"; then
            echo "Bug fix must include test"
            exit 1
          fi
      
      - name: Run tests
        run: pytest --tb=short
      
      - name: Check coverage didn't decrease
        run: |
          pytest --cov=. --cov-report=term
          # Compare with main branch coverage
```

## Best Practices

1. **Always Test First**: Never fix without reproducing
2. **Minimal Changes**: Fix only the bug, nothing else
3. **Document the Fix**: Explain what was wrong and why
4. **Test Thoroughly**: Include edge cases
5. **Prevent Recurrence**: Add monitoring/logging
6. **Learn from Bugs**: Update coding standards