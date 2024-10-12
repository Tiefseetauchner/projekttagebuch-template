# Projekttagebuch

Dieses Repo beinhaltet die Basic Structure für ein Projekttagebuch

## Bearbeiten

Das meiste in diesem Template ist in LaTeX geschrieben, aber es gibt ein paar Eigenheiten, um die Verwendung von LaTeX zu minimieren.

- variables.json
  Diese Datei beinhaltet einige Variablen die dynamisch beim Ausführen von compile.py angepasst werden. Dazu zählen:
  - Teamname
  - Teammitglieder Liste
  - Teammitglieder Rollen Liste
  - Der primaryContact, welcher eine Referenz zu einem der Teammitglieder sein muss, und auf der Titelseite sein muss. Einfacher Index, starting at 0.
  - Kurze Beschreibung des Projektes
- TagesberichteMD/...
  - Beim Kompilieren wird aus den Markdown Files aus dem Ordner dynamisch LaTeX erzeugt und in das Dokument eingefügt.
  - Einfach in Markdown schreiben und es ist super!
- TeX files
  - Wo es weniger leicht vermeidbar ist, LaTeX zu verwenden ist in den anderen Sections. Theorethisch könnte man das auch mit Markdown machen aber da war ich zu faul. Darum, wenn in den restlichen sections etwas ist, was sich ändern soll, muss man das jeweilige .tex file anpassen

## Kompilieren

Für das Compilen von dem Script ist eine Python Installation sowie eine LaTeX Installation (miktex, texlive, ...) benötigt, die pdflatex anbietet. Außerdem braucht man eine pandoc installation im Pfad.

Dann einfach `compile.py` ausführen :)
