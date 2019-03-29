import sys

def foo1(n):
    sum = 0
    for i in range(n+1):
        sum += i

    print("Suma brojeva je ", sum)

def foo2(n = int(sys.argv[1])):
    sum = 0
    for i in range(n+1):
        sum += i**2

    print("Suma kvadrata brojeva je ", sum)

def foo3():
    print("Unesi prvi string:")
    str1 = input()
    print("Unesi drugi string:")
    str2 = input()
    print(len(str2))
    print("Modifikovan string je", str1[0:3]*2 + str2[len(str2)-3:len(str2)]*2)

def foo4():
    lista = []
    for i in range(100):
        lista.append(i)

    j = 99
    while j>=0:
        print(lista[j])
        j -= 1


foo1(10)
foo2()
foo3()
foo4()
