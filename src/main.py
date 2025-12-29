"""
Todo In-Memory CLI Application - Phase I
Hackathon II

A simple in-memory task management application with FULLY COLORFUL CLI output.
All data is stored in memory and lost when the program exits.

COLOR SCHEME:
- RED: Errors, incomplete marker (✘), delete success
- YELLOW: Warnings, incomplete task emphasis, pending status
- GREEN: Success (add), completed marker (✔), completed task text
- BLUE: Headers, menus, update success
- MAGENTA: Descriptions, cancelled actions, summary
- CYAN: Prompts, task IDs, menu numbers, toggle feedback
- WHITE: Task titles, menu text, separators
"""

from cli.colors import (
    # Base color codes
    RESET,
    RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE,
    BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN,
    BOLD_WHITE, BOLD_BLUE, BOLD_MAGENTA,
    # Helper
    colorize
)

# Import colorama for menu colors
from colorama import Fore, Style, init
init(autoreset=True)

# =============================================================================
# IN-MEMORY STORAGE
# =============================================================================

tasks = []          # List of task dictionaries


# =============================================================================
# TASK OPERATIONS
# =============================================================================

def add_task(title, description=""):
    """Add a new task to the in-memory list."""
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    return task


def get_task_by_id(tid):
    """Find task by ID. Returns None if not found."""
    for task in tasks:
        if task["id"] == tid:
            return task
    return None


def delete_task_by_id(tid):
    """Delete task by ID. Returns True if deleted, False if not found."""
    task = get_task_by_id(tid)
    if task:
        tasks.remove(task)
        # Renumber remaining tasks starting from 1
        for i, t in enumerate(tasks, start=1):
            t["id"] = i
        return True
    return False


def toggle_complete(tid):
    """Toggle task completion status. Returns (success, new_status)."""
    task = get_task_by_id(tid)
    if task:
        task["completed"] = not task["completed"]
        return True, task["completed"]
    return False, None


# =============================================================================
# COLOR HELPER FUNCTIONS
# =============================================================================

def c_red(text):
    return f"{BRIGHT_RED}{text}{RESET}"

def c_green(text):
    return f"{BRIGHT_GREEN}{text}{RESET}"

def c_yellow(text):
    return f"{BRIGHT_YELLOW}{text}{RESET}"

def c_blue(text):
    return f"{BOLD_BLUE}{text}{RESET}"

def c_magenta(text):
    return f"{BRIGHT_MAGENTA}{text}{RESET}"

def c_cyan(text):
    return f"{BRIGHT_CYAN}{text}{RESET}"

def c_white(text):
    return f"{BOLD_WHITE}{text}{RESET}"


# =============================================================================
# CLI HANDLERS
# =============================================================================

def display_welcome():
    """Display welcome banner in BLUE."""
    print()
    print(c_blue("=" * 50))
    print(c_blue("         TODO APPLICATION - PHASE I"))
    print(c_blue("        In-Memory Task Management"))
    print(c_blue("=" * 50))
    print()


def display_menu():
    """Display main menu with colorama colors per specification."""
    print(c_blue("\n" + "=" * 35))
    print(c_blue("           MAIN MENU"))
    print(c_blue("=" * 35))
    print()
    # [1] Add Task - yellow number, yellow text
    print(f"  {Fore.YELLOW}[1]{Style.RESET_ALL} {Fore.YELLOW}Add Task{Style.RESET_ALL}")
    # [2] View Tasks - yellow number, green text
    print(f"  {Fore.YELLOW}[2]{Style.RESET_ALL} {Fore.GREEN}View Tasks{Style.RESET_ALL}")
    # [3] Update Task - yellow number, red text
    print(f"  {Fore.YELLOW}[3]{Style.RESET_ALL} {Fore.RED}Update Task{Style.RESET_ALL}")
    # [4] Delete Task - yellow number, pink (magenta) text
    print(f"  {Fore.YELLOW}[4]{Style.RESET_ALL} {Fore.MAGENTA}Delete Task{Style.RESET_ALL}")
    # [5] Mark Complete/Incomplete - yellow number, blue text
    print(f"  {Fore.YELLOW}[5]{Style.RESET_ALL} {Fore.BLUE}Mark Complete/Incomplete{Style.RESET_ALL}")
    # [6] Exit - yellow number, orange (light red) text
    print(f"  {Fore.YELLOW}[6]{Style.RESET_ALL} {Fore.LIGHTRED_EX}Exit{Style.RESET_ALL}")
    print()


