def draw_line(length, label=''):
    line = '-' * length
    if label:
        line = line + label
    print(line)


def draw_interval(length):
    if length > 0:
        draw_interval(length - 1)
        draw_line(length)
        draw_interval(length - 1)


def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


inches = int(input('Inches on the ruler '))
length = int(input('Ticks on the inch markings '))
draw_ruler(inches, length)
