# GP BREED DATA

## Cel projektu

GP BREED DATA jest systemem informacji hodowlanej dla rasy Gończy Polski.

Głównym celem jest stworzenie kompletnej, wiarygodnej i rozwijalnej bazy danych psów, rodowodów oraz informacji hodowlanych.

System ma umożliwiać:

- przechowywanie danych psów,
- generowanie rodowodów,
- analizę genealogiczną,
- obliczanie współczynników inbredu,
- obsługę hodowli i przydomków,
- moderację danych użytkowników,
- import danych ze starszych baz.

---

# Aktualna architektura

## Backend

Technologie:

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker

## Frontend

Planowane:

- aplikacja webowa

## Baza danych

PostgreSQL uruchomiony w Dockerze.

---

# Główne założenia biznesowe

## Psy

Każdy pies posiada:

- nazwę,
- przydomek hodowlany,
- płeć,
- datę urodzenia,
- rodziców,
- historię,
- identyfikatory.

Rodowód nie będzie zapisywany jako statyczny dokument.

Będzie generowany dynamicznie na podstawie relacji rodziców.

---

# Główne encje systemu

## Animal

Najważniejsza encja.

Reprezentuje psa.

---

## Kennel

Osobna baza hodowli.

Przydomki hodowlane nie będą wpisywane jako zwykły tekst.

System będzie wykrywał potencjalne duplikaty.

---

## Party

Uniwersalna encja reprezentująca:

- osobę,
- hodowcę,
- hodowlę,
- organizację.

---

## Litter

Mioty.

Powiązane z:

- ojcem,
- matką,
- hodowlą,
- potomstwem.

---

# Planowane moduły

## Genealogia

- rodowody 4, 8, 10 pokoleń,
- przodkowie,
- potomstwo,
- wspólni przodkowie.

## Analiza hodowlana

- COI,
- AVK,
- kalkulator planowanego skojarzenia.

## Moderacja

Użytkownicy zgłaszają dane.

Administrator:

- zatwierdza,
- odrzuca,
- poprawia.

---

# Import danych

Priorytet:

Zabezpieczenie istniejącej bazy.

Plan:

Stara baza
↓
Importer
↓
Dane surowe
↓
Walidacja
↓
PostgreSQL

Zdjęcia nie są priorytetem.

Najważniejsze:

- psy,
- rodzice,
- rodowody,
- hodowle.

---

# Aktualny status

## Gotowe:

- GitHub
- Visual Studio Code
- Docker
- PostgreSQL
- FastAPI
- Python virtual environment

## W trakcie:

- projekt bazy danych,
- modele SQLAlchemy.

---

# Zasady pracy

1. Każda większa zmiana trafia do dokumentacji.
2. Każdy etap kończy się działającym kodem.
3. Po każdym większym kroku robimy commit Git.
4. Nie rozwijamy nowych modułów przed zakończeniem aktualnego etapu.

---

# Aktualny etap

ETAP 1:
Fundament backendu.

Cel:

Utworzenie pierwszych modeli bazy danych i migracji.
