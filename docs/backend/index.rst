Omówienie
=========

Komponent odpowiedzialny za trwałość przechowywanych informacji.


Dokumentacja API
----------------

Komponent udostępnia automatycznie rzeczywistą dokumentacje API pod adresem: `/api/docs`.

Dokumentacja ze środowiska przejściowego jest dostępna: `Dokumentacji API <https://small-eod.vercel.app/api/docs/>`_. 

Generowanie dokumentacji API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dokumentacja API zgodna z Swagger 2.0 może zostać także wygenerowana z wykorzystaniem:

.. code-block:: python

   python manage.py generate_swagger

Dokumentacja bazuje na `drf_yasg2`, dzięki czemu współpracuje ona z generatorami SDK.
