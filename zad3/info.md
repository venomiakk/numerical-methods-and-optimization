**wielomian interpolowany** - zbiór punktów użytych do interpolacji (wejście)  
**wielomian interpolacyjny** - funkcja przybliżająca (wyjście)

#### Wariant 1: Lagrange'a dla węzłów równoodległych

Program ma umożliwiać wczytanie stablicowanych wartości funkcji oraz umożliwiać wybór jednej z kilku funkcji:
- liniowa
- |x|
- wielomian
- trygonometryczna 
- i ich złożenia. 

Wartości wielomianów ***interpolowanych*** należy obliczać używając schematu Hornera.  

Wartości wielomianów ***interpolacyjnych*** należy obliczać bezpośrednio, skorzystanie ze schematu Hornera nie jest bowiem możliwe bez uprzedniego przekształcenia wielomianu interpolacyjnego do postaci kanonicznej.

###### Użytkownik wybiera:
- funkcję
- przedział interpolacji 
- liczbę węzłów interpolacyjnych.  

Dla równoodległych odstępów argumentu oraz węzłów Czebyszewa położenie węzłów wyliczane jest z odpowiednich wzorów,  
~~*dla nierównych odstępów argumentu trzeba zapewnić możliwość wczytania położenia węzłów w sposób przyjazny dla użytkownika (plik albo odpowiednia kontrolka GUI).*~~  

Wartości w węzłach ***interpolacyjnych*** wyliczane są przy użyciu funkcji wybranej przez użytkownika.  

Program ma rysować wykres funkcji oryginalnej i wielomianu *interpolującego* oraz zaznaczać węzły interpolacji (węzły interpolacji powinny pokrywać się z punktami przecięcia wykresów funkcji i wielomianu interpolacyjnego - jeśli jest inaczej, to jest to wyraźna oznaka błędu w programie).

W sprawozdaniu należy zamieścić przykładowe wykresy. Zbadać w jaki sposób zmiana liczby węzłów wpływa na dokładność interpolacji. Ile węzłów potrzeba do interpolacji wielomianu N-tego stopnia?