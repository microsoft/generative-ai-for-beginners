<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:51:42+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "no"
}
-->
# Transkripsjonsdatapreparering

Skript for transkripsjonsdatapreparering laster ned transkripsjoner av YouTube-videoer og klargjør dem for bruk med eksempelsøket "Semantic Search with OpenAI Embeddings and Functions".

Skript for transkripsjonsdatapreparering er testet på de nyeste versjonene av Windows 11, macOS Ventura og Ubuntu 22.04 (og nyere).

## Opprett nødvendige Azure OpenAI Service-ressurser

1. Opprett en ressursgruppe

1. Opprett en Azure OpenAI Service-ressurs.

1. Hent endepunktet og nøklene for bruk i denne applikasjonen

1. Implementer følgende modeller:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

## Nødvendig programvare

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) eller nyere

## Miljøvariabler

Følgende miljøvariabler er nødvendige for å kjøre skript for transkripsjonsdatapreparering fra YouTube.

### På Windows

Anbefaler å legge til variablene til `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

### På Linux og macOS

Anbefaler å legge til følgende eksporteringer til `~/.bashrc` or `~/.zshrc`-filen.

## Installer de nødvendige Python-bibliotekene

1. Installer [git-klienten](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) hvis den ikke allerede er installert.
1. Fra et `Terminal`-vindu, klon eksemplet til din foretrukne repo-mappe.

1. Naviger til `data_prep`-mappen.

1. Opprett et Python virtuelt miljø.

    På Windows:

    På macOS og Linux:

1. Aktiver Python virtuelt miljø.

   På Windows:

   På macOS og Linux:

1. Installer de nødvendige bibliotekene.

   På Windows:

   På macOS og Linux:

## Kjør skript for transkripsjonsdatapreparering fra YouTube

### På Windows

### På macOS og Linux

**Ansvarsfraskrivelse**:
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruken av denne oversettelsen.