# Kata: https://www.codewars.com/kata/59d582cafbdd0b7ef90000a0/train/python

import re
from pprint import pprint
from typing import List, Tuple, Union



def to_polynomial(coefficients: List[Tuple[int, int]], variable) -> Union[None, str]:
    string = ''

    
    for c, e in coefficients:
        if e >= 2:
            string += f"{c:+}{variable}^{e}"
        elif e == 1:
            string += f"{c:+}{variable}"
        elif e == 0:
            string += f"{c:+}"
        
    string = re.sub(r'1(?=.*1)', '', string)
    if string[0] == '+':
        return string[1:]
    return string



def polynomial_product(P: str, Q: str) :
    # matches terms inside polynomial
    poly_regex = r'([-]?(?:(?:\d+[a-zA-Z]\^\d+)|(?:\d+[a-zA-Z])|(?:\d+)|(?:[a-zA-z](?:\^\d+)?)))'
    # coeff_regex = r"(?P<coeff>[-]?(?:(?:\d+)|(?:(?<!\d)[a-zA-Z])))"
    # power_regex = r"(?P<expo>(?:(?<=\^)\d+))"
    term_regex = r"(?P<coeff>-?(?:(?:\d+)|(?:(?<!\d)[A-Za-z])))\w?\^(?P<expo>(?<=\^)\d+)"

    pattern = re.compile(poly_regex)
    term_pattern = re.compile(term_regex)

    # remove spaces to prevent errors
    P, Q = re.sub(r'\s', '', P), re.sub(r'\s', '', Q)
  
    p_terms = pattern.findall(P)
    q_terms = pattern.findall(Q)
    # all_terms  = p_terms + q_terms
    # pprint(all_terms)

    # doesn't matter which poloynomial is searched since both have the same variable
    variable = re.search(r'\w', P)
    if variable: variable = variable.group()
    print(variable)

    # coefficient and exponential logic
    # returnListType = Union[List[Tuple[int, int]], None]

    def terms_to_tuple(termList: List[str]):
        """ 
            Converts a list of string terms into a tuple denoting
            the coefficient and exponent of the term in thhat respective order

            :return: List[Tuple(int, int)]
        """
        broken_terms = []

        for term in termList:
            # terms like 2u, 24x, 27xy are single terms
            if re.match(r'-?\d+\w', term) and term[-1].isalpha():
                coeff = re.match(r'-?\d+', term).group()
                broken_terms.append((int(coeff), 1))

            # in the case a term is just a variable like x or -A
            # these are still single terms
            elif re.match(r'-?[a-zA-Z]', term) and 0 < len(term) < 3:
                coeff = -1 if term[0] == '-' else 1
                broken_terms.append((coeff, 1))
            
            # 20, 1/2, -86 are constants
            elif re.match(r'-?\d+$', term):
                broken_terms.append((int(term), 0))
            
            # everthing else has an exponent like 3x^3, a^2, -u^6 
            else:
                coeff, exponent = term_pattern.match(term).groups()
                if coeff[-1].isalpha():     # there is no coeffiecent before variable
                    coeff = -1 if coeff[0] == '-' else 1
                else:
                    coeff = int(coeff)
                
                broken_terms.append((coeff, int(exponent)))
            
        
        # sort the terms by degree before returning
        broken_terms.sort(key=lambda x: x[1], reverse=True)
        return broken_terms
    
    # redefine P-terms and Q-terms with the broken terms
    p_terms[:] = terms_to_tuple(p_terms)
    q_terms[:] = terms_to_tuple(q_terms)

    # print(p_terms, q_terms)


    # multiplication logic
    # The answer will have terms to the highest added degree.
    # Therefore len(result) = highest degree of 1st poly + highest degree of 2nd poly + 1
    #   * +1 because of the constant is not covered by the degree
    # the index denotes the degree of the new term 
    answer = [0] * (p_terms[0][1] + q_terms[0][1] + 1)
    
    for (coeff, expo) in p_terms:
        # multiply each term to the others in the second polynomial
        for (coeff2, expo2) in q_terms:
            answer[expo+expo2] += coeff * coeff2

    print(answer)
    answer_in_terms = [(answer[i], i) for i in range(len(answer)-1, -1, -1) if answer[i]!=0]
    print(answer_in_terms)

    return answer_in_terms, variable #to_polynomial(answer_in_terms, variable)

p = "B^49+17B^32+32B^10-27B^14-46B^26-B^3-38B^15-B^31+32B^22-B^9-B^7+18B^23+20B^40+26B^30-B^5-B+6B^44-B^13+27B^6-1+3B^16-B^25-7B^33+11B^34+29B^8+41B^36"
q = "B^35-B^9+20B^15+26B^25-13B^31-B^8+B^20-5+37B^13-9B^43-6B^32-48B^41+29B^30+23B^5+B^42+28B^14-B^38-17B^27+B^19+42B^36-47B^48+5B^33-4B^26+15B^23-3B-B^40+45B^37-B^16-B^47+B^2+21B^28+B^24+29B^10"
expected = '270b^98+15b^97+828b^96+46b^95-540b^94-270b^93-1671b^92-1488b^91+839b^90-2079b^89-331b^88-340b^87-2660b^86-1170b^85+197b^84-2149b^83+761b^82+189b^81-1068b^80-236b^79-1782b^78-1202b^77-1317b^76-1449b^75+981b^74+1044b^73+550b^72+2108b^71-711b^70+973b^69-919b^68-403b^67-3508b^66-964b^65-1710b^64+635b^63-2296b^62+1162b^61-1043b^60+1824b^59+558b^58+2201b^57+783b^56+250b^55-324b^54-1201b^53-3829b^52+1710b^51-995b^50-833b^49-2478b^48+1095b^47-850b^46-1018b^45+2198b^44-3037b^43-1732b^42-294b^41+304b^40-2325b^39+10b^38+493b^37+793b^36-781b^35-1524b^34-335b^33+1502b^32-180b^31+969b^30+837b^29+2491b^28-1458b^27-1289b^26-2368b^25+3093b^24-1200b^23-1676b^22-2516b^21+1032b^20+340b^19+1841b^18+636b^17-1102b^16+393b^15-71b^14-138b^13+316b^12+290b^11+1265b^10-2304b^9-1885b^8+2025b^6-288b^5+30b^4-1215b^2-225b'
ans, vari = polynomial_product(p, q)
got = to_polynomial(ans, vari)

assert got == ans, ValueError()

#polynomial_product('u^2-1', '2u + 1')


#print(to_polynomial([(2, 3), (1, 2), (-2, 1), (-1, 0)], 'u'))
