'''
Implement a function is_balanced(expression) that takes a string 
containing parentheses, curly braces, and square brackets,and determines whether 
the expression is balanced. 

An expression is considered balanced if each opening bracket has a corresponding closing 
bracket in the correct order.

sample input = 

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False 

'''
def isBalanced(expression):
#Call an empty stack to store the opening brackets
    stack = []

    #Add a dictionary of the opening and closing brackets
    openBrackets = {
        "(",
        "{",
        "["
    }
    closeBrackets = {
        ")":
        "(",
        "}":
        "{",
        "]":
        "["
    }

    #