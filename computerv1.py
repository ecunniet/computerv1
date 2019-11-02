import sys

def all_ex(split, sign):
    nbrs = []
    start = 0
    print (sign)
    space_index = split.find(sign)
    while space_index != -1:
        nbrs.append(split[start:space_index])
        start = (space_index + 1)
        space_index = split.find(sign, start)
    nbrs.append(split[start:])
    return (nbrs)

def split_eq(eq):
    nbrs = []
    # separe les deux cotes
    j = 0
    split_half = eq.split('=')
    for split in split_half:
        nbrs.append(all_ex(split, "+"))
        for nb in nbrs[len(nbrs) - 1]:
            tmp = all_ex(nb, '-')
            if len(tmp) > 1:
                i = 0
                while i < len(tmp):
                nbrs[len(nbrs) - 1] = tmp[i][len(nbrs) - 1]all_ex(nb, '-')
                i++
    return ('hello')

# quand on lance le programme
if __name__ == "__main__":
    # verifier pas trop arguments? vous si 3 calculs possible en meme temps en bonus
    i = len(sys.argv)
    if i == 2:
        eq = split_eq(sys.argv[1])
        print(eq)
