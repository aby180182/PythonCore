def sorter(textbooks):
    textbooks.sort(key=lambda v: v.upper())
    return textbooks