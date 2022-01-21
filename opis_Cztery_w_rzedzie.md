<h2>Smach Piotr GL.03</h2>
<h3>Cztery w rzędzie - Projekt z Języków Symbolicznych</h3>
<b>Dokumentacja</b><br>
<b><a href="https://github.com/sm-xh/4inrow_js">Github</a></b>
<hr>
<h2>Omówienie projektu</h2>
<p>Projekt realizuję implementację gry <b>Cztery w rzędzie</b>. Gra składa się z macierzy 6x7. W każdej partii należy dążyć do połączenia czterech krążków w tym samym kolorze. Należy starać się, żeby pionki wpadły na odpowiednie miejsca tak, aby stworzyły nieprzerwany ciąg złożony z czterech krążków. Rząd może być poziomy, pionowy lub ukośny.
</p>
<p>Sterowanie w grze odbywa się za pomoca myszki. </p>

<h3>Omówienie rozwiązania</h3>
<ul>
    <li>Do wrzucania kolejnych żetonów, wykorzystywane są przyciski wyświetlane nad każdą kolumną</li>
    <li>Po zakończeniu gry, ale też w każdym jej momencie możliwe jest rozpoczęcie rozgrywki od początku</li>
    <li>Rozgrywka kończy się w momencie gdy gracz ułożył linię 4 żetonów w pionie/poziomie/na skos, lub w momencie gdy plansza została zapełniona</li>
    <li>Poszczególne sekcje gry zostały rozdzielone pomiędzy dwa moduły, w których znajdują się dwie klasy - jedna realizująca interfejs użytkownika, druga reprezentująca logikę gry</li>
    <li>Gra odbywa się w oknie 800x800 pikseli. Te jak i inne stałe programu zostały zawarte w pliku <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/constans.py">constans.py</a>.</li>
    <li>Każde z menu oraz sama gra działa z taktowaniem 30 klatek na sekundę. Ustawienie to jest sterowane za pomocą zmiennej <b>userInterface.clock</b> </li>
    <li>Po każdym ruchu gracza wykonywana jest funkcja <b>Game.<a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py#L49">isGameOver()</a></b>, która weryfikuje czy gra nie powinna się zakończyć po danym ruchu</li>
</ul>
<hr>
<h2>Moduły oraz ich zawartości</h2>
<h3>Moduł <a href = https://github.com/sm-xh/4inrow_js/blob/master/gameLogic.py><i>gameLogic.py</i></a></h3>
<p>&nbsp;&nbsp;&nbsp;&nbsp;
    Moduł zawiera wszystkie zmienne oraz funkcje związane z logiką gry. Zawiera jedną klasę <a href="https://github.com/sm-xh/4inrow_js/blob/master/gameLogic.py#L5">Game()</a>, która składa się z <a href="https://github.com/sm-xh/4inrow_js/blob/master/gameLogic.py#L7">konstruktora</a> ze zmiennymi gry oraz z metod implementujących reguły gry.
</p>
Metody zawarte w klasie <a href="https://github.com/sm-xh/4inrow_js/blob/master/gameLogic.py#L5">Game()</a>:
<ol>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/master/gameLogic.py#L18">resetBoard()</a> - odpowiada za resetowanie planszy do gry. Powoduje stworzenie nowej istancji klasy <a href="https://github.com/sm-xh/4inrow_js/blob/master/gameLogic.py#L5">Game()</a>.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py#L20">getTurn()</a> - funkcja zwracająca w formie stringu informację o tym, kto aktualnie wykonuje turę.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py#L27">changeTurn()</a> - funkcja zmieniająca wartość zmiennej Game._turn, które przechowuje informację o aktualnej turze</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py#L35">player_move(position)</a> - funkcja realizująca ruch gracza. Przyjmuje zmienną wejściową "position", która zawiera pozycję myszki w momencie kliknięcia w przycisk. Następnie wypełnia Game._board(), zgodnie z zasadami gry.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py#L49">isGameOver()</a> - funkcja, która sprawdza czy gra się już nie zakończyła - czy nie zostały ułożone 4 żetony w pionie/poziomie/na skos lub, czy plansza nie została już zapełniona. Jeśli gra została zakończona, funkcja ustawia zmienną Game.()_game_over na True, Game._winner() na wartość funkcji <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py#L20">getTurn()</a>.  Jeśli żaden z warunków nie został spełniony, funkcja wywołuje funkcję <a href ="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py#L27">changeTurn()</a>.</li>
</ol>

