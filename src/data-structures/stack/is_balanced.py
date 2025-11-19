from stack import Stack

def is_balanced(input_str: str) -> bool:
    my_stack = Stack()
    for char in input_str:
        if char == "(":
            my_stack.push(char)
        if char == ")":
            matching = my_stack.pop()
            if matching is None:
                return False
    return my_stack.peek() is None

if __name__ == "__main__":

    tests = ['(',
             '())',
             '(()()',
             '(())',
             ')()(()',
             '())(()']

    for t in tests:
             print(is_balanced(t))

