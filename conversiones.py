import sys

sol_peruano =float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
conver_Peso_chileno = float(sys.argv[4])

soles = sol_peruano * conver_Peso_chileno
argentino = peso_argentino * conver_Peso_chileno
dolar = dolar_americano * conver_Peso_chileno

print(f"Los {conver_Peso_chileno:.0f} pesos chilenos equivalen a:" )
print(f"{soles:.1f} soles" )
print(f"{argentino:.1f} Pesos Argentinos")
print(f"{dolar:.1f} Dólares")
