# 🎬 AI YouTube Script Generator Agent

An AI-powered YouTube Script Generator built using **LangGraph**, **LangChain**, and **Groq LLM**.

This project demonstrates how to build a simple multi-agent AI workflow where each agent is responsible for one task in the content creation pipeline.

---

## ✨ Features

- 📝 Cleans and improves raw text
- ✍️ Converts text into an engaging YouTube script
- 🌐 Generates a natural conversational output (Hinglish-ready pipeline)
- ⚡ Powered by Groq's ultra-fast Llama 3.3 70B model
- 🔄 Built with LangGraph stateful workflows

---

## 🏗️ Workflow

```
Raw Input
     │
     ▼
Editor Agent
(Fixes grammar & improves flow)
     │
     ▼
Script Writer Agent
(Creates engaging YouTube script)
     │
     ▼
Translator Agent
(Produces conversational final output)
     │
     ▼
Final Script
```

---

## 📂 Project Structure

```
youtube-script-generator/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🧠 Agents

### 1. Editor Agent

Responsibilities:

- Fix grammatical mistakes
- Remove spelling errors
- Improve readability
- Keep the original meaning unchanged

---

### 2. Script Writer Agent

Responsibilities:

- Convert edited text into an engaging YouTube script
- Improve storytelling
- Create conversational flow
- Add energy and personality

---

### 3. Translator Agent

Responsibilities:

- Convert the script into a natural conversational output
- Can easily be modified to generate Hinglish or other languages

---

## ⚙️ Tech Stack

- Python
- LangGraph
- LangChain
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/youtube-script-generator.git

cd youtube-script-generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key
```

Get your API key from

https://console.groq.com/

---

## ▶️ Run

```bash
python main.py
```

---

## 💻 Example

### Input

```
AI agents are the future of tech. they can think, plan, and act on their tasks
```

---

### Workflow

```
Input
   ↓
Editor
   ↓
Script Writer
   ↓
Translator
   ↓
Final Output
```

---

### Example Output

```
Imagine having an assistant that doesn't just answer questions—but actually thinks, plans, and completes tasks for you.

That's exactly what AI agents are.

They're changing the future of technology by working independently, making decisions, and helping humans become more productive than ever before.
```

---

## 📚 State Definition

```python
class PipelineState(TypedDict):
    raw_input: str
    edited_text: str
    script_text: str
    final_output: str
```

---

## 🔄 LangGraph Flow

```
START
  │
  ▼
Editor
  │
  ▼
Script Writer
  │
  ▼
Translator
  │
  ▼
END
```

---

## 🚀 Future Improvements

- Multiple language support
- Long-form YouTube scripts
- Hook generation
- CTA generator
- Thumbnail title generator
- SEO description generation
- Hashtag generation
- Viral title suggestions
- Memory support
- RAG integration
- Multi-model support

---

## 📖 Learning Objectives

This project is a great beginner-friendly introduction to:

- LangGraph
- AI Agents
- State Management
- Workflow Automation
- LLM Pipelines
- Prompt Engineering

---

## 🤝 Contributing

Contributions are welcome!

Feel free to open an issue or submit a pull request if you'd like to improve the project.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

## 📄 License

This project is licensed under the MIT License.
