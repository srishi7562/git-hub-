#  program that accepts an integer (n) and computes the value of n+nn+nnn.

b = int(input("Input the integer : "))

n1 = ("%s" % b)
n2 = ("%s%s" % (b, b))
n3 = ("%s%s%s" % (b, b, b))

print(n1 +n2 +n3)
