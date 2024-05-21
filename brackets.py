def valid_bracket(sequence):
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
is_valid = valid_bracket(sequence)
print("Is the sequence correct?", is_valid)


def fix_bracket(sequence):
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


fixed_sequence = fix_bracket(sequence)
print("Fixed sequence:", fixed_sequence)
