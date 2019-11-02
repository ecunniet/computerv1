import sys
import re

def split_eq(eq):
    eq = re.sub("\s", '', eq)
    x = re.split("=", eq, 1)
    print x
    side_1 = re.findall("(?:(?:-|[+])\s*)?(?:\d*\.)?\d+\s*\*\s*[xX]\^\d+",x[0])
    side_2 = re.findall("(?:(?:-|[+])\s*)?(?:\d*\.)?\d+\s*\*\s*[xX]\^\d+", x[1])
    for all in side_2:
        if all[0] == '-':
            side_1.append('+' + all[1:])
        elif all[0] == '+':
            side_1.append('-' + all[1:])
        else:
            side_1.append('-' + all)
    for expression in side_1:
        print expression,
    print '= 0'
    return (side_1)

def reduce_eq(eq):
    new = []
    i = 0
    max = len(eq)
    while i < max:
        match = re.findall("[xX]\^(\d+)", eq[i])[0]
        j = i + 1
        count = float(re.findall("((?:(?:-|[+])\s*)?(?:\d*\.)?\d+)\s*\*\s*[xX]\^\d+", eq[i])[0])
        print count
        while j < max:
            if(match == re.findall("[xX]\^(\d+)", eq[j])[0]):
                count = count + float(re.findall("((?:(?:-|[+])\s*)?(?:\d*\.)?\d+)\s*\*\s*[xX]\^\d+", eq[j])[0])
                print j,
                print " = ",
                print count
                print eq
                del eq[j]
                print eq
                max -= 1
                print max
            else:
                j += 1
        new.append(count)
        i += 1
    print new
    return 0
# quand on lance le programme
if __name__ == "__main__":
    # verifier pas trop arguments? vous si 3 calculs possible en meme temps en bonus
    i = len(sys.argv)
    if i == 2:
        eq = split_eq(sys.argv[1])
        reduce_eq(eq)
