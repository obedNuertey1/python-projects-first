def arithmetic_arranger(problems, display_answers=False):
    # Limit of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Containers for the arranged output
    first_line = []
    second_line = []
    lines = []
    answers = []

