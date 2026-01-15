"""A simple demo of using the Colorama library to print colored text
to the terminal.

Tasks covered in this demo:
- How to import and initialize Colorama
- How to use Foreground (text) colors
- How to use Background colors
- How to use Style (BRIGHT, DIM, RESET)
- Why we usually run this in a real terminal instead of the IDLE shell
"""

# We import specific names from the colorama module so we can use them directly:
#   init   -> function we call once to set up Colorama (especially important on Windows)
#   Fore   -> contains constants for text (foreground) colors like Fore.RED, Fore.GREEN
#   Back   -> contains constants for background colors like Back.YELLOW
#   Style  -> contains style constants like Style.BRIGHT, Style.DIM, Style.RESET_ALL
from colorama import init, Fore, Back, Style

# ---------------------------------------------------------------------------
# 1. INITIALIZING COLORAMA
# ---------------------------------------------------------------------------

# On Windows terminals, Colorama works by intercepting ANSI color codes that
# we print and translating them into the Windows API calls needed to actually
# change text color.
#
# Calling init() sets this up. You should usually do this ONCE near the start
# of your program.
#
# The argument "autoreset=True" means:
#   After each print statement, Colorama will automatically reset the text
#   color and style back to normal.
#
# Without autoreset=True, the color/style would "stick" and affect all future
# print statements until we manually reset them using Style.RESET_ALL.
#
init(autoreset=True)# Initialize Colorama with autoreset enabled.

# ---------------------------------------------------------------------------
# 2. BASIC COLOR DEMO
# ---------------------------------------------------------------------------
def basic_colors_demo():
    """
    Show simple examples of foreground (text) colors, background colors,
    and styles.
    """

    print("=== BASIC COLOR DEMO ===")

    # Foreground (text) colors:
    # We prepend the string with Fore.COLOR_NAME.
    # Example: Fore.RED changes the color of the following text to red.
    print(Fore.RED + "This text is RED.")
    print(Fore.GREEN + "This text is GREEN.")
    print(Fore.BLUE + "This text is BLUE.")

    # Background colors:
    # Back.COLOR_NAME changes the background color.
    print(Back.YELLOW + "This has a YELLOW background.")
    print(Back.CYAN + "This has a CYAN background.")

    # Styles:
    # Style.BRIGHT makes the text brighter/bold (depending on the terminal).
    print(Style.BRIGHT + "This text is BRIGHT (bold).")

    # Style.DIM makes the text dimmer (if supported by the terminal).
    print(Style.DIM + "This text is DIM (less intense).")

    # Note: Because we used init(autoreset=True), the color/style will go
    # back to normal after each print(), so we don't need to call RESET_ALL
    # manually in this function.

    print("Back to normal text after each line because of autoreset=True.\n")


# ---------------------------------------------------------------------------
# 3. COMBINING FOREGROUND, BACKGROUND, AND STYLE
# ---------------------------------------------------------------------------
def combined_color_demo():
    """
    Combining foreground color, background color, and style.
    We do this by concatenating the constants before the text.
    """

    print("=== COMBINED COLOR DEMO ===")
    # We can combine like this:
    #   Style.BRIGHT + Fore.WHITE + Back.RED
    #
    # The order doesn't matter much, but it's common to do Style, then Fore,
    # then Back for readability.
    print(Style.BRIGHT + Fore.WHITE + Back.RED + "Bright WHITE text on RED background")
    print(Style.BRIGHT + Fore.BLACK + Back.GREEN + "Bright BLACK text on GREEN background")
    print(Style.DIM + Fore.YELLOW + Back.BLUE + "Dim YELLOW text on BLUE background")

    # Again, autoreset=True will reset everything after each print.
    print("Normal text again after combined styles.\n")


# ---------------------------------------------------------------------------
# 4. REALISTIC USE CASE: COLORED STATUS MESSAGES
# ---------------------------------------------------------------------------
def print_status(message, status_type):
    """
    Print a message with a color based on the "status_type".

    status_type can be one of:
        "info"     -> blue
        "success"  -> green
        "warning"  -> yellow
        "error"    -> red

    This kind of function is useful in real applications where you want
    to visually distinguish different kinds of output messages.
    """

    # We choose a color based on the status_type
    if status_type == "info":
        color = Fore.BLUE
        label = "[INFO]   "
    elif status_type == "success":
        color = Fore.GREEN
        label = "[SUCCESS]"
    elif status_type == "warning":
        color = Fore.YELLOW
        label = "[WARNING]"
    elif status_type == "error":
        color = Fore.RED
        label = "[ERROR]  "
    else:
        # Default to white if status_type is not recognized.
        color = Fore.WHITE
        label = "[OTHER]  "

    # We use Style.BRIGHT to make the label stand out.
    # Notice that we only color the label and then append the message.
    # Because autoreset=True, only this line is affected.
    print(Style.BRIGHT + color + label + " " + message)

# ---------------------------------------------------------------------------
# 4b. DEMO OF THE STATUS FUNCTION
# ---------------------------------------------------------------------------
def status_demo():
    """
    Show how the print_status function would be used in a program.
    """
    print("=== STATUS MESSAGE DEMO ===")
    # Example status messages:
    print_status("Program started.", "info") # Info message
    print_status("Data loaded successfully.", "success") # Success message
    print_status("Disk space is getting low.", "warning") # Warning message
    print_status("Could not connect to the server.", "error") # Error message
    print_status("This is a custom type.", "custom") # Unrecognized type

    print() # End of status demo

# ---------------------------------------------------------------------------
# 5. MAIN ENTRY POINT
# ---------------------------------------------------------------------------
def main():
    """
    Main function to run all demos.
    This is the function that will be called when we run the script.
    """

    # Explain to the user what's going on:
    print("Colorama Demo Starting...")
    print("If you are running this in IDLE and don't see colors,")
    print("try running this script from Command Prompt or PowerShell instead.")
    print()

    basic_colors_demo()
    combined_color_demo()
    status_demo()

    print("Demo complete. Press Enter to exit.")
    input()  # Keep the window open if run by double-clicking on Windows.

# "Only run main() if this file is being run as a script,
# not if it's being imported as a module."
if __name__ == "__main__":
    main()