# Skill: todo_phase1_input_validation

## Skill Name
`todo_phase1_input_validation`

## Purpose
Defines and validates input handling rules for the "Add Todo" feature. Ensures CLI input is properly validated before storing in memory, with clear error messages for invalid input.

## Phase I Feature Supported
**Add Todo** - Validates the text input users provide when creating new todo items via CLI.

## When to Use
- When specifying input validation rules for Add Todo
- When defining error messages for invalid todo input
- When reviewing Add Todo acceptance criteria for input handling
- When designing the CLI prompt for todo text entry

## When NOT to Use
- For menu navigation input (use menu-specific skill)
- For todo ID validation in Delete/Complete features
- For output formatting or display logic
- For any persistence or storage logic

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `user_input` | Yes | The raw text entered by user at CLI prompt |
| `max_length` | No | Maximum allowed characters (default: 100) |

## Outputs

| Output | Description |
|--------|-------------|
| `is_valid` | Boolean - true if input passes all checks |
| `error_message` | Specific error message if invalid (empty if valid) |
| `sanitized_input` | Cleaned input ready for storage |

## Step-by-Step Process

### Step 1: Check for Empty Input
```
IF input is empty or whitespace-only:
  RETURN is_valid=false, error_message="Todo text cannot be empty"
```

### Step 2: Check Length Constraints
```
IF input length > max_length:
  RETURN is_valid=false, error_message="Todo text exceeds maximum length of [max_length] characters"
```

### Step 3: Trim Whitespace
```
sanitized_input = input.strip()
```

### Step 4: Return Valid Result
```
RETURN is_valid=true, error_message="", sanitized_input=sanitized_input
```

## Phase I Constraints

| Constraint | How This Skill Complies |
|------------|------------------------|
| In-memory only | Validates input before memory storage; no file/DB operations |
| CLI input only | Designed for `input()` function text entry |
| No external deps | Uses Python built-in string methods only |
| Single user | No user identification or session handling |

## Example Usage

**Valid Input:**
```
Input: "Buy groceries"
Output: {is_valid: true, error_message: "", sanitized_input: "Buy groceries"}
```

**Invalid Input (empty):**
```
Input: "   "
Output: {is_valid: false, error_message: "Todo text cannot be empty", sanitized_input: ""}
```

**Invalid Input (too long):**
```
Input: "[150 character string]"
Output: {is_valid: false, error_message: "Todo text exceeds maximum length of 100 characters", sanitized_input: ""}
```

## Governance Compliance

| Rule | Status |
|------|--------|
| 1. Project-Specific | Add Todo input validation only |
| 2. Phase Boundary | CLI input, no persistence |
| 3. Required Structure | All 8 sections present |
| 4. Spec-Driven | Supports Add Todo spec |
| 5. Judge-Oriented | Clear, demonstrable validation |
| 6. Granularity | Single responsibility |
| 7. Execution | Helper, no auto-execution |
| 8. Naming | `todo_phase1_*` convention |
| 9. Output Quality | Deterministic, structured |
| 10. Confirmation | Confirmed above |
