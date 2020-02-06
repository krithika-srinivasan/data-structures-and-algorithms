def remove_blanx(s):
    output = []
    for c in s:
        if c == ' ':
           output.append('%20')
        else:
           output.append(c)

    return ''.join(output)


s = 'Muffy Unni'
print(remove_blanx(s))