def my_var():
    var1 = 42
    var2 = "42"
    var3 = "quarante-deux"
    var4 = 42.0
    var5 = True
    var6 = [42]
    var7 = {42: 42}
    var8 = (42,)
    var9 = set()

    print(var1, "est de type", type(var1))
    print(var2, "est de type", type(var2))
    print(var3, "est de type", type(var3))
    print(var4, "est de type", type(var4))
    print(var5, "est de type", type(var5))
    print(var6, "est de type", type(var6))
    print(var7, "est de type", type(var7))
    print(var8, "est de type", type(var8))
    print(var9, "est de type", type(var9))

if __name__ == '__main__':
    my_var()
