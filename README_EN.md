# Interactive MBTI Test Game 🐾

🌐 **English** | [Bahasa Indonesia](README.md)

An MBTI personality test visual novel built with **Ren'Py**, featuring **AI Companions** powered by OpenAI (GPT-4o). Players answer 20 interactive story questions accompanied by one of five animal companions — each representing a **Big Five (OCEAN)** trait — that react in real time to every choice the player makes, complete with dynamically changing emotional expressions.

> ⚠️ **Disclaimer:** This is a simple personality test inspired by the Myers-Briggs Type Indicator (MBTI). The results are an initial reflection / self-discovery aid, not a professional diagnosis.

Made by **Fuzakis Project**.

---

## Features

- 🎲 **60 story questions** in 3 packets (A/B/C), shuffled with anti-repeat across sessions
- 🦊 **5 AI Companions** with Big Five personas: Kitsuko (Openness), Onyen (Conscientiousness), Iwank (Extraversion), Susagi (Agreeableness), Jakouko (Neuroticism)
- 🎭 **Emotion parser** — companion sprite expressions change based on emotion tags from the AI (Ekman's emotion model)
- 🧮 **4-dimension MBTI scoring** (I/E, S/N, T/F, J/P) + a Spirit Animal for each type
- 💬 **Free chat** with your companion + **persistent memory** per player (JSON)
- 🏆 Achievements, music room, multi-profile support, bilingual (ID/EN)
- 📊 Automatic CSV logging (latency, token usage, test results) for research purposes

---

## Project Setup

### 1. Prerequisites

- [Ren'Py SDK](https://www.renpy.org/latest.html) **8.5.x** (developed on 8.5.2)
- An OpenAI API key (default model: `gpt-4o`)
- Windows/Mac/Linux (developed & tested on Windows 11)

### 2. Clone & register with Ren'Py

```bash
git clone https://github.com/fuzakis/Interactive-MBTI-Game.git
```

Open the **Ren'Py Launcher** → `preferences` → set the *Projects Directory* to the parent folder of the clone (or move the project folder into your existing projects directory). The project will appear in the list under its folder name.

### 3. Configure the API Key (`game/.env`)

Create a `game/.env` file (never committed to git, and excluded from builds):

```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxx
```

The loader lives in `game/definitions.rpy` — lookup order: `game/.env` → env var `OPENAI_API_KEY_2` → env var `OPENAI_API_KEY`. If all are empty, a warning is printed to the console and every AI call returns a connection error message (the game still runs, but companions can't talk).

### 4. SSL Fix (included, do not remove)

Ren'Py's bundled Python often fails to verify HTTPS certificates. The file `game/01_fix_ssl.rpy` (runs at `init -999`) monkeypatches `certifi.where()` to point at `game/python-packages/certifi/cacert.pem`. Make sure the `game/python-packages/certifi/` folder exists.

### 5. Run

Ren'Py Launcher → select the project → **Launch Project**. Debug logs (AI prompts, latency, running MBTI scores) appear in the console / `log.txt`.

---

## System Architecture

```
game/
├── 01_fix_ssl.rpy               # certifi monkeypatch (init -999) for HTTPS
├── definitions.rpy              # Personas/system prompts, API call, .env loader,
│                                #   auto-generated companion images, AI memory (JSON)
├── script.rpy                   # Main flow: splash → companion select → AI tutorial
│                                #   → test → results & evaluation → free chat → ending
├── questions_data.rpy           # [GENERATED] Question packet lists (A/B/C) + dimensions
├── questions_logic.rpy          # Packet shuffling, question loop, ai_react_logic,
│                                #   breakdown_ai_text (sentence splitter)
├── questions_logic_generated.rpy# [GENERATED] 60 questions × 2 languages (labels + menus + scoring)
├── logger.rpy                   # CSV logging (API chat, MBTI results, token recap)
├── custom_screens.rpy           # Custom screens (companion selection, result diagram,
│                                #   achievements, music room, profiles, free chat hub)
├── screens.rpy / gui.rpy / options.rpy  # Standard Ren'Py UI (modified)
└── .env                         # API key (DO NOT commit)
```

---

## How Each System Works

### 1. Prompt Engineering & Personality

Each companion has a **persona system prompt** in `get_system_prompt()` (`definitions.rpy`), available in both languages. Each persona is structured as:

- **ROLE** — character identity (e.g. "You are Jakouko representing the Neuroticism trait")
- **TRAITS** — the personality traits to roleplay
- **SPEECH STYLE** — signature language patterns (Iwank says "Woof!", Susagi stutters politely, Jakouko is paranoid with broken sentences)
- **TAG RULES** — the emotion-tag format contract (see Emotion Parser)
- **DIALOGUE EXAMPLES** — few-shot examples to keep the style consistent

There is a special `"psychologist"` persona — an objective mode **without** emotion tags, used for the detailed MBTI result explanation.

On top of the system prompt, each context has its own **user prompt** (in `script.rpy` / `questions_logic.rpy`): the interactive tutorial, per-question reactions (with a recap of the last 5 choices so the conversation stays coherent), the 3-part final evaluation (separated by `###`), and free chat (with a 10–15 message sliding memory window).

### 2. API Call

`get_ai_feedback(user_text, personality_key, lang, token_limit)` in `definitions.rpy`:

1. Assemble the persona system prompt + the context-specific user prompt
2. POST to `https://api.openai.com/v1/chat/completions` via `urllib` (model `gpt-4o`, `temperature 0.9`)
3. Sanitize the response: `{` `}` → `(` `)` (because `{}` is a Ren'Py text tag), strip outer quotes
4. Accumulate token usage into session variables + append a row to `PA_Log_API_Chat.csv`
5. On error → return `"[NEUTRAL] (Error Koneksi: ...)"` so the game never crashes

`token_limit` per context: question reaction 300 · tutorial 500 · free chat 800–1000 · final evaluation 1500 · psychologist explanation 2000.

### 3. Emotion Parser

Contract with the AI: insert `[HAPPY] [SAD] [ANGRY] [FEAR] [SURPRISE] [DISGUST] [NEUTRAL]` tags at every tone change.

Parsing flow (used in the tutorial, question reactions, evaluation, and chat):

1. **`breakdown_ai_text()`** splits the response into sentences: per line → strip paragraph-wrapping quotes → split at `.` `!` `?` (ellipses `...` do NOT split) → split before `[` tags
2. Each sentence is checked with the regex `\[(.*?)\]` — "wild" tags are mapped to valid emotions (e.g. `[WORRIED]`/`[ANXIOUS]` → fear, `[EXCITED]` → happy, `[WOOF]` → neutral)
3. If the emotion changed → `renpy.show("companion <personality> <emotion>")` swaps the sprite
4. Tags are stripped from the text, then `renpy.say()` displays each clean sentence one at a time (click-per-sentence pacing)

Emotion sprites are auto-generated at init from the pattern `images/<Folder>/<Name> <emotion>.png`, with an automatic blink animation when a `_blink.png` file exists (anti-crash: falls back to the static image).

The special `[SPIRIT]` tag in the final evaluation triggers the Spirit Animal reveal with a zoom animation.

### 4. MBTI Scoring

- 4 global counters: `IE`, `SN`, `TF`, `JP` (start at 0)
- Every question tests **2 dimensions at once** (e.g. "E/I & S/N"); each choice adds/subtracts **±5** on those 2 dimensions
- 20 questions per session → each dimension is tested ±10 times
- Letter determination in `scene_hasil_tes`: score `>= 0` → **E / N / F / P**, negative score → **I / S / T / J**
- Dominance percentage: `50 + (|score| / 2)`
- The 4-letter result maps to a **Spirit Animal** (`spirit_animals` dict, 16 types × 2 languages)

### 5. Question System (Generated)

`questions_data.rpy` and `questions_logic_generated.rpy` are produced by an external generator. The pattern for each question:

```
label show_question_<id>_<lang>:
    scene bg <location>
    $ narasi_asli = "..."          # stored as context for the AI prompt
    n "..."                        # staged narration
    menu:
        "<choice A>":
            $ IE -= 5 / $ SN -= 5  # score 2 dimensions
            $ user_choice_text = "..." ; $ last_answer = "Introvert & Sensing"
            jump <label>_A         # append user_journey_summary → call ai_react_logic
```

Shuffling: pick a packet not yet played (`persistent.used_packet_titles`), then shuffle question order with a simple LCG.

### 6. AI Memory & Player Profiles

- For each (player, companion) pair, a JSON file is stored in the save directory: `<name>_<companion>.json` containing `last_mbti`, `known_facts`, `chat_history`
- Free chat injects the last 10 messages into the prompt (sliding window) so the companion "remembers" conversations across sessions
- `profile_manager_screen` scans all JSON files to build the multi-profile list

### 7. Research Logging (CSV)

| File | Contents |
|---|---|
| `PA_Log_API_Chat.csv` | Timestamp, character, model, latency, tokens in/out/total, prompt, response — per API call |
| `PA_Log_MBTI_Akhir.csv` | Name, MBTI result, spirit animal, raw scores, final memory — per completed session |
| `PA_Rekap_10_Permainan.csv` | Recap of interaction count & total tokens per session |

These files contain participant data → **never committed** (see `.gitignore`).

---

## Build & Distribution

- **PC:** Ren'Py Launcher → Build Distributions. `options.rpy` already excludes large Python packages (~3GB) and `game/.env` from the build.
- **Android:** configured in `android.json` (landscape, `INTERNET` + `VIBRATE` permissions). Keystores are **not** included in the repo — generate your own via RAPT.
- **API key in builds:** `game/.env` is excluded from builds by default. For private/testing distribution, copy your `.env` into the built game's `game/` folder (or remove the `build.classify('game/.env', None)` line before building). ⚠️ Any key shipped inside a build can be extracted by players — the same risk as hardcoding. For a public launch, the proper solution is a small proxy server that holds the key; do not ship a raw key publicly.

## Development Notes

- **`CATATAN_PENTING.md`** — things to watch out for so the game doesn't break (cross-file dependencies, emotion-tag contract, persistent data, etc.). **Read before changing code.** (Indonesian)
- **`catatan update ke game MBTI.md`** — list of improvements based on Expert Evaluator feedback (SATGAS PPKS PENS) and user testing results. (Indonesian)
