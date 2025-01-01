# Customization by Zero Team

# Eliza (อีไลซ่า) 🤖

<div align="center">
  <img src="./docs/static/img/eliza_banner.jpg" alt="Eliza Banner" width="100%" />
</div>

<div align="center">

📖 [คู่มือ](https://elizaos.github.io/eliza/) | 🎯 [ตัวอย่าง](https://github.com/thejoven/awesome-eliza)

</div>

## ✨ ฟีเจอร์

- 🛠️ สามารถเชื่อมต่อ Discord, Twitter และ Telegram ได้
- 🔗 ซัพพอร์ตครบทุกโมเดล (Llama, Grok, OpenAI, Anthropic, ฯลฯ)
- 👥 มัลติเอเจนต์และห้องสนทนา
- 📚 ง่ายต่อการดึงและเข้าถึงข้อมูลเอกสาร
- 💾 มีหน่วยความจำและที่จัดเก็บข้อมูล
- 🚀 ง่ายต่อการปรับแต่งไม่ว่าจะเป็นการสร้าง clients หรือกำหนด action
- ☁️ รองรับหลายโมเดล (local Llama, OpenAI, Anthropic, Groq, ฯลฯ)
- 📦 ครบเครื่องเรื่อง AI agent!

## 🎯 ตัวอย่างการนำไปใช้

- 🤖 แชทบอท
- 🕵️ เอเจนต์อิสระ (Autonomous Agent)
- 📈 จัดการฝั่งธุรกิจ
- 🎮 ตัวละครในเกมที่ไม่ใช่ผู้เล่น (NPC)
- 🧠 การเทรด

## 🚀 เริ่มต้นการใช้งาน

### สิ่งที่จำเป็นก่อนเริ่มใช้งาน

- [Python 2.7+](https://www.python.org/downloads/)
- [Node.js 23+](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [pnpm](https://pnpm.io/installation)

> **หมายเหตุสำหรับผู้ใช้ Windows:** จำเป็นต้องมี [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual)

### เริ่มใช้งานด้วยตัวอย่าง (แนะนำ)

```bash
git clone https://github.com/elizaos/eliza-starter.git

cp .env.example .env

pnpm i && pnpm start
```

จากนั้นอ่าน [คู่มือ](https://elizaos.github.io/eliza/) เพื่อศึกษาวิธีการปรับแต่ง Eliza

### เริ่มใช้งาน Eliza ด้วยตนเอง (แนะนำสำหรับคนที่มีประสบการณ์)

```bash
# โคลน repo
git clone https://github.com/elizaos/eliza.git

# Checkout release ล่าสุด
# โปรเจกต์นี้มีการอัปเดตอยู่บ่อยครั้ง เราแนะนำให้ checkout release ล่าสุดเสมอ
git checkout $(git describe --tags --abbrev=0)
```

### เริ่มใช้งาน Eliza ผ่าน Gitpod

[![เปิดใน Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/elizaos/eliza/tree/main)

### แก้ไขไฟล์ .env

คัดลอก .env.example ไปเป็น .env และระบุค่าที่เหมาะสม

```
cp .env.example .env
```

หมายเหตุ: ไม่จำเป็นต้องใช้ .env หากคุณอยากใช้งานเอเจนต์หลายๆตัวพร้อมกัน คุณสามารถส่ง secrets ผ่าน JSON ของตัวละครได้

### เริ่มใช้งาน Eliza แบบอัตโนมัติ

จะทำการติดตั้งโปรเจกต์ทั้งหมด และเริ่มต้น bot ด้วยตัวละครแบบค่าเริ่มต้น

```bash
sh scripts/start.sh
```

### แก้ไขไฟล์ตัวละคร

1. เปิด `agent/src/character.ts` เพื่อแก้ไขตัวละครเริ่มต้น นำคอมเม้นออกและเริ่มแก้ไข

2. การโหลดตัวละคร custom:
    - ใช้ `pnpm start --characters="path/to/your/character.json"`
    - สามารถโหลดหลายๆตัวละครพร้อมกันได้
3. เชื่อมต่อกับ X (Twitter)
    - เปลี่ยน `"clients": []` เป็น `"clients": ["twitter"]` ในไฟล์ตัวละครเพื่อเชื่อมต่อกับ X (Twitter)

### เริ่มใช้งาน Eliza ด้วยตนเอง

```bash
pnpm i
pnpm build
pnpm start

# โปรเจกต์นี้มีการอัปเดตอยู่บ่อยครั้ง บางครั้งอาจต้องทำการ clean โปรเจกต์ถ้าหากกลับมาทำใหม่
pnpm clean
```

#### สิ่งที่จำเป็นเพิ่มเติม

คุณอาจต้องติดตั้ง Sharp ถ้าหากคุณเห็นข้อความ error เมื่อเริ่มต้น สามารถลองติดตั้งด้วยคำสั่งต่อไปนี้:

```
pnpm install --include=optional sharp
```

### ชุมชนและข้อมูลการติดต่อ

- [GitHub Issues](https://github.com/elizaos/eliza/issues). เหมาะสำหรับ: เมื่อปัญหาที่พบเมื่อใช้ Eliza และข้อเสนอแนะเกี่ยวกับฟีเจอร์เพิ่มเติม
- [Discord](https://discord.gg/ai16z). เหมาะสำหรับ: แชร์ผลงานแอปพลิเคชั่นและพบปะกับคอมมูนิตี้

## ผู้มีส่วนร่วม

<a href="https://github.com/elizaos/eliza/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=elizaos/eliza" />
</a>

## ประวัติดาว

[![Star History Chart](https://api.star-history.com/svg?repos=elizaos/eliza&type=Date)](https://star-history.com/#elizaos/eliza&Date)
