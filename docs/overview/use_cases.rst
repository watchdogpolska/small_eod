Przypadki użycia
=================

Rejestrowanie korespondencji przychodzącej tradycyjnej
-------------------------------------------------------
**Cel**: publikacja korespondencji przychodzącej tradycyjnej

**Zdarzenie inicjujące**: Wybranie opcji dodania korespondencji przychodzącej przez upoważnionego użytkownika

**Scenariusz (scenariusze) procesów biznesowych**

* Pracownik wybiera dodanie nowego listu
* System wyświetla formularz dodawania nowego listu
    
    * Pola wynikają z interfejsu API
    * Użytkownik pomija pole "Sprawa"
* Użytkownik wypełnia formularz i zatwierdza dodanie listu
* System weryfikuje wprowadzone dane i potwierdza ich przyjęcie.
* Archiwista wyświetla listę listów bez przypisanych spraw.
* Użytkownik wybiera edycje listu.
* System wyświetla formularz edycji listu.
    
    * Pola wynikają z interfejsu API

**Sytuacje wyjątkowe**
Podane dane nie spełniają reguł walidacji – system wyświetla komunikat błędu, proces nie jest kontynuowany do czasu poprawienia błędów i ponownego zatwierdzenia

**Warunki początkowe**
* Użytkownik jest uprawniony do dodania nowego listu.

**Warunki końcowe**
* Osoby przypisane do powiadomień sprawy otrzymują powiadomienie o nowym liście.
* List jest dostępny na liście listów w sprawie.
* List nie jest dostępny na liście listów nie przypisanych.


Rejestrowanie teczki sprawy
----------------------------
**Cel:** publikacja archiwalnej teczki sprawy

**Zdarzenie inicjujące:** Wybranie opcji dodania nowej sprawy przez upoważnionego użytkownika

**Scenariusz (scenariusze) procesów biznesowych**

* Pracownik wybiera dodanie nowej sprawy
* System wyświetla formularz dodawania nowej sprawy
    
    * Pola wynikają z interfejsu API
    * Interfejs umożliwia wprowadzenie także danych wielu listów
* Użytkownik wypełnia formularz i zatwierdza dodanie sprawy
* System weryfikuje wprowadzone dane i potwierdza ich przyjęcie.

**Sytuacje wyjątkowe**
Podane dane nie spełniają reguł walidacji – system wyświetla komunikat błędu, proces nie jest kontynuowany do czasu poprawienia błędów i ponownego zatwierdzenia

**Warunki początkowe**
* Użytkownik jest uprawniony do dodania nowego listu.

**Warunki końcowe**

* Osoby przypisane do powiadomień sprawy otrzymują powiadomienie o nowych listach.
* Sprawa jest dostępna.
* List jest dostępny na liście listów w sprawie.
* List nie jest dostępny na liście listów nie przypisanych.


Utworzenie kolekcji
-------------------
**Cel:** utworzenie kolekcji spraw

**Zdarzenie inicjujące:** Wybranie opcji dodania nowej kolekcji przez upoważnionego użytkownika

**Scenariusz (scenariusze) procesów biznesowych**

* Pracownik wybiera utworzenie nowej kolekcji
* System wyświetla formularz dodawania nowej kolekcji
    
    * Pola wynikają z interfejsu API
* Użytkownik wypełnia formularz i zatwierdza utworzenie kolekcji
* System weryfikuje wprowadzone dane i potwierdza ich przyjęcie.

**Sytuacje wyjątkowe**
Podane dane nie spełniają reguł walidacji – system wyświetla komunikat błędu, proces nie jest kontynuowany do czasu poprawienia błędów i ponownego zatwierdzenia

**Warunki początkowe**
* Użytkownik jest uprawniony do dodania nowej kolekcji.

**Warunki końcowe**
* Użytkownik posiada odnośnik umożliwiający dostęp do kolekcji oraz odczyt wszystkich listów, wydarzeń i notatek w danej sprawie.
