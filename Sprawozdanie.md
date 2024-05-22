---
title: Working with MyST Markdown
subtitle: A live demo
authors:
  - name: Rowan Cockett
    orcid: 0000-0002-7859-8394
    affiliations:
      - Executable Books
license: CC-BY-4.0
---

# Wzorce sekwencyjne GSP (uogólniony)
## Autor
Mateusz Krakowski 301772

## Cel projektu
Celem projektu jest zbadanie własności zaimplementowanego przez siebie algorytmu GSP: czas
wykonania, uzyskiwane wyniki dla różnych wartości parametrów algorytmu oraz kilku zbiorów
wejściowych.

## Wprowadzenie i definicja problemu
W dzisiejszej erze danych, gromadzenie ogromnych ilości informacji stało się powszechne w różnych dziedzinach. Wraz z tym wzrostem danych pojawiła się potrzeba efektywnej analizy sekwencji zdarzeń, by wyciągać wartościowe wnioski. Narzędzia do odkrywania sekwencyjnych wzorców, jak algorytm GSP (Generalized Sequential Pattern), odgrywają kluczową rolę.

Projekt skupia się na analizie sekwencji zdarzeń w dużych zbiorach danych. Szczególnie ważna jest identyfikacja częstych sekwencji zdarzeń lub transakcji, takich jak historia zakupów klientów w sklepach detalicznych czy sekwencje odwiedzanych stron internetowych przez użytkowników. Algorytm GSP pozwala na odkrycie istotnych wzorców zachowań lub preferencji, co może być użyteczne w podejmowaniu decyzji biznesowych, personalizacji ofert czy optymalizacji interfejsów użytkownika. Poprzez jego zastosowanie, dane wejściowe przetwarzane są w postaci sekwencji zdarzeń, ustalane jest minimalne wsparcie, a następnie identyfikowane są sekwencje spełniające to kryterium. Dzięki temu możliwe jest wyróżnienie istotnych wzorców, umożliwiając bardziej szczegółową analizę i trafniejsze decyzje biznesowe. Wsparcie należy rozumieć jako liczbę występowania zjawiska w bazie danych.

## Sposób działania algorytmu GSP

1. Tworzenie częstych jednoelementowych zbiorów: W pierwszym kroku identyfikowane są pojedyncze elementy występujące często w danych sekwencyjnych.
2. Generowanie kandydatów: Na podstawie częstych jednoelementowych zbiorów generowane są kandydaci na częste sekwencje dwuelementowe poprzez łączenie jednoelementowych zbiorów.
3. Analiza wsparcia: Dla każdego kandydata obliczane jest wsparcie, czyli częstość występowania danej sekwencji w danych wejściowych. Kandydaci, których wsparcie jest niższe niż minimalne określone wsparcie, są odrzucani.
4. Generowanie kolejnych poziomów kandydatów: Proces generowania kandydatów i analizy wsparcia jest powtarzany, aby wygenerować kandydatów na sekwencje trójelementowe, czteroelementowe i tak dalej, dopóki nie zostaną osiągnięte wszystkie pożądane sekwencje lub nie będzie już możliwe wygenerowanie kolejnych kandydatów.
5. Koniec algorytmu: Algorytm kończy się, gdy nie można już wygenerować nowych kandydatów lub osiągnięte zostanie maksymalne poziom wsparcia.
6. Prezentacja wyników: Ostateczne częste sekwencje, czyli te, które spełniają kryteria minimalnego wsparcia, są prezentowane jako wynik działania algorytmu.

## Bibliografia
@article{smith2020,
    author = {Smith, John},
    title = {The Importance of Markdown in Academic Writing},
    journal = {Journal of Academic Writing},
    year = {2020},
    volume = {10},
    number = {2},
    pages = {123-135}
}


## Brudne notaki
https://www.overleaf.com/project/6627b511a3dcf5a655488004


### TODO
1. Wprowadzenie i definicja problemu
2. Charakterystyka proponowanego algorytmu/rozwiązania z odniesieniem do literatury
3. Opis implementacji
4. Instrukcja użytkownika (jak uruchomić/korzystać z implementacji)
5. Charakterystyka wykorzystywanych zbiorów danych
6. Wyniki eksperymentów pokazujących właściwości proponowanego rozwiązania
7. Wnioski
8. Bibliografia
### Key concepts 
GSP
items


### Pytania 08.05.2024

- Czy robić odległość między itemkami, wsm to time constraints, sliding windows, and taxonomies? - Podane przez Pana bazy nie wspierają tego problemu, chyba że arbitralnie wyborę że time constraints 
Okienko!
- Czy używać języka matematycznego, czy mogę ograniczyć się do opisówki?
bez
- Jak mają wyglądać testy? mierzyć czas?
pomeszać bazy, porównać do innych implementacji gsp
- Co Pana najbardziej interesuje w sprawozdaniu?

- Czy możemy spotkać się za 2 tygodni o 13:30?
Tak
- Czy implementować w czystym Pythonie? Pythonowe loopy są okrutnie wolne... więc użyć bibliotek
Python


## TEST
Number of frequent patterns with min_support=0.01: 9932
Time taken: 413.12 seconds
Number of frequent patterns with min_support=0.02: 246
Time taken: 85.19 seconds
Number of frequent patterns with min_support=0.03: 89
Time taken: 16.67 seconds
Number of frequent patterns with min_support=0.04: 40
Time taken: 3.37 seconds
Number of frequent patterns with min_support=0.05: 17
Time taken: 0.62 seconds
Number of frequent patterns with min_support=0.06: 6
Time taken: 0.11 seconds
Number of frequent patterns with min_support=0.08: 1
Time taken: 0.05 seconds
Number of frequent patterns with min_support=0.1: 0
Time taken: 0.05 seconds