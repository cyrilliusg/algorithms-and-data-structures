from stack import Stack


def calculate_postfix_expression(s: str) -> int:
    stack = Stack()

    current_operation = None

    for char in s:
        if char.isdigit():
            char = int(char)
            stack.push(char)
            continue

        current_operation = char
        if stack.size() == 2 and current_operation == '+':
            stack.push(stack.pop() + stack.pop())
        elif stack.size() == 2 and current_operation == '*':
            stack.push(stack.pop() * stack.pop())
        elif stack.size() == 2 and current_operation == '-':
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.push(left_operand - right_operand)
        elif stack.size() == 2 and current_operation in ['/', ':']:
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.push(left_operand / right_operand)
        elif stack.size() == 1 and current_operation is None:
            continue
        elif stack.size() == 1 and current_operation == '=':
            return stack.pop()
