# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 12:33:47 2022

@author: User
"""

from Practica2_1 import Hotel, codi_in_llista_hotels, importar_hotels, Barri, importar_barris, Districte, importar_districtes, omplir_llista_barris, mostrar_hotels
from Practica2_2 import ordenar_per_estrelles, mostrar_noms_hotels, buscar_per_nom, buscar_per_estrelles, buscar_hotels, hotel_mes_proper

# EXERCICI 3.1 -- FUNCIONA
def ordenar_per_nom(hotels):  
    return sorted(hotels, key = lambda x: x.nom.lower())

"""    
PROVA EX 3.1 
         
a=(ordenar_per_nom(hotels))
for x in a:
    print(x)
"""


# EXERCICI 3.2 -- FUNCIONA
def carrers_amb_hotels(ll_hotels):
    carrers = set()
    for hotel in ll_hotels:
        carrers.add(hotel.carrer)
    return list(carrers)

"""
PROVA 3.2:
    
res = importar_hotels("hotels.csv", ";")
for hotel in res:
    print(hotel.carrer)
res2 = carrers_amb_hotels(res)
print(res2)
"""

# EXERCICI 3.3 -- FUNCIONA
def estrelles_per_barri(ll_hotels, dicc_barris): #key: codi barri, #objecte: nom, codi districte
    #for x in ll_hotels:
        #print(x)
    #print(dicc_barris)
    dicc = {}
    for hotel in ll_hotels:
        #print(hotel)
        codi_barri = hotel.codi_barri
        #print(codi_barri)
        estrelles = hotel.estrelles
        #print(estrelles)
        nom_barri = dicc_barris[codi_barri].nom
        #print(nom_barri)

        if nom_barri not in dicc:
            dicc[nom_barri]=[0,0,0,0,0]
        
        dicc[nom_barri][estrelles-1] +=1
        
    return dicc

"""
PROVA 3.3:
   
res = estrelles_per_barri(importar_hotels("hotels.csv", ";"), importar_barris("barris.csv", ";"))
print("resultat:",res)
"""


# EXERCICI 3.4  - FUNCIONA
def densitat_per_districte(hotels,dicc_barris, dicc_districtes):  #key codi_districte valor densitat hotels que té el districte
    dicc ={}
    for hotel in hotels:
        #print(hotel, hotel.codi_barri, dicc_barris[hotel.codi_barri].codi_districte)
        codi_districte = dicc_barris[hotel.codi_barri].codi_districte
        #print(codi_districte)
        if codi_districte not in dicc:
            dicc[codi_districte] = 0
        dicc[codi_districte]+=1
        #print(dicc)
        for codi_districtes in dicc:
            dicc[codi_districte] = dicc[codi_districtes] / dicc_districtes[codi_districtes].extensio
        
    return dicc
"""
PROVA 3.4  

res = densitat_per_districte(importar_hotels("hotels.csv",";"),importar_barris("barris.csv",";"), importar_districtes("districtes.csv",";"))
print(res)
"""


# EXERCICI 3.5
def afegir_prefixe_int(hotel):
    #print(hotel.telefon)
    if hotel.telefon != "+":
        hotel.telefon = "+34" + hotel.telefon
    #print(hotel.telefon)

"""
PROVA 3.5:
     
a = Hotel("Hotel H10 Itaca","HB-004151","Roma",22,9,"08015","932265594",41.381193,2.145467,4)
print(a)
afegir_prefixe_int(a)
print(a)
"""

# EXERCICI 3.6
def modificar_telefons(ll_hotels):
    #for x in ll_hotels:
        #print(x)
    list(map(afegir_prefixe_int, ll_hotels))
    #for x in ll_hotels:
        #print(x)

"""
PROVA 3.6:
    
res = importar_hotels("hotels.csv", ";")
for x in res:
    print(x)
print()
modificar_telefons(res)
for x in res:
    print(x)
"""