# Small_EOD
![Build Status](https://github.com/watchdogpolska/small_eod/workflows/Django%20application/badge.svg?branch=dev) ![Build Status](https://github.com/watchdogpolska/small_eod/workflows/YAML%20files/badge.svg?branch=dev)

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

 
## Technologia

* Back-end - Django
* Front-end - Vue / React (cokolwiek elastycznego)

Dodatkowe uwagi:

* Wdrażamy w Stowarzyszeniu kontenery, więc nie obawiamy się małych usług, lecz obecnie ta aplikacja jeszcze nie wykorzystuje kontenerów
* Dodatkowe integracje tj. e-mail, ePUAP, Envelo wydaje się, że mogą być odrębnymi usługami, lecz komunikującymi się

## Jeżeli chcesz rozwijać projekt

## Dla deweloperów
### Uruchomienie projektu
Pobierz kod źródłowy projektu komendą git lub pracująć na `Windows`/`Mac` wykorzystaj [GitHub Desktop](https://desktop.github.com/)
```bash
git clone git@github.com:watchdogpolska/small_eod.git
```
Przed wykonaniem commitu można uruchomić testy lokalnie, np. jednostkowo:
* test formatu tekstu
```bash
make lint
```
* testy django
```bash
make test-django-backend
```
* zbudowanie kontenerów
```bash
make build
```
* testowanie backendu django
```bash
make test-django-backend
```

Badź grupowo, wszystkie powyższe:
```bash
make test-local
```

* automatyczne sformatowanie tekstu (np. w przypadku błędów ze strony `make lint`)
```bash
make fmt
```
## Dla leniwych
#### Docker
* W celu prowadzenia rozwoju oprogramowania zainstaluj: [Docker](https://docs.docker.com/install/) i jeśli pracujesz na Linuxie: [docker-compose](https://docs.docker.com/compose/install/) (Docker dla Windows i Mac powinień już posiadać)
* Cały stack można włączyć za pomocą komendy:
```bash
docker-compose up
```
* W razie problemów bądź pytań otwórz [issue](https://github.com/watchdogpolska/small_eod/issues)
#### PyCharm
* Niezależnie od platformy polecane: [Pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html#)
* Skonfiguruj `remote interpreter` (w przypadku błędów połączenia upewnij się że Twoja konfiguracja TLS jest prawidłowa)
![interpreter](./docs/images/interpreter.png)

* Ustaw `path mappings`
![interpreter2](./docs/images/interpreter2.png)
* Możesz cieszyć się interaktywnym debuggerem i miłym środowiskiem pracy.
![interpreter2](./docs/images/debugger.png)
* [Skonfiguruj `default template` dla testów django i zobacz jak można pracować z PyCharm](./docs/images/workflow.gif)

Utwórz konto administratora:
```bash
docker-compose run web python manage.py createsuperuser
```
W przypadku wystąpienia problemów zweryfikuj powyższe polecenia z ```/Dockerfile```.
Po adresem [http://localhost:8000/admin/](http://localhost:8000/admin/) dostępne jest logowanie z wykorzystaniem loginu i hasła.
