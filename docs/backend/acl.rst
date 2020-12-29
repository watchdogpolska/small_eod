Uprawnienia
===========

Klasy uprawnień mają następujące znaczenie:

    * change - edycja wszystkich elementów danego typu
    * view - wyświetlanie wszystkich elementów danego typu
    * delete - usunięcie wszystkich elementów danego typu
    * change_own - edycja elementów danego typu utworzonych przez tego samego użytkownika
    * change_all - edycja elementów danego typu utworzonych przez dowolnego użytkownika

W celu kontroli dostępu wykorzystywane jest:

    * uwierzytelnianie poprzez GSuite - oznaczone w dokumentacji API jako ``sessionAuth``
    * uwierzytelnianie hasłem - wyłącznie w celach administracyjnych, tożsame z oznaczeniem w API jako ``sessionAuth``
    * uwierzytelnianie token JWT - oznaczone w dokumentacji API jako ``bearerAuth``.

Dokumentacja API pomija uwierzytelnianie w ten sposób jako standardowy protokół.

Rodzaje uprawnień
-----------------

System wyróżnia następujące uprawnienia:

Feature
^^^^^^^^

    * Feature.change
    * Feature.view
    * Feature.delete
    * Feature.create

FeatureOption
^^^^^^^^^^^^^

    * FeatureOption.change
    * FeatureOption.view
    * FeatureOption.delete
    * FeatureOption.create

Case
^^^^

    * Case.change
    * Case.view
    * Case.delete
    * Case.create

Institution
^^^^^^^^^^^

    * Institution.change
    * Institution.view
    * Institution.delete
    * Institution.create

Tag
^^^^

    * Tag.change
    * Tag.view
    * Tag.delete
    * Tag.create

Collection
^^^^^^^^^^

    * Collection.change_own
    * Collection.change_all
    * Collection.view
    * Collection.delete
    * Collection.create

Letter
^^^^^^^

    * Letter.change_own
    * Letter.change_all
    * Letter.view
    * Letter.delete
    * Letter.create

Channel
^^^^^^^

    * Channel.change
    * Channel.view
    * Channel.delete
    * Channel.create

Note
^^^^

    * Note.change_own
    * Note.change_all
    * Note.view
    * Note.delete
    * Note.create

Event
^^^^^

    * Event.change_own
    * Event.change_all
    * Event.view
    * Event.delete
    * Event.create

User
^^^^

    * User.change_own
    * User.change_all
    * User.view
    * User.delete
    * User.create

DocumentType
^^^^^^^^^^^^

    * DocumentType.change
    * DocumentType.view
    * DocumentType.delete
    * DocumentType.create

AdministrativeUnit
^^^^^^^^^^^^^^^^^^

    * AdministrativeUnit.change
    * AdministrativeUnit.view
    * AdministrativeUnit.delete
    * AdministrativeUnit.create
