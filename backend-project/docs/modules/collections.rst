Kolekecje
=========

Założenia
---------

Moduł odpowiedzialny za luźne zgrupowania spraw, które będą w szczególny sposób udostępniane na zewnątrz systemu wyłącznie do odczytu.

Zgrupowanie może być dynamiczne np. "wszystkie sprawy własne Stowarzyszenia" (dla wglądu przez członków Stowarzyszenia, którzy nie mają dostępu do wszystkich spraw klientów Stowarzyszenia) lub "wszystkie sprawy z Polską Fundacją Narodową" (dla dziennikarza, który poprosił o taki dostęp, gdyż monitoruje temat) lub "wszystkie sprawy oznaczone danym znaczkiem (tagiem)".

Celem jest stworzenie luźnej warstwy prezentacji (nie zarządzania!) danych sprawy dla osób zewnętrznych, które nie mają uprawnień do edycji spraw, ani konta w systemie.

Dostęp do spraw z kolekcji może (nie musi!) wymagać uwierzytelniania danymi dostępowymi stworzonymi specjalnie dla danego odnośnika np. kodem JWT, token linku.

Zakres spraw w kolekcji może ulegać zmianie w czasie w sposób automatyczny, gdyż kolekcja będzie zawierała kryterium wyszukiwania spraw. Można także pokusić się o stworzenie w warstwie prezentacji mechanizmu do statycznych kolekcji, gdzie – podczas zapisu – zapytanie będzie konwertowane do zapytania zawierającego wykaz identyfikatory spraw. Przykładowo "tag=NSA" => "id=1 OR id=2 OR id=3 OR id=4 OR id=5". Format języka zapytań wymaga zdefiniowania (zob. `zagadnienie #103 <https://github.com/watchdogpolska/small_eod/issues/103>`_).

Kolekcje będą stanowiły także podstawę do integracji z oprogramowaniem zewnętrznych np. Wordpress. Przykładowo redaktor strony Stowarzyszenia opracowuje artykuł, który chce uwiarygodnić poprzez dostęp do materiałów źródłowych opisanych spraw. Obecnie musi ręcznie przekopiować pliki do Wordpress. Jednak można to usprawnić poprzez pozwolenie na stworzenie kolekcji, która będzie zawierała sprawy wymienione w artykule, a następnie umieszczenie w treści artykułu znacznika "`shortcode <https://en.support.wordpress.com/shortcodes/>`_" lub poprzez `oEmbed <https://oembed.com/>`_ lub dodatkowe pole w Wordpress umożliwi czytelnikom dostęp do wybranych spraw z kolekcji. Taki mechanizm integracji oznacza, że nie ma ryzyka ujawnienia poufnych danych w przypadku skompromitowania Wordpressa, gdyż Wordpress nie posiada szczególnej praw dostępu do systemu, zatem możemy na wykorzystanie takiej integracji każdemu, w przeciwieństwie do integracji, które będą modyfikowały dane w systemie i posiadały w nim szczególne prawa.

W back-endzie powyższe przekłada się na:

* ścieżka ``/collection/{collectionId}/*`` zawiera ``*/case/*/note``, ``*/case/*/letter`` i ``*/case/*/*event``
* ścieżki ``/collection/{collectionId}/case/*`` są wyłącznie do odczytu (metoda GET), aby umożliwić wyłącznie odczyt danych
* ścieżki ``/collection/{collectionId}/case/*`` posiadają zdefiniowane inne formy uwierzytelniania (parametr ``security`` zawierający ``bearerAuth``)

W front-endzie przekłada się to na sekcje prezentacji kolekcji, która może zawierać uproszczony interfejs do odczytu. Podobne mechanizmy w interfejsie użytkownika:

* udostępnienie katalogu w Google Drive - widok odczytu folderu dla użytkownika, który posiada link jest inny niż użytkownika, który jest uwierzytelniony i zarządza dokumentami


Architektura
------------

Model
~~~~~

.. automodule:: small_eod.collections.models
   :members:

