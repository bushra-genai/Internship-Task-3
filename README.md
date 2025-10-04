# Internship-Task-3

🔎 RAG-based Knowledge Search — GlobalMart AI Assistant

An intelligent RAG (Retrieval-Augmented Generation) mini-project built using Streamlit, FAISS, and Sentence Transformers.
This app allows users to ask natural-language questions about GlobalMart, and it retrieves the most relevant information from its knowledge base using vector embeddings.

🚀 Key Features

✅ RAG-powered Search — Uses embeddings to find the most semantically relevant facts.
✅ FAISS Vector Indexing — Enables fast and accurate similarity search.
✅ Sentence Transformers Model — Encodes both questions and facts into dense embeddings.
✅ Streamlit Interface — Clean and interactive web app for instant Q&A.
✅ Lightweight & Fast — Runs locally with minimal setup, no external APIs required.

🧠 How It Works

A small knowledge base of GlobalMart facts is defined in Python.

The SentenceTransformer model (all-MiniLM-L6-v2) converts all facts into vector embeddings.

These embeddings are stored in a FAISS index for quick similarity search.

When a user enters a query, it’s encoded and compared to all facts.

The top 3 most relevant results are shown on screen.

🖼️ App Interface
🔎 RAG-based Knowledge Search
Ask me anything about GlobalMart and I’ll fetch the most relevant facts.

📌 Top Relevant Facts:
✅ GlobalMart sells electronics like smartphones, laptops, and tablets.
✅ GlobalMart offers home appliances including refrigerators and washing machines.
✅ GlobalMart provides fresh groceries including fruits, vegetables, and dairy products.

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/bushra-genai/Internship-Task-3
cd globalmart-rag

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the App
streamlit run app.py

📁 Project Structure
globalmart-rag/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Required dependencies
├── README.md             # Project documentation

🧩 Requirements File Example

Here’s what your requirements.txt may look like:

streamlit
sentence-transformers
faiss-cpu
numpy

🧪 Example Queries

Try asking:

“What kind of products does GlobalMart sell?”

“Does GlobalMart offer home appliances?”

“Tell me about books in GlobalMart.”

“What sports items can I buy from GlobalMart?”

👩‍💻 Developed By

Bushra Mubeen
💼 AI & Machine Learning Developer
🌐 LinkedIn Profile
 (https://www.linkedin.com/in/bushra-ai)
📧 bushrasarwar589@gmail.com

🪪 License

This project is licensed under the MIT License — you’re free to use, modify, and share it with attribution.
