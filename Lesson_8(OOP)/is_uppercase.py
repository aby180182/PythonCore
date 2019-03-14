def is_uppercase(inp):
    for c in inp:
        if c.islower():
            return False
    return True