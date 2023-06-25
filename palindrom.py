a = input()

def palicheck(a):
    def reverse_string(s):
        return "".join(reversed(s))
    if a == reverse_string(a):
        print(True)
    else:
        print(False)
palicheck(a)



