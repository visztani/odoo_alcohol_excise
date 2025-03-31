# ADÓRAKTÁR

## Törzsadatok

- **Cég**
  - Engedélyszám (Keretengedély)

- **Partner**
  - Adószám
  - Gyártó esetén méret (alkohol esetén hektoliterben)
  - Jövedéki ügyfél?
  - B2C?
  - B2B?
    - Telephely(ek)
      - Cím
      - Nyitvatartási szám
      - Elérhetőség
        - Adóraktár
          - Engedélyszám
        - Kisker
          - semmi

- **TERMÉK**
  - KNKód
  - Fajtakód
  - EU kód (Sör: B000) [Excise Product Code]
  - Adóalap (pl.: HLF)
  - Adóalap mértékegysége (pl.: Alk%)
  - LOT
  - Best Before

- **ADÓMÉRTÉK KÓD**
  - Adómérték kód
  - Összeg
  - Devizanem

- **RAKTÁR (saját)**
  - Tulajdonos (Cég vagy Partner)
  - Engedélyszám
  - Vámhivatal hivatkozási száma
    - Raktárhely(ek)
      - Terméktulajdonos (Cég vagy Partner)
      - Készlettípus
        - 1 - Biztosítékköteles
        - 2 - Biztosítékmentes
        - 3 - Adózott
        - 4 - Nem jövedéki termék

## MOZGÁSOK

- **Törzsadatok**
  - (Partner adatok)
  - (AHK)
  - RAKTÁR.*
  - Sorok Összesített adóalapja
  - Jogcímkód
  - Rendszám

- **Sorok**
  - Sorszám (1-től)
  - Termék
    - Név
    - (Alkohol%)
  - Mennyiség
  - Mennyiségi egység
  - Adóalap soronként
  - Adóalap mértékegység
  - Adómérték kód
  - RAKTÁR.Raktárhely.Készlettípus

## DOKUMENTUMOK

- **Szállítólevél**
  - MOZGÁS.Törzsadatok
  - MOZGÁS.SOROK

- **Gyártási bizonylat**
  - MOZGÁS.Törzsadatok
  - MOZGÁS.SOROK

## ELEKTRONIKUS ADATKÖZLÉS (NAV)

- **Napi jelentés (J28)**
  - Időszak
  - Cég (engedélyes)
  - Cég.Adószám
  - RAKTÁR.Engedélyszám
  - RAKTÁR.Telephely
  - Cég.Bejelentő.Adóazon
    - Csökkenés
      - Kitárolás
        - MOZGÁS.Termék.KNKód
        - MOZGÁS.Termék.Fajtakód
        - MOZGÁS.Termék.Adóalap
        - RAKTÁR.Raktárhely.Készlettípus
          - MOZGÁS.Törzsadatok.Jogcímkód
          - MOZGÁS.Sorok.Adóalap soronként
          - MOZGÁS.Sorok.Adómérték kód
          - Partner.Név
          - Partner.Telephely.Cím
          - Partner.Adószám
          - MOZGÁS.ID
      - Gyártás
        - MOZGÁS.Törzsadatok.Jogcímkód
    - Növekedés
      - Gyártás
        - MOZGÁS.Termék.KNKód
        - MOZGÁS.Termék.Fajtakód
        - MOZGÁS.Termék.Adóalap
        - RAKTÁR.Raktárhely.Készlettípus
          - MOZGÁS.Törzsadatok.Jogcímkód
          - MOZGÁS.Sorok.Adóalap soronként
          - MOZGÁS.Sorok.Adómérték kód

- **Havi jelentés (BEV_J02)**
  - Cég.Engedélyszám(keretengedély)
  - Cég.Adószám
  - Cég.Székhely
  - Időszak
  - Bevallás fajtája (6)
  - Cég.Pénzforgalmi számla
  - Cég.Bejelentő
    - Sorok (fajtakódonként)
      - Idöszak.MOZGÁS.SOROK.Termék.Fajtakód
      - Időszak.MOZGÁS.SOROK.Termék.Adóalap soronként * ADÓMÉRTÉK KÓD.Összeg

- **EMCS visszaigazolás (IE818M)**
  - Üzenetazonosító(RAKTÁR.Engedélszám+YYY.MM.DD+XYZ)
  - MOZGÁS.AHK
  - Cég.Engedélyszám (keretengedély)
  - Cég.Név
  - Cég.Székhely.Cím
  - Cég.Adószám
  - Keltezés.Helység
  - Keltezés.Dátum
  - Cég.Bejelentő.Adóazonosító
  - Cég.Telephely.Engedélyszám
  - RAKTÁR.Tulajdonos
  - RAKTÁR.Telephely.Cím
  - Nyelvkód
  - RAKTÁR.Vámhivatal Hivatkozási Száma
  - Keltezés.Dátum
  - MOZGÁS.Törzsadatok.Jogcímkód
    - Sorok
      - MOZGÁS.Sorok.Sorszám
      - MOZGÁS.Sorok.Termék.EU Kód
      - MOZGÁS.Sorok.Termék.Fajtakód
      - MOZGÁS.Sorok.Adóalap soronként
      - RAKTÁR.Raktárhely.Készlettípus

- **EMCS feladás (IE818)**

## JELENTÉSEK

- **Készletmozgás**
  - MOZGÁSOK
- **Készlet**
  - RAKTÁR
