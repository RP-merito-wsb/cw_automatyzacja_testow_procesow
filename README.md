# Projekt Testowania API

## Opis

To jest aplikacja napisana w Pythonie, która automatyzuje testowanie publicznych endpointów API za pomocą `curl` i Pythona. Wysyła żądania HTTP GET do wybranych endpointów, sprawdza kody statusu HTTP i weryfikuje obecność kluczowych elementów w odpowiedziach JSON.

## Pliki

- `api_test.py`: Główna aplikacja do testowania API.
- `test_api_test.py`: Testy jednostkowe dla aplikacji.
- `Makefile`: Zautomatyzowane procesy dla instalacji zależności, uruchamiania testów i aplikacji.

## Użycie

1. Instalacja zależności:
    ```sh
    make install
    ```

2. Uruchomienie testów jednostkowych:
    ```sh
    make test
    ```

3. Uruchomienie aplikacji:
    ```sh
    make run
    ```

## Struktura Projektu

