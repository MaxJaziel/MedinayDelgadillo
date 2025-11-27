frios = 0
calidos = 0
templados = 0
muycaluroso = 0
promedio = 0
maxima = 0
minima = 100
n = int(input("Numero de dias a registrar:"))
for i in range (1 , n + 1):
    temperatura = float(input(f"Ingrese la temperatura:"))
    if temperatura > maxima:
        maxima = temperatura
    if temperatura < minima:
        minima = temperatura
    if temperatura <10:
        frios += 1
    elif temperatura <24.9 and temperatura >10:
        templados += 1
    elif temperatura >24.9 and temperatura<34:
        calidos += 1
    elif temperatura >= 35:
        muycaluroso += 1
    promedio = promedio + temperatura 
promediof = promedio / n         
print("1.Mostrar promedio ,maxima y minima")
print("2.Mostrar conteo y porcentaje por categoria")
print("3.Clasificar promedio")
opcion= int(input("Elige una opcion:"))
match opcion:
    case 1:
        print(f"\nEl promedio es:{promediof}°\nLa maxima temperatura es {maxima}° y la minima {minima}°")
    case 2:
        print(f"\nDias frios:{frios}")
        print(f"Dias templados:{templados}")
        print(f"Dias calidos:{calidos}")
        print(f"Dias muy calurosos:{muycaluroso}")
        porcentajef = frios * 100 / n
        porcentajet = templados * 100 / n
        porcentajec = calidos * 100 / n
        porcentajemuyc = muycaluroso * 100 / n
        print("\nPorcentaje Total:")
        print(f"{porcentajef}% Frios")
        print(f"{porcentajet}% Templados")
        print(f"{porcentajec}% calidos")
        print(f"{porcentajemuyc}% muy calurosos")
    case 3:
        if promediof <10:
            print("El promedio es frio")
        elif promediof >10 and promediof <24.9:
            print("El promedio es templado")
        elif promediof >25 and promediof <35:
            print("El promedio es calido")
        elif promediof >= 35:
            print("El promedio es muy caluroso")
