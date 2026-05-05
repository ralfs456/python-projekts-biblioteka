
1. Kāpēc es izvēlējos "math" bibliotēku?

Es izvēlējos math bibliotēku, jo:
- Tā ir iebūvēta Python, tāpēc nekas papildus nav jāinstalē.
- Tā ir ļoti praktiska – skolā matemātikas un fizikas stundās bieži vajag rēķināt kvadrātsaknes, noapaļot skaitļus vai strādāt ar leņķiem, un šī bibliotēka to visu izdara ātri un precīzi.
- To ir viegli saprast un sākt lietot pat iesācējam.


2. Projekta failu struktūra un 15 funkcijas.

math.sqrt(x) (sqrt_piemers.py) – Aprēķina skaitļa x kvadrātsakni. Izmanto ģeometrijā un Pitagora teorēmā.

math.pow(x, y) (pow_piemers.py) – Aprēķina x kāpinājumu pakāpē y. 

math.floor(x) (floor_piemers.py) – Noapaļo decimālskaitli uz leju līdz tuvākajam veselam skaitlim. (Piemērs: 7.6 uz 7).

math.ceil(x) (ceil_piemers.py) – Noapaļo decimālskaitli uz augšu līdz tuvākajam veselam skaitlim. (Piemērs: 7.4 uz 8).

math.pi (pi_piemers.py) – Matemātiskā konstante PI (PI ~ 3.14159). Izmanto apļa laukuma un apkārtmēra aprēķinos.

math.factorial(n) (factorial_piemers.py) – Aprēķina skaitļa n faktoriālu (n! = n * (n-1) * ... * 1).

math.log(x, baze) (log_piemers.py) – Aprēķina logaritmu. Bez bāzes — dabiskais logaritms, ar bāzi 10 — decimāllogaritms.

math.sin() / cos() / tan() (trig_piemers.py) – Trigonometriskās funkcijas. Lieto leņķus radiānos, izmanto fizikā un ģeometrijā.

math.radians() / degrees() (conversion_piemers.py) – Pārvērš grādus radiānos vai otrādi. Nepieciešams trigonometrijā.

math.gcd(a, b) (gcd_piemers.py) – Aprēķina divu skaitļu lielāko kopīgo dalītāju. (Piemērs: gcd(48, 18) = 6).

math.fabs(x) (fabs_piemers.py) – Atgriež skaitļa absolūto vērtību (moduli) kā decimālskaitli (vienmēr pozitīvs rezultāts).

math.exp(x) (exp_piemers.py) – Aprēķina e pakāpē x (e ~ 2.718). Izmanto eksponenciālā augšanā.

math.hypot(a, b) (hypot_piemers.py) – Aprēķina taisnleņķa trijstūra hipotenūzu.

math.isfinite() / isinf() (check_piemers.py) – Pārbauda, vai skaitlis ir normāls (beidzīgs) vai bezgalīgs.

math.comb(n, k) (comb_piemers.py) – Aprēķina kombināciju skaitu — cik veidos var izvēlēties k elementus no n bez atkārtošanās.


3. Secinājumi.

Ieguvumi (Plusi):
- Ātrums un precizitāte: Aprēķini notiek acumirklī un ar ļoti augstu precizitāti, kas ir svarīgi matemātiskos aprēķinos.
- Vienkārša lietošana: Funkciju nosaukumi ir loģiski un viegli sasaistāmi ar skolas programmā apgūto (piemēram, sin, cos, sqrt, PI).
- Nav jāraksta sarežģītas formulas: Tādas lietas kā faktoriāls, kombinācijas vai lielākais kopīgais dalītājs var izrēķināt ar vienu komandu, nerakstot garus ciklus.

Ierobežojumi (Mīnusi):
- Datu tipu ierobežojumi: Funkcijas strādā tikai ar skaitļiem. Ievadot tekstu vai tukšu vērtību, programma avarēs.
- Kļūdu riski: Rēķinot, piemēram, kvadrātsakni no negatīva skaitļa vai faktoriālu no decimālskaitļa, programma izmetīs ValueError, tāpēc pirms tam kodā vienmēr ir jāveic lietotāja ievadīto datu pārbaude.
- Trūkst komplekso skaitļu atbalsta: Šī bibliotēka ir paredzēta tikai reāliem skaitļiem (kompleksajiem skaitļiem Python ir jāizmanto cita bibliotēka – cmath).
