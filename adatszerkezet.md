ADÓRAKTÁR
    Cég
        Engedélyszám ("keretengedély")
    Jövedéki raktár
        Engedélyszám
        Gyártó esetében méret (hektoliterben megadva)
            Raktárhely
                Biztosíték
                    1 - Biztosítékköteles
                    2 - biztosítékmentes
                    3 - adózott
                    4 - nem jövedéki termék     
        
        Jövedéki termék
            Fajtakód
            KNkód
            EU-kód (Sör: B000)
                
                Jövedéki mozgások
                    Jogcímkód
                        Betárolás
                            Másik adóraktárból (Partner)
                                Partner
                                    Engedélyszám
                                    Jövedéki partner
                        Gyártásból

                        Kitárolás
                            Másik adóraktárba (Partner)


Törzsadatok

    Cég
        Adószám
        Engedélyszám (Keretengedély)
    
    Partner
        Adószám
        Gyártó esetén méret (alkohol esetén hektoliterben)
            Telephely(ek)
                Cím
                Nyitvatartás
                Elérhetőség
                    Adóraktár
                        Engedélyszám
                    Kisker
                        semmi
    
    TERMÉK
        KNKód
        Fajtakód
        EU kód (Sör: B000)
        Adóalap (pl.: HLF)
        Adóalap mértékegysége (pl.: Alk%)
        LOT
        BB
    
    ADÓMÉRTÉK KÓD
        Adómérték kód
        Összeg
        Devizanem

    RAKTÁR (saját)
        Tulajdonos (Cég vagy Partner)
        Engedélyszám
            Raktárhely(ek)
                Terméktulajdonos (Cég vagy Partner)
                Készlettípus
                    1 - Biztosítékköteles
                    2 - Biztosítékmentes
                    3 - Adózott
                    4 - Nem jövedéki termék

    MOZGÁSOK
        Törzsadatok
            (Partner adatok)
            RAKTÁR.*
            Sorok Összesített adóalapja
        Sorok
            Jogcímkód
            Termék
                Név
                (Alkohol%)
            Mennyiség
            Mennyiségi egység
            Adóalap soronként
            Adóalap mértékegység
            Adómérték kód
            RAKTÁR.Raktárhely.Készlettípus


    DOKUMENTUMOK
        Szállítólevél
            MOZGÁS.Törzsadatok
            Rendszám
            MOZGÁS.SOROK
        Gyártási bizonylat
            MOZGÁS.Törzsadatok
            MOZGÁS.SOROK


    ELEKTRONIKUS ADATKÖZLÉS (NAV)
        Napi jelentés (J28)
            Időszak
            Cég (engedélyes)
            Cég.Adószám
            RAKTÁR.Engedélyszám
            RAKTÁR.Telephely
            Cég.Bejelentő.Adóazon
                Csökkenés
                    Kitárolás
                        MOZGÁS.Termék.KNKód
                        MOZGÁS.Termék.Fajtakód
                        MOZGÁS.Termék.Adóalap
                        RAKTÁR.Raktárhely.Készlettípus
                            MOZGÁS.Sorok.Jogcímkód
                            MOZGÁS.Sorok.Adóalap soronként
                            MOZGÁS.Sorok.Adómérték kód
                            Partner.Név
                            Partner.Telephely.Cím
                            Partner.Adószám
                            MOZGÁS.ID
                    Gyártás
                        MOZGÁS.jogcímkód
                Növekedés
                    Gyártás
                        MOZGÁS.Termék.KNKód
                        MOZGÁS.Termék.Fajtakód
                        MOZGÁS.Termék.Adóalap
                        RAKTÁR.Raktárhely.Készlettípus
                            MOZGÁS.Sorok.Jogcímkód
                            MOZGÁS.Sorok.Adóalap soronként
                            MOZGÁS.Sorok.Adómérték kód
        Havi jelentés (BEV_J02)
            Cég.Engedélyszám(keretengedély)
            Cég.Adószám
            Cég.Székhely
            Időszak
            Bevallás fajtája (6)
            Cég.Pénzforgalmi számla
            Cég.Bejelentő
                Sorok (fajtakódonként)
                    Idöszak.MOZGÁS.SOROK.Termék.Fajtakód
                    Időszak.MOZGÁS.SOROK.Termék.Adóalap soronként * ADÓMÉRTÉK KÓD.Összeg

        EMCS visszaigazolás (IE818M)
        EMCS feladás (IE818)
    
    JELENTÉSEK
        Készletmozgás
        Készlet