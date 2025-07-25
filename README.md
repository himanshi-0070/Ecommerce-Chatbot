# Ecommerce-Chatbot

A **Retrieval-Augmented Generation (RAG) chatbot** built in Python that leverages OpenAI’s GPT-3.5-turbo model to provide intelligent responses to customer queries. The chatbot retrieves relevant data from your CSV files to ground its answers in real business information.

---

## 🚀 Features

- **Retrieval-Augmented Generation:** Combines LLM power with contextual data from CSVs.
- **OpenAI GPT-3.5-turbo Integration:** Uses state-of-the-art natural language processing.
- **Secure API Key Management:** Credentials stored safely in a `.env` file.
- **Modular Design:** Clean separation between data retrieval and LLM interaction.
- **CLI Testing:** Easily test chatbot responses using `test_rag.py`.

---

## 📁 Project Structure

```
openai_rag_chatbot/
│
├── __pycache__/                       # Python bytecode cache
├── data/                              # (If used) Directory for any additional data files
├── Order_Data_Dataset (1).csv         # Order data (example file, add your own)
├── Product_Information_Dataset (1).csv# Product data (example file, add your own)
├── embeddings/                        # (If used) Directory for storing embeddings
├── llm/                               # (If used) Directory for LLM-related resources
├── llm_wrapper.py                     # Handles OpenAI API communication
├── rag/                               # (If used) Directory for RAG components
├── README.md                          # This file
├── config.py                          # Configuration management
├── requirements.txt                   # Python dependencies
└── test_rag.py                        # CLI interface for testing chatbot
```

---

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/himanshi-0070/Ecommerce-Chatbot.git
   cd Ecommerce-Chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** Ensure `openai` and `python-dotenv` are included in `requirements.txt`.

3. **Add your OpenAI API key:**
   - Create a `.env` file in the root directory.
   - Add your key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

4. **Prepare your CSV files:**
   - Place your `Product_Information_Dataset (1).csv` and `Order_Data_Dataset (1).csv` in the root directory.
   - Ensure they follow the required format (customize as needed).

---

## ⚙️ Dependencies

- Python 3.8+
- [openai](https://pypi.org/project/openai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- (Optional) pandas (if used in your CSV handling)

Install with:
```bash
pip install openai python-dotenv pandas
```

---

## 🚦 Usage Example

Test the chatbot via CLI:

```bash
python test_rag.py
```

You’ll be prompted to enter your question. The chatbot will:

1. Retrieve relevant info from `Product_Information_Dataset (1).csv` and `Order_Data_Dataset (1).csv`.
2. Build a context-aware prompt.
3. Query OpenAI’s API via `llm_wrapper.py`.
4. Display the answer.

**Example interaction:**
```
> What is the status of order #12345?
Bot: Order #12345 for product "Wireless Mouse" was shipped on 2025-07-20 and is currently in transit.
```

---

## 📈 Future Improvements

- Add web or chat UI (e.g., Streamlit, Flask, or Telegram bot integration)
- Support more data sources (e.g., databases or APIs)
- User authentication and session management
- Enhanced logging and error handling
- Multi-turn conversation support
- More advanced retrieval (e.g., vector search, semantic similarity)

---

## 📝 License

MIT License

---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.

---
