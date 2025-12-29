# Skill: todo_phase1_todo_display_formatter

## Skill Name
`todo_phase1_todo_display_formatter`

## Purpose
Formats todo items from the in-memory list for clear CLI display. Ensures consistent, judge-friendly output that shows todo ID, text, and completion status in a readable format.

## Phase I Feature Supported
**List Todos** - Formats and displays all todos stored in memory to the CLI.

## When to Use
- When implementing the "List Todos" display output
- When defining how todos appear in the CLI
- When specifying the format for completed vs incomplete todos
- When designing empty-list messaging
- During demo preparation to ensure readable output

## When NOT to Use
- For input validation (use `todo_phase1_input_validation`)
- For menu navigation display
- For storing or modifying todo data
- For any persistence operations

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `todos` | Yes | List of todo items from in-memory storage |
| `show_index` | No | Whether to display index numbers (default: true) |

Each todo item expected structure:
```python
{
    "id": int,
    "text": str,
    "completed": bool
}
```

## Outputs

| Output | Description |
|--------|-------------|
| `formatted_output` | String ready for CLI print |
| `todo_count` | Total number of todos displayed |
| `completed_count` | Number of completed todos |

## Step-by-Step Process

### Step 1: Check for Empty List
```
IF todos is empty:
  RETURN formatted_output="No todos yet. Add one with option 1!"
```

### Step 2: Build Header
```
header = "\n===== YOUR TODOS =====\n"
```

### Step 3: Format Each Todo
```
FOR each todo in todos:
  status_marker = "[X]" if todo.completed else "[ ]"
  line = "{index}. {status_marker} {text}"
  append line to output
```

### Step 4: Build Footer with Summary
```
footer = "\n----------------------"
footer += "Total: {todo_count} | Completed: {completed_count}"
```

### Step 5: Combine and Return
```
formatted_output = header + lines + footer
RETURN formatted_output, todo_count, completed_count
```

## Phase I Constraints

| Constraint | How This Skill Complies |
|------------|------------------------|
| In-memory only | Reads from in-memory list, no file/DB access |
| CLI output only | Formats for terminal print(), no GUI |
| No external deps | Uses Python string formatting only |
| Single user | No user-specific filtering |

## Example Usage

**With Todos:**
```
Input: [
  {"id": 1, "text": "Buy groceries", "completed": false},
  {"id": 2, "text": "Call mom", "completed": true}
]

Output:
===== YOUR TODOS =====

1. [ ] Buy groceries
2. [X] Call mom

----------------------
Total: 2 | Completed: 1
```

**Empty List:**
```
Input: []

Output:
No todos yet. Add one with option 1!
```

## Judge Readiness

- Clear visual hierarchy with header/footer
- Obvious completion status markers `[X]` vs `[ ]`
- Summary statistics at bottom
- Friendly empty-state message
- Readable in < 5 seconds

## Governance Compliance

| Rule | Status |
|------|--------|
| 1. Project-Specific | List Todos display only |
| 2. Phase Boundary | CLI output, in-memory read |
| 3. Required Structure | All 8 sections present |
| 4. Spec-Driven | Supports List Todos spec |
| 5. Judge-Oriented | Clear, scannable output |
| 6. Granularity | Single responsibility |
| 7. Execution | Helper, no auto-execution |
| 8. Naming | `todo_phase1_*` convention |
| 9. Output Quality | Deterministic, structured |
| 10. Confirmation | Confirmed above |
