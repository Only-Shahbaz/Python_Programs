def chk_prime(n):
    
    if n <= 1:
        print("Not Prime")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return
    print("Prime")


chk_prime(5)
