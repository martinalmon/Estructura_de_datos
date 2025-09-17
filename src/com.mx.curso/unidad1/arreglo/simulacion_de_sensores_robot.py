#simulamos ña entrada de sensores con esta lista 
sensores=[120, 85, 210, 150]

#hacemos un loop que recorra las lecturas de la lista, 
# con condicionales para que dependiendo ddel parametro muestre la alerta o no 
for valor  in sensores:
    
    if valor < 100:#condicional para alerta..
        print(f"¡¡ALERTA!! colisión inminente, distancia:{valor}")
    else :
        print(f"sin riesgo de colision distancia segura de {valor}")