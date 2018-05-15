p = 2

while True:
    prime = True
    for n in range(2, p/2):
        if p % n == 0:
            prime = False
            break
    if prime:
        print (p)
    p += 1



