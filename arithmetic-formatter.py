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

        # Determine the width of the problem
        max_width = max(len(operand1), len(operand2)) + 2

        # Build the lines
        first_line.append(operand1.rjust(max_width))
        second_line.append(operator + operand2.rjust(max_width - 1))
        lines.append("-" * max_width)

        # Calculate the answer if needed
        if display_answers:
            if operator == '+':
                result = int(operand1) + int(operand2)
            else:
                result = int(operand1) - int(operand2)
            answers.append(str(result).rjust(max_width))

    # Combine the arranged output
    arranged_problems = "    ".join(first_line) + "\n"
    arranged_problems += "    ".join(second_line) + "\n"
    arranged_problems += "    ".join(lines)

    if display_answers:
        arranged_problems += "\n" + "    ".join(answers)

    return arranged_problems

