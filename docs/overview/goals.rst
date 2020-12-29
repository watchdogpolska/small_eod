Założenia projektu
===================

Zarządzanie
----------------------
* System rozwijany będzie małymi etapami, aby jak najszybciej dostarczał wartość dla biura Stowarzyszenia [#ZA1]
* System będzie rozwijany jako darmowe i otwarte oprogramowanie dążyć do stałej gotowości przyjęcia nowego wsparcia [#ZA2]
* W rozwoju projektu należy dążyć do ciągłość funkcjonowania procesów Stowarzyszenia [#ZA3]
* System będzie otwarty na wdrożenie w innych podmiotach, które podejmują niezależnie działania zbieżne z celami Stowarzyszenia [#ZA4]
* System będzie rozwijany w sposób umożliwiający włączenie nowych osób, także w niewielkim stopniu zaangażowania [#ZA5]

Technologia
---------------------
W doborze technologii preferowane będą rozwiązania, które umożliwiają ograniczenie kosztów utrzymania, w szczególności osobowych i licencyjnych [#ZT1] tj.:
    
    * wykorzystanie środowisk chmurowych
    * wykorzystanie konteneryzacji
    * aktywne utrzymywane w długoletniej perspektywie.

Uwaga: Na dzień 1 października 2019 roku `HyperOne <https://www.hyperone.com/>`_ udostępnia Stowarzyszeniu zasoby informatyczne bez opłat. W ofercie posiada usługi tj. Wirtualne Maszyny, Bazy Danych (PostgreSQL i MySQL), Kontenery. W przygotowaniu są usługi tj. skład obiektowy (~Amazon S3, Swift), SMTP-as-a-service (~SendGrid, ~Mailgun), Kubernetes-as-a-service (Amazon EKS, Google Kubernetes Engine).


Funkcjonalności
-----------------
* W początkowych etapach system będzie przeznaczony do archiwizacji dokumentów pochodzących z różnych kanałów tj.
    
    * poczta tradycyjna
    * poczta e-mail
    * Envelo

* W przyszłości system będzie służył także do:
    
    * zarządzanie przebiegiem procesu sporządzenia pism
    * powiadamiania o nowych pismach
    * kontroli terminów
    * wysyłkę pism poprzez:
        
        * Envelo
        * ePUAP
        * poczta tradycyjna
        
* Platforma udostępnia skuteczne API
* Uwierzytelnienie z wykorzystaniem GSuite


Panel zarządzania
------------------

Technologia
^^^^^^^^^^^^
* framework - React
* protokół komunikacji - REST
* framework UI - AntDesign


Struktura Panelu Zarządzania
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Struktura **Panelu Zarządzania** składa się z trzech sekcji:
    
    * sekcji publicznej
    * sekcji prezentacji kolekcji
    * sekcji edycji

Sekcje publiczna umożliwia:
    
    * zalogowanie do sekcji edycji z wykorzystaniem GSuite
    * uzyskanie podstawowych informacji o projekcie (3-4 zdania)
    * odesłanie do GitHub w celu uzyskania szczegółowych informacji o projekcie

Sekcja prezentacji kolekcji umożliwi zapoznanie się (tylko do odczytu) z sprawami zebranymi w danej kolekcji oraz materiałami z nią powiązanymi (listami, notatkami, wydarzeniami). Dostęp do treści kolekcji będzie możliwy na podstawie przesłanego linku zawierającego token. Niektóre kolekcje mogą być publicznie i nie wymagać żadnego tokenu.

W V2 możemy zacząć od prezentowania wszystkich danych w postaci tabelarycznej.

Sekcja edycji umożliwia:
    
    * odczyt, dodanie i dodanie jednostek administracyjnych (zaimportowanych wstępnie z bazy TERYT)
    * odczyt, dodanie i edycje spraw z uwzględnieniem:
        
        * adaptacji do uprawnień użytkownika
        * filtrowania wyszukiwanych spraw – zob. obecne  ``./ui/v1/case_list.png``
        * edycja sprawy umożliwia określenie:
            
            * instytucji - na podstawie kolekcji instytucji
            * wskazania wartości pól danych statycznych - zgodnie z regułami danego słownika
            * użytkowników odpowiedzialnych
            * użytkowników powiadamianych
        * uzyskanie uzyskania chronologicznej wiedzy na temat elementów powiązanych (listów, notatek, wydarzeń) – zob. pokrewne ``./ui/v1/porady_case_view.png``
        * możliwość wyboru opisu listów wyłącznie spośród przewidzianych wcześniej opisów listów
        * możliwości dodania bez znaczącej zmiany kontekstu sprawy (UX) - zob. obecne ``./ui/v1/case_change.png``:
            
            * wielu listu z uwzględnieniem:
                
                * dodania wielu plików do sprawy
                * wykorzystanie drag-and-drop plików
                * zarządzania kolejnością listów
            * wydarzenia
            * notatki
    * odczyt listów niepowiązanych z sprawami w celu:
    * prostego utworzenie nowej sprawy i powiązania z nową sprawą
    * powiązania z istniejącą sprawą
    * odczyt, dodanie i edycje opisów listów (kolekcja na potrzeby wyboru wartości pola "Opis" w formularzu edycji listu)
    * odczyt, dodanie i edycje słowników (kolekcja na temat pól danych statystycznych w formularzu edycji sprawy)
    * odczyt, dodanie i edycja użytkowników

W przypadku prezentacji odczytu sprawy (a za tym także listów, notatek i wydarzeń) możemy współdzielić komponenty z sekcją prezentacji.

W V2 możemy zacząć od prezentowania wszystkich danych w postaci tabelarycznej.
