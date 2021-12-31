from Stack import Stack


infix_stack = Stack()
postfix_stack = Stack()

# first, we need to split up the string into individual characters and convert them to
# to integers. Also wipe out any whitespace

# removing whitespace from expression


def convert_to_postfix(expression):
    output_string = ""
    for i in expression:
        if i == "(":
            infix_stack.push(i)
        elif i == "-" or i == "+":
            infix_stack.push(i)
        elif i == "*" or i == "/":
            # if the last item in the stack is of greater or equal precedence, pop it
            last_item = infix_stack.peek()
            while last_item == "*" or last_item == "/":
                output_string += infix_stack.pop()
                last_item = infix_stack.peek()
            infix_stack.push(i)
        elif i == ")":
            # while we don't come across an opening delimiter, keep popping operators
            last_item = infix_stack.peek()
            while last_item != "(":
                output_string += infix_stack.pop()
                last_item = infix_stack.peek()
            infix_stack.pop()
        else:
            if str(i).isnumeric():
                output_string += i
            elif i == " ":
                output_string += i
            else:
                raise ValueError

    for i in range(len(infix_stack)):
        output_string += infix_stack.pop()

    print(infix_stack)
    return output_string


if __name__ == "__main__":
    ex = "( 4 * 12 ) + 1 "
    print(convert_to_postfix(ex))
