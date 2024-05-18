# Alcohol Excise tracking for Odoo
 
## Hungarian extension / modification for Tax Warehouses receiving, sending, storing excise products (storing only, no manufacturing) under duty suspension

### To-do tasks

- [x] Excise Move törlés tiltása (reporting alatt)
- [x] Biztosítékköteles helyett készlettípus bevezetése (0 - biztosítékmentes, 1 - biztosítékköteles, 3 - adózott jöv. termék, 4 - nem jöv. term.)
- [ ] Jogcímkód terméksoronként a fejlécből, de változtatható legyen (pl. értékesítés és promóciós termék ugyanazzal a szállítással)
- [ ] Reportingban a visszaszállított tétel mínusz előjellel (?)
- [x] Reportingban a készletmozgás adott időszakra
- [ ] Reporting alatt HLF megejelenítése
- [x] Reporting alatt "Sender" oszlop hozzáadása (feladó cég)
- [ ] ÁNYK export napi jelentés (J28)
- [ ] ÁNYK havi jelentés (BEV J02)
- [ ] ÁNYK I815M export
- [ ] Ha az excise category-ban az additional category is beállításra kerül, akkor duplán kerül be az excis move-ba az adott move line
- [ ] Excise Category alatt a kategóriában az "additional category " tiltása, mivel dupla move line jelenséghez vezet
- [ ] Fordítás
- [ ] 2.14. Készletfelvétel során megállapított készlet többlet
- [ ] 2.21. Szabadforgalomba bocsátott jövedéki termék kiszállítást követő 72 órán belül részben vagy teljes mennyiségben történő visszaszállítása*
- [ ] 72 órán belüli visszaszállítás esetén: eredeti bizonylat száma, JOGCÍMKÓD csere, Vendor, Delivery address.
- [ ] 3.7. A Jöt. 9. § (1) bekezdés c) pont cb) alpontja szerint megsemmisítés
- [ ] 3.23. Szabadforgalomba bocsátott, az adóraktárban adófizetési kötelezettséget eredményező módon elfogyasztott, felhasznált jövedéki termék*
- [ ] 3.27. Készletfelvétel során megállapított készlethiány
- [ ] Gyártás modul

### Követelmények

