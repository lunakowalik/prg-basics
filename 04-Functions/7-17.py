def f(palindrome):
    return palindrome == palindrome[::-1]


print(f'f("radar") returns "{f("radar")}"')
print(f'f("12-11-21") returns "{f("12-11-21")}"')
print(f'f("book") returns "{f("book")}"')