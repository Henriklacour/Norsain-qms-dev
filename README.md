Norsain QMS Dev
Et kvalitetsledelsessystem (QMS) basert på ISO 9001:2015, utviklet med Supabase (PostgreSQL), Python og OpenAI AI-agent. Prosjektet støtter organisering av dokumenter, prosesser, risikoer og forbedringer for å oppfylle ISO 9001-krav som dokumentert informasjon, lederskap og kontinuerlig forbedring.
Formål

Lagre og håndtere QMS-data (f.eks. kvalitetspolicy, risikoer, dokumenter) i en Supabase-database.
Automatisere prosesser med OpenAI AI-agent (f.eks. generere risikovurderinger eller forbedringsforslag).
Tilby en strukturert utviklingsplattform som er enkel å bruke og vedlikeholde.

Installasjon

Klon repoet:
Åpne GitHub Desktop, velg File > Clone Repository, skriv https://github.com/Henriklacour/Norsain-qms-dev.git.
Velg en lokal mappe (f.eks. ~/Documents/GitHub/Norsain-qms-dev) og klikk Clone.


Åpne i VS Code:
Klikk Repository > Open in Visual Studio Code i GitHub Desktop.


Sett opp virtuelt miljø:python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Konfigurer miljøvariabler:
Kopier .env.example til .env:cp .env.example .env


Rediger .env med Supabase- og OpenAI-nøkler (fås fra supabase.com og platform.openai.com).


Sett opp Supabase:
Logg inn på supabase.com og opprett et prosjekt.
Gå til SQL Editor i Supabase Dashboard og kjør skript fra sql/-mappen (f.eks. schemas.sql, tables.sql).



Prosjektstruktur

src/: Python-kode for QMS-logikk og AI-agent.
qms/: Supabase-tilkobling og CRUD-operasjoner.
utils/: Hjelpefunksjoner (f.eks. logging).


sql/: SQL-skript for Supabase-databaser.
tests/: Enhetstester med pytest.
docs/: Dokumentasjon, inkludert brukermanual og databasestruktur.
scripts/: Automatiserings-skript (f.eks. miljøoppsett).

Bruk

Legge til et dokument:from src.qms.crud import add_document
print(add_document("Testdokument", "Innhold her"))


Teste Supabase-tilkobling:from src.qms.supabase_client import supabase
print("Tilkoblet!") if supabase else print("Feil!")


Kjøre tester:pytest tests/


Se docs/brukermanual.md for detaljerte instruksjoner.

Vedlikehold

Oppdater avhengigheter:pip freeze > requirements.txt


Commit endringer via GitHub Desktop:
Skriv en klar melding, klikk Commit to main, deretter Push origin.


Bruk GitHub Issues for spørsmål eller feilrapporter: Issues.
Se docs/database_design.md for databasestruktur.

Kontakt
Spørsmål? Opprett en issue på GitHub.