
#* The "Walrus Operator", or :=, is an assignment operator. In this example, we are assigning the variable user_input to the output of the input(). The operator assigns is treated as an expression, whereby whatever is assigned because an expression that can be evaluated. In this case, the expression is used in a boolean evaluation.

while (user_input := input('Enter q or p: ')) != 'q':
    if user_input == 'p':
        print("Hello!")

# NOTE: for expressions like the above, wrap it in paranthesis


