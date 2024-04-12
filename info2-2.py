
IDVLAN = int(input("Cual es el número de Vlan? "))
if IDVLAN >= 1 and IDVLAN <= 1005:
    print("Este es UNA Vlan de rango normal.")
elif IDVLAN >=1006 and IDVLAN <= 4095:
    print("Este es una vlan de rango extendido")
else:
    print("la vlan es desconocida.")