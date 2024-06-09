from stack import Stack


def are_brackets_balanced(s):
    stack = Stack()

    # Проходим по каждому символу в строке
    for char in s:
        if char == '(':  # Если символ - открывающая скобка, добавляем в стек
            stack.push(char)
        elif char == ')':  # Если символ - закрывающая скобка
            if not stack:  # Если стек пуст -- скобки не сбалансированы
                return False
            stack.pop()  # Удаляем последнюю открывающую скобку из стека

    return stack.size() == 0  # Если стек пуст -- скобки сбалансированы


if __name__ == '__main__':
    print(are_brackets_balanced("(()((())()))"))  # True
    print(are_brackets_balanced("(()()(())"))  # False
    print(are_brackets_balanced("()"))  # True
    print(are_brackets_balanced("()()"))  # True
    print(are_brackets_balanced("(()((())()))"))  # True
    print(are_brackets_balanced("(()()(()"))  # False
