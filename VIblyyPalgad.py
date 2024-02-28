
from module1 import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("0-Näita andmed veerudes\n1-andmete lisamine\n")
    valik=int(input())
    if valik==1:    
        inimesed,palgad=inimeste_ja_palgade_lisamine(inimesed,palgad,int(input("Mitu inimest lisame? ")))
        
    elif valik==0:        
        andmed_veerudes(inimesed,palgad)
    elif valik==2:
        
