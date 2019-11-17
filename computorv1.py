#!/usr/bin/env python
# coding: utf-8
import sys
import re

def split_eq(eq):
    eq = re.sub("\s", '', eq)
    x = re.split("=", eq, 1)
    if len(x) < 2:
        print "There is a problem with your equation."
        sys.exit(0);
    side_1 = re.findall("(?:(?:-|[+])\s*)?(?:\d*\.)?\d+\s*\*\s*[xX](?:-|[+])?\^(?:-|[+])?(?:\d*\.)?\d+",x[0])
    side_2 = re.findall("(?:(?:-|[+])\s*)?(?:\d*\.)?\d+\s*\*\s*[xX]\^(?:-|[+])?(?:\d*\.)?\d+", x[1])
    for all in side_2:
        if float(re.findall("((?:(?:-|[+])\s*)?(?:\d*\.)?\d+)\s*\*\s*[xX]\^(?:-|[+])?(?:\d*\.)?\d+", all)[0]) != 0:
            if all[0] == '-':
                side_1.append('+' + all[1:])
            elif all[0] == '+':
                side_1.append('-' + all[1:])
            else:
                side_1.append('-' + all)
    return (side_1)

def reduce_eq(eq):
    new = []
    i = 0
    max = len(eq)
    while i < max:
        match = float(re.findall("[xX]\^((?:-|[+])?(?:\d*\.)?\d+)", eq[i])[0])
        j = i + 1
        count = float(re.findall("((?:(?:-|[+])\s*)?(?:\d*\.)?\d+)\s*\*\s*[xX]\^(?:-|[+])?(?:\d*\.)?\d+", eq[i])[0])
        while j < max:
            if(match == float(re.findall("[xX]\^((?:-|[+])?(?:\d*\.)?\d+)", eq[j])[0])):
                count = count + float(re.findall("((?:(?:-|[+])\s*)?(?:\d*\.)?\d+)\s*\*\s*[xX]\^(?:-|[+])?(?:\d*\.)?\d+", eq[j])[0])
                del eq[j]
                max -= 1
            else:
                j += 1
        new.append(count)
        i += 1
    i = 0
    str_tmp = "Reduced form: "
    while i < max:
        if new[i] == 0:
            while new[i] == 0:
                del new[i]
                del eq[i]
                max -= 1
                if max == i:
                    break
        if max <= i:
            break
        if i != 0 and new[i] > 0:
            str_tmp += " + "
        eq[i] = re.findall("([xX]\^(?:-|[+])?(?:\d*\.)?\d+)", eq[i])[0]
        if new[i] == int(new[i]):
            new[i] = int(new[i])
        str_tmp += str(new[i]) + " * X^" + str(int(float(re.findall("[xX]\^((?:-|[+])?(?:\d*\.)?\d+)", eq[i])[0])))
        i += 1
    str_tmp = re.sub("\s*-\s*", " - ", str_tmp)
    is_soluble([new, eq])
    print str_tmp + ' = 0'
    return [new, eq]

def check_degre(eq):
    count = 0
    for all in eq:
        tmp = int(float(re.findall("[xX]\^((?:-|[+])?(?:\d*\.)?\d+)", all)[0]))
        if count < tmp:
            count = tmp
    print "Polynomial degree: " + str(count)
    if count > 2:
        print "The polynomial degree is stricly greater than 2, I can't solve."
        sys.exit(0)
    return count

def is_soluble(double_tab):
    expo_0 = 0
    coef_0 = 0
    for eq in double_tab[1]:
        expo_recup = float(re.findall("[xX]\^((?:-|[+])?(?:\d*\.)?\d+)", eq)[0])
        if expo_recup < 0 or expo_recup != int(expo_recup):
            print "There is a problem with at least one of your exponents. I can only process positive integers as exponents."
            sys.exit(0)
        if int(float(re.findall("[xX]\^((?:-|[+])?(?:\d*\.)?\d+)", eq)[0])) != 0:
            expo_0 = 1
    for new in double_tab[0]:
        if new != 0:
            coef_0 = 1
    if coef_0 == 0 :
        print "The solution could be any real number."
        sys.exit(0)
    elif expo_0 == 0:
        print "There are no solution to this equation."
        sys.exit(0)

def find_coef(tab_1,tab_2):
    count = 0
    coef = [None, None, None]
    max = len(tab_2)
    while count < 3:
        i = 0
        while i < max:
            tmp = int(float(re.findall("[xX]\^((?:-|[+])?(?:\d*\.)?\d+)", tab_2[i])[0]))
            if tmp == count:
                coef[count] = tab_1[i]
            i += 1
        if coef[count] is None:
            coef[count] = 0
        count +=1
    return coef

def abs_1(nb):
    if nb < 0:
        nb *= -1
    if nb != 0:
        nb = (nb * nb) / nb
    return nb

def racine_carre(delta):
    x1 = (delta * 1.0) / 2
    x2 = (x1 + (delta / x1)) / 2
    while (abs_1(x1 - x2) > 0):
        x1 = x2
        x2 = (x1 + (delta / x1)) / 2
    return x2

def print_int_or_float(solution):
    if solution == int(solution):
        print(int(solution))
    else:
        print("%g" % solution)

def solve_the_equation(tab_1, tab_2):
    coef = find_coef(tab_1,tab_2)
    delta = coef[1] * coef[1] - 4 * coef[2] * coef[0]
    if delta > 0:
        print ("Discriminant is strictly positive, the two solutions are:")
        solution_1 = (- coef[1] - racine_carre(delta)) / (2 * coef[2])
        solution_2 = (- coef[1] + racine_carre(delta)) / (2 * coef[2])
        print_int_or_float(solution_1)
        print_int_or_float(solution_2)
    elif delta == 0:
        print("Discriminant is equal to zero, the solution is:")
        solution = (- coef[1]) / (2 * coef[2])
        print_int_or_float(solution)
    else:
        print ("Discriminant is strictly negative, this equations has no solutions in real numbers but two solutions in complex numbers that are:")
        print "(",
        if coef[1] != 0:
            print (- coef[1]),
        print "− i√(", -delta, ")) / ", (2 * coef[2]), ")"
        print "(",
        if coef[1] != 0:
            print (- coef[1]), "+",
        print "i√(", -delta, ")) / ", (2 * coef[2]), ")"
    return 0

if __name__ == "__main__":
    i = len(sys.argv)
    if i == 2:
        eq = split_eq(sys.argv[1])
        double_tab = reduce_eq(eq)
        degree = check_degre(double_tab[1])
        if degree == 2:
            solve_the_equation(double_tab[0], double_tab[1])
        else:
            coef = find_coef(double_tab[0],double_tab[1])
            print ("The solution is:")
            solution = 0.0
            if coef[0] != 0:
                solution -= coef[0]
            if coef[1] != 0:
                solution /= coef[1] * 1.0
            print_int_or_float(solution)
            sys.exit(0)
