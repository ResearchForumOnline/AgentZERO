# Customization by Zero Team

# Eliza

<img src="./docs/static/img/eliza_banner.jpg" alt="Eliza Banner" width="100%" />

## 功能

- 🛠 支持discord/推特/telegram连接
- 👥 支持多模态agent
- 📚 简单的导入文档并与文档交互
- 💾 可检索的内存和文档存储
- 🚀 高可拓展性，你可以自定义客户端和行为来进行功能拓展
- ☁️ 多模型支持，包括Llama、OpenAI、Grok、Anthropic等
- 📦 简单好用

你可以用Eliza做什么？

- 🤖 聊天机器人
- 🕵️ 自主Agents
- 📈 业务流程自动化处理
- 🎮 游戏NPC

# 开始使用

**前置要求(必须):**

- [Python 2.7+](https://www.python.org/downloads/)
- [Node.js 23+](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [pnpm](https://pnpm.io/installation)

以下是两种基础的Eliza下载方案, 请根据情况自行选择。

## (A) 使用启动器(Starter): 推荐

```
git clone https://github.com/elizaos/eliza-starter.git
cd eliza-starter
cp .env.example .env
```

## (B) 手动启动Eliza: 仅在您知道自己在做什么时才推荐

```
git clone https://github.com/elizaos/eliza.git
cd eliza
# 切换最新发布的版本(Checkout the latest release)
# Eliza的迭代速度非常快, 所以我们建议经常性的切换到最新的发布版本以免出现问题(This project iterates fast, so we recommend checking out the latest release)
git checkout $(git describe --tags --abbrev=0)
```

在将代码下载到本地后, 我们要做两件事:

### 1. 编辑.env文件(环境变量)

- 将 `.env.example` 复制为 `.env` 并在其中填写适当的值
- 编辑推特环境并输入你的推特账号和密码

**最简化配置方案**:

```
OPENAI_API_KEY=sk-xxx # 配置OpenAI 的API, sk-开头, 注意, 目前不支持AzureOpenAI!

## 如配置Twitter/X, 则需配置
# Twitter/X Configuration
TWITTER_DRY_RUN=false
TWITTER_USERNAME=abc         # Your Twitter/X account username
TWITTER_PASSWORD=abc         # Your Twitter/X account password
TWITTER_EMAIL= xxx@gmail.com # Your Twitter/X account email
TWITTER_COOKIES= ''          # Your Twitter/X cookies, copy from broswer
TWITTER_2FA_SECRET=          # Two-factor authentication
```

### 2. 编辑角色文件

- 标准的角色个性定义在文件 `characters/*.character.json`中, 您可以修改它或者直接使用它。
- 您也可以使用 `node --loader ts-node/esm src/index.ts --characters="path/to/your/character.json"` 加载角色并同时运行多个机器人。
- 需要说明的是, 在`characters/*.character.json`中, `clients字段对应**服务**, 默认可选`"twitter", "discord", "telegram"`等, 如果在`clients`中填入了如"twitter"等内容, 则需要在
上面的`env`配置对应的环境变量。对`discord`和`telegram`同理。

```
{
    "name": "trump",
    "clients": ["twitter"],
    "modelProvider": "openai",
```

在完成环境变量和角色文件的配置后，输入以下命令行启动你的bot：

```
(A) 使用启动器(Starter)
sh scripts/start.sh


(B) 手动启动Eliza
pnpm i
pnpm build
pnpm start
```

# 自定义Eliza

### 添加常规行为

为避免在核心目录中的 Git 冲突，我们建议将自定义操作添加到 custom_actions 目录中，并在 elizaConfig.yaml 文件中配置这些操作。可以参考 elizaConfig.example.yaml 文件中的示例。

## 配置不同的大模型

### 配置Llama

您可以通过设置 `XAI_MODEL` 环境变量为 `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo` 或 `meta-llama/Meta-Llama-3.1-405B-Instruct` 来运行 Llama 70B 或 405B 模型

### 配置OpenAI

您可以通过设置 `XAI_MODEL` 环境变量为 `gpt-4o-mini` 或 `gpt-4o` 来运行 OpenAI 模型

## 其他要求

您可能需要安装 Sharp。如果在启动时看到错误，请尝试使用以下命令安装：

```
pnpm install --include=optional sharp
```

# 环境设置

您需要在 .env 文件中添加环境变量以连接到各种平台：

```
# Required environment variables
DISCORD_APPLICATION_ID=
DISCORD_API_TOKEN= # Bot token
OPENAI_API_KEY=sk-* # OpenAI API key, starting with sk-
ELEVENLABS_XI_API_KEY= # API key from elevenlabs

# ELEVENLABS SETTINGS
ELEVENLABS_MODEL_ID=eleven_multilingual_v2
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM
ELEVENLABS_VOICE_STABILITY=0.5
ELEVENLABS_VOICE_SIMILARITY_BOOST=0.9
ELEVENLABS_VOICE_STYLE=0.66
ELEVENLABS_VOICE_USE_SPEAKER_BOOST=false
ELEVENLABS_OPTIMIZE_STREAMING_LATENCY=4
ELEVENLABS_OUTPUT_FORMAT=pcm_16000

TWITTER_DRY_RUN=false
TWITTER_USERNAME= # Account username
TWITTER_PASSWORD= # Account password
TWITTER_EMAIL= # Account email

X_SERVER_URL=
XAI_API_KEY=
XAI_MODEL=


# For asking Claude stuff
ANTHROPIC_API_KEY=

# EVM
EVM_PRIVATE_KEY=EXAMPLE_WALLET_PRIVATE_KEY

# Solana
SOLANA_PRIVATE_KEY=EXAMPLE_WALLET_PRIVATE_KEY
SOLANA_PUBLIC_KEY=EXAMPLE_WALLET_PUBLIC_KEY

# Fallback Wallet Configuration (deprecated)
WALLET_PRIVATE_KEY=EXAMPLE_WALLET_PRIVATE_KEY
WALLET_PUBLIC_KEY=EXAMPLE_WALLET_PUBLIC_KEY

BIRDEYE_API_KEY=

SOL_ADDRESS=So11111111111111111111111111111111111111112
SLIPPAGE=1
RPC_URL=https://api.mainnet-beta.solana.com
HELIUS_API_KEY=


## Telegram
TELEGRAM_BOT_TOKEN=

TOGETHER_API_KEY=
```

# 本地设置

### CUDA设置

如果你有高性能的英伟达显卡，你可以以下命令行通过CUDA来做本地加速

```
pnpm install
npx --no node-llama-cpp source download --gpu cuda
```

确保你安装了完整的CUDA工具包，包括cuDNN和cuBLAS

### 本地运行

添加 XAI_MODEL 并将其设置为上述 [使用 Llama 运行](#run-with-llama) 中的选项之一
您可以将 X_SERVER_URL 和 XAI_API_KEY 留空，它会从 huggingface 下载模型并在本地查询

# 客户端

关于怎么设置discord bot，可以查看discord的官方文档

# 开发

## 测试

几种测试方法的命令行：

```bash
pnpm test           # Run tests once
pnpm test:watch    # Run tests in watch mode
```

对于数据库特定的测试：

```bash
pnpm test:sqlite   # Run tests with SQLite
pnpm test:sqljs    # Run tests with SQL.js
```

测试使用 Jest 编写，位于 src/\*_/_.test.ts 文件中。测试环境配置如下：

- 从 .env.test 加载环境变量
- 使用 2 分钟的超时时间来运行长时间运行的测试
- 支持 ESM 模块
- 按顺序运行测试 (--runInBand)

要创建新测试，请在要测试的代码旁边添加一个 .test.ts 文件。
