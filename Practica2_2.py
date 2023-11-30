"""
Created on Thu Dec 15 14:25:43 2022

Lucía R i Aránzazu
"""

from Practica2_1 import codi_in_llista_hotels, importar_hotels, importar_barris, importar_districtes, omplir_llista_barris, mostrar_hotels

# EXERCICI 2.1 -- FUNCIONA
def ordenar_per_estrelles(ll_hotels):
    return sorted(ll_hotels.copy())

"""
PROVA PER COMPROVAR 2.1:
        
with open("hotels.csv", "w") as Hotels:
    Hotels.write("EQUIPAMENT;NOM_CARRER;NUM_CARRER_1;CODI_BARRI;CODI_POSTAL;TELEFON_NUM;LATITUD;LONGITUD;NIVELL_ESTR.\nHotel Amrey Sant Pau - HB-004046;Sant Antoni Maria Claret;173;35;8041;934335151;41414013;2177888;2\nHotel Amrey Sant Pau - HB-004046;Sant Antoni Maria Claret;173;35;8041;934335151;41414013;2177888;2\nHotel Sansi Pedralbes - HB-004086;Pearson;1;21;8034;932063880;41393699;2111575;4\nHotel Sansi Pedralbes - HB-004086;Pearson;1;21;8034;932063880;41393699;2111575;4\nHotel Silken Sant Gervasi - HB-004054;Sant Gervasi de Cassoles;26;25;8022;932531740;41404710;2138854;3\nHotel Silken Sant Gervasi - HB-004054;Sant Gervasi de Cassoles;26;25;8022;932531740;41404710;2138854;3")
with open("hotels.csv","r") as Hotels:
    print(Hotels.read())

res = importar_hotels("hotels.csv", ";")
ll = ordenar_per_estrelles(res)
for i in res:
    print(i)
print()
for w in ll:
    print(w)
"""

# EXERCICI 2.2 -- FUNCIONA
def mostrar_noms_hotels(hotels):
    for hotel in hotels:
        print(hotel.nom,hotel.codi_hotel)
        
"""
PROVA PER COMPROVAR 2.2:
 
res = importar_hotels("hotels.csv",';')
mostrar_noms_hotels(res)
"""

# EXERCICI 2.3 -- FUNCIONA
def buscar_per_nom(ll_hotels, string):
    buscats = []
    for hotels in ll_hotels:
        #print(hotels)
        if string.lower() in hotels.nom.lower():
            buscats.append(hotels)
    #print("llista final")
    #for x in buscats:
        #print(x)
    return buscats

"""
PROVA PER COMPROVAR 2.3:

res = importar_hotels("hotels.csv", ";")
buscar_per_nom(res, "Sant")
    
"""


# EXERCICI 2.4
def buscar_per_estrelles(ll_hotels,n_estrelles):
    def estrelles(hotel):
        return hotel.estrelles == n_estrelles          
    llista = list(filter(estrelles, ll_hotels))
    return llista
    
"""
PROVA PER COMPROVAR 2.4:

print("\nimpressió hotels:")
res = importar_hotels("hotels.csv",';')
for x in res:
    print(x)

print("\nimpressió llista hotels amb 3 estrelles: ")
res2 = (buscar_per_estrelles(res, 3))
for x in res2:
    print(x)
"""

# EXERCICI 2.5
def buscar_hotels(ll_hotels):
    criteri = input( "Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): ")
    if criteri == "1":
        nom_hotel = input("Introdueix nom hotel: ")
        res = buscar_per_nom(ll_hotels,nom_hotel)
        if res != []:
            print("S'han trobat",  len(res), "hotels amb aquest nom")
            mostrar_noms_hotels(res)
        else:
            print("No s'han trobat hotels")
            
    elif criteri == "2":
        error = True
        while error:
            try:
                num_estrelles = int(input("Introdueix estrelles hotel: "))
            except ValueError:
                print("Error: el número d'estrelles ha de ser un valor enter")
            else:
                if num_estrelles < 1 or num_estrelles > 5:
                    print("Error: el número d'estrelles ha de ser un valor entre 1 i 5")
                else:
                    error = False
        res = buscar_per_estrelles(ll_hotels,num_estrelles)
        
        if res != []: # REVISAR QUE LA SALIDA SIEMPRE SEA UNA LISTA, REVISAR FUNCIÓN 4
            print("S'han trobat", len(res), "hotels de",  num_estrelles, "estrelles")
            mostrar_noms_hotels(res)
        else:
            print("No s'han trobat hotels")
    else:
        print("Error: criteri de cerca no vàlid")

"""
PROVA PER COMPROVAR 2.5:

res = importar_hotels("hotels.csv", ";")
for x in res:
    print(x)
buscar_hotels(res)
"""

# EXERCICI 2.6
def hotel_mes_proper(hotels,latitud,longitud):
    if hotels==[]:
        return None, None
    
    i=0
    for hotel in hotels:
        if i==0:
            min_dist = hotel.distancia(latitud, longitud)
            hotelproper = hotel
            i+=1
        else:
            distancia = hotel.distancia(latitud, longitud) 
            if distancia < min_dist:
                min_dist, hotelproper = distancia, hotel

    return hotelproper, min_dist

"""
PROVA PER COMPROVAR 2.6:
    
h1=Hotel("Hotel Amrey Sant Pau", "HB-004046", "Sant Antoni Maria Claret", 173, 35, 8041, 934335151, 41414013, 2177888, 2)
h2=Hotel("Hotel Sansi Pedralbes", "HB-004086", "Pearson", 1, 21,8034,932063880,41393699,2111575,4)
h3=Hotel("Hotel Silken Sant Gervasi" ,"HB-004054", "Sant Gervasi de Cassoles",26,25,8022,932531740,41404710,2138854,3)
res1, res2 = hotel_mes_proper([h1,h2, h3], 41.404482, 2.191193)
print("resultats 1:", res1)
print("resultat 2:",res2)
"""