def faktoriyel(n):
    return 1 if n <= 1 else n * faktoriyel(n - 1)

def yazdir(n):
    if n > 10:
        return
    print(f"{n}! = {faktoriyel(n)}")
    yazdir(n + 1)

yazdir(1)
