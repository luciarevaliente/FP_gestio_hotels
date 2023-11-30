"""
Created on Thu Dec  1 10:50:18 2022

Lucía R i Aránzazu
"""
# LLIBRERIES
import math

# CONSTANTS
RADI_TERRA = 6378.137

# EXERCICI 1
# funció per passar a radians
def Radians(graus):
    return graus*math.pi/180
    
# classe Hotel()
class Hotel():
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles):
        self.nom = nom
        self.codi_hotel = codi_hotel
        self.carrer = carrer
        self.numero = numero
        self.codi_barri = codi_barri
        self.codi_postal = codi_postal
        self.telefon = telefon
        self.latitud = latitud
        self.longitud = longitud
        self.estrelles = estrelles
        
    def __str__(self):
        return self.nom + " " + "(" + str(self.codi_hotel)+ ")" + " " + self.carrer + "," + str(self.numero) + " " + str(self.codi_postal) + " " + "(barri: " + str(self.codi_barri) + ")" + " " + str(self.telefon) + " " + "(" + str(self.latitud) + "," + str(self.longitud) + ")" + " " + str(self.estrelles) + " estrelles"
        
    def __gt__(self,altre_hotel):
        if self.estrelles > altre_hotel.estrelles:
            return True
        else:
            return False
    def distancia(self, latitud, longitud):
        try:
            if type(latitud)!=float:
                error = "latitud"
                raise TypeError
            elif type(longitud)!=float:
                error = "longitud"
                raise TypeError
            else:
                lat1 = Radians(self.latitud)
                lat2 = Radians(latitud)
                lon1 = Radians(self.longitud)
                lon2 = Radians(longitud)
                dist = math.acos(math.sin(lat1)*math.sin(lat2)+math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1))
                return dist
        except TypeError:
            print(error, "ha de ser un valor real")
            
""" 
PROVA PER COMPROVAR EXERCICI 1: 
         
a = Hotel("Hotel H10 Itaca","HB-004151","Roma",22,9,"08015",932265594,41.381193,2.145467,4)
print(a)
print(a.distancia(4.5,5))
"""

#EXERCICI 2 -- FUNCIONA
def codi_in_llista_hotels(llista_hotel,codi):
    for hotel in llista_hotel:
        if hotel.codi_hotel == codi:
            return True
    return False

"""
PROVA PER COMPROVAR EXERCICI 2: 
 
codi_hotel=2846832
llista=[2846832,123,3455,222]
print(codi_in_llista_hotels(llista,codi_hotel))
"""

# EXERCICI 3
def importar_hotels(fitxer, separador):
    try:
        with open(fitxer, "r", encoding="ISO-8859-1") as Fitxer:
            hotels = []
            index = 0
            num_hotels = 0
            for linia in Fitxer:
                if index != 0:
                    linia = linia[:-1]
                    #print(linia)
                    dades = linia.split(separador)
                    dades[0]=dades[0].split("- ")
                    #print(dades)
                    res = codi_in_llista_hotels(hotels, dades[0][1])
                    #print(res)
                    if res == False:
                        hotel = Hotel(str(dades[0][0]), str(dades[0][1]), str(dades[1]), int(dades[2]), int(dades[3]), int(dades[4]), str(dades[5]), (float(dades[6])/1000000), (float(dades[7])/1000000), int(dades[8]))
                        #print(hotel)
                        hotels.append(hotel)
                        #print(hotels)
                        num_hotels += 1
                        #print(num_hotels)
                index += 1
                #print()
            print("S'han importat correctament", num_hotels, "hotels")
            return hotels
    except FileNotFoundError:
        print("fitxer no trobat")

