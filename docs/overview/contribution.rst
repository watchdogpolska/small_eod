Udział w projekcie
====================

W celu rozwoju projektu kod źródłowy projektu można pobrać za pomocą komendy git:

.. code-block:: bash
   
   git clone git@github.com:watchdogpolska/small_eod.git

W przypadku pracy w środowisku ``Windows/Mac`` można wykorzystać `GitHub Desktop <https://desktop.github.com/>`_. W celu pobrania należy `postępować zgodnie z instrukcją <https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>`_.

Projekt realizowany jest zgodnie z filozofią open-source. Szczegółowe informacje na temat:

* w jaki sposób wprowadzić zmiany do projektu sa dostępne w `https://github.com/firstcontributions/first-contributions <https://github.com/firstcontributions/first-contributions>`_
* udziału w projektach open-source i sposobie organizacji pracy dostępne w artykule "`How to Contribute to Open Source <https://opensource.guide/how-to-contribute/>`_"

Zadania do wykonania są zarejestrowane jako zagadnienia oznaczone etykietą good first issue w portalu GitHub. W celu ich realizacji wystarczy komentarz o rozpoczęciu prac, a następnie utworzenie żądania wcielenia zmian (pull request).

Komunikacja w projekcie
------------------------

Bieżąca komunikacja projektu odbywa się z wykorzystaniem Slacka organizacji `CodeForPoznań <https://join.slack.com/t/codeforpoznan/shared_invite/enQtNjQ5MTU1MDI0NDA0LWNhYTA3NGQ0MmQ5ODgxODE3ODJlZjc3NWE0NTMzZjhmNDBkN2QwMzNhYWY5OWQ5MGE2OGM3NjAyODBlY2VjNjU>`_ na kanale **#watchdog**. 
Odbywają się regularne spotkania statusowe (`szczegóły <https://github.com/watchdogpolska/small_eod/issues/547>`_), gdzie można uzyskać wprowadzenie w projekt, dowiedzieć się na temat zadań i usunąć inne trudności we współpracy.

Uruchamianie projektu
----------------------

W celu ułatwienia rozwoju projektu wykorzystywane jest oprogramowanie Docker. Umożliwia ona uruchomienie wszystkich usług niezbędnych do pracy nad projektem. Usługi zostały opisane w pliku ``docker-compose.yml``.

W celu uruchomienia środowiska aplikacji wymagane jest:

* instalacja `Docker <https://docs.docker.com/install/>`_, zgodnie z `dokumentacją projektu Docker <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_.
* instalacja `docker-compose <https://docs.docker.com/compose/install/>`_, w przypadku pracy na Linux (Docker dla Windows i Mac jest dostarczony z tym oprogramowaniem w standardzie)

Aby dowiedzieć się więcej o oprogramowaniem zapoznaj się z wideo `Docker dla webdevelopera - #01 - Czym jest Docker? <https://www.youtube.com/watch?v=P4ZC3cFN0WQ>`_.

W celu uruchomienia projektu należy wykonać:

.. code-block:: bash
    
    docker-compose up


Po pomyślnym uruchomieniu projektu środowisko pod adresem `http://localhost:8000/admin/ <http://localhost:8000/admin/>`_ winno być możliwe logowanie z wykorzystaniem loginu i hasła, a wszelkie zmiany kodu aplikacji w lokalnym repozytorium będą automatycznie załadowane przez Django.

W celu utworzenia konta administratora należy wykonać:

.. code-block:: bash

    docker-compose run backend python manage.py createsuperuser


W celu utworzenia próbnych danych należy wykonać:

.. code-block:: bash

    docker-compose run backend python manage.py init_data

W razie problemów z uruchomieniem projektu utwórz `nowe zagadnienie <https://github.com/watchdogpolska/small_eod/issues/new>`_

Testy automatyczne
----------------------
Projekt wykorzystuje testy automatyczne, które zapewniają weryfikacje wszystkich wprowadzonych zmian. Wszelkie proponowane zmiany z wykorzystaniem `GitHub Actions <https://github.com/watchdogpolska/small_eod/actions>`_.

Wszelkie zmiany w repozytorium będą uruchamiały serie testów automatycznych, ale przed ich dodaniem masz możliwość wykonania testów lokalnie za pomocą `Makefile <https://en.wikipedia.org/wiki/Makefile>`_.

W celu wykonanie testów automatycznych formatowania należy wykonać:

.. code-block:: bash
    
    make lint


Większość problemów w formatowania można naprawić z wykorzystaniem automatycznego formatowania za pomocą wykonania:

.. code-block:: bash
    
    make fmt


W celu wykonania testów automatycznych back-endu należy wykonać:

.. code-block:: bash

    make test-django-backend

Dokumentacja
------------

W celu wygenerowania aktualnej wersji niniejszej dokumentacji należy wykonać:

.. code-block:: bash

    make docs

Wdrożenie automatyczne
----------------------

Każda zmiana znajdująca się na gałęzi ``dev`` jest wdrażana z wykorzystaniem GitHub Actions do usługi `*Strona* od HyperOne <https://www.hyperone.com/services/compute/website/>`_, która jest usługą klasy platform-as-a-service.

Dla potrzeb środowiska testowego w HyperOne zostały uruchomione:

* dwie odrębne usługi *Strona*:
    
    * dla back-endu – oparte o środowisko wykonawcze ``h1cr.io/website/python-passenger:3.7``
    * dla front-endu – oparte o środowisko wykonawcze ``h1cr.io/website/nginx-static:latest``
* usługa `Baza danych <https://www.hyperone.com/services/storage/database/>`_ w wariancie PostgreSQL 11
* kontenery w klasycznej infrastrukturze Stowarzyszenia (bazującej na `Wirtualnych Maszynach <https://www.hyperone.com/services/compute/vm/)* HyperOne>`_:
    
    * Minio – dla usługi składowania plików – do momentu opracowania zarządzanej usługi przez dostawcę usług chmurowych
    * Balancer – dla zintegrowania usług *Strona* – do momentu opracowania zarządzanej usługi przez dostawcę usług chmurowych

Dostęp do wersji demo
-----------------------

W sprawie dostępu do `wersji demo <https://demo.small-eod.siecobywatelska.pl/admin/>`_ napisz na Slacku.



Materiały dodatkowe
-----------------------
`Konfiguracja środowiska z użyciem IntelliJ PyCharm <https://github.com/watchdogpolska/small_eod/blob/dev/docs/pycharm/README.md>`_


Wsparcie Vercel
-----------------------
Projekt wspierany jest przez firmę `Vercel <http://vercel.com/?utm_source=watchdogpolska&utm_campaign=small_eod>`_
