Databasestruktur for Norsain QMS Dev
Oversikt
Databasen støtter ISO 9001:2015 og er organisert i schemas for modularitet. Den bruker Supabase (PostgreSQL) med tabeller for QMS-data.
Schemas

kontekst: Forhold, interesseparter, omfang (ISO kap. 4).
lederskap: Policy, roller (ISO kap. 5).
planlegging: Risikoer, mål, endringer (ISO kap. 6).
støtte: Ressurser, ansatte, infrastruktur (ISO kap. 7).

Tabeller

kontekst.dokumenter: Håndterer QMS-dokumenter (tittel, innhold, opprettet).