"""
PROVA PER COMPROVAR EXERCICI 3:

with open("hotels.csv", "w") as Hotels:
    Hotels.write("EQUIPAMENT;NOM_CARRER;NUM_CARRER_1;CODI_BARRI;CODI_POSTAL;TELEFON_NUM;LATITUD;LONGITUD;NIVELL_ESTR.\nHotel Amrey Sant Pau - HB-004046;Sant Antoni Maria Claret;173;35;8041;934335151;41414013;2177888;2\nHotel Amrey Sant Pau - HB-004046;Sant Antoni Maria Claret;173;35;8041;934335151;41414013;2177888;2\nHotel Sansi Pedralbes - HB-004086;Pearson;1;21;8034;932063880;41393699;2111575;4\nHotel Sansi Pedralbes - HB-004086;Pearson;1;21;8034;932063880;41393699;2111575;4\nHotel Silken Sant Gervasi - HB-004054;Sant Gervasi de Cassoles;26;25;8022;932531740;41404710;2138854;3\nHotel Silken Sant Gervasi - HB-004054;Sant Gervasi de Cassoles;26;25;8022;932531740;41404710;2138854;3\nHotel Viladomat - HB-004071;Viladomat;197;9;8015;932296565;41383696;2151861;3\nHotel NH Barcelona del Mar - HB-004161;Espronceda;6;35;8005;935029700;41401596;2210084;4\nHotel H10 Racó del Pi - HB-004164;Pi;7;2;8002;933426190;41383352;2173961;3\n")
with open("hotels.csv","r") as Hotels:
    print(Hotels.read())

res = importar_hotels("hotels.csv", ";")
for x in res:
    print(x)
"""

# EXERCICI 4
class Barri():
    def __init__(self, nom, codi_districte):
        try:
            self.nom = nom
            self.codi_districte = codi_districte
            if type(codi_districte)!=int or codi_districte<0:
                raise TypeError
        except TypeError:
            print("codi_districte ha de ser un valor enter positiu")
    
    def __str__(self):
        return self.nom + " (districte: " + str(self.codi_districte) + ")"

"""
PROVA PER COMPROVAR EXERCICI 4:    
    
a = Barri("la Maternitat i Sant Ramon", -4)
b = Barri("la Maternitat i Sant Ramon", 4)
print(b)
c = Barri("la Maternitat i Sant Ramon", 4.5)
d = Barri("la Maternitat i Sant Ramon", -4.5)
"""

# EXERCICI 5
def importar_barris(fitxer, separador):
    try:
        diccionari = {}
        index = 0
        num_barris = 0
        with open(fitxer, "r", encoding="ISO-8859-1") as Fitxer:
            for linia in Fitxer:
                if index != 0:
                    linia = linia[:-1]
                    #print(linia)
                    dades=linia.split(separador) 
                    #print(dades)
                    barri = Barri(str(dades[2]),int(dades[1])) 
                    #print(barri)
                    diccionari[int(dades[0])]=barri 
                    num_barris += 1
                index += 1
                #print(num_barris,diccionari)
            print("S'han importat correctament", num_barris,"barris")
            return diccionari
    except FileNotFoundError:
        print("fitxer no trobat")
        
"""
PROVA PER COMPROVAR EXERCICI 5:    

with open("barris.csv","w") as Barris:
    Barris.write("CODI_BARRI;CODI_DISTRICTE;NOM_BARRI\n1;1;el Raval\n2;1;el Barri Gòtic\n3;1;la Barceloneta\n4;1;Sant Pere, Santa Caterina i la Ribera\n5;2;el Fort Pienc\n6;2;la Sagrada Família\n7;2;la Dreta de Eixample\n8;2;l'Antiga Esquerra de l'Eixample\n9;2;la Nova Esquerra de l'Eixample\n10;2;Sant Antoni\n11;3;el Poble-sec\n12;3;la Marina del Prat Vermell\n13;3;la Marina del Port\n14;3;la Font de la Guatlla\n15;3;Hostafrancs\n16;3;la Bordeta\n17;3;Sants - Badal\n18;3;Sants\n19;4;les Corts\n20;4;la Maternitat i Sant Ramon\n21;4;Pedralbes\n22;5;Vallvidrera, el Tibidabo i les Planes\n23;5;Sarrià\n24;5;les Tres Torres\n25;5;Sant Gervasi - la Bonanova\n26;5;Sant Gervasi - Galvany\n27;5;el Putxet i el Farró\n28;6;Vallcarca i els Penitents\n29;6;el Coll\n30;6;la Salut\n31;6;la Vila de Gràcia\n32;6;el Camp d'en Grassot i Gràcia Nova\n33;7;el Baix Guinardó\n34;7;Can Baró\n35;7;el Guinardó\n36;7;la Font d'en Fargues\n")
with open("barris.csv","r") as Barris:
    print(Barris.read())

res = importar_barris("barris.csv", ";")
print(res)
for value in res.values():
    print(value)
"""

