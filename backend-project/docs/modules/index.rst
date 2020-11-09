Moduły
======

Model danych jest dostępny w dokumentacji API.


Dokumentacja API
----------------
Szczegółowy model danych został udokumentowany w `Dokumentacji API <https://small-eod.vercel.app/api/docs/>`_. 

Wizualizacja pliku ``./swagger.yaml`` możliwa jest poprzez `Swagger Editor <https://editor.swagger.io/?url=https://raw.githubusercontent.com/watchdogpolska/small_eod/dev/docs/swagger.yaml>`_ lub `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/watchdogpolska/small_eod/dev/docs/swagger.yaml>`_.


Generowanie dokumentacji API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dokumentacja API zgodna z Swagger 2.0 może zostać wygenerowana z wykorzystaniem:

.. code-block:: python
   
   python manage.py generate_swagger


Dokumentacja bazuje na `drf_yasg2`, dzięki czemu współpracuje ona z generatorami SDK.


SDK
^^^^^

Dostępne są SDK dla następujących języków programowania:

* JavaScript - `small-eod-sdk-javascript <https://github.com/watchdogpolska/small-eod-sdk-javascript>`_


Modele
-------

.. toctree::
   :maxdepth: 2

   administrative_units.rst
   cases.rst
   channels.rst
   collections.rst
   events.rst
   features.rst
   files.rst
   institutions.rst
   letters.rst
   notes.rst
   tags.rst
   users.rst


Uprawnienia
------------

.. include:: uprawnienia.rst
