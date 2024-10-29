def is_valid_sequence(sequence):
    stack = []
    brackets = {')': '(', ']': '['}
    
    for char in sequence:
        if char in brackets.values():  
            stack.append(char)
        elif char in brackets.keys():  
            if not stack or stack.pop() != brackets[char]:
                return "No"
    
    return "Yes" if not stack else "No"

print(is_valid_sequence(input("Введите последовательность: ")))