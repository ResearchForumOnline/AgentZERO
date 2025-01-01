# Customization by Zero Team

# Eliza 🤖

<div align="center">
  <img src="./docs/static/img/eliza_banner.jpg" alt="Eliza Banner" width="100%" />
</div>

## ✨ Caratteristiche

- 🛠️ Connettori completi per Discord, Twitter e Telegram
- 🔗 Supporto per tutti i modelli (Llama, Grok, OpenAI, Anthropic, ecc.)
- 👥 Supporto multi-agente e per stanze
- 📚 Acquisisci e interagisci facilmente con i tuoi documenti
- 💾 Memoria recuperabile e archivio documenti
- 🚀 Altamente estensibile - crea le tue azioni e clients personalizzati
- ☁️ Supporto di numerosi modelli (Llama locale, OpenAI, Anthropic, Groq, ecc.)
- 📦 Funziona e basta!

## 🎯 Casi d'uso

- 🤖 Chatbot
- 🕵️ Agenti Autonomi
- 📈 Gestione dei processi aziendali
- 🎮 NPC per Videogiochi
- 🧠 Trading

## 🚀 Avvio Rapido

### Prerequisiti

- [Python 2.7+](https://www.python.org/downloads/)
- [Node.js 23+](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [pnpm](https://pnpm.io/installation)

> **Nota per gli utenti Windows:** È richiesto WSL

### Modifica il file .env

Copia .env.example in .env e inserisci i valori appropriati

```
cp .env.example .env
```

### Avvia Eliza Automaticamente

Questo script eseguirà tutti i comandi necessari per configurare il progetto e avviare il bot con il personaggio predefinito.

```bash
sh scripts/start.sh
```

### Modifica il file del personaggio

1. Apri `packages/agent/src/character.ts` per modificare il personaggio predefinito. Decommenta e modifica.

2. Per caricare personaggi personalizzati:
    - Usa `pnpm start --characters="percorso/del/tuo/personaggio.json"`
    - È possibile caricare più file di personaggi contemporaneamente

### Avvia Eliza Manualmente

```bash
pnpm i
pnpm build
pnpm start

# Il progetto evolve rapidamente; a volte è necessario pulire il progetto se si ritorna sul progetto dopo un po' di tempo
pnpm clean
```

#### Requisiti Aggiuntivi

Potrebbe essere necessario installare Sharp. Se vedi un errore all'avvio, prova a installarlo con il seguente comando:

```
pnpm install --include=optional sharp
```

### Comunità e contatti

- [GitHub Issues](https://github.com/elizaos/eliza/issues). Ideale per segnalare bug riscontrati durante l’utilizzo di Eliza e proporre nuove funzionalità.
- [Discord](https://discord.gg/ai16z). Ideale per condividere le tue applicazioni e interagire con la comunità.

## Contributori

<a href="https://github.com/elizaos/eliza/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=elizaos/eliza" />
</a>

## Cronologia Stelle

[![Grafico Cronologia Stelle](https://api.star-history.com/svg?repos=elizaos/eliza&type=Date)](https://star-history.com/#elizaos/eliza&Date)
