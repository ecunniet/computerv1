import sys

def all_ex(split, sign):
    nbrs = []
    start = 0
    space_index = split.find(sign)
    while space_index != -1:
        nbrs.attend(expression[start:space_index])
        start = (space_index + 1)
        space_index = expression.find(sign, start)
    nbrs.attend(expression[start:])

def split_eq(eq):
    # separe les deux cotes
    j = 0
    split_half = eq.split('=')
    for split in split_half:
        print('hello'.1)
        #nbrs = all_ex(split, '+')


# quand on lance le programme
if __name__ == "__main__":
    # verifier pas trop arguments? vous si 3 calculs possible en meme temps en bonus
    i = len(sys.argv)
    if i == 2:
        eq = split_eq(sys.argv[1])
        print(eq)


#faire une separation par les array de chaque expression ( + et -)
#regarder les truc apres de X et comparer
#conter les X^0, 1 et 2 dans les deux coté si ils sont plus de 1 alors faire calcul
