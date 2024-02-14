from stack import Stack


def calculate_postfix_expression(s: str) -> int:
    stack = Stack()

    current_operation = None

    for char in s:
        try:
            char = int(char)
        except ValueError:
            current_operation = char
            if stack.size() == 2 and current_operation == '+':
                stack.push(stack.pop() + stack.pop())
            elif stack.size() == 2 and current_operation == '*':
                stack.push(stack.pop() * stack.pop())
            elif stack.size() == 1 and current_operation is None:
                continue
            elif stack.size() == 1 and current_operation == '=':
                return stack.pop()
        else:
            stack.push(char)