[Szállítólevél adattartalma - Jöt. VH. rendelet 36. §](https://net.jogtar.hu/jogszabaly?docid=a1600045.ngm)
    
[2016. évi LXViii. Törvény a jövedéki adóról](https://net.jogtar.hu/jogszabaly?docid=a1600068.tv)

[45/2016. (XI. 29.) NGM rendelet a jövedéki adóról szóló 2016. évi LXVIII. törvény egyes rendelkezéseinek végrehajtásáról](https://net.jogtar.hu/jogszabaly?docid=a1600045.ngm)

__Jöt. 20.§(1) a) (elektronikus nyilvántartási kötelezettség)__

- __Vh. rendelet szerinti adattartalom:__


   - Adóraktári nyilvántartás és az adóraktár Jöt. 24. § szerinti adatszolgáltatásának adattartalma

    -   A „*” jelzéssel ellátott adatokat a Jöt. 24. §-a szerinti adatszolgáltatásában kell megküldeni.
    -   A „**” jelzéssel ellátott adatokat akkor kell a Jöt. 24. §-a szerinti adatszolgáltatásában megküldeni, ha az adóraktár engedélyese nem küldi a szabadforgalomba bocsátással egyidejűleg az adatokat.

    -   A „b” jelzéssel ellátott adatokról kell a kizárólag bérfőzést végző adóraktárnak adatszolgáltatást teljesítenie. Ha egy pont jelzéssel van megjelölve, valamennyi alszámos bontására is vonatkozik a jelzésbeli tartalom.

        -   I. Általános adatok

            -   1. __Adóraktári telephely engedélyszáma*__

            -   2. __Tárgyidőszak*__

            -   3. __Adóraktári készlettípus*__

        -   II. __Termékkészlet elszámolás (termék megnevezése, jövedéki termék KN-kódja*, jövedéki termék fajtakódja*, termék mennyisége*, [dohánygyártmány esetében kiszerelési egység és kiskereskedelmi eladási ár is]*)__

            -   1. Nyitókészlet* (kizárólag a 2017. június 30-át követő első adatszolgáltatás alkalmával beküldendő)
                <details>    
                   <summary><b>2. Készletnövekedés (bizonylatszám)</b></summary>
                    
                -   2.1. *  Előállított jövedéki termék*
                    -   2.1.1. Bioetanol esetében az alábbi bontásban
                        -   2.1.1.1. EU termelésű alapanyagból fenntarthatósági igazolással rendelkezik
                        -   2.1.1.2. EU termelésű alapanyagból fenntarthatósági igazolással nem rendelkezik
                        -   2.1.1.3. Harmadik országban termelt alapanyagból fenntarthatósági igazolással rendelkezik
                        -   2.1.1.4. Harmadik országban termelt alapanyagból fenntarthatósági igazolással nem rendelkezik

                    -   2.1.2. A Jöt. 3. § (3) bekezdés 22. pontja szerint sörnek minősülő, erjesztést követően előállított még nem késztermék
                -   2.2. Cigarettán kívüli dohánygyártmány Jöt. 77. § (3) bekezdés b) pontja szerinti zárjegy eltávolítás utáni készletre vétele*
                -   2.3. *  Előállított nem jövedéki termék és az adófizetési kötelezettség alól mentesült jövedéki termék
                    -   2.3.1. Jöt. 133. § (1) bekezdés e) pontja szerinti gyógyszer, gyógyhatású készítmény, gyógyszeranyag, intermedier*
                    -   2.3.2. Jöt. 133. § (1) bekezdés f) pontja szerinti ecet*
                    -   2.3.3. Jöt. 133. § (1) bekezdés g) pontja szerinti aroma*
                    -   2.3.4. Jöt. 133. § (1) bekezdés h) pontja szerinti csokoládé és egyéb élelmiszer*
                    -   2.3.5. Jöt. 133. § (1) bekezdés i) pontja szerinti vegyipari, kozmetikai és egyéb, nem emberi fogyasztásra szolgáló termék*
                    -   2.3.6. Jöt. 133. § (1) bekezdés k) pontja szerinti teljesen denaturált alkohol*
                    -   2.3.7. Előállított ETBE*
                    -   2.3.8. Jöt. 112. § (1) bekezdés cb) pontja szerinti termék*
                    -   2.3.9. Jövedéki termék előállításához alapanyagként szolgáló nem jövedéki termék
                -   2.4. Adófizetési kötelezettség alóli mentesülés kapcsán keletkezett, jövedéki terméknek minősülő melléktermék, hulladék
                -   2.5. Adófelfüggesztési eljárás keretében átvett jövedéki termék
                    -   2.5.1. saját adóraktárból
                    -   2.5.2. __nem saját adóraktárból__
                    -   2.5.3. __tagállamból__
                    -   2.5.4. __bejegyzett feladótól__
                    -   2.5.5. adófelfüggesztési eljárás keretében történő szállításból visszaszállított
                -   2.6. __*  Adófelfüggesztési eljárás keretében átvett csendes és habzóbor*__
                    -   2.6.1. Egyszerűsített adóraktártól
                    -   2.6.2. Kisüzemi bortermelőtől
                    -   2.6.3. Másik tagállamból a Jöt. 51. §-a szerint
                -   2.7. Adóraktárban importált jövedéki termék
                -   2.8. Légijárműből lefejtett, adóraktárba szállított repülőgép-üzemanyag*
                -   2.9. Terméktávvezeték adóraktártól vagy adóraktárnak nem minősülő csővezetékes szállításból átvett energiatermék*
                -   2.10. A Jöt. 12. § h) pontja szerinti jövedéki termék visszavétele*
                -   2.11. Bérfőzetőtől a párlat kiadása nélkül, adózatlanul megvásárolt mennyiség*
                -   2.12. __Beszerzett nem jövedéki termék__
                -   2.13. Mintaként vett, de fel nem használt termék*
                -   2.14. <span style="color:red">Készletfelvétel során megállapított készlet többlet</span>
                    -   2.14.1. az állami adó- és vámhatóság jelenlétében
                    -   2.14.2. nem az állami adó- és vámhatóság jelenlétében*
                -   2.15. Termékkészlet átvezetése biztosítékköteles készletből a Jöt. 21. § (4) bekezdés a) és b) pontja szerinti termékkészletbe (növekedés)*
                -   2.16. Termékkészlet átvezetése a Jöt. 21. § (4) bekezdés a) és b) pontja szerinti termékkészletből biztosítékköteles készletbe (növekedés)*
                -   2.17. __*  Magánfőzőtől átvett párlat*__
                -   2.18. Bérfőzetőtől átvett adózott párlat*
                -   2.19. *  Szabadforgalomból átvett*
                    -   2.19.1. az adóraktár engedélyese által belföldön szabadforgalomba bocsátott jövedéki termék
                    -   2.19.2. egyéb jövedéki termék
                -   2.20. Dohánygyártmány kiskereskedelmi eladási ár változása miatti készletátvezetése (növekedés)*
                -   2.21. <span style="color:red">Szabadforgalomba bocsátott jövedéki termék kiszállítást követő 72 órán belül részben vagy teljes mennyiségben történő visszaszállítása*</span>
                -   2.22. Adózott termék átvétele saját adóraktárból*
                -   2.23. Jövedéki termék átvezetése KN-kód vagy fajtkód változása esetén (növekedés)*
                -   2.24. *  A Jöt. 9. § (1) bekezdés a) pontja szerint értékesített jövedéki termék kiszállítást követő 72 órán belül részben vagy teljes mennyiségben történő visszaszállítása
                -   2.25. *  Adóraktárban végzett felhasználói engedélyes tevékenységből átvett termék a Jöt. 24. § (11) bekezdése szerint*
                -   2.26. *  A Jöt. 9. § (1) bekezdés n) és o) pontja és a DCA megállapodás XVI. cikke szerint kiszolgált jövedéki termék visszaszállítása*
                -   2.27. *  A Jöt. 62. § (13) bekezdése szerinti termék átvétele adófelfüggesztés alatt álló készletbe tagállamból*
                -   2.28. *  A Jöt. 62. § (13) bekezdése szerinti termék átvétele saját adóraktárból*
                -   2.29. *  Másik tagállamban szabadforgalomba bocsátott jövedéki termék átvétele
            </details>
            
            <details>
            <summary><b>3. Készletcsökkenés (bizonylat száma)</b></summary>

            - 3.1. __* Jövedéki termék előállításához felhasznált jövedéki termék*__
                - 3.1.1. __A Jöt. 3. § (3) bekezdés 22. pontja szerint sörnek minősülő, erjesztést követően előállított még nem késztermék__
            - 3.2. __Jövedéki termék vagy nem jövedéki termék előállításához alapanyagként felhasznált nem jövedéki termék__
            - 3.3. ETBE előállításához felhasznált jövedéki termék*
            - 3.4. A Jöt. 9. § (1) bekezdés a) pontja szerint értékesített jövedéki termék*
            - 3.5. A Jöt. 9. § (1) bekezdés b) pontja szerint átadott jövedéki termék*
            - 3.6. A Jöt. 9. § (1) bekezdés c) pont ca) alpontja szerinti célra a mintavételi szabályzat szerint vett minta (helye, időpontja, célja)
                - 3.6.1. az állami adó- és vámhatóság jelenlétében
                - 3.6.2. nem az állami adó- és vámhatóság jelenlétében*
            - 3.7. <span style="color:red">A Jöt. 9. § (1) bekezdés c) pont cb) alpontja szerint megsemmisítés</span>
                - 3.7.1. az állami adó- és vámhatóság jelenlétében
                    - 3.7.1.1. adóraktárból elszállítás révén
                    - 3.7.1.2. adóraktárban
                - 3.7.2. nem az állami adó- és vámhatóság jelenlétében*
                    - 3.7.2.1. adóraktárból elszállítás révén
                    - 3.7.2.2. adóraktárban
            - 3.8. Cigarettán kívüli dohánygyártmányok Jöt. 77. § (3) bekezdés b) pontja szerinti zárjegy eltávolítást követő kivezetése az adózott készletből*
            - 3.9. * A Jöt. 9. § (1) bekezdés e) és f) pontja szerint jövedéki termék olyan károsodása, amelyet az állami adó- és vámhatóság teljes megsemmisülésként vagy helyrehozhatatlan károsodásként elismert (időpont, mód/körülmények, kárenyhítés érdekében tett intézkedés), a Jöt. 9. § (4) bekezdés b) pontja szerint elismert mennyiségű hiány kivételével
            - 3.10. A Jöt. 112. § (1) bekezdés a) pontja szerint jövedéki termék kiszolgálása*
            - 3.11. A Jöt. 112. § (1) bekezdés b) pontja szerint jövedéki termék kiszolgálása*
            - 3.12. A Jöt. 112. § (1) bekezdés c) pont ca) alpontja szerint felhasznált jövedéki termék*
            - 3.13. A Jöt. 112. § (1) bekezdés c) pont cb) alpontja szerint felhasznált jövedéki termék*
            - 3.14. A Jöt. 112. § (1) bekezdés c) pont cc) alpontja szerint felhasznált jövedéki termék*
            - 3.15. A Jöt. 133. § (1) bekezdés e) pontja szerint felhasznált jövedéki termék gyógyszer, gyógyhatású készítmény, gyógyszeranyag, intermedier előállításához*
            - 3.16. A Jöt. 133. § (1) bekezdés f) pontja szerinti felhasznált jövedéki termék ecet előállításához*
            - 3.17. A Jöt. 133. § (1) bekezdés g) pontja szerint felhasznált jövedéki termék aroma előállításához*
            - 3.18. A Jöt. 133. § (1) bekezdés h) pontja szerint felhasznált jövedéki termék csokoládé és egyéb élelmiszer előállításhoz*
            - 3.19. A Jöt. 133. § (1) bekezdés i) pontja szerint felhasznált jövedéki termék vegyipari, kozmetikai és egyéb, nem emberi fogyasztásra szolgáló termék előállításához*
            - 3.20. A Jöt. 133. § (1) bekezdés k) és m) pontja szerint felhasznált jövedéki termék teljesen denaturált alkohol előállításához*
            - 3.21. Terméktávvezeték adóraktárnak vagy adóraktárnak nem minősülő csővezetékes szállításnál adófelfüggesztési eljárás keretében átadott energiatermék*
            - 3.22. __Szabadforgalomba bocsátott jövedéki termék**__
                - 3.22.1. magánszemély részére
                - 3.22.2. jövedéki engedélyes kereskedő részére (az átvevő neve, címe, engedélyszáma, adószáma, bizonylat száma)
                - 3.22.3. jövedéki kiskereskedő részére (az átvevő neve, címe, adószáma, bizonylat száma)
                - 3.22.4. * más tagállamba
                - 3.22.5. felhasználói engedélyes részére (az átvevő neve, címe, adószáma, engedélyszáma, bizonylat száma)
                - 3.22.6. nyilvántartásba vett felhasználó részére (az átvevő neve, címe, adószáma, bizonylat száma)
                - 3.22.7. dohány-kiskereskedelmi ellátó részére (az átvevő neve, címe, adószáma, engedélyszáma, bizonylat száma)
                - 3.22.8. * 5 liternél vagy 5 kilogrammnál nagyobb kiszerelésű egyéb ellenőrzött ásványolaj Jöt. 7. § (1) bekezdés f) pontja szerinti értékesítése vagy szállítása (az átvevő neve, címe, adószáma, bizonylat száma)
                - 3.22.9. kisüzemi bortermelő részére (az átvevő neve, címe, adószáma, bizonylat száma)
                - 3.22.10. légiutas-ellátási tevékenységre (az átvevő neve, címe, adószáma, bizonylat száma)
                - 3.22.11. 5 liter vagy 5 kilogramm vagy annál kisebb kiszerelésű egyéb ellenőrzött ásványolaj kiszállítása (bizonylat száma, engedélyes esetén az engedélyszám, magánszemélyt kivéve az átvevő neve, címe, adószáma)
                - 3.22.12. egyéb személy részére (az átvevő neve, címe, adószáma, bizonylat száma)
                - 3.22.13. * Tagállamba, harmadik országba történő kiszállítás céljából, zárjegy nélkül a Jöt. 62. § (13) bekezdése szerinti termék
            - 3.23. <span style="color:red">Szabadforgalomba bocsátott, az adóraktárban adófizetési kötelezettséget eredményező módon elfogyasztott, felhasznált jövedéki termék*</span>
            - 3.24. __Adófelfüggesztési eljárás keretében feladott jövedéki termék__
                - 3.24.1. saját adóraktárba
                - 3.24.2. nem saját adóraktárba
                - 3.24.3. tagállamba
                - 3.24.4. harmadik országba
                - 3.24.5. másik tagállamba diplomáciai és konzuli képviselet és annak tagjai részére
                - 3.24.6. másik tagállamba nemzetközi szervezet és annak tagjai részére
                - 3.24.7. másik tagállamba Észak-atlanti Szerződésben részes állam fegyveres erői, polgári állománya és étterme, kantinja részére
                - 3.24.8. * másik tagállamba a tagállam közös biztonság- és védelempolitika keretében folytatott uniós tevékenység végrehajtása céljából végzett védelmi feladat ellátásában részt vevő fegyveres erői, polgári állománya és étterme, kantinja részére
            - 3.25. Termékkészlet-átvezetés biztosítékköteles készletből a Jöt. 21. § (4) bekezdés a) és b) pontja szerinti termékkészletbe (csökkenés)*
            - 3.26. Termékkészlet átvezetés a Jöt. 21. § (4) bekezdés a) és b) pontja szerinti termékkészletből biztosítékköteles készletbe (csökkenés)*
            - 3.27. <span style="color:red">Készletfelvétel során megállapított készlethiány
                - 3.27.1. az állami adó- és vámhatóság jelenlétében
                    - 3.27.1.1. adóköteles hiány
                    - 3.27.1.2. nem adóköteles hiány
                - 3.27.2. nem az állami adó- és vámhatóság jelenlétében*
                    - 3.27.2.1. adóköteles hiány
                    - 3.27.2.2. nem adóköteles hiány<span>
            - 3.28. Adófizetési kötelezettség alóli mentesülés kapcsán keletkezett, jövedéki terméknek minősülő melléktermék, hulladék
                - 3.28.1. felhasználása termék előállításhoz
                - 3.28.2. megsemmisítése
                - 3.28.3. feladása, átadása
            - 3.29. Dohánygyártmány kiskereskedelmi eladási ár változása miatti készletátvezetése (csökkenés)*
            - 3.30. Adózott termék átadása saját adóraktár részére*
            - 3.31. @Jövedéki termék átvezetése KN-kód vagy fajtakód változása esetén (csökkenés)*</span>
            - 3.32. * A Jöt. 9. § (1) bekezdés n) és o) pontja és a DCA megállapodás XVI. cikke szerint jövedéki termék kiszolgálása**
            - 3.33. * Adóraktárban végzett felhasználói engedélyes tevékenységhez kiadott termék a Jöt. 24. § (11) bekezdése szerint*
            - 3.34. *
            - 3.35. * A Jöt. 62. § (13) bekezdése szerinti termék feladása saját adóraktár részére*
            - 3.36. * Adóraktárban a Jöt. 3. § (3) bekezdés 1. pontja szerinti alkoholmentesítéssel előállított csendes bor feladása egyszerűsített adóraktár vagy kisüzemi bortermelő részére*
            - 3.37. * A Jöt. 67. § (1b) bekezdése szerinti jövedéki termék továbbforgalmazása
                - 3.37.1. tagállamba
                - 3.37.2. harmadik országba*
                - 3.37.3. belföldre**
            - 3.38. * Csővezetékes szállítás keretében az adóraktárban feladott jövedéki termék harmadik országba*
            </details>
            


 ### Original UK module description
 ### Introduction

