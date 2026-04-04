edad : int = 18
altura : float = 1.8
nom : str = "Carlos"
ape = 'Chan'
esVerde : bool = False

print(f"{nom} {ape} tiene {edad+10} años y su carro {"es" if esVerde else "no es"} verde")

print(f"su altura es {altura}")

#operador ternario
"""
es = "Mayor edad" if edad > 18 else "niño"
"""