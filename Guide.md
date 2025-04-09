
Projekt: RPG mängu loomine
Autor: Aleksander Bekasov
Kuupäev: 10.04.2025

Sisukord

Sissejuhatus (projekti eesmärk)

Tehniline osa. Mis oli kasutatud projekti koostamisel? Koodi kirjutamisel?

Kasutusjuhend

Kokkuvõte. Kas on õnnestunud teha, mis oli planeeritud? Mis jäi tegemata?

Sissejuhatus (projekti eesmärk)
Projekti eesmärgiks oli luua lihtne tekstipõhine RPG mäng, kus kasutaja saab luua oma tegelase, teda arendada ja seigelda erinevates kohtades. Mängu peamine eesmärk on võimaldada kasutajale valida tegelane, võidelda erinevate koletistega ning arendada oma tegelast läbi kogutud kogemuste. Mängu arendamisel keskenduti peamiselt kasutaja liidesele (GUI) ja mängu loogika loomisele, et pakkuda lõbusat ja interaktiivset mängukogemust.

Tehniline osa. Mis oli kasutatud projekti koostamisel? Koodi kirjutamisel?
Projekti koostamiseks kasutati järgmisi tööriistu ja tehnoloogiaid:

Python: Põhitöötluskeel, mis on sobilik mängude arendamiseks tänu oma lihtsusele ja võimsusele.

Tkinter: Pythonis sisseehitatud GUI raamatukogu, mis võimaldab luua kasutajasõbralikke aknaid, nuppe ja dialooge.

PIL (Pillow): Piltide töötlemise teek, mida kasutati tegelaste ja koletiste piltide kuvamiseks mängu liideses.

Failisüsteem: Andmete salvestamiseks ja laadimiseks kasutati lihtsat tekstifaili (savefile.txt), kus hoiustatakse kasutaja tegelaste andmed (nagu tervis, rünnaku tugevus, tase jne).

Random: Kasutati juhuslike väärtuste genereerimiseks koletiste rünnakute ja nende välimuse määramiseks.

Mängu loogika on jagatud mitmeks osaks: tegelaste loomine ja haldamine (mõlemad kasutaja ja koletised), lahingu süsteem ja andmete salvestamine. Kasutaja saab oma tegelase nime määrata, seda muuta ja isegi kustutada, samuti saab ta koletistega võidelda ja oma tegelast tasandada.

Kasutusjuhend
Tegelkaste loomine:

Kui mäng algab, kuvatakse graafiline liides, kus kasutaja saab valida olemasoleva tegelase või luua uue tegelase.

Uue tegelase loomisel sisestab kasutaja oma kangelase nime. Kui nimi on juba olemas, ei saa uut tegelast luua.

Tegelaste haldamine:

Kasutaja saab oma loodud tegelasi muuta, kustutada või ümber nimetada.

Kui tegelane on valitud, saab kasutaja seda laadida ja alustada lahingut koletistega.

Lahingusüsteem:

Lahingud toimuvad igal kord, kui kasutaja otsustab "Võidelda". Koletis ilmub juhuslikult ja kasutaja saab valida rünnaku, tervenemise või põgenemise.

Iga võidetud koletis annab kogemusi, mis aitavad tegelasel taset tõsta.

Salvestamine ja laadimine:

Kõik tegelaste andmed salvestatakse faili ja neid saab hiljem laadida, et jätkata mängimist.

Kokkuvõte. Kas on õnnestunud teha, mis oli planeeritud? Mis jäi tegemata?
Projekt on edukalt viidud lõpule ja kõik põhifunktsioonid töötavad nagu kavandatud. Kasutaja saab luua, muuta ja kustutada tegelasi, samuti saab ta võidelda koletistega ja arendada oma tegelast. Mängu liides on lihtne ja kasutajasõbralik.

Siiski on veel mitmeid funktsioone, mida oleks soovinud lisada:

Muusika menüüde ja lahingute ajal: Tundub, et mängu atmosfääri täiendaks hästi taustamuusika, eriti menüüde ja lahingute ajal.

Graafilised pildid koletistest: Kuigi mäng sisaldab graafilist liidest, on koletised veel ainult tekstilised. Plaanis oli lisada igale koletisele unikaalsed pildid, et muuta mäng visuaalselt atraktiivsemaks.

Kangelase avataride valik: Kasutajad saavad hetkel ainult oma tegelase nime määrata, kuid oleks huvitav lisada valik erinevate avataride vahel, et iga mängija saaks oma kangelasele visuaalse identiteedi määrata.

Kokkuvõttes on projekt täitnud oma algsed eesmärgid, kuid kindlasti on veel palju arendamisvõimalusi, et muuta mäng täiuslikumaks ja kaasahaaravamaks.
