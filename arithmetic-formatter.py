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
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if operands have more than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
