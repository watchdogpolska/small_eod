# Small_EOD

System służący do usprawnienia obiegu dokumentów Stowarzyszenia, w szczególności w zakresie:

* obiegu korespondencji w zakresie spraw sądowych
* archiwizacji dokumentacji

## Założenia

* system rozwijany będzie małymi etapami, aby jak najszybciej dostarczał wartość dla biura Stowarzysznia
* w początkowych etapach system będzie przeznaczony do archiwizacji dokumentów pochodzących z różnych mediów
* w przyszłości system będzie służył także do:

    * zarządzanie przebiegiem procesu sporządzenia pism
    * powiadamiania o nowych pismach
    * kontroli terminów
    * wysyłkę pism poprzez odpowiednie kolejki:
        * Envelo - realizowane automatycznie
        * ePUAP - realizowane manualnie przez osoby uprawnione, a następnie automatycznie
        * Poczta tradycyjna - realizowane manualnie przez osoby uprawnione

* należy zachować ciągłość funkcjonowania procesów Stowarzyszenia
* system trwale będzie miał charakter wewnętrzny dla Stowarzyszenia
    * publikacja danych z systemu odbywać się będzie poprzez API
* Platforma udostępnia skuteczne API
* Uwierzytelnienie z wykorzystaniem GSuite

## Stan aktualny

* W odrębnym systemie Stowarzyszenie wykorzystuje rejestr korespondencji w dwóch tabelach SQL (przychodzące i wychodzące)

* System umożliwia:

    * rejestracje dokumentów papierowych
    * rejestracje spraw
    
* Panel redakcyjny został wykonany w oparciu o ```django-admin```.

## Pilne zmiany

* Automatyczna rejestracja w dotychczasowym systemie korespondencji
* Opracowanie elastycznego interfejsu użytkownika nie opartego o ```django-grappeli```, w szczególności umożliwiającego:

    * sprawne zarejestrowanie sprawy
    * zarejestrowanie sprawy i jednoczesne wielu archiwalnych listów
    * przesłanie załączników poprzez przeciągnięcie i upuszczenie

* Wprowadzenie poczekalni, czyli pism, które nie posiadają wszystkich metadanych, co jest konieczne, aby importować:

    * E-maile oznaczone odpowiednią etykietą (GSuite wprowadzane w Stowarzyszeniu może powiadamiać i udostępniać przez API)
    * Skany pism bezpośrednio z skanera (drukarka wysyła przez SMTP i można poprzez IMAP pobrać zeskanowany dokument)

* Obserwowanie spraw - powiadomienie o zmianach osób, których sprawa dotyczy
* Kontrolę terminu

    * rejestracje terminu w sprawie
    * powiadomienie o upływie terminu
 
## Technologia

* Back-end - Django
* Front-end - Vue / React (cokolwiek elastycznego)

Dodatkowe uwagi:

* Wdrażamy w Stowarzyszeniu kontenery, więc nie obawiamy się małych usług, lecz obecnie ta aplikacja jeszcze nie wykorzystuje kontenerów
* Dodatkowe integracje tj. e-mail, ePUAP, Envelo wydaje się, że mogą być odrębnymi usługami, lecz komunikującymi się

## Uruchomienie projektu

Instalacja Docker opisana została na 

Uruchomienie bazy danych i serwera plików;

```
docker-compose up nginx db
```

Uruchomienie serwera aplikacyjnego:

```bash
docker-compose up web
```

Aplikacja nie posiada front-endu oraz domyślnie wykorzystuje logowanie GSuite. W celu utworzenia konta użytkownika wykonaj:

```bash
docker-compose run web python manage.py createsuperuser
```

Za sprawą usługi ```web``` pod adresem ```http://localhost:8000/admin/``` dostępne jest logowanie z wykorzystaniem loginu i hasła.