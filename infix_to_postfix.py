# First, we define a Stack class with all standard stack operations.

class Stack:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            return "pop() not possible"
        last = self.elements[-1]
        self.elements = self.elements[:-1]
        return last

    def top(self):
        return self.elements[-1]

    def __str__(self):
        return " ".join([str(element) for element in self.elements])

    def __len__(self):
        return len(self.elements)


def InfixToPostfix(infix):

    """
    Returns the postfix representation of a given input infix expression.

    INPUT(S)
        infix - str

    OUTPUT(S)
        postfix - list

    EXAMPLES(S)
        InfixToPostfix("3^4/(5*6)+10") = ['3', '4', '^', '5', '6', '*', '/', '10', '+']
        InfixToPostfix("3+4/5") = ['3', '4', '5', '/', '+']

    """

    # We remove all whitespaces from the infix expression.

    infix = infix.replace(" ", "")

    # We initialise the postfix list.

    postfix = []

    # We create a stack for the operators.

    operators = Stack()

    # We initialise a few variables to control the appending of elements to the postfix list and the pushing of
    # elements to the operator stack

    just_added_operand = False
    num_added_operands = 0

    # We define the permissible operators and the precedence order.

    allowed_operators = {"+", "-", "*", "/", "^", "(", ")"}
    priority = {"^": 3, "/": 2, "*": 2, "+": 1, "-": 1}

    # We initialise a counter variable to iterate through the infix expression.

    i = 0

    while i < len(infix):

        # The current symbol being analysed is defined based on the value of i.

        symbol = infix[i]

        # If the symbol is an open parenthesis, we create a sub-expression up to where its corresponding closing
        # parenthesis is present. This sub-expression is then fed back into the InfixToPostfix function.

        if symbol == "(":
            sub_expression = ""
            num_open = 1
            while num_open != 0:
                i += 1
                symbol = infix[i]
                if symbol == "(":
                    num_open += 1
                elif symbol == ")":
                    num_open -= 1
                sub_expression += infix[i]

            # The postfix representation of the sub-expression is appended to the main postfix representation.

            for character in InfixToPostfix(sub_expression[:-1]):
                postfix.append(character)
                num_added_operands += 1

        # If the symbol is not an operator, it must be an operand and is added to the postfix list.

        elif symbol not in allowed_operators and just_added_operand is False:
            postfix.append(symbol)
            just_added_operand = True
            num_added_operands += 1

        # If the symbol is not an operator and an operand has just been added, it must be the subsequent digit of
        # the operand. This is appended to the previously added operand.

        elif symbol not in allowed_operators and just_added_operand is True:
            postfix.append(postfix.pop() + symbol)
            just_added_operand = True

        # If the symbol is an operator, it is pushed onto the operator stack.

        elif symbol in allowed_operators:
            operators.push(symbol)
            just_added_operand = False

        # If we have reached the end of the infix expression, we can simply pop all the remaining operators in the
        # stack.

        if i == len(infix) - 1:
            while not operators.is_empty():
                postfix.append(operators.pop())

        # If the number of operands added is even and the next character in the infix expression is not a number,
        # We can pop those operators who have higher precedence than the operator that will occur next.

        elif num_added_operands % 2 == 0 and not infix[i + 1].isdigit():
            num_added_operands -= 1
            while priority[infix[i + 1]] <= priority[operators.top()]:
                postfix.append(operators.pop())
                if operators.is_empty():
                    break

        # We move on to the next character in the infix expression.

        i += 1

    # We return the postfix representation as a list.

    return postfix


def EvaluatePostfix(postfix):

    """
        Returns the numerical value of the input postfix expression.

        INPUT(S)
            postfix - list

        OUTPUT(S)
            final_value - float

        EXAMPLES(S)
            EvaluatePostfix(['3', '4', '^', '5', '6', '*', '/', '10', '+']) = 12.7

    """

    # We define a helper function to actually perform mathematical operations.

    def perform_operation(a, b, op):

        # The operands are converted from str to float.

        a = float(a)
        b = float(b)

        # Depending on the operator, the necessary operation is performed in the required order of operands.

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        elif op == "^":
            return a ** b

    # We define the allowed operators and create an empty stack for the operands.

    allowed_operators = {"+", "-", "*", "/", "^"}
    operands = Stack()

    # We iterate through the postfix expression and push operands to the operand stack. If an operator is encountered
    # we pop two operands and perform the necessary operation. The result is pushed back into the operand stack.

    for element in postfix:
        if element not in allowed_operators:
            operands.push(element)
        else:
            operand2 = operands.pop()
            operand1 = operands.pop()
            operands.push(perform_operation(operand1, operand2, element))

    # The final value is the only remaining element in the operand stack.

    final_value = operands.pop()

    # We return the final value.

    return final_value