<h3> Moduł <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py">menus.py</a></h3>
<p>
&nbsp;&nbsp;&nbsp;&nbsp;Moduł definuje kolejne menu kotekstowe służące do obsługi gry oraz implementuje w nich logikę gry zawartej w module <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py">gameLogic.py</a>. Zawiera jedną klasę <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L7">userInterface</a>, która  składa się z <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L10">konstruktora</a> z ustawieniami gry tj. rozmiar okna, definicja zegara modułu <b>pygame</b>, czcionki i ich rozmiary.
</p>
Metody zawarte w klasie <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L7">userInterface</a>:
<ol>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L32">startScreen()</a> - funkcja implementująca ekran startowy gry. Podobnie jak reszta menu, okienko jest odświeżane 30 klatek na sekunde (zmienna _clock.tick). Menu daje możliwość:
    <ol>
        <li>Rozpoczęcia gry - wywoływana jest funkcja <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L133">startgame()</a>.</li>
        <li>Zapoznania się z regułami gry - wywoływana jest funkcja <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L86">about()</a>.</a></li>
        <li>Wyjścia z gry</li>
    </ol>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L86">about()</a> - funkcja implementująca menu z informacjami na temat zasad gry. Wyświetla ona zasady zawarte w zmiennej <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L88">instructions_txt</a>. Jedyną akcją do wykonania w menu, jest powrót do menu startowego - wywołanie funkcji <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L32">startScreen()</a>.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L133">playgame()</a> - funkcja implementująca okienko z właściwą grą. Po bezpośrednim wywołaniu funkcji rysowany jest obszar do gry - plansza 6x7. W tym celu została wykorzystana pętla rysująca w róznych odstępach okręgi oraz przyciski do wrzucania monet (<a href="https://www.pygame.org/docs/ref/draw.html">pygame.draw</a>).</li>
