# Pricer – Architecture Overview

## 1. Project Purpose
Projekt *Pricer* ma być modułowym systemem do:
- generowania harmonogramów (schedule generator),
- obsługi instrumentów rynku finansowego (FRA, IRS, depo, cashflow),
- obliczania day count fraction,
- ładowania danych rynkowych (z CSV lub SQL),
- kalibracji krzywych dyskontujących i forwardowych,
- wyceny instrumentów (pricing engine).

System jest rozwijany iteracyjnie – docelowo ma wspierać wielowalutowy, multi-curve workflow z możliwością podłączenia różnych źródeł danych.

---

## 2. Docelowa struktura pakietów
pricer/
├── dates/
│ ├── holidays.py # ładowanie + normalizacja kalendarzy
│ ├── calendar.py # BusinessDayCalendar – logika dni roboczych
│ ├── daycount.py # wszystkie day-county (ACT, 30E360, ISDA)
│ └── schedule.py # generator harmonogramów („Schedule”)
│
├── marketdata/
│ ├── sources.py # CSV/SQL sources: abstrakcja wejścia
│ ├── loaders.py # FRA/IRS QuotesLoader
│ └── models.py # struktury danych np. FRAQuote
│
├── curves/
│ ├── discount_curve.py # DF-y, interpolacja
│ ├── forwarding_curve.py # forward rates
│ ├── curve_bootstrapper.py# bootstrap krzywych
│ └── curve_set.py # grupowanie krzywych
│
├── instruments/
│ ├── base.py # Cashflow, Leg, Instrument
│ ├── deposits.py
│ ├── fras.py
│ ├── swaps.py
│ └── simple_flows.py
│
├── pricers/
│ ├── fra_pricer.py
│ ├── swap_pricer.py
│ └── portfolio_pricer.py
│
└── utils/
└── ...

---

## 3. Key Components and Responsibilities

### **3.1 Module: dates/**
- 🔹 `holidays.py` – wczytywanie kalendarzy z CSV lub z bazy  
- 🔹 `calendar.py` – logika dni roboczych i przesuwania dat  
- 🔹 `daycount.py` – konwencje naliczania odsetek  
- 🔹 `schedule.py` – konstrukcja harmonogramów płatności

---

### **3.2 Module: marketdata/**
Źródła danych rynkowych:
- `CsvMarketDataSource`
- `SqlMarketDataSource`

Loader’y:
- `FRAQuotesLoader`
- `IRSQuotesLoader`
- Format: struktury typu `FRAQuote`, `SwapQuote`.

---

### **3.3 Module: curves/**
- Budowanie discount curve i forward curve  
- Bootstrap z FRA/IRS  
- Utrzymanie krzywych per waluta / per collateral

---

### **3.4 Module: instruments/**
- Logiczne reprezentacje instrumentów finansowych  
- Zależne od schedule i day-count  
- Przekształcają input → cashflow table

---

### **3.5 Module: pricers/**
- Moduły wyceny:
  - FRA
  - IRS (par rate, NPV)
  - Portfolio
- Korzystają z krzywych, instrumentów i harmonogramów

---

## 4. Data Sources – CSV i SQL (DB Abstraction Layer)
System pozwala korzystać z dwóch źródeł danych:

### CSV
- szybki start, brak konfiguracji

### SQL
- skalowalne, dane historyczne, integracja z rynkiem

Abstrakcja:
- `MarketDataSource` → `CsvMarketDataSource` / `SqlMarketDataSource`
- `HolidaysProvider` → `CsvHolidaysProvider` / `DbHolidaysProvider`

Pozwala to przełączać backend jednym parametrem konfiguracyjnym.

---

## 5. Roadmap (kolejne kroki)
1. Refaktoryzacja `schedule.py` do struktury dates/
2. Dodanie klasy `BusinessDayCalendar`
3. Wydzielenie daycount do `dates/daycount.py`
4. Wprowadzenie warstwy źródeł danych (marketdata/sources.py)
5. Pierwsza discount curve (PLN-OIS)
6. FRA pricing → curve calibration
7. IRS pricing → full multi-curve

---

## 6. Testy
Testy przeglądowe:
- testy kalendarza i day-countów,
- testy generatora schedule,
- testy instrumentów,
- testy pricerów.

Struktura:
tests/test_dates_.py
tests/test_curves_.py
tests/test_instruments_.py
tests/test_pricers_.py

---

## 7. Przyszła rozbudowa
- interfejs REST / API
- integracja z SQL Server / PostgreSQL
- scenario / what-if engine
- Monte Carlo dla wyceny opcjonalnej
