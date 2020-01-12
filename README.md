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

## Uruchomienie projektu

### Ubuntu

W celu prowadzenia rozwoju oprogramowania zalecana jest instalacja oprogramowania bez dodatkowej warstwy wirtualizacji. W celu przeprowadzenia takowej instalacji należy przeprowadzić instalacje w sposób przedstawiony poniżej.

Niniejsza procedura została zweryfikowana dla Ubuntu 18.10.

Pobierz kod źródłowy projektu:

```bash
git clone git@github.com:watchdogpolska/small_eod.git
```

Zainstaluj wymagane zależności:

```bash
sudo apt-get install -y libmariadbclient-dev-compat gcc
```

Zainstaluj serwer bazodanowy:

```bash
sudo apt-get install mariadb-server-10.1
```

Zainicjalizuj bazę danych:

```bash
sudo mysql < contrib/docker/docker-entrypoint-initdb.d/*
```

Utwórz użytkownika bazy danych:

```bash
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO '$(whoami)'@'localhost' IDENTIFIED BY 'password';"
```

Ustaw zmienną środowiskową z danymi dostępowymi do serwera bazodanowego:

```bash
export DATABASE_URL="mysql://$(whoami):password@localhost/small_eod"
```

Zainstaluj zależności systemowe dla Python:

```bash
sudo apt-get install virtualenv python3-pip python3-dev
```

Utwórz i aktywuj wirtualne środowisko Python:

```bash
virtualenv -p python3 env && source env/bin/activate
```

Zainstaluj zależności Python w wirtualnym środowisku Python:

```bash
pip install -r requirements/development.txt 
```

Zainicjalizuj tabele bazy danych:

```bash
python manage.py migrate
```

Utwórz konto administratora:

```bash
python manage.py createsuperuser
```

Uruchom serwer WWW:

```bash
python manage.py runsever
```

W przypadku wystąpienia problemów zweryfikuj powyższe polecenia z ```/Dockerfile```.

Po adresem ```http://localhost:8000/admin/``` dostępne jest logowanie z wykorzystaniem loginu i hasła.

Aplikacja nie posiada front-endu oraz domyślnie wykorzystuje logowanie GSuite. W celu utworzenia konta użytkownika wykonaj:

```bash
python manage.py createsuperuser
```

### Docker

W celu wsparcia wykonania testów wykorzystywane jest oprogramowanie Docker. 

W celu pracy nad rozwojem automatycznych testów wykonaj instalacje przedstawioną poniżej.

Celem długoterminowym jest wykorzystanie Docker także w środowisku produkcyjnym, do czego obecny kształt obrazów Docker nie jest przystosowany.

Instalacja Docker opisana została opisana w [dokumentacji projektu Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

Uruchomienie zależności aplikacji:

```bash
docker-compose up -d db nginx
```

Uruchomienie serwera aplikacyjnego:

```bash
docker-compose up -d --build web 
```

Wykonanie testów:

```bash
docker-compose run web python manage.py test --keepdb
```
