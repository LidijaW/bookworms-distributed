# bookworms-distributed

Projekt za kolegij Raspodijeljeni sustavi.

Aplikacija implementira mikroservisnu arhitekturu za sustav pregleda i recenzija knjiga.

## Arhitektura

Sustav se sastoji od više mikroservisa:

- API Gateway
- User/Auth Service
- Book Service
- Review Service

Svi servisi komuniciraju putem REST API-ja i pokreću se u Docker kontejnerima.

## Tehnologije

- Python
- FastAPI
- Docker
- DynamoDB
