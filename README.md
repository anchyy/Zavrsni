# Opis projekta

Tema ovog projekta je izrada Web shopa za prodaju narukvica od konca.

Projekt je izrađen u Flasku, Paython web frameworku, namijenjenom razvoju web aplikacija.
U svom osnovnom paketu nema puno usluga ali je lako proširiv - Flask ekstenzije. Ekstenzije
omogućuju da se web aplikacije lako prošire prema potrebama projekta.
U dokumentu requirements.txt navedeni su potrebni paketi koji su korišteni pri izradi projekta.

## Struktura

Struktura aplikacije sastoji se od sljedećih elemenata:

> - config.py – sadrži konfiguracijske postavke aplikacije
> - requirements.txt – tekstualna datoteka koja služi za instalaciju svih potrebnih biblioteka
> - app/ - sadrži glavnu aplikaciju i pod aplikacije te bazu podataka:
> -__init__.py
> - main.py
> -models.py
> - sqlConnector.py
> - webshopDB.sqlite
> - static/ - datoteke CSS, JS, fontovi 
> -templates/ - HTML predlošci


## Tok rada aplikacije

Aplikacija se sastoji od base.html - baza koja uključuje zagljavlje i podnože koji se nasljeđuju na sve ostale html datoteke,
index.html - naslovna stranica aplikacije

Nakon što se pojavi naslovna stranica korisnik može u kartici Proizvodi vidjeti paletu proizvoda po kategorijama.
Ukoliko ih želi kupiti mora se prethodno registrirati i logirati. Nakon što izabere proizvode za kupnju dodaje ih u košaricu.
Nakon toga klikom na ikonu košarice može otići na blagajnu. Radi jednostavnosti
aplikacije stavljeno je plačanje pouzečem. U košarici ima pregled svojih proizvoda sa količinom i cijenom.
Ukoliko se predomisli može ukloniti određeni artikal. Nakon potvrde narudžbe korisniku stiže email sa brojem narudžbe i obavijesti.
Opisani postupak predstavlja tok događaja aplikacije.

## Instalacija i pokretanje aplikacije

Potrebno je imati instaliranu verziju Pythona minimalno 3.7

- git clone https://github.com/anchyy/Zavrsni.git
- cd Zavrsni
- pip intall -r requirements.txt
- flask run

