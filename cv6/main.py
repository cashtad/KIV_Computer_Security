

# p = 99
# e = 27
# d = 83
# n = 319
# x = 280
# print(p)
# # c = p ^ e % n
# c = pow(p,e) % n
# print(f"{p} -> {c}")
# p = pow(c,d) % n
# print(f"{c} -> {p}")
# c = 133
# e = 27
# d = 83
# n = 319
# x = 280
# p = pow(c,d) % n
# print(f"{c} -> {p}")

Pvelke = 55
p = 107
g = 3
x = 61
k = 27

print("P = " + str(Pvelke))


y = pow(g,x) % p
print("y = " + str(y))

K = pow(y,k) % p
print("K = " + str(K))

Ca = pow(g,k) % p
print("Ca = " + str(Ca))

Cb = (Pvelke * K) % p
print("Cb = " + str(Cb))

#dec
print("dec")

K = pow(Ca,x) % p
print("K = " + str(K))

Kinv = 37

Pvelke = Kinv * Cb % p
print("P = " + str(Pvelke))


