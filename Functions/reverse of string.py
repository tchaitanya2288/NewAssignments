def rev_str(a_str):
    new_str = ''
    index   = len(a_str)
    while index:
        index -= 1
        new_str += a_str[index]
    return new_str
print(rev_str("Aws123"))