Następnie funkcja jest zapętlana do momentu, aż rozgrywka się nie zakończy, lub nie zostanie wcisnięty przycisk RESET (wywołanie funkcji <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L195">playAgain()</a>). W pętli głównej obsługiwane są eventy kliknięcia w przycisk do wrzucanie monet oraz przycisku reset. Aby przejść do kolejnej iteracji pętli, musi zostać obsłużone kliknięcie w przycisk. Powoduje ono wywołanie funkcji <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/gameLogic.py#L35">Game().playermove()</a>, która odpowiada za wykonanie ruchu aktualnego gracza - wrzucenie żetonu, czyli wprowadzenie wartość do macierzy Game()._board oraz wypełnienie pola gry, do którego powinna trafić moenta (jeśli nie jest pełna). Dodatkowo pętla na zmianę wyświetla informację o tym, kto aktualnie wykonuje ruch.
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L200">endOfGame()</a> - funkcja wywoływana zakończeniu rozgrywki (po wrzuceniu żetonu, parametr Game()._game_over jest ustawiony na True). Ekran wyświetla infomację o tym kto wygrał (kolor gracza/informację o remisie) oraz pozwala na podjęcie dwóch akcji, które zostały zdefiniowane w pętli głównej. Tymi zdarzenaimi jest rozpoczęcie gry od nowa lub wyjście.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/menus.py#L195">playAgain()</a> - funkcja resetująca menu gry - tworzona jest nowa instancja klasy <a href="https://github.com/sm-xh/4inrow_js/blob/master/gameLogic.py#L5">Game()</a>.</li>
</ol>
<h3> Moduł <a href="https://github.com/sm-xh/4inrow_js/blob/master/gameExceptions.py">gameExceptions.py</a></h3>
<p>
&nbsp;&nbsp;&nbsp;&nbsp;Moduł implementuje dwa wyjątki obsługiwane w programie.
<ol>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/51713cdaa4f4861445e9c77589a4fef001d68f49/gameExceptions.py#L6">WrongBoardSizeException(Exception)</a> - własna klasa wyjątku zgłaszana w momentu, gdy gracz próbuje wystartować grę ze zmiennymi <a href="https://github.com/sm-xh/4inrow_js/blob/51713cdaa4f4861445e9c77589a4fef001d68f49/constans.py#L3">ROW_COUNT</a>, <a href="https://github.com/sm-xh/4inrow_js/blob/51713cdaa4f4861445e9c77589a4fef001d68f49/constans.py#L4">COLUMN_COUNT</a> innymi niż zgodnymi z założeniami zadania (6x7). Wystąpienie wyjątku powoduje wywołanie okienka popup z komunikatem i wyjście z gry.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/51713cdaa4f4861445e9c77589a4fef001d68f49/gameExceptions.py#L13">ColumnFullException(Exception)</a> - wyjątek, który jest zgłaszany jest obsługiwany, powoduje wywołanie okienka z instrukcją, ale gra nie jest zatrzymywana.</li>
</ol>
<hr>
<h2>Testy jednostkowe</h2>
Testy zostały zdefiniowane w module <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/tests.py">tests.py</a>. Testy są uruchamiane za pomocą pliku <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/tests_run.py">tests_run.py</a> - należy wykonać polecenie "python tests_run.py". Omówienie poszczególnych testów:
<ol>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/tests.py#L4">test_init_move()</a> - Wykonanie po dwa ruchy przez każdego z graczy - monety spadają na dół pola gry lub zatrzymują się na już wrzuconym żetonie.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/tests.py#L18">test_winning_horizontally()</a> - Ułożenie poziomej linii monet przez drugiego gracza - oczekiwana informacja o jego wygranej</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/tests.py#L32">test_winning_vertically()</a> - Ułożenie pionowej linii monet przez jednego gracza - oczekiwana informacja o jego wygranej.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/tests.py#L83">test_winning_cross()</a> - Ułożenie skośnej linii przez dowolnego gracza - oczekiwana informacja o jego wygranej.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/tests.py#L111">test_draw()</a> - Zapełnienie pola gry tak, że żaden gracz nie ułożył linii - oczekiwana informacja o remisie.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/tests.py#L44">test_winning_plus4_in_row()</a> - Ułożenie linii dłuższej niż 4 przez jednego z graczy - oczekiwana informacja o jego wygranej.</li>
    <li><a href="https://github.com/sm-xh/4inrow_js/blob/master/tests.py#L182">test_full_column()</a> - Próba wrzucenia monety do zapełnionej kolumny - oczekiwana informacja o błędzie (realizacja poprzez okienko typu popup).</li>
</ol>
<hr>
<h2>Uwagi praktyczne</h2>
<ol>
    <li>Głównym problemem podczas tworzenia projektu było złe zarządzanie czasem poprzez developera, co uniemożliwiło rozbudowanie projektu w taki sposób, aby spełniał wszystkie założenia. Pracę starano zorganizować się w taki sposób, aby skupić się na najważniejszych aspektach programu.</li>
    <li>Mimo wykorzystania modułu do przechowywania stałych <a href="https://github.com/sm-xh/4inrow_js/blob/6dc8547345641031df0b03fe8999f1d2319ecb9d/constans.py">constans.py</a>, w programie występują tzw. <i>magic numbers</i>, których znaczenie nie jest oczywiste. Problem ten starano załagodzić się wykorzstaniem komentarzy.</li>
    <li>Funkcja sprawdzająca czy gra została zakończona mogłaby zostać zoptymalizowana i sprawdzać tylko komórki, które są w obszarze ostatnio zapełnionej komórki.</li>
</ol>
