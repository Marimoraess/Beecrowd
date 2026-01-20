R = int(input(), 16)
G = int(input(), 16)
B = int(input(), 16)

num_verdes = (R // G) ** 2
num_azuis_por_verde = (G // B) ** 2
num_azuis_total = num_verdes * num_azuis_por_verde

total = 1 + num_verdes + num_azuis_total

print(hex(total)[2:])
