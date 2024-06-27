def is_valid_parentheses(str):
    stack = []
    closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
    
    for c in str:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False

print(is_valid_parentheses("()"))        # True
print(is_valid_parentheses("([)]"))      # False
