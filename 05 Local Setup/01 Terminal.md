# Commandline (Terminal)


## Navigation
Mit dem Terminal installieren wir neue Programme, wir halten alte aktuell, und wir können damit unsere Eigen-Kreationen, unsere eigene Programme, auslösen. Das Terminal können wir auch dazu nutzen, sehr komplexe Aufgaben zu lösen. 

Deshalb wollen wir uns dieses Werkzeug näher anschauen. Lernen wir die Basis-Befehle kennen. [Hier findet ihr ein wunderbares Cheatsheet dafür](https://www.git-tower.com/blog/command-line-cheat-sheet/).

Windows hat eine ähnliche Applikation. Hier nennt es sich Command Prompt. Ein Cheet Sheet, die Befehle sind leicht anders, findest Du [hier](https://serverspace.io/support/help/windows-cmd-commands-cheat-sheet/). 

Versucht nun das Folgende:

1. Öffene das Terminal (oder den Command Prompt)
2. Navigiere auf den Desktop.
3. Kreiere einen Ordner.
4. Navigiere in den Ordner.

Extra:
1. Mac- und Linux-Nutzer: versucht mit ```brew install wget``` Wget zu installieren. Wer mehr über Wget wissen will, kann 
2. Lade mit der Zeile ```wget https://data.snf.ch/exportcsv/Grant.csv``` die SNF-Daten herunter.


## Say
Der Terminal ist natürlich nicht nur dazu da, Dokumente herumzuschieben, oder neue zu erschaffen. Lassen wir den Computer damit reden. (Auch dafür gibt es [Alternativen für PC](https://superuser.com/questions/223913/os-x-say-command-for-windows))

```say hello```
```say hallo, ich bins```
```man say ```
Damit rufen wir das ganze Manual auf. Schauen wir uns an, was wir alles damit machen könnne. Mit ```q``` verlassen wir den Modus wieder.

```say -v ?``` oder ```say voice ?``` damit können wir alle gespeicherte Sprachen abrufen.

Mit dem Befehl say -f "namedesfiles" können wir uns ganze Dokumente vorlesen lassen.

Wir können den Computer sagen, dass er gewisse Tätigkeiten zu genau bestimmten Zeiten ausführt. Mit derselben Funktionialität funktionieren Dutzende Dienste, und Apps. E-Mail-Dienste zum Beispiele. Sie sind je nach Einstellung einfach alle 15 Minuten oder jede Minute so eingestellt.


## Crontabs
Damit wir dem Computer entsprechend einstellen können, müssen wir zuerst den entsprechenden Editor auswählen. Auch das können wir mit dem Terminal erledigen. Das ist das Eingabesystem für unser Gerät. Der gängigste Editor für Unix-Geräte (Apple und Linux) ist der VIM Editor. Dieser ist allerdings ziemlich kompliziert. Wir arbeiten besser mit dem Nano Editor.

Dafür gebt ihr ein: export EDITOR=nano

Nun öffnen wir den Crontab: ```crontab -e```

Und wir geben die fünf * Zeichen ein, und dann ```say "hello you"```

Der Computer wird nun jede Minute "hello you" sagen.

Das lässt sich natürlich verfeinern. Wie, erschliesst sich auf der Site Crontab.guru.

## wc
Gehen wir zurück auf die Commandline. Und schauen wir an, wie wir damit riesige Datensätze befragen und behandelnd können.

Alle, die vorhin die Daten nicht herunter geladen haben. Ihr könnt das natürlich auch händisch tun. Ladet die Daten in den Folder herunter, den ihr vorhin auf dem Desktop kreiert habt. Die Daten sind [hier:](https://data.snf.ch/exportcsv/Grant.csv).

Zählen wir, wie viele Wörter das File hat: ```wc Grant.csv.```

Das Ergebnis zählt eigentlich nicht nur die Wörter, sondern die Linien, die Wörter und die Zeichen.

Zeigen wir nur die Zeilen an: wc -l P3P3_GrantExport.csv. Das gleich können wir nun auch für die Wörter: ```wc -w Grant.csv ```oder die Zeichen ```wc -m Grant.csv``` tun. Wer mehr für wcwissen will, googelt wc unix. So viel mehr kann wc aber nicht wirklich, aber es ist sehr nützlich, um sich über eine grössere Datensammlunge eine Übersicht zu verschaffen.

## grep und Piping
```grep``` steht für "Globally search a Regular Expression and Print". Also: Ein bestimmtes Textmuster suchen und das Resultat dann ausdrucken. Macht das Sinn?

Versuchen wir es.

Geben wir folgendes ein ```grep "Geschichte" Grant.csv```
Wir bekommen ein Fenster voller Text in der Commandline. Diesen ganze Inhalt können wir abspeicher, folgendermassen ```grep "Geschichte" Grant.csv > geschichte.csv```
Auf eurem Desktop sollte nun ein File mit dem Namen "geschichte.csv" erscheinen. Versucht das nun mit Excel oder Google Spreadsheets zu öffnen. Das macht schon sehr viel mehr Sinn.
Wir können Befehle auch kombinieren. Also wc und grep. Mit dem Piping-Zeichen. Auf dem Mac findet ihr das Zeichen mit "alt" und 7.
Dann geben wir ein ```grep "Geschichte" Grant.csv | wc -l```

Wer mehr wissen will, dem kann ich dieses Buch empfehlen: [Datascience from the Command Line](https://datascienceatthecommandline.com/) ![Datascience from the Command Line](https://datascienceatthecommandline.com/img/poster.1600w.webp)