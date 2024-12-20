from math import log

def bigger_product (u, v) :
    '''
    큰 정수 u, v를 곱하라 
    input :
    - int u, v : number
    output : result (= u * v)
    '''
    threshold = 4
    
    if ((u == 0) or (v == 0)) : return 0

    n = int(max(log(u, 10), log(v, 10)))
    if (n <= threshold) : return u * v

    m = 10 ** (n // 2)
    
    x = u // m; y = u % m
    a = v // m; b = v % m
    
    r = bigger_product(x+y, a+b)
    p = bigger_product(x, a)
    q = bigger_product(y, b)
    
    return p*(m**2) + (r-p-q)*m + q


if (__name__ == "__main__") :
    u = 123456789
    v = 987654321

    result = bigger_product(u, v)
    print(result)
    # result = 121932631112635269
