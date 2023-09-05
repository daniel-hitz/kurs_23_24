# INSTALL ANACONDA

1. [Anaconda-Package](https://www.anaconda.com/download) herunterladen
2. Anaconda Cloud Account erstellen
3. Anaconda Navigator starten
4. (Im Terminal oder in der QT Console)
	- ```conda -V```
	- ```conda update conda```
	- ```conda create -n CAS-Datenjournalismus python=3.8 anaconda```
	- ```conda activate CAS-Datenjournalismus  ```
	- ```conda deactivate CAS-Datenjournalismus  ```
	- ```conda install "XXX"``` (pandas, openpyxl, matplotlib, requests, beautifulsoup4 (war schon installiert), selenium, geopandas, descartes, pysal)
	- ```conda install nbconvert==5.4.1```
5. "Launch" Jupyter Notebook. Das Terminal starten und Jupyter Notebook öffnet im Browser. Du siehst nun die File-Struktur auf der Ebene, auf der Du Jupyter Notebook installiert hat.
6. Zum "Desktop" Navigieren
7. "New", "Python 3". Und es tut sich ein neues Arbeitsfeld auf, das in der Bedienung identisch ist zu Google Colab.
