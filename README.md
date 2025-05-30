# Omniscience - The Book

*Omniscience – The Book* is a vast collection of all possible combinations of the 26 letters of the English (Latin) alphabet and whitespace, capturing every conceivable piece of all written and unwritten information.

Inspired by Jorge Luis Borges' *The Library of Babel*, this project exists as a finite yet incomprehensibly large repository of text. It contains exactly **5.205884145 × 10^1465** pages, each consisting of **1,024** characters.

For perspective, this number far exceeds the estimated number of atoms in the observable universe (**~10^82**). While its scope is immense, the contents of *Omniscience – The Book* are fixed, making it both a monument to possibility and a paradox of predetermined knowledge.

---

Upon entering the main page, you will be greeted with a random page of the book and its number, concealed for your own convenience. You can reveal the number by pressing the "Toggle Page Number Visibility" button.

The "Copy Page Number to Clipboard" button copies the page number into your clipboard should you want to preserve this intimidating set of digits for the future.

And finally, the "Refresh" button opens a new random page for you to discover.

---

The "Page Lookup" page allows you to open any page of the book if you specify its number.

---

The exact number of pages is:


52058841447977422466306650800768460845035711587028762087026510429628906226879952706605296216838944708530773234945243898571006266248265602011320595606800448841498058223281093753832674976222351583079578317902157617483874393623718606010207755509875364350152856622874570887842276822148722690130721257900960053280759282403991093531270649416886091828400210162303209136261237584479515630616561225553325377912149606276738630016106114613889637762442302690116973861931389492090207824016724545175008374807345256152687155360679280068341624724020984843191420519441262978310148659753585986945716701694933164699474237212699813579834369704676343652199542039865939843245841770495420757295137460454643577337872217697494558971300779787433955817739808561058762719962067613112693999283344344036420167078910506278305990623781191707209785670079565710078526854083678562224463322675608524073083594133876649940848643380445690634958730473822643370260143972278370865722097583192912095607032223290597789710013911419388200738602088178157651558771795741127992318527705319005818071900544738909529211499683333574502119686290004976494740072938725706383826816238871139207121039500805757385755926382288711420339352188364869997683234599176440273478485176994201991887593631370881466640798751350734766327180637806848805356327898634411039817891092598261485418211355729368789163496207398426625753569985528619769853985669745329689698047964769779053677446100430681167279460966030896041454759802162941182832641

---

# Some quotes from *The Library of Babel*

> "For every rational line or forthright statement there are leagues of senseless cacophony, verbal nonsense, and incoherency."

> "Within the century experts had determined what the language actually was: a Samoyed-Lithuanian dialect of Guarani, with inflections from classical Arabic."

> "All-the detailed history of the future, the autobiographies of the archangels, the faithful catalog of the Library, thousands and thousands of false catalogs, the proof of the falsity of those false catalogs, a proof of the falsity of the true catalog, the gnostic gospel of Basilides, the commentary upon that gospel, the commentary on the commentary on that gospel, the true story of your death, the translation of every book into every language, the interpolations of every book into all books, the treatise Bede could have written (but did not) on the mythology of the Saxon people, the lost books of Tacitus."

>"Letizia Alvarez de Toledo has observed that the vast Library is pointless; strictly speaking, all that is required is a single volume, of the common size, printed in nine- or ten-point type, that would consist of an infinite number of infinitely thin pages."

---

# How to run

A container image exists in DockerHub for this application. To run it execute the following command:

```shell
$ docker run -p 8000:8000 mshyshovua/omniscience:latest
```

You should be able to access the application at the address: http://localhost:8000

Docker compose file is available too:

```yaml
version: '3.9'
services:
  omniscience:
    image: 'mshyshovua/omniscience:latest'
    ports:
    - '8000:8000'

```

The application can be accessed online at the address: https://omniscience.mshyshov.site