def handle_add_task():
    """Handle Add Task - Success in GREEN."""
    print(c_blue("\n" + "-" * 35))
    print(c_blue("          ADD NEW TASK"))
    print(c_blue("-" * 35))

    # Get title (required) - prompt in CYAN
    while True:
        title = input(f"{CYAN}Enter task title: {RESET}").strip()
        if title:
            break
        print(c_red("Error: Title cannot be empty."))

    # Get description (optional) - prompt in CYAN
    description = input(f"{CYAN}Enter description (optional): {RESET}").strip()

    # Create task
    task = add_task(title, description)

    # Success feedback - GREEN
    print()
    print(c_green("✓ Task added successfully!"))
    # Show task with CYAN ID, WHITE separator, WHITE title
    print(f"  {c_cyan('ID: ' + str(task['id']))} {c_white('|')} {c_white(task['title'])}")


def handle_view_tasks():
    """Handle View Tasks with FULL 7-COLOR display."""
    print(c_blue("\n" + "-" * 35))
    print(c_blue("          YOUR TASKS"))
    print(c_blue("-" * 35))

    if not tasks:
        print(c_yellow("\nNo tasks yet. Add one with option 1!"))
        return

    print()
    for task in tasks:
        # Task ID in CYAN
        tid_display = c_cyan("[" + str(task["id"]) + "]")

        # Separator in WHITE
        sep = c_white("|")

        # Title in WHITE (bold)
        title_display = c_white(task["title"])

        if task["completed"]:
            # Completed: GREEN checkmark, GREEN status label
            marker = c_green("✔")
            status = c_green("(DONE)")
            # Full line has: CYAN id, WHITE sep, GREEN marker, WHITE title, GREEN status
        else:
            # Incomplete: RED X marker, YELLOW status label
            marker = c_red("✘")
            status = c_yellow("(PENDING)")
            # Full line has: CYAN id, WHITE sep, RED marker, WHITE title, YELLOW status

        # Print task line with 4+ colors per line
        print(f"  {tid_display} {sep} {marker} {title_display} {status}")

        # Description in MAGENTA
        if task["description"]:
            print(f"       {c_magenta(task['description'])}")

    # Summary section
    print()
    print(c_white("-" * 35))
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    # Summary in MAGENTA
    summary_text = f"Total: {total} | Completed: {completed} | Pending: {pending}"
    print(f"  {c_magenta(summary_text)}")


def handle_update_task():
    """Handle Update Task - Success in BLUE."""
    print(c_blue("\n" + "-" * 35))
    print(c_blue("          UPDATE TASK"))
    print(c_blue("-" * 35))

    # Get task ID - prompt in CYAN
    try:
        tid = int(input(f"{CYAN}Enter task ID to update: {RESET}"))
    except ValueError:
        print(c_red("Error: Invalid ID. Please enter a number."))
        return

    task = get_task_by_id(tid)
    if not task:
        print(c_red(f"Error: Task #{tid} not found."))
        return

    # Show current values - title in WHITE, description in MAGENTA
    print()
    print(f"  Current title: {c_white(task['title'])}")
    desc_display = task['description'] if task['description'] else "(none)"
    print(f"  Current description: {c_magenta(desc_display)}")
    print()

    # Get new values - prompts in CYAN
    new_title = input(f"{CYAN}New title (Enter to keep current): {RESET}").strip()
    new_desc = input(f"{CYAN}New description (Enter to keep current): {RESET}").strip()

    # Update only if provided
    if new_title:
        task["title"] = new_title
    if new_desc:
        task["description"] = new_desc

    # Success in BLUE
    print()
    print(c_blue(f"✓ Task #{tid} updated successfully!"))


