# 🤖✨ Smart Assistant for Research Summarization

An AI-powered interactive assistant that helps you **summarize, understand, and evaluate** research papers or any PDF/TXT documents. Built with **Streamlit**, this tool leverages state-of-the-art NLP models to extract key insights, generate answers, challenge users with questions, and evaluate the quality of responses.

---

## 🔍 Features

- 📄 Upload PDF/TXT documents  
- 📝 Summarize long texts using advanced NLP techniques  
- ❓ Ask questions and receive contextual answers  
- 🧠 Challenge Mode: Test your comprehension with AI-generated questions  
- 📊 Evaluate model vs ground truth answers with semantic scoring (F1, BERTScore, SBERT, etc.)  
- 🎨 Beautiful, animated UI with assistant illustration, sidebar steps, and glowing elements

---

## 🖼️ UI Preview


<img width="1902" height="1025" alt="Screenshot 2025-07-13 222333" src="https://github.com/user-attachments/assets/3433472f-ffca-47a2-a847-b5a9cff24dd8" />


---

## 🚀 Technologies Used

- **Streamlit** – Interactive Python Web App Framework  
- **Sentence-BERT** – Semantic similarity for answer evaluation  
- **Transformers (Hugging Face)** – For summarization & QA models  
- **Python** – Core logic and module design  
- **Custom CSS/HTML** – Modern UI/UX layout and effects

---

## 📁 Project Structure

smart-assistant/
│
├── app.py                    # Main Streamlit app                     
│
├── UI/
│   ├── styles.css            # Custom UI styling
│   └── assistant.html        # Animated assistant graphic
│
├── modules/                  # Core logic modules
│   ├── document_loader.py       # Handles PDF/TXT reading
│   ├── summarizer.py            # Generates summaries
│   ├── question_answering.py    # Answers questions using LLMs
│   ├── challenge_mode.py        # Challenge questions generation & checking
│   └── evaluate_response.py     # Model vs ground-truth comparison
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── screenshots/             # UI images (optional)



---

## 🛠️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/jauwaad0786/Smart-Assistant-for-Research-Summarization.git
cd Smart-Assistant-for-Research-Summarization

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py

🧩 Upcoming Enhancements
🔗 Chat-like interface with conversation history

🌍 Multilingual support

📚 Memory-based learning model

🧠 GPT-style interactive tutor

📥 Google Drive & Notion integrations

📊 Analytics dashboard

🤝 Contributing
Contributions are welcome!
Feel free to fork the repo, create a feature branch, and submit a pull request.

📧 Contact
Jauwaad Bin Irshad
📫 Email: shaikhjauwaad@gmail.com
🔗 GitHub: @jauwaad0786
