def recursion(x): 
    print("Вызов №:",x)

    recursion(x + 1)
    recursion(1)

recursion(5)
