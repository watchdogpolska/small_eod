Instalacja
==========

Wymagane składniki
-------------------

  * `Node.js <https://nodejs.org/en/download/>`_
  * `Yarn <https://yarnpkg.com/getting-started/install>`_
  * `npm <https://www.npmjs.com/get-npm>`_ (na niektórych dystrybucjach Linuxa Node.js nie jest domyślnie instalowany z npm)


Procedura
----------

#. Utwórz własny `fork repozytorium <https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo>`_ (krok nie jest konieczny, jeżeli nie zamierzasz wprowadzać zmian do oryginalnego repozytorium)

#. Pobierz repozytorium na swój dysk z wykorzystaniem polecenia:

    .. code-block:: bash
    
        git clone git@github.com:<nazwa profilu>/small_eod.git
   
#. Przejdź do katalogu zawierającego frontend z wykorzystaniem polecenia:

   .. code-block:: bash
        
        cd small_eod/frontend-project

#. Zainstaluj zależności za pomocą narzędzia yarn z wykorzystaniem polecenia:

   .. code-block:: bash
        
        yarn
   

#. Projekt możesz uruchomić poleceniem:

   .. code-block:: bash
        
        yarn start
   

   W celu jego poprawnego działania musisz mieć poprawnie uruchomiony backend (serwer API). Możesz wykorzystać ogólnodostępne deweloperskie API poprzez uruchomienie poleceniem:

   .. code-block:: bash
        
        yarn start:public-api
   

#. W celu uruchomienia testów wykonaj polecenie:

   .. code-block:: bash
        
        yarn test
   

Zmienne środowiskowe
--------------------

.. list-table::
    :header-rows: 1

    * - Nazwa
      - Opis
      - Domyślna wartość
    * - ``API_URL``
      - adres URL serwera API (backend)
      - ``http://backend:8000/``
    * - ``COMMIT_SHA``
      - identyfikator SHA commitu dla buildu
      - undefined
    * - ``COMMIT_BRANCH``
      - identyfikator gałęzi dla buildu
      - undefined
    * - ``REACT_APP_ENV``
      - rodzaj środowiska React
      - ``dev``