# EXERCICI 6 
class Districte():
    def __init__(self, nom, extensio, poblacio):
        try:
            self.nom = nom
            self.extensio = extensio
            self.poblacio = poblacio 
            self.llista_barris= []          
            if type(extensio)!=float:
                raise TypeError("extensió ha de ser un valor real positiu")
            if type(poblacio)!=int :
                raise TypeError("població ha de ser un valor enter positiu")
        except TypeError as missatge:
            print(missatge)
            
    def __str__(self):
        if self.llista_barris!=[]:
            self.llista_barris= ','.join(self.llista_barris) 
            return self.nom + " " + "(" + str(self.extensio)+ " km2" + "," +str(self.poblacio)+ " habitants" + ")" + " barris: "+ self.llista_barris       
        else:
            return self.nom + " " + "(" + str(self.extensio)+ " km2"+","+str(self.poblacio)+" habitants" + ")"+" " +"barris: N/D"
    
    def __densitat__(self):
        return self.poblacio/self.extensio

    
"""
PROVA PER COMPROVAR EXERCICI 6:  

a= Districte("Ciutat Vella",411,109672)
print(a)
"""

# EXERCICI 7 
def importar_districtes(fitxer, separador):
    try:
        diccionari = {}
        index = 0
        num_districtes = 0
        with open(fitxer, "r", encoding="ISO-8859-1") as Fitxer:
            for linia in Fitxer:
                if index != 0:
                    linia = linia[:-1]
                    #print(linia)
                    dades=linia.split(separador)
                    #print(dades)
                    districte = Districte(str(dades[1]), float(dades[2]), int(dades[3]))
                    #print(districte)
                    diccionari[int(dades[0])]=districte
                    #print(diccionari)
                    num_districtes += 1
                index += 1
            print("S'han importat correctament", num_districtes,"districtes")
            return diccionari
                    
    except FileNotFoundError:
        print("fitxer no trobat")
        
"""
PROVA PER COMPROVAR EXERCICI 7:  

with open("districtes.csv","w") as Districtes_txt:
    Districtes_txt.write("CODI_DISTRICTE;NOM_DISTRICTE;SUPERFICIE;POBLACIO\n1;Ciutat Vella;4.11;109672\n2;Eixample;7.46;269349\n3;Sants-Montjuïc;22.68;187026\n4;Les Corts;6.02;81576\n5;Sarrià-Sant Gervasi;19.91;149201\n6;Gràcia;4.19;123276\n7;Horta-Guinardó;11.96;173944\n8;Nou Barris;8.05;173552\n9;Sant Andreu;6.59;151537\n10;Sant Martí;10.39;241181")
with open("districtes.csv","r") as Districtes_txt:
    print(Districtes_txt.read())
dicc = importar_districtes("districtes.csv",";")
print("dicc:", dicc)
print("Nom: ", dicc[1].nom)
"""

# EXERCICI 8
def omplir_llista_barris(dicc_barris, dicc_districtes):
    res = True
    for districtes in dicc_districtes.values():
        #print(districtes.llista_barris)
        if districtes.llista_barris != []:
            print("El diccionari de districtes ja conté informació dels barris")
            res = False
            break
    #print("res:", res)
    if res == True:
        for c_districtes,districtes in dicc_districtes.items():
            #print("codi districte:", c_districtes)
            for c_barris, barris in dicc_barris.items():
                #print("barri:", barris.nom, "Codi districte:" ,barris.codi_districte)
                if barris.codi_districte == c_districtes:
                    #print("estoy dentro")
                    districtes.llista_barris.append(dicc_barris[c_barris])
            #for x in districtes.llista_barris:
                #print(x)
            #print()
    
"""
PROVA 1.8:
res1 = importar_barris("barris.csv", ";")
print(res1)

print()
res2 = importar_districtes("districtes.csv", ";")
print(res2)
for x in res2.values():
    print(x.llista_barris)
print()

omplir_llista_barris(res1, res2)
"""
    
# EXERCICI 9 -- FUNCIONA
def mostrar_hotels(llista_hotels):
    for hotel in llista_hotels:
        print(hotel.nom,hotel.codi_hotel,hotel.carrer, hotel.numero, hotel.codi_barri, hotel.codi_postal, hotel.telefon, hotel.latitud, hotel.longitud, hotel.estrelles)

"""
PROVA PER COMPROVAR EXERCICI 9:  

mostrar_hotels([Hotel("Hotel Amrey Sant Pau","HB-004046","Sant Antoni Maria Claret",173,35,8041,934335151,41414013,2177888,2),Hotel("Hotel Amrey Sant Pau","HB-004046","Sant Antoni Maria Claret",173,35,8041,934335151,41414013,2177888,2)])

"""
