import json
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

load_dotenv()

def inicializar_banco_vetorial():
    with open("data/cardapio.json", "r", encoding="utf-8") as f:
        pratos = json.load(f)

    documentos = []
    for item in pratos:
        conteudo = f"Prato: {item['nome']} | Restaurante: {item['restaurante']} | Categoria: {item['categoria']} | Preço: R${item['preco']} | Descrição: {item['descricao']} | Tags: {', '.join(item['tags'])}"
        metadata = {
            "id": item["id"],
            "nome": item["nome"],
            "preco": item["preco"],
            "restaurante": item["restaurante"]
        }
        documentos.append(Document(page_content=conteudo, metadata=metadata))

    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    vectorstore = Chroma.from_documents(
        documents=documentos,
        embedding=embeddings,
        collection_name="cardapio_delivery"
    )
    
    return vectorstore

if __name__ == "__main__":
    db = inicializar_banco_vetorial()
    print("✅ Banco de dados vetorial inicializado com sucesso!")
