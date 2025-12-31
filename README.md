# 🤖 Advanced Python Chatbot 
## Created by Liam De Wet

This repository contains **two versions of a Python-based chatbot** that demonstrate the evolution from a **basic intent-based chatbot** to a **modern, AI-powered assistant** using **sentence embeddings, memory, confidence handling, and a desktop GUI**.

This project was built as a learning and portfolio showcase, focusing on **AI concepts, clean architecture, and real-world assistant features**.

---

## 📌 Project Overview

| Version | Description |
|------|------------|
| **Version 1 – Basic Chatbot** | Traditional intent-based chatbot using classical NLP and a neural network classifier |
| **Version 2 – Advanced AI Chatbot** | Semantic AI assistant using sentence embeddings, memory, confidence thresholds, learning, and a desktop GUI |

Both versions share the same goal:
> **To build an intelligent, extensible chatbot in Python** — but with increasing levels of sophistication.

---

## 🧩 Version 1 – Basic Intent-Based Chatbot

### 🔹 Description
The first version of the chatbot is a **classic intent-classification system**. It uses predefined intents, patterns, and responses stored in a JSON file and trains a neural network to classify user input.

This version focuses on:
- Understanding chatbot fundamentals
- Text preprocessing
- Neural network training
- Intent classification

---

### ⚙️ How It Works (Version 1)

1. **User input** is tokenized and lemmatized using NLTK
2. Input is converted into a **Bag-of-Words vector**
3. A **PyTorch neural network** predicts the intent
4. A response is selected from the matching intent
5. Optional intent-to-function mapping (e.g., stocks)

---

### 🛠️ Technologies Used (Version 1)

- Python
- PyTorch
- NLTK (tokenization & lemmatization)
- NumPy
- JSON (intent storage)

---

### ✅ Features (Version 1)

- Intent classification using a neural network
- Bag-of-Words text representation
- Custom intents via `intents.json`
- Train / save / load model
- Simple CLI interface

---

### ⚠️ Limitations (Version 1)

- Poor handling of paraphrasing
- No understanding of sentence meaning
- No memory or context
- Always responds even when unsure
- Requires retraining to add new knowledge

---

## 🚀 Version 2 – Advanced AI Chatbot (Current)

### 🔹 Description
The second version is a **major architectural upgrade**. Instead of training a classifier, it uses **sentence embeddings** to understand the *semantic meaning* of user input.

This version behaves more like a **real AI assistant** rather than a scripted chatbot.

---

### 🧠 How It Works (Version 2)

1. Each intent pattern is converted into a **sentence embedding** using a transformer model
2. User input is embedded at runtime
3. **Cosine similarity** is used to find the closest matching intent
4. A **confidence threshold** decides whether the bot should respond or fall back
5. Memory and intent-routing logic enhance responses
6. The chatbot runs inside a **desktop GUI (Tkinter)**

---

### 🌟 Key Features (Version 2)

#### 🧠 Semantic Understanding
- Uses **Sentence Transformers (MiniLM)**
- Understands paraphrasing and similar meanings
- No retraining required when adding new patterns

#### 📊 Confidence Threshold + Fallback
- Uses similarity scores as confidence
- Responds only when confident
- Human-like fallback messages when unsure

#### 🧠 Short-Term Memory
- Remembers:
  - User name
  - Last message
  - Last intent
  - Last topic
- Supports questions like:
  - *"What did I ask earlier?"*
  - *"What is my name?"*

#### 🔀 Intent → Function Router
- Certain intents trigger Python functions
- Examples:
  - Stock portfolio lookup
  - Cybersecurity tips
  - Linux command tips
  - Network troubleshooting advice

#### 📚 Online Learning
- Bot can learn new responses from the user
- New knowledge is saved to `learned_intents.json`
- No restart or retraining required

#### 🎭 Personality Modes
- Configurable chatbot personalities:
  - Friendly
  - Professional
  - Hacker
- Affects tone and fallback responses

#### 🖥️ Desktop GUI
- Built using **Tkinter**
- Scrollable chat window
- Input box + send button
- Real-time interaction

---

### 🛠️ Technologies Used (Version 2)

- Python
- Sentence Transformers (`all-MiniLM-L6-v2`)
- PyTorch (backend dependency)
- HuggingFace Transformers
- NumPy
- JSON (persistent knowledge storage)
- Tkinter (desktop GUI)

---

## 📂 Project Structure

```
more_adv_chatbot/
│
├── main.py               # Advanced chatbot logic + GUI
├── intents.json          # Core intent knowledge base
├── learned_intents.json  # User-taught knowledge (auto-created)
└── README.md             # Project documentation
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```bash
pip install torch sentence-transformers numpy nltk
```

### 2️⃣ Run the chatbot

```bash
python main.py
```

A desktop window will open with the chatbot interface.

---

## 🎯 Use Cases

- Learning NLP & AI concepts
- Portfolio project
- Desktop AI assistant
- Cybersecurity / Linux helper
- Educational chatbot

---

## 🧪 Example Interactions

```
User: My name is Alex
Bot: Nice to meet you, Alex!

User: What did I ask earlier?
Bot: You previously asked about your name.

User: Give me a cybersecurity tip
Bot: Always use multi-factor authentication whenever possible.
```


---

## 👨‍💻 Author

Fully built by Myself with passion as a learning and portfolio project to explore **AI, NLP, and intelligent assistant design** in Python.

---

⭐ *If you like this project, consider giving it a star on GitHub!*

