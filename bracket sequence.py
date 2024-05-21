def is_valid_bracket_sequence(sequence):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()

    return not stack

#[((())()(())]] incorrect
#[(())()(())] correct

sequence = input("Enter brackets sequence: ")
is_valid = is_valid_bracket_sequence(sequence)
print("Is the sequence correct?", is_valid)

def fix_bracket_sequence(sequence):
    stack = []
    result = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.append(char)
            result.append(char)
        elif char in ')]}':
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
                result.append(char)
            else:
                continue

    while stack:
        open_bracket = stack.pop()
        if open_bracket == '(':
            result.append(')')
        elif open_bracket == '[':
            result.append(']')
        elif open_bracket == '{':
            result.append('}')

    return ''.join(result)

fixed_sequence = fix_bracket_sequence(sequence)
print("Fixed sequence:", fixed_sequence)