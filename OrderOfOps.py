from Stack import Stack


class OrderOfOps:

    def __init__(self, expression):
        self.__infix_stack = Stack()
        self.__postfix_stack = Stack()
        self.__expression = expression

    def __convert_to_postfix(self, expression):
        output_string = ""
        for i in expression:
            if i == "(":
                self.__infix_stack.push(i)
            elif i == "-" or i == "+":
                # while the last item in the stack is of greater or equal precedence, pop it
                last_item = self.__infix_stack.peek()
                while last_item == "*" or last_item == "/" or last_item == "+" or last_item == "-":
                    output_string += self.__infix_stack.pop()
                    last_item = self.__infix_stack.peek()
                self.__infix_stack.push(i)
            elif i == "*" or i == "/":
                # while the last item in the stack is of greater or equal precedence, pop it
                last_item = self.__infix_stack.peek()
                while last_item == "*" or last_item == "/":
                    output_string += self.__infix_stack.pop()
                    last_item = self.__infix_stack.peek()
                self.__infix_stack.push(i)
            elif i == ")":
                # while we don't come across an opening delimiter, keep popping operators
                last_item = self.__infix_stack.peek()
                while last_item != "(":
                    output_string += self.__infix_stack.pop()
                    last_item = self.__infix_stack.peek()
                self.__infix_stack.pop()
            else:
                if str(i).isnumeric():
                    output_string += i
                elif i == " ":
                    output_string += i
                else:
                    raise ValueError

        # pop everything else left in the stack
        for i in range(len(self.__infix_stack)):
            output_string += self.__infix_stack.pop()

        return output_string

    # Converting to an array makes it easier to keep multi-digit numbers apart from single digit ones
    # and takes care of having to deal with whitespace when parsing through a string

    def __convert_to_array(self, postfix_expression):
        postfix_array = []
        i = 0
        while i in range(len(postfix_expression)):
            if postfix_expression[i] == " ":
                pass
            elif postfix_expression[i].isnumeric() and postfix_expression[i+1] == " ":
                postfix_array.append(int(postfix_expression[i]))
            elif postfix_expression[i].isnumeric():
                j = i
                substring = ""
                while postfix_expression[j] != " ":
                    substring += postfix_expression[j]
                    j += 1
                    i += 1

                postfix_array.append(int(substring))
            elif postfix_expression[i] == "-":
                postfix_array.append(postfix_expression[i])
            elif postfix_expression[i] == "+":
                postfix_array.append(postfix_expression[i])
            elif postfix_expression[i] == "*":
                postfix_array.append(postfix_expression[i])
            elif postfix_expression[i] == "/":
                postfix_array.append(postfix_expression[i])

            i += 1

        return postfix_array

    def __evaluate_postfix(self, postfix_arr):
        for i in postfix_arr:
            if i == "-":
                b = self.__postfix_stack.pop()
                a = self.__postfix_stack.pop()
                self.__postfix_stack.push(a - b)
            elif i == "+":
                b = self.__postfix_stack.pop()
                a = self.__postfix_stack.pop()
                self.__postfix_stack.push(a + b)
            elif i == "*":
                b = self.__postfix_stack.pop()
                a = self.__postfix_stack.pop()
                self.__postfix_stack.push(a * b)
            elif i == "/":
                b = self.__postfix_stack.pop()
                a = self.__postfix_stack.pop()
                self.__postfix_stack.push(a / b)

            else:
                self.__postfix_stack.push(i)

        # The last item left in the stack is the calculated expression
        return self.__postfix_stack.pop()

    def calculate(self):
        pfix_string = self.__convert_to_postfix(self.__expression)
        pfix_arr = self.__convert_to_array(pfix_string)
        result = self.__evaluate_postfix(pfix_arr)
        return result
