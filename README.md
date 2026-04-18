<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ORION AI - README Generator</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <style>
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .gradient-bg {
            background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        .code-block {
            background: #1e1e1e;
            border-radius: 8px;
            padding: 20px;
            font-family: 'Courier New', monospace;
            color: #d4d4d4;
            overflow-x: auto;
            position: relative;
        }
        
        .copy-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.3s;
        }
        
        .copy-btn:hover {
            background: #764ba2;
        }
        
        .copied {
            background: #10b981 !important;
        }
        
        pre {
            margin: 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        
        .glow {
            box-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
        }
    </style>
</head>
<body class="bg-gray-900 text-white min-h-screen">
    <!-- Hero Section -->
    <div class="gradient-bg py-20">
        <div class="max-w-6xl mx-auto px-6 text-center">
            <h1 class="text-6xl font-bold mb-4">🚀 ORION AI README</h1>
            <p class="text-2xl mb-8">Premium GitHub README Generator</p>
            <button onclick="copyReadme()" class="bg-white text-purple-600 px-8 py-4 rounded-full font-bold text-lg hover:scale-105 transition transform glow">
                📋 Copy README to Clipboard
            </button>
        </div>
    </div>

    <!-- README Preview -->
    <div class="max-w-6xl mx-auto px-6 py-12">
        <div class="bg-gray-800 rounded-xl p-8 mb-8">
            <h2 class="text-3xl font-bold mb-6 text-purple-400">📄 Your Premium README.md</h2>
            <div class="code-block">
                <button class="copy-btn" onclick="copyReadme()">📋 Copy</button>
                <pre id="readme-content"><div align="center">

# 🌌 ORION AI

### *Your Intelligent AI Companion with Personality*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-121212?style=for-the-badge)](https://langchain.com/)
[![Mistral AI](https://img.shields.io/badge/Mistral_AI-FF7000?style=for-the-badge&logo=ai&logoColor=white)](https://mistral.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)](https://huggingface.co/spaces/Anmoldhiman17/orion-ai)

<p align="center">
  <a href="https://github.com/anmoldhiman17/orion-ai-chatbot">
    <img src="https://img.shields.io/badge/GitHub-View_Repo-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <a href="https://huggingface.co/spaces/Anmoldhiman17/orion-ai">
    <img src="https://img.shields.io/badge/🤗_Live_Demo-Visit_Now-FFD21E?style=for-the-badge" alt="Live Demo">
  </a>
</p>

---

### 🎯 *Experience the future of conversational AI with multiple personalities*

</div>

<br>

## 🎥 See It In Action

<div align="center">

### ✨ Live Demo Available Now!

[![Live Demo](https://img.shields.io/badge/🚀_TRY_ORION_AI_NOW-Visit_Live_Demo-FF4B4B?style=for-the-badge&logoColor=white)](https://huggingface.co/spaces/Anmoldhiman17/orion-ai)

> 💡 **Pro Tip:** Add your screenshots here to showcase the stunning UI!
> 
> ```markdown
> ![ORION AI Demo](assets/demo.gif)
> ![Screenshot 1](assets/screenshot1.png)
> ![Screenshot 2](assets/screenshot2.png)
> ```

</div>

---

## 🌟 Why ORION AI?

<table>
<tr>
<td width="50%">

### 🎭 **Multi-Personality Engine**
Switch between 5 distinct AI personalities on-the-fly. From serious to silly, ORION adapts to your mood.

</td>
<td width="50%">

### 🧠 **Context-Aware Memory**
Powered by LangChain's advanced memory system, ORION remembers your conversation history for seamless interactions.

</td>
</tr>
<tr>
<td width="50%">

### ⚡ **Lightning Fast**
Built on Mistral's cutting-edge small language model (mistral-small-2501) for rapid, intelligent responses.

</td>
<td width="50%">

### 🎨 **Futuristic UI/UX**
Dark-themed, sleek interface designed for the modern user. Clean, intuitive, and visually stunning.

</td>
</tr>
</table>

---

## ✨ Features That Make ORION Special

<div align="center">

| Feature | Description |
|---------|-------------|
| 😡 **Angry Mode** | Aggressive, direct responses with attitude |
| 😂 **Funny Mode** | Comedy genius - jokes, puns, and humor |
| 😢 **Sad Mode** | Empathetic, emotional, and understanding |
| 🧠 **Smart Mode** | Intelligent, analytical, and professional |
| 🤖 **Robot Mode** | Mechanical, precise, and systematic |

</div>

### 🎯 Core Capabilities

- ✅ **Real-time conversational AI** with instant responses
- ✅ **Session-based memory** that persists throughout your chat
- ✅ **Seamless mode switching** - change personalities mid-conversation
- ✅ **Context understanding** - ORION remembers what you talked about
- ✅ **Custom dark theme** with smooth animations
- ✅ **Responsive design** - works on desktop and mobile
- ✅ **Zero-config deployment** on Hugging Face Spaces

---

## 🧰 Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **🎨 Frontend** | Streamlit | Interactive web interface |
| **⚙️ Backend** | Python 3.8+ | Core application logic |
| **🤖 AI Engine** | Mistral AI (mistral-small-2501) | Language model processing |
| **🔗 Framework** | LangChain | Conversation management & memory |
| **💾 Memory** | ConversationBufferMemory | Session state management |
| **🎭 Styling** | Custom CSS | Dark theme & animations |

</div>

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Mistral AI API key ([Get it here](https://console.mistral.ai/))
- Git

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/anmoldhiman17/orion-ai-chatbot.git

# Navigate to project directory
cd orion-ai-chatbot

# Install dependencies
pip install -r requirements.txt
```

### 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

> ⚠️ **Security Note:** Never commit your `.env` file to version control!

### ▶️ Run Locally

```bash
# Start the Streamlit app
streamlit run app.py

# Your app will be available at:
# 🌐 Local URL: http://localhost:8501
```

---

## 💬 Usage Example

```plaintext
👤 User: Tell me a joke about programming

🤖 ORION AI (Funny Mode):
Why do programmers prefer dark mode?
Because light attracts bugs! 🐛💡

---

👤 User: *switches to Smart Mode*
👤 User: Explain quantum computing

🤖 ORION AI (Smart Mode):
Quantum computing leverages quantum mechanics principles,
specifically superposition and entanglement, to process
information in ways classical computers cannot...
```

---

## 🏗️ Project Structure

```
orion-ai-chatbot/
│
├── 📄 app.py                 # Main Streamlit application
├── 📄 requirements.txt       # Python dependencies
├── 📄 .env                   # Environment variables (not in repo)
├── 📄 .gitignore            # Git ignore rules
├── 📄 README.md             # This file
│
├── 📁 assets/               # Images and media
│   ├── demo.gif
│   ├── screenshot1.png
│   └── screenshot2.png
│
└── 📁 utils/                # Helper modules (if any)
    └── helpers.py
```

---

## 🌐 Deployment

### Hugging Face Spaces

ORION AI is proudly deployed on **Hugging Face Spaces** with Streamlit runtime:

1. **Fork this repo** to your GitHub account
2. **Create a new Space** on [Hugging Face](https://huggingface.co/spaces)
3. **Select Streamlit** as the SDK
4. **Link your GitHub repo**
5. **Add your `MISTRAL_API_KEY`** in Space secrets
6. **Deploy!** 🚀

> 🔗 **Live Demo:** [https://huggingface.co/spaces/Anmoldhiman17/orion-ai](https://huggingface.co/spaces/Anmoldhiman17/orion-ai)

### Alternative Platforms

- **Streamlit Cloud** - Native Streamlit hosting
- **Railway** - Containerized deployment
- **Render** - Free tier available
- **AWS/GCP/Azure** - Enterprise deployment

---

## 🔮 Future Improvements

<div align="center">

| Feature | Status | Priority |
|---------|--------|----------|
| 🎤 Voice input/output | 📋 Planned | High |
| 🌍 Multi-language support | 📋 Planned | High |
| 💾 Chat history export | 📋 Planned | Medium |
| 🎨 Custom personality creator | 🔄 In Progress | Medium |
| 📊 Analytics dashboard | 📋 Planned | Low |
| 🔌 API endpoint | 📋 Planned | Low |

</div>

**Want to contribute?** Check out our [Contributing Guidelines](#-contributing) below!

---

## 🤝 Contributing

We love contributions! Here's how you can help make ORION AI even better:

1. **🍴 Fork the repository**
2. **🌿 Create your feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **💾 Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **📤 Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **🔀 Open a Pull Request**

### 🐛 Found a Bug?

Open an issue on [GitHub Issues](https://github.com/anmoldhiman17/orion-ai-chatbot/issues) with:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - you're free to use, modify, and distribute this project!
```

---

## 👨‍💻 Author

<div align="center">

### **Anmol Dhiman**

[![GitHub](https://img.shields.io/badge/GitHub-anmoldhiman17-181717?style=for-the-badge&logo=github)](https://github.com/anmoldhiman17)
[![Hugging Face](https://img.shields.io/badge/🤗_Hugging_Face-Anmoldhiman17-FFD21E?style=for-the-badge)](https://huggingface.co/Anmoldhiman17)

</div>

> 💼 **Passionate about AI, ML, and building tools that make a difference**

---

## ⭐ Show Your Support

<div align="center">

### If you like ORION AI, give it a ⭐️ on GitHub!

[![Star on GitHub](https://img.shields.io/github/stars/anmoldhiman17/orion-ai-chatbot?style=social)](https://github.com/anmoldhiman17/orion-ai-chatbot)

**Your star motivates me to keep improving ORION AI! 🚀**

</div>

---

## 🙏 Acknowledgments

- **Mistral AI** for providing the powerful language model
- **LangChain** for the robust conversation framework
- **Streamlit** for the amazing web app framework
- **Hugging Face** for free hosting and community support
- **All contributors** who help improve this project

---

<div align="center">

### 🌟 Built with ❤️ and AI

**ORION AI** - *Where Technology Meets Personality*

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Powered by Mistral](https://img.shields.io/badge/Powered%20by-Mistral%20AI-FF7000?style=for-the-badge)](https://mistral.ai/)

---

**[⬆ Back to Top](#-orion-ai)**

</div></pre>
            </div>
        </div>

        <!-- Info Section -->
        <div class="bg-gradient-to-r from-purple-900 to-indigo-900 rounded-xl p-8 text-center">
            <h3 class="text-2xl font-bold mb-4">✨ README Generated Successfully!</h3>
            <p class="text-lg mb-6">Click the button above to copy the entire README.md content to your clipboard</p>
            <div class="flex gap-4 justify-center flex-wrap">
                <a href="https://github.com/anmoldhiman17/orion-ai-chatbot" target="_blank" class="bg-white text-purple-600 px-6 py-3 rounded-lg font-semibold hover:scale-105 transition transform">
                    🔗 View GitHub Repo
                </a>
                <a href="https://huggingface.co/spaces/Anmoldhiman17/orion-ai" target="_blank" class="bg-yellow-400 text-gray-900 px-6 py-3 rounded-lg font-semibold hover:scale-105 transition transform">
                    🚀 View Live Demo
                </a>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-800 py-8 mt-12">
        <div class="max-w-6xl mx-auto px-6 text-center text-gray-400">
            <p>Made with ❤️ for ORION AI by Anmol Dhiman</p>
            <p class="mt-2">⭐ Star the repo if you find this useful!</p>
        </div>
    </footer>

    <script>
        function copyReadme() {
            const readmeContent = document.getElementById('readme-content').innerText;
            
            navigator.clipboard.writeText(readmeContent).then(() => {
                const buttons = document.querySelectorAll('.copy-btn');
                buttons.forEach(btn => {
                    const originalText = btn.textContent;
                    btn.textContent = '✅ Copied!';
                    btn.classList.add('copied');
                    
                    setTimeout(() => {
                        btn.textContent = originalText;
                        btn.classList.remove('copied');
                    }, 2000);
                });
                
                // Show toast notification
                showToast();
            }).catch(err => {
                alert('Failed to copy. Please select and copy manually.');
                console.error('Copy failed:', err);
            });
        }
        
        function showToast() {
            const toast = document.createElement('div');
            toast.className = 'fixed top-4 right-4 bg-green-500 text-white px-6 py-4 rounded-lg shadow-lg z-50';
            toast.innerHTML = '<strong>✅ Success!</strong> README copied to clipboard!';
            document.body.appendChild(toast);
            
            setTimeout(() => {
                toast.style.transition = 'opacity 0.3s';
                toast.style.opacity = '0';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }
        
        // Add smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    </script>
</body>
</html>
