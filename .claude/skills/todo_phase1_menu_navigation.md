# Skill: todo_phase1_menu_navigation

## Skill Name
`todo_phase1_menu_navigation`

## Purpose
Defines the main menu structure and validates user menu selections for the Todo CLI application. Ensures consistent menu display and proper handling of valid/invalid menu choices.

## Phase I Feature Supported
**CLI Menu Navigation** - The main interface through which users access all Phase I features (Add, List, Complete, Delete, Exit).

## When to Use
- When designing the main menu layout
- When specifying menu option numbering and labels
- When defining invalid menu choice error handling
- When implementing the main application loop
- During demo to ensure smooth navigation

## When NOT to Use
- For todo input validation (use `todo_phase1_input_validation`)
- For todo display formatting (use `todo_phase1_todo_display_formatter`)
- For specific feature logic (add, delete, complete)
- For any data storage operations

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `user_choice` | Yes | Raw input from user at menu prompt |
| `valid_options` | No | List of valid option numbers (default: ["1","2","3","4","5"]) |

## Outputs

| Output | Description |
|--------|-------------|
| `menu_display` | Formatted menu string for CLI output |
| `is_valid_choice` | Boolean - true if selection is valid |
| `selected_option` | Parsed option number (or null if invalid) |
| `error_message` | Error message for invalid selection |

## Step-by-Step Process

### Step 1: Generate Menu Display
```
menu_display = """
==============================
       TODO APP - PHASE I
==============================

  1. Add Todo
  2. List Todos
  3. Mark Todo Complete
  4. Delete Todo
  5. Exit

==============================
Enter your choice (1-5): """
```

### Step 2: Validate User Choice
```
IF user_choice is empty:
  RETURN is_valid_choice=false, error_message="Please enter a choice"

IF user_choice not in valid_options:
  RETURN is_valid_choice=false, error_message="Invalid choice. Please enter 1-5"

RETURN is_valid_choice=true, selected_option=int(user_choice)
```

### Step 3: Map Option to Action
```
Option Map:
  1 -> ADD_TODO
  2 -> LIST_TODOS
  3 -> MARK_COMPLETE
  4 -> DELETE_TODO
  5 -> EXIT
```

### Step 4: Return Navigation Result
```
RETURN {
  menu_display,
  is_valid_choice,
  selected_option,
  error_message (if any)
}
```

## Phase I Constraints

| Constraint | How This Skill Complies |
|------------|------------------------|
| In-memory only | Menu state not persisted |
| CLI only | Text-based menu via print/input |
| No external deps | Python built-in only |
| Single user | No user sessions or auth |
| 5 options only | Add, List, Complete, Delete, Exit |

## Example Usage

**Valid Selection:**
```
Input: user_choice="2"

Output: {
  is_valid_choice: true,
  selected_option: 2,
  error_message: ""
}
Action: LIST_TODOS
```

**Invalid Selection:**
```
Input: user_choice="7"

Output: {
  is_valid_choice: false,
  selected_option: null,
  error_message: "Invalid choice. Please enter 1-5"
}
```

**Empty Selection:**
```
Input: user_choice=""

Output: {
  is_valid_choice: false,
  selected_option: null,
  error_message: "Please enter a choice"
}
```

## Judge Readiness

- Clean, centered menu header
- Numbered options (1-5) for quick selection
- Clear prompt indicating valid range
- Immediate feedback on invalid input
- Professional appearance in < 3 seconds scan

## Governance Compliance

| Rule | Status |
|------|--------|
| 1. Project-Specific | CLI Menu navigation only |
| 2. Phase Boundary | CLI I/O, no persistence |
| 3. Required Structure | All 8 sections present |
| 4. Spec-Driven | Supports CLI Menu spec |
| 5. Judge-Oriented | Clean, professional menu |
| 6. Granularity | Single responsibility |
| 7. Execution | Helper, no auto-execution |
| 8. Naming | `todo_phase1_*` convention |
| 9. Output Quality | Deterministic, structured |
| 10. Confirmation | Confirmed above |
