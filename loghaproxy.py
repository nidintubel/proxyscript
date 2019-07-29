#!/usr/bin/env piython
# -*- coding: utf-8 -*-

from operator import itemgetter
from collections import OrderedDict
from datetime import datetime


a1=list()
a2=list()
a3=list()
a4=list()
a5=list()
a6=list()
a7=list()
a8=list()
a9=list()
a10=list()
a11=list()
a12=list()
a13=list()
a14=list()
a15=list()
a16=list()
a17=list()
a18=list()
a19=list()
a20=list()
a21=list()
a22=list()
a23=list()
a24=list()
a25=list()

with open("/home/jakob/Skripte/haproxy.log.9", "r") as f:                   #Logfile einlesen
    for line in f:                                                          #für jede Zeile im Logfile
        if "gdata" in line:                                                 #wenn auf der Zeile der String gdata vorkommt
            continue                                                        #springe sofort zur nächsten Zeile (gdata Einträge des Virenscanners sollen ausgelassen werden)
        else:                                                               #sonst
            matching = line.split()                                         #die Zeile des Logfiles in eine Liste matching schreiben
            if matching[2] >= "06:25:40" and matching[2] < "07:25:40" :     #wenn der Zeiteintrag in der Liste matching an Position 2 zwischen den beiden Uhrzeiten ist
                ip = matching[5].split(":")                                 #splitte den IP Eintrag der Liste matching an Position 5 beim Doppelpunkt (Die Portangabe soll weg)
                ip0 = ip[0]                                                 #ip0 ist jetzt die Position 0 des gesplitteten IP Eintrags also nur noch die IP Adresse
                ipsplit = ip0.split(".")                                    #splitte ip0 bei den Punkten um die Einzelbestandteile der IP Adresse zu erhalten
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" : 
                    a1.append(ip[0])                                        #alle IP Adressen die die obige Bedingung erfüllen werden in die Liste a1 geschrieben
            elif matching[2] >= "07:25:40" and matching[2] < "08:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a2.append(ip[0])
            elif matching[2] >= "08:25:40" and matching[2] < "09:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a3.append(ip[0])
            elif matching[2] >= "09:25:40" and matching[2] < "10:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a4.append(ip[0])
            elif matching[2] >= "10:25:40" and matching[2] < "11:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a5.append(ip[0])
            elif matching[2] >= "11:25:40" and matching[2] < "12:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a6.append(ip[0])
            elif matching[2] >= "12:25:40" and matching[2] < "13:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a7.append(ip[0])
            elif matching[2] >= "13:25:40" and matching[2] < "14:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a8.append(ip[0])
            elif matching[2] >= "14:25:40" and matching[2] < "15:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a9.append(ip[0])
            elif matching[2] >= "15:25:40" and matching[2] < "16:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a10.append(ip[0])
            elif matching[2] >= "16:25:40" and matching[2] < "17:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a11.append(ip[0])
            elif matching[2] >= "17:25:40" and matching[2] < "18:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a12.append(ip[0])
            elif matching[2] >= "18:25:40" and matching[2] < "19:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a13.append(ip[0])
            elif matching[2] >= "19:25:40" and matching[2] < "20:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a14.append(ip[0])
            elif matching[2] >= "20:25:40" and matching[2] < "21:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a15.append(ip[0])
            elif matching[2] >= "21:25:40" and matching[2] < "22:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a16.append(ip[0])
            elif matching[2] >= "22:25:40" and matching[2] < "23:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a17.append(ip[0])
            elif matching[2] >= "23:25:40" or matching[2] < "00:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a18.append(ip[0])
            elif matching[2] >= "00:25:40" and matching[2] < "01:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a19.append(ip[0])
            elif matching[2] >= "01:25:40" and matching[2] < "02:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a20.append(ip[0])
            elif matching[2] >= "02:25:40" and matching[2] < "03:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a21.append(ip[0])
            elif matching[2] >= "03:25:40" and matching[2] < "04:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a22.append(ip[0])
            elif matching[2] >= "04:25:40" and matching[2] < "05:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a23.append(ip[0])
            elif matching[2] >= "05:25:40" and matching[2] < "06:25:40" :
                ip = matching[5].split(":")
                ip0 = ip[0]
                ipsplit = ip0.split(".")
                if ipsplit[0] == "172" and ipsplit[1] == "16" and len(ipsplit[2]) < 3 and ipsplit[2] !="0" and ipsplit[2] != "1" and ipsplit[2] != "2" :
                    a24.append(ip[0])
            else:
                ip = matching[5].split(":")
                a25.append(ip[0])



