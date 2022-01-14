#Markdown

Repozytorium z kodem na GitHub'ie: https://github.com/sm-xh/4inrow_js

<h3>Treść projektu:</h3>
<ul>
    <li>Okno wyświetlające siatkę 7 kolumn x 6 wierszy, przycisk nad każdą kolumną,
    informację "Tura gracza 1” lub "Tura gracza 2”, przycisk do resetowania gry
    oraz rozwijalną listę wyboru reguł gry.</li>
    <li> Początkowo pola siatki są puste.</li>
    <li>Gracze na zmianę wrzucają monety do wybranych przez siebie kolumn.</li>
    <li>Pola w których jest moneta gracza 1 są czerwone, pola z monetami gracza 2
    są żółte (tkinter, Canvas, http://stackoverflow.com/a/12254442).</li>
    <li>Gracze wybierają kolumnę klikając przycisk nad nią.</li>
    <li>Wygrywa gracz który pierwszy ustawi cztery monety w linii (poziomo, pionowo
    lub po skosie).</li>
    <li>Gdy gra się kończy, wyświetlane jest okienko z napisem "Wygrał gracz 1” lub
    <li>"Wygrał gracz 2”, zależnie kto wygrał grę. Możliwe jest zresetowanie planszy
    bez zamykania głównego okna.</li>
    <li>Reprezentacja reguł gry ma być realizowana poprzez hierarchię klas. Klasa
    bazowa definiuje między innymi funkcję wirtualną ktoWygral() nadpisywaną w
    klasach pochodnych. Realizowane powinny być przynajmniej dwa zestawy reguł,
    jako dwie klasy pochodne.</li>
</ul>

<h3>Testy:</h3>
<ol>
    <li>Wykonanie po dwa ruchy przez każdego z graczy - monety spadają na dół pola
gry lub zatrzymują się na już wrzuconym żetonie.
    <li>Ułożenie pionowej linii monet przez jednego gracza - oczekiwana informacja o
jego wygranej.
    <li>Ułożenie poziomej linii monet przez drugiego gracza - oczekiwana informacja o
jego wygranej.
    <li>Ułożenie skośnej linii przez dowolnego gracza - oczekiwana informacja o
jego wygranej.
    <li>Zapełnienie pola gry tak, że żaden gracz nie ułożył linii - oczekiwana informacja
o remisie.
    <li>Ułożenie linii dłuższej niż 4 przez jednego z graczy - oczekiwana informacja o
jego wygranej. <br>
[c][c][c][ ][c][c][c]<br>
[ż][ż][ż][ ][ż][ż][ż] <- w następnym ruchu gracz żółty wrzuci monetę w
środkową kolumnę.
    <li>Próba wrzucenia monety do zapełnionej kolumny - oczekiwana informacja o błędzie.
</ol>