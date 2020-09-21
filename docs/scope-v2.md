# Zakres etapu v2

Projekt rozwijany jest w modelu iteracyjnym, co sprawia, że z jednej strony jest określony szeroki zakres możliwego rozwoju projektu. Z drugiej jednak strony są określone funkcjonalności, których realizacja jest możliwa bezpośrednio lub które powinny być zrealizowane w pierwszej kolejności.

Niniejszy dokument ma na celu zdefiniowania minimalnego zakresu funkcjonalności, który jest konieczny, aby uznać za zakończoną realizacje etapu `v2` aplikacji.

Celem etapu v2 jest zmiana technologii przy minimalnym rozszerzeniu zakresu funkcjonalności aplikacji. Zakres funkcjonalności uległ nieznacznemu poszerzeniu ze względu na ich duże znaczenie dla organizacji lub weryfikacje architektoniczną.

## Zakres zadań

W ramach etapu konieczne jest:

* projektowanie i implementacja
* wdrożenie w środowisku organizacji:, w tym:
  * migracja danych z etapu `v1`
  * nieznaczne korekty funkcjonalności w celu zagwarantowania efektywnego wykorzystania
* całkowite wygaszenie rozwiązania z etapu `v1`

Etap wdrożenia dopuszcza wprowadzenie niedostępności systemu, nawet na okres tygodnia dni.

## Architektura

Aplikacja powinna uwzględniać:

* serwer API – wykonany w Django udostępniający API w technologii REST
* interfejs użytkownika – wykonany w React wykorzystujący serwer API
* serwer plików zgodny z S3 – przyjmujący, przechowujący i udostępniający dane binarne

Dla systemu przyjęto następujące wymagania dostępności:

* RPO – (TODO: Ustalić z Zarządem)
* RTO – (TODO: Ustalić z Zarządem)

## Zakres funkcjonalności

### Podstawowe funkcjonalności

Wykorzystano tekst *pogrubiony* w celu wskazania funkcjonalności, które nie są zostały dostarczone w etapie `v1`.

Przyjęto, poza wyraźnie zaznaczonymi, że wszelkie funkcjonalności są realizowane z wykorzystaniem interfejsu użytkownika, wskazanego w architekturze, wykonanego w technologii React.

Dostrzegalne funkcjonalności:

* pola tekstowe aplikacji nie wymagają wprowadzenia ręcznie indywidualnie identyfikatorów, a są automatycznie podpowiadane
* zarządzanie jednostkami administracyjnymi
  * odczyt wykazu jednostek administracyjnych w postaci tabeli
  * dodanie jednostki administracyjnej
  * edycja jednostki administracyjnej
  * usunięcie jednostek administracyjnych
  * zaimportowanych wstępnie z bazy TERYT
* zarządzanie sprawami:
  * odczyt wykazu spraw w postaci tabeli
  * dodanie sprawy
  * edycja sprawy
  * usunięcie spraw
  * **utworzenie sprawy, który nie zawiera kompletu informacji**
  * filtrowania wyszukiwanych spraw, w tym:
    * z wykorzystaniem pól niedostępnych w tabeli – zob. obecne  ```./ui/v1/case_list.png```
    * **wyszukania spraw, które nie zawierają kompletu informacji i ich sprawnego uzupełnienia**
  * formularz sprawy umożliwia:
    * bezpośrednie dodanie powiązanych z daną sprawą listów (w Django to było wykonane przez inline), ze względu na dokonywanie archiwizacji "teczek" sprawy, czyli przetwarzania zbioru dokumentów należących do jednej sprawy, z uwzględnieniem:
      * braku znaczącej zmiany kontekstu (UX) - zob. obecne ```./ui/v1/case_change.png```
      * **dodania wielu plików do jednego listu**
      * **wykorzystanie mechanizmu drag-and-drop dla przekazywania plików**
      * zarządzania kolejnością listów
    * określenie wartości pól danych statycznych - zgodnie z regułami danego słownika
    * określenie użytkowników odpowiedzialnych
    * określenie użytkowników powiadamianych
    * określenie własności listu
