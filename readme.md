# 🤖 Multi-Agent OS
Autonomous AI Agents Collaborating to Solve Tasks
A powerful multi-agent system where specialized AI agents work together like a team — planning, researching, coding, testing, and reporting.


## Overview
**Multi-Agent OS** is an AI system built with Python that simulates a team of intelligent agents collaborating to solve complex tasks step-by-step.
Instead of relying on a single AI model, this system divides responsibilities across multiple agents, each with a specific role — just like a real software team.


## 🧠 How It Works
1. 🧠 **Planner** breaks down the task
2. 🔍 **Researcher** gathers information
3. 💻 **Coder** writes the code
4. 🧪 **Tester** validates the output
5. 📄 **Reporter** generates the final result

All agents communicate through a shared **state system** and execute via a **graph-based pipeline**.


## 🧩 Agents Architecture

| Agent         | Responsibility          |
| ------------- | ----------------------- |
| 🧠 Planner    | Task decomposition      |
| 🔍 Researcher | Information gathering   |
| 💻 Coder      | Code generation         |
| 🧪 Tester     | Code validation         |
| 📄 Reporter   | Final output generation |


🏗️ Project Structure

Multi-agent-OS/
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── coder.py
│   ├── tester.py
│   └── reporter.py
│
├── core/
│   ├── graph.py
│   ├── state.py
│
├── tools/
│
├── main.py
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-os.git
cd multi-agent-os
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt


## 🤖 Setup Local AI (FREE with Ollama)

Download Ollama:
👉 https://ollama.com

Pull model:

```bash
ollama pull llama

## ▶️ Run the Project

```bash
python main.py
```

Example input:

```
Enter your task: Build a Python calculator
```

---

## ⚠️ Fix (Important)

If you see this warning:

```
LangChainDeprecationWarning: Ollama class deprecated
```

Run:

```bash
pip install -U langchain-ollama
```

Update your import:

```python
from langchain_ollama import OllamaLLM
```

---

## 🛠️ Tech Stack

* Python 🐍
* LangChain
* Ollama (Llama3)
* Graph-based execution

---

## ✨ Features

* 🔄 Multi-agent collaboration
* ⚡ Automated task pipeline
* 🧠 AI-powered decision making
* 📊 Structured state management
* 🧪 Built-in testing system

---

## 📈 Future Improvements

* 🎤 Voice-based interaction (Jarvis style)
* 🌐 Web UI dashboard
* 🧠 Memory & context persistence
* ⚡ Faster parallel execution


## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.


## ⭐ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 🚀 Share it

---

## 👨‍💻 Author
Abhinav 

## 💡 Inspiration
Inspired by real-world software teams and modern AI agent systems.


## 🧠 Final Note
This project is a step toward building **fully autonomous AI systems** that can think, plan, and execute tasks independently.

