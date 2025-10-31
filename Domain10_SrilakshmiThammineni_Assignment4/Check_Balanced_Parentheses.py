def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':          # opening bracket
            stack.append(ch)
        elif ch in ')}]':        # closing bracket
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0
print(is_balanced("({[]})")) 
print(is_balanced("([)]"))    
print(is_balanced("{[()]}"))   
print(is_balanced("{[(])}"))  