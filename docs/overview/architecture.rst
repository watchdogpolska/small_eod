Architektura
=============

System składa się z następujących komponentów:

    * Backend - Django, dostępny w podkatalogu ``backend-project``
    * Frontend - React, dostępny w podkatalogu ``frontend-project``
    * Minio - podsystem składowania plików binarnych (dokumenty, zdjęcia itp.)
    * Baza danych PostgreSQL

Dodatkowe uwagi:

    * Projekt Stowarzyszenia korzysta z kontenerów Docker
    * Dodatkowe integracje tj. e-mail, ePUAP, Envelo mogą być odrębnymi usługami, lecz komunikującymi się (microservices)
    * Back-end udostępnia dokumentacja REST API zgodną z Swagger
    * Została opracowana biblioteka: `small-eod-sdk-javascript <https://github.com/watchdogpolska/small-eod-sdk-javascript/>`_

Backend
^^^^^^^^^
Backend utworzony z wykorzystaniem: 

    * `Django <https://www.djangoproject.com>`_
    * `Django Rest Framework <https://www.django-rest-framework.org>`_

Szczegółowa dokumentacja dostępna w sekcji "Backend".

Frontend
^^^^^^^^^
Frontend został napisany z wykorzystaniem:

    * `React <https://reactjs.org/>`_
    * `Redux <https://redux.js.org/>`_
    * `TypeScript <https://www.typescriptlang.org/>`_
    * `Less <http://lesscss.org/>`_
    * `AntDesign <https://ant.design/>`_

Szczegółowa dokumentacja dostępna w sekcji "Frontend".