This app has been developed to help users of Odoo who work with alcoholic beverages track their excise liability.

The UK legislation is laid down in [HMRC notice 226](https://www.gov.uk/government/publications/excise-notice-226-beer-duty/excise-notice-226-beer-duty--2). Other EU countries work under similar rules.

This software is Free and Open source.
### Installation

You must have the Inventory (stock) module installed before you install the Excise module. Clone the repository into the custom add-ons folder defined in your Odoo configuration file. After updating your Apps list the Excise-Alcohol app will become available for installation.

  

### Setup

Under Inventory – Configuration – Excise (Excise Categories) you can set up the categories of alcoholic beverages you work with. The installation process will populate this list with the UK categories defined [here](https://www.gov.uk/government/publications/rates-and-allowance-excise-duty-alcohol-duty/alcohol-duty-rates-from-24-march-2014).

  

![](https://kodoo.co.uk/web/image/1265/1.png)  

  

If you operate a bonded warehouse you can enter your warehouse number on the Warehouse screen.

The presence of a warehouse number tells the system that the location stores product duty-unpaid.

![](https://kodoo.co.uk/web/image/1266/2.png)  

  

If you have a duty paid area within your warehouse (e.g. a returns area) you should set this up as a location. (enable the setting Storage Locations). Check the “Duty Paid Location” setting to indicate that this location stores Duty paid stock within an otherwise duty free warehouse.

![](https://kodoo.co.uk/web/image/1267/3.png)  

  

The system will calculate duty when moving stock from a duty-unpaid location to a duty-paid location. The system will prohibit moving excisable stock from a duty paid location to a duty unpaid location.

  

### Product Setup

![](https://kodoo.co.uk/web/image/1268/4.png)  
  

On the Excise tab of the Product card select Track Excise if Excise should be calculated. Enter the ABV and select the relevant Category. Enter the volume of product for excise purposes in Litres.

If you use attributes to specify packaging you can specify the Excisable volume of the product at variant level.

### Reporting

Under the reporting menu look at the Excise moves.

![](https://kodoo.co.uk/web/image/1269/5.png)  

An Excise move is created per movement per excise category. If the category has an additional category (High-streingth beer) then two excise move records will be created.

You can view these Excise moves either grouped or in a pivot. Use standard Odoo filtering to assist the completion of returns.