def handle_delete_task():
    """Handle Delete Task - Success in RED."""
    print(c_blue("\n" + "-" * 35))
    print(c_blue("          DELETE TASK"))
    print(c_blue("-" * 35))

    # Get task ID - prompt in CYAN
    try:
        tid = int(input(f"{CYAN}Enter task ID to delete: {RESET}"))
    except ValueError:
        print(c_red("Error: Invalid ID. Please enter a number."))
        return

    task = get_task_by_id(tid)
    if not task:
        print(c_red(f"Error: Task #{tid} not found."))
        return

    # Show task to be deleted - CYAN ID, WHITE title
    print()
    print(f"  Task: {c_cyan('[' + str(tid) + ']')} {c_white(task['title'])}")
    print()

    # Confirmation in YELLOW
    print(c_yellow("Are you sure you want to delete this task?"))
    confirm = input(f"{CYAN}Confirm (Y/N): {RESET}").strip().upper()

    if confirm == "Y":
        delete_task_by_id(tid)
        # Delete success in RED
        print()
        print(c_red(f"✓ Task #{tid} deleted!"))
    else:
        # Cancelled in MAGENTA
        print(c_magenta("Deletion cancelled."))


def handle_toggle_complete():
    """Handle Mark Complete/Incomplete - Feedback in CYAN."""
    print(c_blue("\n" + "-" * 35))
    print(c_blue("    TOGGLE COMPLETION STATUS"))
    print(c_blue("-" * 35))

    # Get task ID - prompt in CYAN
    try:
        tid = int(input(f"{CYAN}Enter task ID to toggle: {RESET}"))
    except ValueError:
        print(c_red("Error: Invalid ID. Please enter a number."))
        return

    task = get_task_by_id(tid)
    if not task:
        print(c_red(f"Error: Task #{tid} not found."))
        return

    # Show current status
    if task["completed"]:
        current = c_green("Complete")
    else:
        current = c_yellow("Incomplete")
    print(f"\n  Current status: {current}")

    success_flag, new_status = toggle_complete(tid)

    if success_flag:
        print()
        if new_status:
            # Marked complete - GREEN marker, CYAN feedback
            print(c_green(f"✓ Task #{tid} marked as COMPLETE!"))
            print(f"  {c_green('✔')} {c_white(task['title'])}")
        else:
            # Marked incomplete - YELLOW feedback
            print(c_yellow(f"✓ Task #{tid} marked as INCOMPLETE!"))
            print(f"  {c_red('✘')} {c_white(task['title'])}")
    else:
        print(c_red(f"Error: Task #{tid} not found."))


def handle_exit():
    """Handle Exit with BLUE farewell."""
    print()
    print(c_blue("=" * 50))
    print(c_blue("    Thank you for using Todo Application!"))
    print(c_blue("    Your tasks have NOT been saved."))
    print(c_blue("              Goodbye!"))
    print(c_blue("=" * 50))
    print()


# =============================================================================
# MAIN LOOP
# =============================================================================

def main():
    """Main application loop."""
    display_welcome()

    while True:
        display_menu()

        try:
            # Prompt in CYAN
            choice = input(f"{CYAN}Enter your choice (1-6): {RESET}").strip()

            if choice == "1":
                handle_add_task()
            elif choice == "2":
                handle_view_tasks()
            elif choice == "3":
                handle_update_task()
            elif choice == "4":
                handle_delete_task()
            elif choice == "5":
                handle_toggle_complete()
            elif choice == "6":
                handle_exit()
                break
            else:
                # Invalid input in RED
                print(c_red("Error: Invalid choice. Please enter 1-6."))

        except KeyboardInterrupt:
            print(c_blue("\n\nInterrupted. Goodbye!"))
            break
        except Exception as e:
            print(c_red(f"Error: {e}"))


if __name__ == "__main__":
    main()
