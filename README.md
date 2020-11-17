# Currency Converter
#### Benjamin Bulis - 5AHIT
## Aufgabenstellung

Representational State Transfer (REST) ist einen Architektur-Stil für verteilte Systeme, welcher auf eine möglichst einfache Architektur abzielt. RESTful Webservices erlauben den Zugriff auf Daten und verwenden üblicherweise weit verbreitete Web-Standards wie HTTP, URIs und JSON. Ein simples RESTful Webservice ist meist über eine bestimmte URL erreichbar und liefert je nach übergebene GET-Parameter unterschiedliche Daten im JSON-Format zurück.

Sie wurden beauftragt, eine schlanke grafische Oberfläche für einen Währungsumwandler zu schreiben, der es erlaubt, einen Betrag aus einer Ursprungs-Währung in eine oder mehrere Zielwährungen umzuwandeln. Dabei soll es möglich sein, sowohl Live-Kurse (RESTful Webservice) als auch (fest hinterlegte) Offline-Daten zu verwenden. Sie müssen **kein eigenes RESTful Webservice implementieren**! Verwenden Sie ein kostenlos verfügbares Webservice, wie zum Beispiel folgendes Service der Europäischen Zentralbank: https://exchangeratesapi.io/

### GUI
* Die grafische Oberfläche erlaubt die Eingabe eines
  * Betrags
  * einer Ursprungswährung im 3-Zeichen-Format (z.B. "EUR") sowie
  * einer oder mehrerer Zielwährungen (durch Komma getrennt, z.B. "GBP,USD")
* Es gibt drei Buttons:
  * Ein Button zum Umrechnen
  * Ein Button zum Schließen
  * einer zum Zurücksetzen der Eingaben
* In einer Statusleiste (unten) wird angezeigt, ob die letzte Abfrage fehlerfrei funktionierte und ggf. welcher Fehler aufgetreten ist
* In einem großen HTML-Textfeld wird die Ausgabe des Converter-Services angezeigt
* Über eine Checkbox kann gesteuert werden, ob Live-Daten aus einem REST-Service oder fest hinterlegte Daten verwendet werden sollen
* Die GUI wird über den Qt Designer und pyuic5 generiert - oder direkt das ui-File eingebunden.
### Model

* Das Model bildet die Schnittstelle zum Webservice bzw. zu den lokal hinterlegten Daten
* Es gibt **zwei** Serivce-**Strategien** (eigene Klassen!):
  * Eine Strategie fragt ein Online-RESTful Service ab (Empfehlung: https://exchangeratesapi.io/) und wandelt das Ergebnis in (HTML-)Text um
  * Eine zweite Strategie verwendet lokal abgelegte (hardgecodete) Werte und liefert wieder das Ergebnis als (HTML-)Text zurück
  * Beide Klassen übernehmen den Betrag, die Ursprungswährung und die Zielwährung(en) als Parameter
  * Eine abstrakte Klasse fasst die Gemeinsamkeiten zusammen (in Python sind abstrakte Klassen mit abc.ABC möglich)

### Controller

* Der Controller ist der Einstiegspunkt für das Programm - er erzeugt die GUI und zeigt sie als Qt-Applikation an
* Er kümmert sich außerdem um das Event-Handling:
  * Zurücksetzen-Button (sofern nicht schon im Designer über Signals und Slots gelöst)
    * Setzt alle Eingabe- und Ausgabefelder zurück
  * Exit-Button (sofern nicht schon im Designer über Signals und Slots gelöst)
    * Schließt die Applikation
  * Umrechnen-Button
    * Ermittelt über die aktuell ausgewählte Strategie das Ergebnis der Umrechnung und übergibt dabei den Betrag, die Ursprungs-Währung und die Ziel-Währung
    * Zeigt das Ergebnis im Ausgabefeld an und aktualisiert die Statusleiste
  * Checkbox
    * Wechselt je nach Checked-Status die Strategie auf RESTful-Service bzw. lokales Service