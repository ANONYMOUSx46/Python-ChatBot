import json
import os
import random
import tkinter as tk
from tkinter import scrolledtext

import torch
import numpy as np
from sentence_transformers import SentenceTransformer, util


# ==========================
# CONFIG
# ==========================
CONFIDENCE_THRESHOLD = 0.6
PERSONALITY = "friendly"  # friendly | professional | hacker


# ==========================
# PERSONALITY RESPONSES
# ==========================
PERSONALITY_FALLBACKS = {
    "friendly": [
        "Hmm, I'm not sure I understand yet 😊",
        "Can you rephrase that for me?"
    ],
    "professional": [
        "I do not have sufficient confidence to answer that.",
        "Please clarify your request."
    ],
    "hacker": [
        "Command not recognized 👀",
        "That input makes no sense… yet."
    ]
}


# ==========================
# CHATBOT ASSISTANT
# ==========================
class ChatbotAssistant:

    def __init__(self, intents_path):
        self.intents_path = intents_path
        self.learned_path = "learned_intents.json"

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.intents = []
        self.patterns = []
        self.responses = {}
        self.embeddings = None

        # Memory
        self.user_name = None
        self.last_message = None
        self.last_intent = None
        self.last_topic = None

        # Function router
        self.function_mappings = {
            "stocks": self.get_stocks,
            "cybersecurity": self.cyber_tip,
            "linux": self.linux_tip,
            "network": self.network_tip
        }

        self.load_intents()


    # ==========================
    # LOAD INTENTS
    # ==========================
    def load_intents(self):
        all_intents = []

        with open(self.intents_path, "r") as f:
            data = json.load(f)
            all_intents.extend(data["intents"])

        if os.path.exists(self.learned_path):
            with open(self.learned_path, "r") as f:
                learned = json.load(f)
                all_intents.extend(learned["intents"])

        for intent in all_intents:
            tag = intent["tag"]
            self.responses[tag] = intent["responses"]
            for pattern in intent["patterns"]:
                self.intents.append(tag)
                self.patterns.append(pattern)

        self.embeddings = self.model.encode(self.patterns, convert_to_tensor=True)


    # ==========================
    # CORE CHAT LOGIC
    # ==========================
    def process_message(self, message):
        self.last_message = message

        # Name detection
        if message.lower().startswith("my name is"):
            self.user_name = message.split("is")[-1].strip()
            return f"Nice to meet you, {self.user_name}!"

        # Memory intents
        if "what did i ask" in message.lower():
            return f"You previously asked: '{self.last_message}'"

        if "what is my name" in message.lower():
            return self.user_name or "You haven't told me your name yet."

        # Embedding similarity
        msg_embedding = self.model.encode(message, convert_to_tensor=True)
        scores = util.cos_sim(msg_embedding, self.embeddings)[0]

        best_score = torch.max(scores).item()
        best_idx = torch.argmax(scores).item()

        # Confidence check
        if best_score < CONFIDENCE_THRESHOLD:
            return random.choice(PERSONALITY_FALLBACKS[PERSONALITY])

        intent = self.intents[best_idx]
        self.last_intent = intent
        self.last_topic = intent

        # Function routing
        if intent in self.function_mappings:
            return self.function_mappings[intent]()

        return random.choice(self.responses[intent])


    # ==========================
    # LEARNING
    # ==========================
    def learn_new_intent(self, user_input, correct_response):
        data = {"intents": []}

        if os.path.exists(self.learned_path):
            with open(self.learned_path, "r") as f:
                data = json.load(f)

        data["intents"].append({
            "tag": f"user_learned_{len(data['intents'])}",
            "patterns": [user_input],
            "responses": [correct_response]
        })

        with open(self.learned_path, "w") as f:
            json.dump(data, f, indent=4)

        self.load_intents()


    # ==========================
    # FUNCTION ROUTES
    # ==========================
    def get_stocks(self):
        stocks = ["AAPL", "MSFT", "NVDA", "META", "GOOG"]
        return f"Your stocks: {', '.join(random.sample(stocks, 3))}"

    def cyber_tip(self):
        tips = [
            "Always hash passwords with bcrypt.",
            "Never trust user input.",
            "Use MFA wherever possible."
        ]
        return random.choice(tips)

    def linux_tip(self):
        tips = [
            "Use `htop` to monitor system resources.",
            "`chmod 600` protects sensitive files.",
            "Pipe commands with | for power."
        ]
        return random.choice(tips)

    def network_tip(self):
        tips = [
            "Use `nmap` to scan open ports.",
            "DNS issues cause most outages.",
            "Always subnet properly."
        ]
        return random.choice(tips)


# ==========================
# TKINTER GUI
# ==========================
class ChatbotGUI:

    def __init__(self, assistant):
        self.bot = assistant

        self.root = tk.Tk()
        self.root.title("Advanced AI Chatbot")

        self.chat = scrolledtext.ScrolledText(self.root, width=60, height=20)
        self.chat.pack(padx=10, pady=10)
        self.chat.config(state=tk.DISABLED)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(side=tk.LEFT, padx=10)
        self.entry.bind("<Return>", self.send)

        self.send_btn = tk.Button(self.root, text="Send", command=self.send)
        self.send_btn.pack(side=tk.RIGHT)

        self.write("Bot", "Hello! I'm your AI assistant 🤖")

        self.root.mainloop()

    def write(self, sender, message):
        self.chat.config(state=tk.NORMAL)
        self.chat.insert(tk.END, f"{sender}: {message}\n")
        self.chat.config(state=tk.DISABLED)
        self.chat.yview(tk.END)

    def send(self, event=None):
        msg = self.entry.get()
        if not msg:
            return
        self.entry.delete(0, tk.END)
        self.write("You", msg)
        response = self.bot.process_message(msg)
        self.write("Bot", response)


# ==========================
# START APP
# ==========================
if __name__ == "__main__":
    assistant = ChatbotAssistant("intents.json")
    ChatbotGUI(assistant)
