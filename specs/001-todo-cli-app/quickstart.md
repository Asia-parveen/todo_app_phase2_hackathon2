# Quickstart: Todo In-Memory CLI Application

**Feature**: 001-todo-cli-app
**Date**: 2025-12-28

## Prerequisites

- Python 3.6 or higher
- Terminal with ANSI color support (most modern terminals)

## Installation

No installation required. This is a standalone Python application with no external dependencies.

## Running the Application

```bash
# From repository root
python src/main.py

# Or if using Python 3 explicitly
python3 src/main.py
```

## Quick Demo (30 seconds)

### 1. Start the Application
```
$ python src/main.py

================================
       TODO APPLICATION
================================

What would you like to do?

  [1] Add Task
  [2] View Tasks
  [3] Update Task
  [4] Delete Task
  [5] Mark Complete/Incomplete
  [6] Exit

Enter your choice (1-6):
```

### 2. Add a Task
```
Enter your choice (1-6): 1

--- ADD TASK ---
Enter task title: Buy groceries
Enter description (optional): Milk, eggs, bread

✓ Task added successfully! (ID: 1)
```

### 3. View Tasks
```
Enter your choice (1-6): 2

--- YOUR TASKS ---
[1] ✘ Buy groceries
    Milk, eggs, bread
----------------------
Total: 1 | Completed: 0
```

### 4. Mark Complete
```
Enter your choice (1-6): 5

Enter task ID to toggle: 1

✓ Task 1 marked as complete!
```

### 5. View Updated Task
```
Enter your choice (1-6): 2

--- YOUR TASKS ---
[1] ✔ Buy groceries
    Milk, eggs, bread
----------------------
Total: 1 | Completed: 1
```

### 6. Exit
```
Enter your choice (1-6): 6

Goodbye! Your tasks have not been saved.
```

## Menu Options

| Option | Action | Description |
|--------|--------|-------------|
| 1 | Add Task | Create new task with title and optional description |
| 2 | View Tasks | Display all tasks with status indicators |
| 3 | Update Task | Modify title or description of existing task |
| 4 | Delete Task | Remove task permanently (with confirmation) |
| 5 | Mark Complete/Incomplete | Toggle task completion status |
| 6 | Exit | Close application (data is not saved) |

## Color Coding

| Color | Meaning |
|-------|---------|
| Green | Success messages, completed tasks |
| Red | Errors, invalid input |
| Yellow | Warnings, incomplete tasks, confirmations |
| Blue | Headers, menu |
| Cyan | Input prompts |

## Important Notes

1. **No Persistence**: All tasks are lost when you exit the application
2. **ID Behavior**: Task IDs are never reused (even after deletion)
3. **Single User**: Application is designed for single-user operation

## Troubleshooting

### Colors not displaying
- Ensure your terminal supports ANSI escape codes
- On Windows, use Windows Terminal, PowerShell, or Git Bash
- Legacy Command Prompt may not support colors

### "Invalid choice" errors
- Enter only numbers 1-6 for menu selection
- Enter only the task ID number when prompted

## Verification Checklist

- [ ] Application starts without errors
- [ ] Menu displays with colors
- [ ] Can add a task
- [ ] Can view tasks
- [ ] Can mark task complete
- [ ] Can delete task (with confirmation)
- [ ] Exit works cleanly
