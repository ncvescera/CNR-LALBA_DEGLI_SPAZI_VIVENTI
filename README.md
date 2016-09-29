# CNR-LALBA_DEGLI_SPAZI_VIVENTI
Script che analizza i documenti di testo inseriti e genera una mappa con il luogo dove sono stati realizzati gli sudi
<h2>Files</h2>
<table>
<tr><th>Nome</th><th>Descrizione</th></tr>
<tr><td><b>Countri.py</b></td><td>classe per contenere i dati estratti dal database</td></tr>
<tr><td><b>Point.py</b></td><td>classe per contenere i dati dei punti inseriti nella mappa</td></tr>
<tr><td><b>ckPkg.sh</b></td><td>script bash che installa le librerie mancanti</td></tr>
<tr><td><b>credential.py</b></td><td>file con le credenziali per connettersi al database</td></tr>
<tr><td><b>firstTime.py</b></td><td>file che avvia ckPkg.py quando necessario</td></tr>
<tr><td><b>installGeon.sh</b></td><td>file che installa la libreria Geon se necessario</td></tr>
<tr><td><b>main.py</b></td><td>script principale</td></tr>
</table>

<h2>Run</h2>
Per eseguire lo script digitare il seguente comando<br> 
`main.py nome_della_cartella`<br>

<h3>Argomenti</h3>
Questo script necessita di <b>un argomento</b>: <b>nome della cartella</b>

<h2>Install</h2>
Per installare le librerie basta eseguire lo script la prima volta e verranno controllate le librerie.<br>
In caso non funsionasse modificare il file `firstTime.py` e settare la variabile <b>firstTime</b> a <b>True</b><br>
`firstTime = True`<br>
Se continua a non funzionare installare manualmente le librerie.

<h3>Librerie</h3>
<table>
<tr><td><b>Nome</b></td><td>Descrizione</td><td>Comando installazione</td></tr>
<tr><td><b>PIP</b></td><td>Libreria per installare le altre librerie</td><td>-</td></tr>
<tr><td><b>popler-utils</b></td><td>Libreria per convertire pdf a txt</td><td>sudo apt-get install popler-utils</td></tr>
<tr><td><b>psycopg2</b></td><td>Libreria per connettersi ad un database postgres</td><td>sudo apt-get install python-psycopg2</td></tr>
<tr><td><b>geonames</b></td><td>Libreria per chiamare geonames</td><td>-</td></tr>
<tr><td><b>geopy</b></td><td>Libreria per chimamare geonames</td><td>sudo apt-get install geopy</td></tr>
<tr><td><b>folium</b></td><td>Libreria per creare una mappa</td><td>sudo apt-get install folium</td></tr>
</table>
