def foo():
    print("hello from foo()")

def bar(par1, par2 ="par2"):
    print("par1_val=", par1, "par2_val=",par2)

if __name__ == "__main__":
    print("hello world!")
    foo()
    for i in range(0,100,5):
        if i % 10 == 0:
            bar(i, par2="svaki drugi")
