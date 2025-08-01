Brukermanual for Norsain QMS Dev
1. Introduksjon
Dette er en brukermanual for et kvalitetsledelsessystem (QMS) basert på ISO 9001:2015. Systemet bruker Supabase, Python og OpenAI AI-agent for å håndtere QMS-data og automatisere prosesser.
2. Prosjektstruktur

src/: Python-kode for QMS og AI-agent.
sql/: SQL-skript for Supabase.
tests/: Enhetstester med pytest.
docs/: Dokumentasjon.
scripts/: Automatisering.

3. Oppsett (macOS)

Klon repoet:
Åpne GitHub Desktop, velg File > Clone Repository, skriv https://github.com/Henriklacour/Norsain-qms-dev.git.
Velg en lokal mappe (f.eks. ~/Documents/GitHub/Norsain-qms-dev).


Åpne i VS Code:
Klikk Repository > Open in Visual Studio Code.


Opprett mapper:
I VS Code File Explorer, høyreklikk i roten > New Folder.
Skriv navn som src, sql, tests, docs, scripts.
For undermapper, f.eks. src/qms: Klikk inn i src, høyreklikk > New Folder > skriv qms.


Opprett filer:
Høyreklikk i riktig mappe > New File.
For eksempel, i src: Skriv __init__.py (ikke src/__init__.py).


Sett opp virtuelt miljø:python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Konfigurer miljøvariabler:
Kopier .env.example til .env: cp .env.example .env.
Rediger .env med Supabase- og OpenAI-nøkler.


Sett opp Supabase:
Logg inn på supabase.com, opprett et prosjekt.
Kjør skript fra sql/ i SQL Editor.



4. Bruk

Legg til dokument:from src.qms.crud import add_document
print(add_document("Test", "Innhold"))


Test tilkobling:from src.qms.supabase_client import supabase
print("Tilkoblet!") if supabase else print("Feil!")


Kjør tester:pytest tests/



5. Vedlikehold

Oppdater avhengigheter: pip freeze > requirements.txt.
Commit via VS Code (Source Control) eller GitHub Desktop (Commit to main, Push origin).
Bruk GitHub Issues for spørsmål: Issues.
Se docs/database_design.md for databasestruktur.

6. Kontakt
Opprett en issue på GitHub for spørsmål.