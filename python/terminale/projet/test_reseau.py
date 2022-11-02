import reseau


r1 = reseau.Reseau("192.168.20.34/24")
r2 = reseau.Reseau("172.16.1.220/16")
r3 = reseau.Reseau("192.154.88.133/26")
r4 = reseau.Reseau("131.108.78.235/21")

print(r1.nb_adresses())
print(r2.nb_adresses())
print(r3.nb_adresses())
print(r4.nb_adresses())
