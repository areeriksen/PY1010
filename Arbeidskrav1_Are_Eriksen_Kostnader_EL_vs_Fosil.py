# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 07:50:49 2024

@author: aeriksen

Dette programmet skal bergene forskjellen i kostnader mellom EL bil og
Bensinbil, gitt 10000 kjørte km i året
"""

#Faste kostnader
forsikring_el = 5000
forsikring_fosil = 7500
trafikk_avg = 8.32*365

#Brukskostnader
drivstoff_el =  0.2*2*10000  #0,2 kwh/km * 2kr kwh * 10000 km
drivstopp_fosil = 1*10000  #1kr/km * 10000 km
bom_el = 0.1*10000  # 0,1 kr/km * 10000 km
bom_fosil = 0.3*10000  #0,3 kr/km * 10000 km

#Beregninger 
kostnad_el = forsikring_el + trafikk_avg +drivstoff_el + bom_el
kostnad_fosil = forsikring_fosil + trafikk_avg +drivstopp_fosil + bom_fosil
differanse = kostnad_fosil - kostnad_el

#Resultat
print("Dette programmet beregner forskjell på kostnader mellom EL bil og benssinbil, ved 10000 krørt km i året")
print("")
print("Kostnader elbil:", kostnad_el )
print("Kostnad bensinbil:", kostnad_fosil )
print("Differansen blir:", differanse)  
print("")
print("Det koster kr:", differanse, "mindre ved å bruke elbil")