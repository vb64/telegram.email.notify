def ecode(text):
    try:
        return text.encode('utf-8')
    except UnicodeDecodeError:
        return text


def remove_new_lines(source):
    sequence = True
    lines = []
    for line in source.splitlines():
        if line.strip():
            lines.append(line)
            sequence = False
        else:
            if not sequence:
                lines.append('')
                sequence = True

    return '\n'.join(lines)


def remove_line_with(source, mask):
    i = source.find(mask)
    if i == -1:
        return source

    i1 = source.rfind('\n', 0, i)
    if i1 == -1:
        return source

    i2 = source.find('\n', i)
    if i2 == -1:
        return source

    return source.replace(source[i1:i2], '')
