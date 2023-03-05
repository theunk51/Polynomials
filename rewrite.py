import re

def polynomial_product(P: str, Q: str):
    # matches terms inside a polynomial string
    poly_regex = r'([-]?(?:(?:\d+[a-zA-Z]\^\d+)|(?:\d+[a-zA-Z])|(?:\d+)|(?:[a-zA-z](?:\^\d+)?)))'
    # finds the coefficient and degree of a term
    term_regex = r"(?P<coeff>-?(?:(?:\d+)|(?:(?<!\d)[A-Za-z])))\w?\^(?P<expo>(?<=\^)\d+)"

    pattern = re.compile(poly_regex)
    term_pattern = re.compile(term_regex)

    # both strings need to be checked for cases like P='1' and Q='76e^5'
    if (variable := re.search(r'[a-zA-Z]', P)) is not None:
        variable = variable.group()
    else:
        if (variable := re.search(r'[a-zA-Z]', Q)) is not None:
            variable = variable.group()
    
    # no variable means 2 constants
    if variable == None:
        return str(int(P) * int(Q))

    # remove spaces to prevent errors
    P, Q = re.sub(r'\s{1,}', '', P), re.sub(r'\s', '', Q)

    p_terms = pattern.findall(P)
    q_terms = pattern.findall(Q)

    def terms_to_tuple(termList: list[str]):
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

    p_terms[:] = terms_to_tuple(p_terms)
    q_terms[:] = terms_to_tuple(q_terms)
    
    # multiplication logic
    # The answer will have terms to the highest added degree.
    # Therefore len(result) = highest degree of 1st poly + highest degree of 2nd poly + 1
    #   * +1 because of the constant is not covered by the degree
    # the index denotes the degree of the new term 
    answer = [0] * (p_terms[0][1] + q_terms[0][1] + 1)
    
    for (coeff, expo) in p_terms:
        # multiply each term in the second polynomial
        for (coeff2, expo2) in q_terms:
            answer[expo+expo2] += coeff * coeff2

    polystring = ''
    for e in range(len(answer)-1, -1, -1):
        if answer[e] != 0:
            c = answer[e]
            # placed here to remove teh hassle of regex
            if c in (1, -1) and e >= 1:
                c = "+" if c == 1 else "-"
                polystring += f"{c}{variable}" if e == 1 else f"{c}{variable}^{e}"
            elif e == 0:
                polystring += "%+s" % str(c)
            elif e == 1:
                polystring += f"{c:+}{variable}"
            else:
                polystring += f"{c:+}{variable}^{e}"
    
    if polystring == '': 
        return '0'
    elif polystring[0] == "+":
        return polystring[1:]
    return polystring

   


P = "13L+49L^8-31L^25+25L^6-16L^29+6L^34-L^16+L^45-13L^12+32L^13-20L^2-L^43+28L^4+29L^38-L^18-40L^42+44L^49"
Q = "44L^14+5L^5-L^16-19L^36+L^44-37L^28-37L^10-4L^37+L^34-L^17-41L^40+29L^31+47L^46-36L^3-24L-16L^27-42L^47-L^35-11L^12+19L^19-18L^38-12L^30-30L^24-40L^45+6L^25-7L^7-18L^43"
excepted = '-1848L^96+2068L^95-1760L^94+44L^93-834L^92+47L^91+2L^90-170L^89-1858L^88+807L^87-198L^86-1375L^85+1319L^84-1093L^83+1665L^82-775L^81+2281L^80-588L^79-422L^78-1697L^77-565L^76-880L^75+78L^74-2550L^73+1975L^72-1444L^71+2628L^70+2070L^69+1046L^68+78L^67+147L^66+1283L^65-84L^64+2734L^63-1036L^62-694L^61-1777L^60+722L^59-1990L^58+1640L^57-3241L^56-1503L^55+2875L^54-2539L^53+3436L^52-3639L^51-109L^50-105L^49-4394L^48+723L^47-2449L^46+1446L^45-2585L^44-499L^43+107L^42-2739L^41-148L^40+9L^39-40L^38-434L^37-1644L^36+1026L^35-1340L^34-685L^33-531L^32-701L^31+154L^30-12L^29+129L^28+2219L^27+887L^26-309L^25+94L^24-675L^23+2612L^22-377L^21+556L^20+171L^19-689L^18-54L^17-3265L^16+697L^15-1584L^14+239L^13+740L^12-2316L^11-1796L^9-91L^8-1708L^7+65L^6+48L^5-468L^4+480L^3-312L^2'


# x = polynomial_product('u^2-1', '2u +1')
#x = polynomial_product('5u-1', '5u+1')
x = polynomial_product(P, Q)
print(x)

