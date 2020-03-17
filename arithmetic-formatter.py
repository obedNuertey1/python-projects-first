def arithmetic_arranger(problems, display_answers=False):
    # Limit of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Containers for the arranged output
    first_line = []
    second_line = []
    lines = []
    answers = []

    # Loop through each problem
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        # Check if the operator is valid
