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

    #Create a for loop that will loop through each character in the expression
    for bracket in expression:
        if bracket in openBrackets:  
            stack.append(bracket)  

        elif bracket in closeBrackets: 
            if len(stack) == 0 or stack[-1] != closeBrackets[bracket]:
                # If the stack is empty or the top of the stack does not match the corresponding opening bracket then expression is not balanced
                return False 
            # Pop the matching opening bracket from the stack
            stack.pop()  
    
    # After iterating through all characters, check if the stack is empty if it's empty the expression is balanced
    return len(stack) == 0  

expression1 = "([]{})"
expression2 = "([)]"
print(isBalanced(expression1))  # Output: True
print(isBalanced(expression2))  # Output: False