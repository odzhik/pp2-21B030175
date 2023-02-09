#Write a function that accepts string from user and print all permutations of that string.

def per(s):
    p = [''.join(p) for p in per(s)]
    return p
s = str(input())

print(per(s))