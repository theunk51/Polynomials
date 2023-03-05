import re
import random
from colorama import Fore

def generate(ncases: int, store=False):
    cases = []
    for _ in range(ncases):
        degree = random.randint(0, 20)
        if degree == 0: 
            print(str(random.randint(-3000, 3000)))
        else:
            polystring = "".join(f'{random.randint(-3000,3000):+}x^{d}' for d in range(degree, -1, -1))
            polystring = re.sub(r"^\+|[+-]?(?<!\d)0x\^?\d*|x\^0|\^1(?!\d)", '', polystring)
            if not store:
                print(polystring)
            else: cases.append(polystring)
    return cases if store else None



def parse(poly: str):
    # make everything uniform
    poly = re.sub(r"x(?!\*{2})", "x**1", re.sub(r"(?<![\*\d])(\d+)(?![x\d])", r"\1x**0", poly))
    terms = re.findall(r"(-?\d*)x\*{2}(\d+)", poly)
    coeffs = [0] * (int(terms[0][1]) + 1)
    # print(Fore.GREEN, len(coeffs), Fore.RESET)
    for coeff, ex in terms:
        coeff = coeff+"1" if coeff in {'-',''} else coeff
       # print(Fore.CYAN, coeff, ex, Fore.RESET)
        coeffs[int(ex)] = int(coeff)

    return coeffs[::-1] # reverse to be in desc degrees
    re.sub()
    # (-?\d*)([a-zA-Z])(\^\d+)?|-?\d+
    #(-?\d*)x\^(\d+)

def divide(P1, P2):
    # P2 is always the divisor
    p1, p2 = parse(P1), parse(P2)
   # print(p1, p2)
    
    quotient: list[int|float] = [0] * max(len(p1)-len(p2)+1, 1) 
    divisor = p2[0]

    expo_diff = len(p1) - len(p2)
    for i in range(expo_diff+1):
        print(Fore.RED, i, Fore.RESET)
        # coefficient for the next quoitent
        mul_constant = p1[0] // divisor
        quotient[i] = mul_constant

        # multiplying by 0 is useless
        if mul_constant != 0:
            # subtract mul_constant * p2 from numerator
            for k in range(1, len(p2)):
                # index = exponential differnce of coeff and p2[k]
               # diffs = [u]
                p1[1] -= mul_constant * p2[k]
                
               #  print(Fore.BLUE, p1, quotient, mul_constant, Fore.RESET)
        p1.pop(0)   

    print( quotient, p1)
        



    # deg1 = len(p1) - 1
    # deg2 = len(p2) -1
   
    # quotient = [] # * max(len(p1)-len(p2)+1, 1)
    # print(deg1, deg2, len(quotient))
    # main_divisor = p2[0]
    
    # for i in range(deg1 - deg2 +1):
    #     print(Fore.GREEN, i, Fore.RESET)
    #     mul_constant = p1[i] // main_divisor
    #     quotient.append(mul_constant)

    #     if mul_constant != 0:    # useless to divide by 0
    #         # for cases where the divisor is not a monomial
    #         for k in  range(1, deg2):
    #             expo_diff = i + k   # b/c the list are reveresed
    #             p1[expo_diff] = -mul_constant * p2[k]
    #             print(Fore.BLUE, p1, expo_diff, mul_constant, Fore.RESET)
    #     # p1.pop(0)
    
    print(quotient, p1)






    # NOTE: remeber to reverse ahen done


    pass

divide('2x**4+5x**3-4x**2+x+1','x+1')  
