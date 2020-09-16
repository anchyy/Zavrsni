# Opis projekta

Tema ovog projekta je izrada Web shopa za prodaju narukvica od konca.

Projekt je izrađen u Flasku, Paython web frameworku, namijenjenom razvoju web aplikacija.
U svom osnovnom paketu nema puno usluga ali je lako proširiv - Flask ekstenzije. Ekstenzije
omogućuju da se web aplikacije lako prošire prema potrebama projekta.
U dokumentu requirements.txt navedeni su potrebni paketi koji su korišteni pri izradi projekta.

## Struktura

Projekt ima svoje pripadajuće virtualno okruženje u mapi venv.
Ostali elementi projekta su:
static - svi dodaci korištenog bootstrapa i potrebne slike
templates - html datoteka
main - glavna datoteka u koju je smješten konfiguracija projekta, modeli baze i view funkcije
requirements.txt - potrebni paketi
sqlConnector.py - datoteka za punjenje baze potrebnim podacima
webshopDB.sqlite - baza za pohranu podataka

## Tok rada aplikacije

Aplikacija se sastoji od base.html - baza koja uključuje zagljavlje i podnože koji se nasljeđuju na sve ostale html datoteke,
index.html - naslovna stranica aplikacije

Nakon što se pojavi naslovna stranica korisnik može u kartici Proizvodi vidjeti paletu proizvoda po kategorijama.
Ukoliko ih želi kupiti mora se prethodno registrirati i logirati. Nakon što izabere proizvode za kupnju dodaje ih u košaricu.
Nakon toga klikom na ikonu košarice može otići na blagajnu. Radi jednostavnosti
aplikacije stavljeno je plačanje pouzečem. U košarici ima pregled svojih proizvoda sa količinom i cijenom.
Ukoliko se predomisli može ukloniti određeni artikal. Nakon potvrde narudžbe korisniku stiže email sa brojem narudžbe i obavijesti.
Opisani postupak predstavlja tok događaja aplikacije.