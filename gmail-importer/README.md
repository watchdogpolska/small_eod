# GMail Importer

Usługa odpowiedzialna za integracje GMail w celu automatycznego importowania nowych wiadomości przychodzących.

Przepływ nowej wiadomości:

1. skrzynka pocztowa jest konfigurowana w celu przesyłania powiadomień (zob. metoda GMail API: [users.watch](https://developers.google.com/gmail/api/reference/rest/v1/users/watch))
2. nowa wiadomość jest oznaczona w GMailu przez użytkownika
3. GMail przesyła powiadomienie do Google PubSub
4. usługa odbiera powiadomienie i je przetwarza:
    * TODO: explain
5. usługa przesyła wiadomość do small-eod
6. użytkownik odczytuje wiadomość

## Konfiguracja

1. utwórz konto usługi Google, [zgodnie z dokumentacją](https://cloud.google.com/pubsub/docs/authentication?authuser=1)
2. przydziel rolę `roles/pubsub.subscriber` do konta usługi, [zgodnie z dokumentacją](https://cloud.google.com/pubsub/docs/access-control)
3. skonfiguruj uwierzytelnienie, [zgodnie z dokumentacją](https://cloud.google.com/docs/authentication/production)
4. skonfiguruj domain-wide delegation dla konta usługi, [zgodnie z dokumentacją](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) z uprawnieniami:

    * `https://www.googleapis.com/auth/gmail.readonly` - na potrzeby wywołania metody `users.watch`

5. 

## Dodatkowa dokumentacja

* [Adding custom intelligence to Gmail with serverless on GCP](https://cloud.google.com/blog/products/application-development/adding-custom-intelligence-to-gmail-with-serverless-on-gcp)
* [Receiving messages using Pull - Google PubSub](https://cloud.google.com/pubsub/docs/pull)