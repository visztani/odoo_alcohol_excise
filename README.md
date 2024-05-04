# Alcohol Excise tracking for Odoo
 
## Hungarian extension / modification for Tax Warehouses receiving, sending, storing excise products (storing only, no manufacturing) under duty suspension

### Követelmények
    
[2016. évi LXViii. Törvény a jövedéki adóról](https://net.jogtar.hu/jogszabaly?docid=a1600068.tv)

[45/2016. (XI. 29.) NGM rendelet a jövedéki adóról szóló 2016. évi LXVIII. törvény egyes rendelkezéseinek végrehajtásáról](https://net.jogtar.hu/jogszabaly?docid=a1600045.ngm)

- list1
    - list2
      <details>
      <summary><b>list3</b></summary>
        
        - list4
        - list5
        - list6
      </details>

__Jöt. 20.§(1) a) (elektronikus nyilvántartási kötelezettség)__

- __Vh. rendelet szerinti adattartalom:__


   - Adóraktári nyilvántartás és az adóraktár Jöt. 24. § szerinti adatszolgáltatásának adattartalma

    -   A „*” jelzéssel ellátott adatokat a Jöt. 24. §-a szerinti adatszolgáltatásában kell megküldeni.
    -   A „**” jelzéssel ellátott adatokat akkor kell a Jöt. 24. §-a szerinti adatszolgáltatásában megküldeni, ha az adóraktár engedélyese nem küldi a szabadforgalomba bocsátással egyidejűleg az adatokat.

    -   A „b” jelzéssel ellátott adatokról kell a kizárólag bérfőzést végző adóraktárnak adatszolgáltatást teljesítenie. Ha egy pont jelzéssel van megjelölve, valamennyi alszámos bontására is vonatkozik a jelzésbeli tartalom.

        -   I. Általános adatok

            -   1. Adóraktári telephely engedélyszáma*

            -   2. Tárgyidőszak*

            -   3. Adóraktári készlettípus*

        -   II. Termékkészlet elszámolás (termék megnevezése, jövedéki termék KN-kódja*, jövedéki termék fajtakódja*, termék mennyisége*, [dohánygyártmány esetében kiszerelési egység és kiskereskedelmi eladási ár is]*)

            -   1. Nyitókészlet* (kizárólag a 2017. június 30-át követő első adatszolgáltatás alkalmával beküldendő)
                <details>    
                    <summary><b>2. __Készletnövekedés (bizonylatszám)__ </b></summary>
                    
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
                    -   2.5.2. nem saját adóraktárból
                    -   2.5.3. tagállamból
                    -   2.5.4. bejegyzett feladótól
                    -   2.5.5. adófelfüggesztési eljárás keretében történő szállításból visszaszállított
                -   2.6. *  Adófelfüggesztési eljárás keretében átvett csendes és habzóbor*
                    -   2.6.1. Egyszerűsített adóraktártól
                    -   2.6.2. Kisüzemi bortermelőtől
                    -   2.6.3. Másik tagállamból a Jöt. 51. §-a szerint
                -   2.7. Adóraktárban importált jövedéki termék
                -   2.8. Légijárműből lefejtett, adóraktárba szállított repülőgép-üzemanyag*
                -   2.9. Terméktávvezeték adóraktártól vagy adóraktárnak nem minősülő csővezetékes szállításból átvett energiatermék*
                -   2.10. A Jöt. 12. § h) pontja szerinti jövedéki termék visszavétele*
                -   2.11. Bérfőzetőtől a párlat kiadása nélkül, adózatlanul megvásárolt mennyiség*
                -   2.12. Beszerzett nem jövedéki termék
                -   2.13. Mintaként vett, de fel nem használt termék*
                -   2.14. Készletfelvétel során megállapított készlet többlet
                    -   2.14.1. az állami adó- és vámhatóság jelenlétében
                    -   2.14.2. nem az állami adó- és vámhatóság jelenlétében*
                -   2.15. Termékkészlet átvezetése biztosítékköteles készletből a Jöt. 21. § (4) bekezdés a) és b) pontja szerinti termékkészletbe (növekedés)*
                -   2.16. Termékkészlet átvezetése a Jöt. 21. § (4) bekezdés a) és b) pontja szerinti termékkészletből biztosítékköteles készletbe (növekedés)*
                -   2.17. *  Magánfőzőtől átvett párlat*
                -   2.18. Bérfőzetőtől átvett adózott párlat*
                -   2.19. *  Szabadforgalomból átvett*
                    -   2.19.1. az adóraktár engedélyese által belföldön szabadforgalomba bocsátott jövedéki termék
                    -   2.19.2. egyéb jövedéki termék
                -   2.20. Dohánygyártmány kiskereskedelmi eladási ár változása miatti készletátvezetése (növekedés)*
                -   2.21. Szabadforgalomba bocsátott jövedéki termék kiszállítást követő 72 órán belül részben vagy teljes mennyiségben történő visszaszállítása*
                -   2.22. Adózott termék átvétele saját adóraktárból*
                -   2.23. Jövedéki termék átvezetése KN-kód vagy fajtkód változása esetén (növekedés)*
                -   2.24. *  A Jöt. 9. § (1) bekezdés a) pontja szerint értékesített jövedéki termék kiszállítást követő 72 órán belül részben vagy teljes mennyiségben történő visszaszállítása
                -   2.25. *  Adóraktárban végzett felhasználói engedélyes tevékenységből átvett termék a Jöt. 24. § (11) bekezdése szerint*
                -   2.26. *  A Jöt. 9. § (1) bekezdés n) és o) pontja és a DCA megállapodás XVI. cikke szerint kiszolgált jövedéki termék visszaszállítása*
                -   2.27. *  A Jöt. 62. § (13) bekezdése szerinti termék átvétele adófelfüggesztés alatt álló készletbe tagállamból*
                -   2.28. *  A Jöt. 62. § (13) bekezdése szerinti termék átvétele saját adóraktárból*
                -   2.29. *  Másik tagállamban szabadforgalomba bocsátott jövedéki termék átvétele
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
