Norsain QMS Dev
Et kvalitetsledelsessystem (QMS) basert på ISO 9001:2015, utviklet med Supabase (PostgreSQL), Python og OpenAI AI-agent. Prosjektet støtter organisering av dokumenter, prosesser, risikoer og forbedringer for å oppfylle ISO 9001-krav.
Formål

Lagre QMS-data i Supabase (f.eks. kvalitetspolicy, risikoer).
Automatisere prosesser med OpenAI (f.eks. risikovurderinger).
Tilby en utviklingsplattform for enkel bruk og vedlikehold.

Installasjon

Klon repoet:
Åpne GitHub Desktop, velg File > Clone Repository, skriv https://github.com/Henriklacour/Norsain-qms-dev.git.
Velg en lokal mappe (f.eks. ~/Prosjekter/Norsain-qms-dev) og klikk Clone.


Åpne i VS Code:
Klikk Repository > Open in Visual Studio Code.


Sett opp virtuelt miljø:python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


Konfigurer miljøvariabler:
Kopier .env.example til .env: cp .env.example .env.
Rediger .env med Supabase- og OpenAI-nøkler.


Sett opp Supabase:
Kjør SQL-skript fra sql/ i Supabase Dashboard.



Prosjektstruktur

src/: Python-kode for QMS og AI-agent.
sql/: SQL-skript for Supabase.
tests/: Enhetstester.
docs/: Dokumentasjon.
scripts/: Automatisering.

Bruk

Test tilkobling: python3 -c "from src.qms.supabase_client import supabase; print('Tilkoblet!')"
Kjør tester: pytest tests/
Se docs/brukermanual.md for detaljer.

Vedlikehold

Commit via VS Code (Source Control) eller GitHub Desktop.
Oppdater avhengigheter: pip freeze > requirements.txt.

Kontakt
Bruk GitHub Issues for spørsmål: Issues.
