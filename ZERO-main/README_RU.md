# Customization by Zero Team

# Eliza 🤖

<div align="center">
  <img src="./docs/static/img/eliza_banner.jpg" alt="Eliza Banner" width="100%" />
</div>

<div align="center">

📖 [Документация](https://elizaos.github.io/eliza/) | 🎯 [Примеры](https://github.com/thejoven/awesome-eliza)

</div>

## ✨ Особенности

- 🛠 Полноценные коннекторы для Discord, Twitter и Telegram
- 👥 Поддержка нескольких агентов и комнат
- 📚 Простое добавление и взаимодействие с вашими документами
- 💾 Запоминание контекта и хранилище документов
- 🚀 Высокая маштабируемость - создавайте свои собственные действия и клиенты для расширения возможностей
- ☁️ Поддерживает множество моделей, включая локальные Llama, OpenAI, Anthropic, Groq и другие
- 📦 Простота в работе!

## 🎯 Для чего это можно использовать?

- 🤖 Чат-боты
- 🕵️ Автономные агенты
- 📈 Обработка бизнес-процессов
- 🎮 NPC в видеоиграх
- 🧠 Торговля

## 🌍 Переводы

<details>
<summary>Доступные языки</summary>

- [中文说明](./README_CN.md)
- [日本語の説明](./README_JA.md)
- [한국어 설명](./README_KOR.md)
- [Instructions en français](./README_FR.md)
- [Instruções em português](./README_PTBR.md)
- [Инструкция на русском](./README_RU.md)

</details><br>

# 🚀Начало работы

**Необходимые условия (ОБЯЗАТЕЛЬНО):**

- [Python 2.7+](https://www.python.org/downloads/)
- [Node.js 23.3+](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [pnpm](https://pnpm.io/installation)
    > **Для Windows пользователей:** требуется WSL

### Редактирование файла .env

- Скопируйте `.env.example` в `.env` и заполните соответствующими значениями

```bash
cp .env.example .env
```

### Редактирование файла персонажа

1. Откройте `src/core/defaultCharacter.ts`, чтобы изменить персонажа по умолчанию.

2. Для загрузки пользовательских персонажей:
    - Используйте команду `pnpm start --characters="path/to/your/character.json"`
    - Можно загружать несколько файлов персонажей одновременно.

### Запуск Eliza

После настройки файла `.env` и файла персонажа вы можете запустить бота с помощью следующей команды:

```bash
pnpm i
pnpm build
pnpm start

# Проект быстро развивается, иногда нужно очищать проект, если вы возвращаетесь к нему спустя время
pnpm clean
```

#### Дополнительные требования

Возможно, потребуется установить Sharp. Если при запуске возникнет ошибка, попробуйте установить его с помощью следующей команды:

```bash
pnpm install --include=optional sharp
```

# Настройка окружения

Вам потребуется добавить переменные окружения в файл `.env` для подключения к различным платформам:

```
# Обязательные переменные окружения
DISCORD_APPLICATION_ID=
DISCORD_API_TOKEN= # Токен бота
OPENAI_API_KEY=sk-* # API-ключ OpenAI, начинающийся с sk-
ELEVENLABS_XI_API_KEY= # API-ключ от elevenlabs
GOOGLE_GENERATIVE_AI_API_KEY= # API-ключ Gemini

# НАСТРОЙКИ ELEVENLABS
ELEVENLABS_MODEL_ID=eleven_multilingual_v2
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM
ELEVENLABS_VOICE_STABILITY=0.5
ELEVENLABS_VOICE_SIMILARITY_BOOST=0.9
ELEVENLABS_VOICE_STYLE=0.66
ELEVENLABS_VOICE_USE_SPEAKER_BOOST=false
ELEVENLABS_OPTIMIZE_STREAMING_LATENCY=4
ELEVENLABS_OUTPUT_FORMAT=pcm_16000

TWITTER_DRY_RUN=false
TWITTER_USERNAME= # Имя пользователя аккаунта
TWITTER_PASSWORD= # Пароль аккаунта
TWITTER_EMAIL= # Email аккаунта

X_SERVER_URL=
XAI_API_KEY=
XAI_MODEL=


# Для запросов к Claude
ANTHROPIC_API_KEY=

# EVM
EVM_PRIVATE_KEY=EXAMPLE_WALLET_PRIVATE_KEY

# Solana
SOLANA_PRIVATE_KEY=EXAMPLE_WALLET_PRIVATE_KEY
SOLANA_PUBLIC_KEY=EXAMPLE_WALLET_PUBLIC_KEY

# Fallback Wallet Configuration (deprecated)
WALLET_PRIVATE_KEY=EXAMPLE_WALLET_PRIVATE_KEY
WALLET_PUBLIC_KEY=EXAMPLE_WALLET_PUBLIC_KEY

BIRDEYE_API_KEY= # API-ключ для BirdEye

SOL_ADDRESS=So11111111111111111111111111111111111111112
SLIPPAGE=1
RPC_URL=https://api.mainnet-beta.solana.com
HELIUS_API_KEY= # API-ключ Helius


## Telegram
TELEGRAM_BOT_TOKEN= # Токен бота Telegram

TOGETHER_API_KEY=

```

# Локальная настройка среды

### Настройка CUDA

Если у вас есть NVIDIA GPU, вы можете установить CUDA для значительного ускорения локального инференса.

```bash
pnpm install
npx --no node-llama-cpp source download --gpu cuda
```

Убедитесь, что вы установили CUDA Toolkit, включая cuDNN и cuBLAS.

### Локальный запуск

Добавьте `XAI_MODEL` и установите его в одно из вышеуказанных значений из [Запуск с Llama](#run-with-llama). Вы можете оставить `X_SERVER_URL` и `XAI_API_KEY` пустыми — модель будет загружена с huggingface и обработана локально.

# Клиенты

## Бот для Discord

Для получения помощи по настройке бота Discord ознакомьтесь с инструкцией: [Настройка приложения бота](https://discordjs.guide/preparations/setting-up-a-bot-application.html).

### Сообщество и контакты

- [GitHub Issues](https://github.com/elizaos/eliza/issues). Лучше всего подходит для: сообщений об ошибках при использовании Eliza и предложений новых функций.
- [Discord](https://discord.gg/ai16z). Лучше всего подходит для: обмена своими приложениями и общения с сообществом.

## Контрибьюторы

<a href="https://github.com/elizaos/eliza/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=elizaos/eliza" />
</a>

## История звёзд

[![График истории звёзд](https://api.star-history.com/svg?repos=elizaos/eliza&type=Date)](https://star-history.com/#elizaos/eliza&Date)
