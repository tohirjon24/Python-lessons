# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#ozim={"ism":"Tohirjon",
#      "Familya":"Turgunov",
#     "Kasbi":"Student",
 #     "Oqish_joyi":"Namdu",
  #    "Kursi":"4",
   #   "Tugilgan_yil":"2002"
    #  }
#print(f"{ozim['ism']} {ozim['Familya']}\n"
      #f"{ozim['Tugilgan_yil']} yilda tugilgan {ozim['Kasbi']}\n"     
      #f"hozirda {ozim['Oqish_joyi']} da oq'iydi")
      
#taomlar={
    #"ali":"osh",
   # "vali":"manti",
  #  "nodir":"tovuq",
 #   "aziz":"qotirma",
 #   "botir":"shorva",
#    "salim":"mastava"
    #}     
#for taom,odam in taomlar.items():
#    print(f"{taom.title()}ning yaxshi korgan taomi {odam}")


#python_izohli_lugati = {
 #   'integer':"Butun son",
  #  'float':"O'nlik son",
   # 'string':"Matn",
    #'list':"Ro'yxat",
    #'tuple':"O'zgarmas ro'yxat"}
#kalit=input("istalgan lugataingizni kiriting: ")
#lugat=python_izohli_lugati.get(kalit,"Bizda bunday lugat yo'q")
#print(f"{kalit.title()} ning tarjimasi {lugat}")

#python_izohli_lugati = {
#    'integer':"Butun son",
#    'float':"O'nlik son",
#    'string':"Matn",
#    'list':"Ro'yxat",
#    'tuple':"O'zgarmas ro'yxat",
#    'integer':'Butun son',
#   'boolean':"Mantiqiy qiymat",
#    'for':"Biror amalni qayta-qayta bajarish tsikli",
#   'if':'Shartlarni tekshirish operatori'}
#for k,q in sorted(python_izohli_lugati.items()):
#    print(f"Kalit:{k}, "
#   f"qiymat:{q}\n")

davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
for davlat in sorted(davlatlar.keys()):
    print(davlat.upper())
print("\nDavlatlarning poytaxtlari: ")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())


davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
kalit=input("Istalgan davlatingiz nomini kiriting: ")
tarjima=davlatlar.get(kalit)
if tarjima==None:
    print("Bizda bunday davlatning poytaxti yo'q")
else:
   
    print(f"Siz kiritgan davlarning poytaxti {tarjima.title()}")

menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
yoq=[]
menyu=[]
for i in range(0,3,1):
    menyu.append(input(f"Istagan {i+1} taomingizni tanlarng"))
for taom in menu:
    if taom in menyu:
        print(f"Bizdagi {taom.title()} ning narxi{menu[taom]} som")
print("\n BIzda yoq taomlar mana bular: ")
for ta in yoq:
    print(ta)
        










