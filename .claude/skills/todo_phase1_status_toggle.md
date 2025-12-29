# Skill: todo_phase1_status_toggle

## Skill Name
`todo_phase1_status_toggle`

## Purpose
Defines the logic for toggling a todo item's completion status. Validates the todo ID exists, toggles the `completed` boolean in memory, and provides clear CLI feedback.

## Phase I Feature Supported
**Mark Todo Complete** - Allows users to mark a todo as complete (or toggle back to incomplete) via CLI.

## When to Use
- When implementing the "Mark Complete" feature
- When specifying how completion status changes
- When defining feedback messages for status changes
- When validating todo ID for completion toggle
- When handling "todo not found" scenarios

## When NOT to Use
- For adding new todos (use `todo_phase1_input_validation`)
- For listing todos (use `todo_phase1_todo_display_formatter`)
- For deleting todos
- For menu navigation

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `todo_id` | Yes | The ID of the todo to toggle |
| `todos` | Yes | The in-memory list of all todos |

## Outputs

| Output | Description |
|--------|-------------|
| `success` | Boolean - true if toggle succeeded |
| `message` | Feedback message for CLI display |
| `new_status` | The new completion status (true/false) |
| `error_type` | Error category if failed (INVALID_ID, NOT_FOUND) |

## Step-by-Step Process

### Step 1: Validate ID Input
```
IF todo_id is empty or not a number:
  RETURN success=false, error_type="INVALID_ID",
         message="Please enter a valid todo number"
```

### Step 2: Find Todo in List
```
todo = find todo in todos WHERE todo.id == todo_id

IF todo not found:
  RETURN success=false, error_type="NOT_FOUND",
         message="Todo #{todo_id} not found"
```

### Step 3: Toggle Status
```
todo.completed = NOT todo.completed
new_status = todo.completed
```

### Step 4: Generate Feedback Message
```
IF new_status == true:
  message = "Marked complete: {todo.text}"
ELSE:
  message = "Marked incomplete: {todo.text}"
```

### Step 5: Return Result
```
RETURN {
  success: true,
  message: message,
  new_status: new_status,
  error_type: null
}
```

## Phase I Constraints

| Constraint | How This Skill Complies |
|------------|------------------------|
| In-memory only | Modifies list in memory, no persistence |
| CLI only | Feedback via print(), input via input() |
| No external deps | Python built-in operations only |
| Single user | No user ownership of todos |
| Toggle behavior | Can mark complete AND incomplete |

## Example Usage

**Successful Toggle (to complete):**
```
Input: todo_id=1, todos=[{id:1, text:"Buy milk", completed:false}]

Output: {
  success: true,
  message: "Marked complete: Buy milk",
  new_status: true
}
```

**Successful Toggle (to incomplete):**
```
Input: todo_id=1, todos=[{id:1, text:"Buy milk", completed:true}]

Output: {
  success: true,
  message: "Marked incomplete: Buy milk",
  new_status: false
}
```

**Todo Not Found:**
```
Input: todo_id=99, todos=[{id:1, text:"Buy milk", completed:false}]

Output: {
  success: false,
  message: "Todo #99 not found",
  error_type: "NOT_FOUND"
}
```

**Invalid ID:**
```
Input: todo_id="abc", todos=[...]

Output: {
  success: false,
  message: "Please enter a valid todo number",
  error_type: "INVALID_ID"
}
```

## Judge Readiness

- Clear success/failure feedback
- Shows todo text in confirmation
- Handles edge cases gracefully
- Toggle behavior (not just "complete")
- Demonstrable in < 10 seconds

## Governance Compliance

| Rule | Status |
|------|--------|
| 1. Project-Specific | Mark Complete feature only |
| 2. Phase Boundary | In-memory toggle, CLI feedback |
| 3. Required Structure | All 8 sections present |
| 4. Spec-Driven | Supports Mark Complete spec |
| 5. Judge-Oriented | Clear feedback messages |
| 6. Granularity | Single responsibility |
| 7. Execution | Helper, no auto-execution |
| 8. Naming | `todo_phase1_*` convention |
| 9. Output Quality | Deterministic, structured |
| 10. Confirmation | Confirmed above |
