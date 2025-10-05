import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Knowledge Base
facts = [
    "GlobalMart sells electronics like smartphones, laptops, and tablets.",
    "GlobalMart offers home appliances including refrigerators and washing machines.",
    "GlobalMart has a wide variety of clothing for men, women, and children.",
    "GlobalMart provides fresh groceries including fruits, vegetables, and dairy products.",
    "GlobalMart also offers sports equipment and fitness accessories.",
    "GlobalMart sells books across various genres including fiction, non-fiction, and textbooks."
]

# Load Model & Build Index
@st.cache_resource
def load_model_and_index():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(facts, convert_to_numpy=True)
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return model, index

model, index = load_model_and_index()

# Search Function
def search(query, model, index, facts, top_k=3):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)
    results = [facts[i] for i in indices[0]]
    return results

# Streamlit UI
st.set_page_config(page_title="RAG Vector Search", page_icon="🔎", layout="centered")

st.title("🔎 RAG-based Knowledge Search")
st.write("Ask me anything about **GlobalMart** and I’ll fetch the most relevant facts.")

query = st.text_input("Enter your question:")

if st.button("Search") and query.strip():
    results = search(query, model, index, facts, top_k=3)

    st.subheader("📌 Top Relevant Facts:")
    for r in results:
        st.success(r)


#Footer
st.markdown("""---""")  # separator line
st.markdown("💡 Developed by **Bushra Mubeen **") 