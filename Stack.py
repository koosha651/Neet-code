# NeetCode Challenge
# Solving Problems from NeetCode website, Stack


1. Valid Parentheses

def parentheses(s):
    stack = []
    closeToOpen = {']': '[', ')' : '(', '}' : '{'}

    for c in s:
        if c in closeToOpen:  # If the 'c' considers as closing character, because the keys in dictionary are closing character
            if stack and stack[-1] == closeToOpen[c]:     # if stack passed when stack was not empty, also it make sure at top of stack the 'c' maching the open parantheses
                stack.pop()
            else:
                return False

        else:              # only we append the opening parantheses charecter and move forward
            stack.append(c)

    return True if not stack else False         # if not stack = if stack was empty


s='}()[]'
parentheses(s)

output: False



#=============================================================================================================================================================================
  
