# -*- coding: utf-8 -*-
"""
Lucía Revaliente i Aránzazu Miguélez

Programació: Pràctica 2 - Hotels
"""

# LLIBRERIES
import math

from Practica2_1 import codi_in_llista_hotels, importar_hotels, importar_barris, importar_districtes, omplir_llista_barris, mostrar_hotels
from Practica2_2 import ordenar_per_estrelles, mostrar_noms_hotels, buscar_per_nom, buscar_per_estrelles, buscar_hotels, hotel_mes_proper
from Practica2_3 import ordenar_per_nom, carrers_amb_hotels, estrelles_per_barri, densitat_per_districte, afegir_prefixe_int, modificar_telefons

# MENU MAIN
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---\n1 - Veure hotels\n2 - Veure hotels per estrelles\n3 - Buscar hotels\n4 - Buscar hotel proper\n5 - Llistat alfabètic d'hotels\n6 - Carrers amb hotels\n7 - Estadística per barris\n8 - Estadística per districtes\n9 - Internacionalitzar telèfons\nS - Sortir del programa")

# MAIN
# Inicialització
RADI_TERRA = 6378.137

# Codi principal
try:
    hotels = importar_hotels("hotels.csv",";")
    dicc_barris= importar_barris("barris.csv",";")
    dicc_districtes= importar_districtes("districtes.csv",";")
except FileNotFoundError as missatge:
    print("Error llegint fitxers: ", missatge)
except TypeError as ex:
    print("Error processant els fitxers: ", ex) 
else:
    omplir_llista_barris(dicc_barris, dicc_districtes)
    opcio= "w"
    while opcio!="s" and opcio!="S":
        mostrar_menu()
        opcio = input("Introdueix l'opció: ")
        if opcio == "1":
            mostrar_hotels(hotels)
            mostrar_menu()
            opcio=input("Introdueix l'opció: ")
            
        elif opcio == "2":
            h = ordenar_per_estrelles(hotels)
            mostrar_hotels(h)
            
        elif opcio == "3":
            buscar_hotels(hotels)
            
        elif opcio == "4":
            try:
                latitud = float(input("Introdueix latitud: "))
                longitud = float(input("Introdueix longitud: "))
            except:
                ValueError("Error: latitud i longitud han de ser valors reals")
            else:
                  hotel,distancia= hotel_mes_proper(hotels,latitud,longitud)
                  print("L'hotel més proper és el",hotel,"a",distancia,"kms")
                  
        elif opcio == "5":
            ordenar = ordenar_per_nom(hotels)
            mostrar_hotels(ordenar)
            
        elif opcio == "6":
            ll_carrers=carrers_amb_hotels(hotels)
            total_carrers = len(ll_carrers)
            print("Hi ha ", total_carrers," carrers amb algun hotel: ",ll_carrers)
            
        elif opcio == "7":
            dicc = estrelles_per_barri(hotels,dicc_barris)
            print(dicc)
            for nom_barri, llista in dicc.items():
                sortida = nom_barri + ": " + str(llista[0]) + " hotels de 1 estrelles, " + str(llista[1]) + " hotels de 2 estrelles, " + str(llista[2]) + " hotels de 3 estrelles, " + str(llista[3]) + " hotels de 4 estrelles, " + str(llista[4]) + " hotels de 5 estrelles"
                print(sortida)
                
        elif opcio == "8":
            dicc = densitat_per_districte(hotels,dicc_barris, dicc_districtes)
            #print(dicc)
            for codi_districte, densitat in dicc.items():
                sortida = "Distrcicte " + str(codi_districte) + ": " + str(densitat) 
                print(sortida)
            
        elif opcio == "9":
            modificar_telefons(hotels)
            mostrar_hotels(hotels)
        
        elif opcio not in "12345678Ss":
            print("Opció no permesa.")

finally:
    print("Sortint del programa")