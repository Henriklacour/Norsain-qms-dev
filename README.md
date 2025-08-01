# Norsain QMS Dev

Et kvalitetsledelsessystem (QMS) basert på ISO 9001:2015, utviklet med Supabase (PostgreSQL), Python og OpenAI AI-agent. Prosjektet støtter organisering av dokumenter, prosesser, risikoer og forbedringer for å oppfylle ISO 9001-krav.

## Formål
- Lagre QMS-data i Supabase (f.eks. kvalitetspolicy, risikoer).
- Automatisere prosesser med OpenAI (f.eks. risikovurderinger).
- Tilby en utviklingsplattform for enkel bruk og vedlikehold.

## Installasjon
1. **Klon repoet**:
   - Åpne GitHub Desktop, velg **File > Clone Repository**, skriv `https://github.com/Henriklacour/Norsain-qms-dev.git`.
   - Velg en lokal mappe (f.eks. `~/Documents/GitHub/Norsain-qms-dev`).
2. **Åpne i VS Code**:
   - Klikk **Repository > Open in Visual Studio Code**.
3. **Sett opp virtuelt miljø**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt