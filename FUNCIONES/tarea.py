def fibonari(n):
    print("ingrese el numero")
    if n < 2:
        return n
    else:
     # fn = fn-1 + fn-2
         return fibonari(n-1) + fibonari(n-2)
    