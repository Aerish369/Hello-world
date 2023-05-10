def div (a,b):
    print(a/b)

def rev(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a, b)
    return inner

div = rev(div)
    
div(2,4)
    