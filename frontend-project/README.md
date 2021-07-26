# small_eod frontend

Zawiera pliki odpowiedzialne za frontend aplikacji small_eod. Został on napisany z wykorzystaniem:

- [React](https://reactjs.org/)
- [Redux](https://redux.js.org/)
- [TypeScript](https://www.typescriptlang.org/)
- [Less](http://lesscss.org/)
- [AntDesign](https://ant.design/)

## Instrukcja instalacji

### Wymagane składniki

- [Node.js](https://nodejs.org/en/download/)
- [Yarn](https://yarnpkg.com/getting-started/install)
- [npm](https://www.npmjs.com/get-npm) (na niektórych dystrybucjach Linuxa Node.js nie jest domyślnie instalowany z npm)

### Instalacja

1. [Utwórz własny fork repozytorium](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) (krok nie jest konieczny, jeżeli nie zamierzasz wprowadzać zmian do oryginalnego repozytorium)

2. Pobierz repozytorium na swój dysk z wykorzystaniem polecenia:

   ```shell
   git clone git@github.com:<nazwa profilu>/small_eod.git
   ```

3. Przejdź do katalogu zawierającego frontend z wykorzystaniem polecenia:

   ```shell
   cd small_eod/frontend-project
   ```

4. Zainstaluj zależności za pomocą narzędzia yarn z wykorzystaniem polecenia:

   ```shell
   yarn
   ```

5. Projekt możesz uruchomić poleceniem:

   ```shell
   yarn start
   ```

   W celu jego poprawnego działania musisz mieć poprawnie uruchomiony backend (serwer API). Możesz wykorzystać ogólnodostępne deweloperskie API poprzez uruchomienie poleceniem:

   ```shell
   yarn start:public-api
   ```

   Aby ominąć logowanie za pomocą OAuth możesz uruchomić aplikację dodając zmienne środowiskowe USER oraz PASSWORD. Przy takim ustawieniu aplikacja wykorzysta logowanie z wykorzystaniem basic auth.

   ```
   USER=root PASSWORD=root yarn start:public-api
   ```

6. W celu uruchomienia testów wykonaj polecenie:

   ```shell
   yarn test
   ```

## Zmienne środowiskowe

| Nazwa           | Opis                                 | Domyślna wartość       |
| --------------- | ------------------------------------ | ---------------------- |
| `API_URL`       | adres URL serwera API (back-end)     | `http://backend:8000/` |
| `COMMIT_SHA`    | identyfikator SHA commitu dla buildu | undefined              |
| `COMMIT_BRANCH` | identyfikator gałęzi dla buildu      | undefined              |
| `REACT_APP_ENV` | rodzaj środowiska React              | `dev`                  |
