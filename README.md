# OrderOfOps
A program that uses postfix and infix expressions to compute expressions requiring order of operations.

USE CASE:
1) Make sure your mathematical expression has a space between each operator, operand, and parentheses. (Operators can only be +, -, *, and /)
2) Create an object of the OrderOfOps class which takes in the expression in its constructor.
3) call .calculate() on the object to evaluate the expression which will return the result.

EXAMPLE:
a = "( 4 + 12 * 2 ) - 3 / 9 * ( 5 * 3 - 1 )"
expression = OrderOfOps(a)
result = expression.calculate()
print(result)

BACKGROUND:
This program uses conversions to and from infix and postfix expressions to allow a computer to evaluate expressions that need to follow the rules of order of operations.
I used 2 stacks to accomplish this. Each stack is implemented with a deque and the deque is implemented with a doubly linked list.
I chose to use a linked list instead of an array so that I don't have to grow/expand the array everytime I need more space which is memory intensive and not time efficient.
One stack is used to convert the string expression that the user provides into a postfix expression.
The second stack is used to evaluate the postfix expression by pushing operands to the stack and popping 2 operands whenever we come across an operator and applying the
appropriate operation to those 2 operands we popped off. Then the result of that mini-operation is pushed back onto the stack and the process repeats until only one item is
left on the stack which will be the result of the computed expression.
