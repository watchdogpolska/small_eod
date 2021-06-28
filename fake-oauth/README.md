# small_eod fake-oauth

Zawiera prosty serwer umożliwiający lokalne testowanie aplikacji, bez konieczności komunikacji z serwerem oauth.

Tylko i wyłącznie do lokalnego testowania.

## Uruchamianie

Serwer uruchomi się razem z pozostałymi komponentami przy użyciu docker-compose.
Uwaga - aby aplikacja korzystała z fake-oauth zamiast prawdziwego serwera oauth, konieczne są zmiany w konfiguracji backend-project. Więcej informacji można znaleźć w folderze projektu backendowego.
Zaimplementowano jedynie absolutne minimum funkcjonalności.

## Ostrzeżenie przeglądarki

Większość przeglądarek wyświetli ostrzeżenie przy pierwszym kontakcie z serwerem, spododowane samodzielnie podpisanym certyfikatem.
O ile w przypadku publicznych serwerów jest to oznaka potencjalnego zagrożenia, w tym przypadku ostrzeżenie można zignorować.
