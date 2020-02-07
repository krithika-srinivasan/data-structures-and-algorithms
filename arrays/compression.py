def compression(s):
    stack = []
    output = []
    for c in s:
        if len(stack) == 0 or c == stack[-1]:
            stack.append(c)
        else:
            count = 0
            char = stack[-1]
            while len(stack) > 0:
                stack.pop()
                count +=1
            app = char + str(count)
            output.append(app)
            stack.append(c)
    if len(stack) > 0:
        count = 0
        char = stack[-1]
        while len(stack) > 0:
            stack.pop()
            count += 1
        app = char + str(count)
        output.append(app)

    result = ''.join(output)
    if len(result) < len(s):
        return result
    else:
        return output

s = 'aaaabbbcddd'
print(compression(s))