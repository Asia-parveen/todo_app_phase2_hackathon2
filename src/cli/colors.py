"""
ANSI Color Constants for Todo CLI Application - FULLY COLORFUL

Color Scheme:
- GREEN: Success messages, completed task text, completed status marker
- RED: Errors, incomplete status marker, delete confirmations
- YELLOW: Warnings, incomplete task text
- BLUE: Headers, menus, update success
- CYAN: Prompts, task IDs, toggle success
- MAGENTA: Task descriptions
- WHITE (BOLD): Task titles
"""

# ANSI escape code prefix
ESC = "\033["

# =============================================================================
# BASE COLORS
# =============================================================================
BLACK = f"{ESC}30m"
RED = f"{ESC}31m"
GREEN = f"{ESC}32m"
YELLOW = f"{ESC}33m"
BLUE = f"{ESC}34m"
MAGENTA = f"{ESC}35m"
CYAN = f"{ESC}36m"
WHITE = f"{ESC}37m"
RESET = f"{ESC}0m"

# =============================================================================
# BRIGHT/BOLD VARIANTS
# =============================================================================
BOLD = f"{ESC}1m"
BOLD_WHITE = f"{ESC}1;37m"
BOLD_GREEN = f"{ESC}1;32m"
BOLD_RED = f"{ESC}1;31m"
BOLD_YELLOW = f"{ESC}1;33m"
BOLD_BLUE = f"{ESC}1;34m"
BOLD_CYAN = f"{ESC}1;36m"
BOLD_MAGENTA = f"{ESC}1;35m"

# Bright colors (high intensity)
BRIGHT_GREEN = f"{ESC}92m"
BRIGHT_RED = f"{ESC}91m"
BRIGHT_YELLOW = f"{ESC}93m"
BRIGHT_BLUE = f"{ESC}94m"
BRIGHT_CYAN = f"{ESC}96m"
BRIGHT_MAGENTA = f"{ESC}95m"
BRIGHT_WHITE = f"{ESC}97m"


# =============================================================================
# COLOR HELPER FUNCTIONS
# =============================================================================

def colorize(text, color):
    """Wrap text with color and reset."""
    return f"{color}{text}{RESET}"


# =============================================================================
# SEMANTIC COLOR FUNCTIONS
# =============================================================================

# --- Success/Error/Warning ---
def success(text):
    """Format success message in BRIGHT GREEN."""
    return colorize(text, BRIGHT_GREEN)


def error(text):
    """Format error message in BRIGHT RED."""
    return colorize(text, BRIGHT_RED)


def warning(text):
    """Format warning message in BRIGHT YELLOW."""
    return colorize(text, BRIGHT_YELLOW)


# --- Headers and Menus ---
def header(text):
    """Format header in BOLD BLUE."""
    return colorize(text, BOLD_BLUE)


def menu_option_num(text):
    """Format menu option number in CYAN."""
    return colorize(text, BRIGHT_CYAN)


def menu_option_text(text):
    """Format menu option text in WHITE."""
    return colorize(text, WHITE)


# --- User Input ---
def prompt_text(text):
    """Format prompt text in CYAN."""
    return colorize(text, CYAN)


# --- Task Display ---
def task_id(text):
    """Format task ID in BRIGHT CYAN."""
    return colorize(text, BRIGHT_CYAN)


def task_title(text):
    """Format task title in BOLD WHITE."""
    return colorize(text, BOLD_WHITE)


def task_description(text):
    """Format task description in MAGENTA."""
    return colorize(text, MAGENTA)


def task_completed_marker():
    """Return GREEN checkmark for completed tasks."""
    return colorize("✔", BRIGHT_GREEN)


def task_incomplete_marker():
    """Return RED X for incomplete tasks."""
    return colorize("✘", BRIGHT_RED)


def completed_task_line(text):
    """Format entire completed task line in GREEN."""
    return colorize(text, GREEN)


def incomplete_task_line(text):
    """Format entire incomplete task line in YELLOW."""
    return colorize(text, YELLOW)


# --- Action Feedback ---
def add_success(text):
    """Format add success in BRIGHT GREEN."""
    return colorize(text, BRIGHT_GREEN)


def update_success(text):
    """Format update success in BRIGHT BLUE."""
    return colorize(text, BRIGHT_BLUE)


def delete_success(text):
    """Format delete success in BRIGHT RED."""
    return colorize(text, BRIGHT_RED)


def toggle_success(text):
    """Format toggle success in BRIGHT CYAN."""
    return colorize(text, BRIGHT_CYAN)


# --- Dividers and Decorations ---
def divider(text):
    """Format divider in BLUE."""
    return colorize(text, BLUE)


def summary(text):
    """Format summary line in BOLD MAGENTA."""
    return colorize(text, BOLD_MAGENTA)