* zarządzanie listami:
  * odczyt wykazu listów w postaci tabeli
  * dodanie listu
  * edycja listu
  * usunięcie listu
  * **dodania wielu plików do jednego listu**
  * **wykorzystanie mechanizmu drag-and-drop dla przekazywania plików**
  * **utworzenie listu, który nie zawiera kompletu informacji**
  * filtrowania wyszukiwanych listów, w tym:
    * z wykorzystaniem pól niedostępnych w tabeli
    * **wyszukania listów, które nie zawierają kompletu informacji i ich sprawnego uzupełnienia**
    * odczyt listów niepowiązanych z sprawami
* odczyt, dodanie i edycje opisów listów (kolekcja na potrzeby wyboru wartości pola "Opis" w formularzu edycji listu)
* odczyt, dodanie i edycje cech i opcji spraw (`Feature` and `FeatureOption`)
  * odczyt wykazu cech i opcji w postaci tabeli
  * dodanie opcji
  * edycja opcji
  * usunięcie opcji
  * **dodanie cechy**
  * **edycja cechy**
  * **usuniecie cechy**
* odczyt, dodanie i edycja kanałów komunikacji (prosty słownik)
* odczyt, dodanie i edycja kanałów tagów (prosty słownik)
* zarządzanie użytkownikami:
  * odczyt, dodanie i edycja użytkowników oraz ich uprawnień – funkcjonalność można zrealizować z wykorzystaniem Django-Admin
  * profil użytkownika – wyłącznie do odczytu
* uwierzytelnienie użytkowników z wykorzystaniem GSuite

### Dodatkowe funkcjonalności

Mile widziane, ale nie jest to konieczne i możliwe jest ich przeniesienie na kolejne etapy realizacja następujących funkcjonalności, które nie są dostępne w etapie `v1`.

#### Kolekcje

Mechanizm ma na celu udostępnienie podzbioru spraw na zewnątrz organizacji bez konieczności uwierzytelniania.

Mechanizm nie istnieje w rozwiązaniu z etapu `v1`.

Szczegółowe funkcjonowanie kolekcji zostało określone w dokumencie `./README.md`.

Dostrzegalne funkcjonalności:

* możliwość zapisania wyników wyszukiwania sprawy jako nowej kolekcji zawierającej kryteria wyszukiwania spraw (A) lub wykaz spraw (B)
* odczyt wykazu kolekcji
* dodanie kolekcji
* edycja kolekcji
* usunięcie kolekcji
* wygenerowanie odnośnika dostępu do kolekcji bez uwierzytelniania
* odczytanie wykazu spraw, a także zawartości samych spraw bez uwierzytelniania na podstawie odnośnika dostępu do kolekcji

#### Wydarzenia

Mechanizm ma na celu usprawnienie organizacji wiedzy na temat wydarzeń nadchodzących w sprawie.

Mechanizm nie istnieje w rozwiązaniu z etapu `v1`.

Dostrzegalne funkcjonalności:

* możliwość utworzenia wydarzenia określającego:
  * tytuł wydarzenia
  * opis wydarzenia
  * datę i czas wydarzenia
  * sprawę wydarzenia
* wyświetlenie informacji o wydarzeniu w kontekście sprawy
* dodanie wydarzenia
* edycje wydarzenia
* usunięcie wydarzenia
* cykliczne powiadomienia do osób obserwujących sprawę o nadchodzącym wydarzeniu w sprawie
* bezpieczne udostępnienie wydarzeń w formacie `iCal` na potrzeby integracji z Kalendarzem Google

##### Notatki

Mechanizm ma na celu wyeliminowanie konieczności dyskusji na temat spraw poza systemem small-eod. Oczekiwane jest, że kolejne osoby będą w ramach dyskusji tworzyły kolejne notatki. Tworzy to mechanizm komentarzy.

Mechanizm nie istnieje w rozwiązaniu z etapu `v1`.

Dostrzegalne funkcjonalności:

* możliwość utworzenia notatki określającej:
  * opis (treść) notatki
  * sprawę notatki
* wyświetlenie informacji o notatce w kontekście sprawy
* dodanie notatki
* edycje notatki
* usunięcie notatki
* podczas wprowadzania opisu notatki [zawołania dodatkowych osób](https://github.blog/2011-03-23-mention-somebody-they-re-notified/)
* natychmiastowe powiadomienie osób obserwujących sprawę o nadchodzącym wydarzeniu w sprawie
* chronologiczne prezentowanie informacji na temat listów, wydarzeń i notatek łącznie
* możliwość bezpośredniej (e-mailowej) odpowiedzi na powiadomienie o nowej notatce
