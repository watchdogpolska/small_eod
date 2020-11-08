Architektura
=============

System składa się z następujących komponentów:

    * Back-end - Django, dostępny w podkatalogu ``backend-project``
    * Front-end - React, dostępny w podkatalogu ``frontend-project``
    * Minio - podsystem składowania plików binarnych (dokumenty, zdjęcia itp.)
    * Baza danych PostgreSQL

Dodatkowe uwagi:

    * Projekt Stowarzyszenia korzysta z kontenerów Docker.
    * Dodatkowe integracje tj. e-mail, ePUAP, Envelo mogą być odrębnymi usługami, lecz komunikującymi się (microservices)
    * Back-end udostępnia dokumentacja REST API zgodną z Swagger
    * Została opracowana biblioteka: `small-eod-sdk-javascript <https://github.com/watchdogpolska/small-eod-sdk-javascript/>`_

Back-end
^^^^^^^^^

Back-end utworzony z wykorzystaniem Django.
Dostępny w podkatalogu ``backend-project``.

.. toctree::
   :maxdepth: 3

   ../modules/index.rst