unique_a1=list()                                    #Liste unique_a1 wird deklariert
for x in a1:                                        #für jeden Eintrag in der Liste a1
    if x not in unique_a1:                          #wenn der Eintrag noch nicht in der neuen unique_a1 Liste steht
        unique_a1.append(x)                         #füge den Eintrag auf die unique_a1 Liste hinzu

unique_a2=list()
for x in a2:
    if x not in unique_a2:
        unique_a2.append(x)

unique_a3=list()
for x in a3:
    if x not in unique_a3:
        unique_a3.append(x)

unique_a4=list()
for x in a4:
    if x not in unique_a4:
        unique_a4.append(x)

unique_a5=list()
for x in a5:
    if x not in unique_a5:
        unique_a5.append(x)

unique_a6=list()
for x in a6:
    if x not in unique_a6:
        unique_a6.append(x)

unique_a7=list()
for x in a7:
    if x not in unique_a7:
        unique_a7.append(x)

unique_a8=list()
for x in a8:
    if x not in unique_a8:
        unique_a8.append(x)

unique_a9=list()
for x in a9:
    if x not in unique_a9:
        unique_a9.append(x)

unique_a10=list()
for x in a10:
    if x not in unique_a10:
        unique_a10.append(x)

unique_a11=list()
for x in a11:
    if x not in unique_a11:
        unique_a11.append(x)

unique_a12=list()
for x in a12:
    if x not in unique_a12:
        unique_a12.append(x)

unique_a13=list()
for x in a13:
    if x not in unique_a13:
        unique_a13.append(x)

unique_a14=list()
for x in a14:
    if x not in unique_a14:
        unique_a14.append(x)

unique_a15=list()
for x in a15:
    if x not in unique_a15:
        unique_a15.append(x)

unique_a16=list()
for x in a16:
    if x not in unique_a16:
        unique_a16.append(x)

unique_a17=list()
for x in a17:
    if x not in unique_a17:
        unique_a17.append(x)

unique_a18=list()
for x in a18:
    if x not in unique_a18:
        unique_a18.append(x)

unique_a19=list()
for x in a19:
    if x not in unique_a19:
        unique_a19.append(x)

unique_a20=list()
for x in a20:
    if x not in unique_a20:
        unique_a20.append(x)

unique_a21=list()
for x in a21:
    if x not in unique_a21:
        unique_a21.append(x)

unique_a22=list()
for x in a22:
    if x not in unique_a22:
        unique_a22.append(x)

unique_a23=list()
for x in a23:
    if x not in unique_a23:
        unique_a23.append(x)

unique_a24=list()
for x in a24:
    if x not in unique_a24:
        unique_a24.append(x)

unique_a25=list()
for x in a25:
    if x not in unique_a25:
        unique_a25.append(x)
        


print"Zeit 06:25 - 07:25 --- " + str(len(unique_a1))
print"Zeit 07:25 - 08:25 --- " + str(len(unique_a2))
print"Zeit 08:25 - 09:25 --- " + str(len(unique_a3))
print"Zeit 09:25 - 10:25 --- " + str(len(unique_a4))
print"Zeit 10:25 - 11:25 --- " + str(len(unique_a5))
print"Zeit 11:25 - 12:25 --- " + str(len(unique_a6))
print"Zeit 12:25 - 13:25 --- " + str(len(unique_a7))
print"Zeit 13:25 - 14:25 --- " + str(len(unique_a8))
print"Zeit 14:25 - 15:25 --- " + str(len(unique_a9))
print"Zeit 15:25 - 16:25 --- " + str(len(unique_a10))
print"Zeit 16:25 - 17:25 --- " + str(len(unique_a11))
print"Zeit 17:25 - 18:25 --- " + str(len(unique_a12))
print"Zeit 18:25 - 19:25 --- " + str(len(unique_a13))
print"Zeit 19:25 - 20:25 --- " + str(len(unique_a14))
print"Zeit 20:25 - 21:25 --- " + str(len(unique_a15))
print"Zeit 21:25 - 22:25 --- " + str(len(unique_a16))
print"Zeit 22:25 - 23:25 --- " + str(len(unique_a17))
print"Zeit 23:25 - 00:25 --- " + str(len(unique_a18))
print"Zeit 00:25 - 01:25 --- " + str(len(unique_a19))
print"Zeit 01:25 - 02:25 --- " + str(len(unique_a20))
print"Zeit 02:25 - 03:25 --- " + str(len(unique_a21))
print"Zeit 03:25 - 04:25 --- " + str(len(unique_a22))
print"Zeit 04:25 - 05:25 --- " + str(len(unique_a23))
print"Zeit 05:25 - 06:25 --- " + str(len(unique_a24))
print"Nicht zuzuordnende Eintraege: " + str(len(unique_a25))
