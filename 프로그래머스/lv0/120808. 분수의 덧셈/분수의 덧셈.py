def solution(numer1, denom1, numer2, denom2):
    a = (numer1*denom2)+(numer2*denom1)
    b = denom1 * denom2
    
    for i in range(1, a + 1):
        if (b % i == 0) & (a % i == 0):
            gcd = i

    answer = [a/gcd, b/gcd]

    return answer