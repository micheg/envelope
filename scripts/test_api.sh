#!/bin/bash

# Verifica che siano stati passati tutti i parametri
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <username> <password>"
    exit 1
fi

# Variabili di configurazione
USERNAME="$1"
PASSWORD="$2"
BASE_URL="http://127.0.0.1:8000/api"
AUTH_URL="$BASE_URL/api-token-auth/"
CREATE_ENVELOPE_URL="$BASE_URL/envelopes/create/"
GET_ENVELOPE_URL="$BASE_URL/envelopes/1/"
LIST_ENVELOPES_URL="$BASE_URL/envelopes/"

# Ottieni il token
echo "Richiesta del token di autenticazione..."
RESPONSE=$(curl -s -X POST $AUTH_URL \
    -H "Content-Type: application/json" \
    -d "{\"username\": \"$USERNAME\", \"password\": \"$PASSWORD\"}")

TOKEN=$(echo $RESPONSE | jq -r '.token')

if [ "$TOKEN" == "null" ]; then
    echo "Errore: Impossibile ottenere il token."
    exit 1
fi

echo "Token ottenuto: $TOKEN"

# Crea un nuovo envelope
echo "Creazione di un nuovo envelope..."
CREATE_RESPONSE=$(curl -s -X POST $CREATE_ENVELOPE_URL \
    -H "Authorization: Token $TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"title": "Nuovo Titolo", "data": {"key": "value"}}')

echo "Risposta dalla creazione dell'envelope: $CREATE_RESPONSE"

# Recupera un envelope specifico
echo "Recupero dell'envelope con ID 1..."
GET_RESPONSE=$(curl -s -X GET $GET_ENVELOPE_URL \
    -H "Authorization: Token $TOKEN" \
    -H "Content-Type: application/json")

echo "Risposta dal recupero dell'envelope: $GET_RESPONSE"

# Elenca tutti gli envelopes
echo "Elenco di tutti gli envelopes..."
LIST_RESPONSE=$(curl -s -X GET $LIST_ENVELOPES_URL \
    -H "Authorization: Token $TOKEN" \
    -H "Content-Type: application/json")

echo "Risposta dall'elenco degli envelopes: $LIST_RESPONSE"

