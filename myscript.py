# ========== IMPORTS ==========
from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from sentence_transformers import SentenceTransformer


from langchain_community.document_loaders import TextLoader

loader = TextLoader("ABOUT_ME.txt")
docs = loader.load()

print("Loaded characters:", len(docs[0].page_content))

print(docs[0].page_content[:200])


splitter=RecursiveCharacterTextSplitter(chunk_size=300,chunk_overlap=50)
chunks=splitter.split_documents(docs)

embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db=FAISS.from_documents(chunks,embeddings)



generator=pipeline("text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct")


# ========== YOUR PERSONAL CONTEXT ==========
BOT_STYLE = """
You are Urvika Singh's personal portfolio chatbot.

IMPORTANT RULES:
- NEVER claim you are Urvika.
- Always talk ABOUT Urvika in third person.
- Use ONLY the information from <CONTEXT>.
- Do NOT guess or assume facts.

STRICT OUTPUT RULES:
- Do NOT show system messages.
- Do NOT show instructions.
- Do NOT show notes.
- Only give the final answer.

Formatting:
- Use bullet points
- Use short, clean sentences
- Break long sentences into multiple lines.

If information is missing, reply exactly:
"I don't have that information in my knowledge base
"""



# ========== MAIN CHAT FUNCTION ==========
def rag_chat(query):
    docs = db.similarity_search(query, k=4)
    context = "\n".join([doc.page_content for doc in docs]) if docs else ""

    prompt = f"""
{BOT_STYLE}

<CONTEXT>
{context}
</CONTEXT>

Question:
{query}

Answer:
"""

    out = generator(
        prompt,
        max_new_tokens=150,
        temperature=0.2,
        return_full_text=False
    )[0]["generated_text"]

    return out.strip()

print("Hi I am Urvika Singh's AI portfolio assistant.")

while True:
    query = input("You: ")

    if query.lower() in ["bye","goodbye","exit"]:
        print("Bot: Bye 👋")
        break

    response = rag_chat(query)
    print("\nBot:", response, "\n")




