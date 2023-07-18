def solve(s):
    lst = []
    strng = ''
    repeat_count = 0
    for i in s:
        if i == '(':
            lst.append((strng, repeat_count))
            strng = ''
            repeat_count = 0
        elif i == ')':
            prev_strng, prev_rep = lst.pop()
            strng = prev_strng + strng * max(prev_rep, 1)
        elif i.isdigit():
            repeat_count = int(i)
        else:
            strng += i
    return strng
print(solve("k(a3(b(a2(c))))"))