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
    i = 0
    str_tmp = "Reduced form: "
    while i < max:
        if new[i] == 0:
            del new[i]
            del eq[i]
            max -= 1
        if i != 0 and new[i] > 0:
            str_tmp += " + "
        eq[i] = re.findall("([xX]\^\d+)", eq[i])[0]
        str_tmp += str(new[i]) + " * " + eq[i]
        i += 1
    str_tmp = re.sub("\s*-\s*", " - ", str_tmp)
    print str_tmp + ' = 0'
    return [new, eq]

def check_degre(eq):
    count = 0
    for all in eq:
        tmp = int(re.findall("[xX]\^(\d+)", all)[0])
        if count < tmp:
            count = tmp
    print "Polynomial degree: " + str(count)
    if count > 2:
        print "The polynomial degree is stricly greater than 2, I can't solve."
        sys.exit(0)
    return count

def find_coef(tab_1,tab_2):
    count = 0
    coef = [None, None, None]
    max = len(tab_2)
    while count < 3:
        i = 0
        while i < max:
            tmp = int(re.findall("[xX]\^(\d+)", tab_2[i])[0])
            if tmp == count:
                coef[count] = tab_1[i]
            i += 1
        if coef[count] is None:
            coef[count] = 0
        count +=1
    print coef,
    return coef

def racine_carre(delta):
    x1 = (delta * 1.0) / 2 #le nombre max de la racine  1
    x2 = (x1 + (delta / x1)) / 2
    while (abs(x1 - x2) > 0):
        x1 = x2                        #on le passe parce que ce seront les meme resultats de toute facon
        x2 = (x1 + (delta / x1)) / 2 # la racine est trouve quand 9 / 3 = 3 et 3 + 3 /2  = 3
    return x2

def solve_the_equation(tab_1, tab_2):
    coef = find_coef(tab_1,tab_2)
    delta = coef[1] * coef[1] - 4 * coef[2] * coef[0]
    if delta > 0:
        solution_1 = (- coef[1] - racine_carre(delta)) / (2 * coef[2])
        solution_2 = (- coef[1] + racine_carre(delta)) / (2 * coef[2])
        print("%.6f" % solution_1)
        print("%.6f" % solution_2)
    elif delta == 0:
        solution = (- coef[1]) / (2 * coef[2])
        print solution
    else:
        print "pas de solution"
    return 0

# quand on lance le programme
if __name__ == "__main__":
    # verifier pas trop arguments? vous si 3 calculs possible en meme temps en bonus
    i = len(sys.argv)
    if i == 2:
        eq = split_eq(sys.argv[1])
        double_tab = reduce_eq(eq)
        degree = check_degre(double_tab[1])
        if degree == 2:
            solve_the_equation(double_tab[0], double_tab[1])
        else:
            print "a faire plus tard"
