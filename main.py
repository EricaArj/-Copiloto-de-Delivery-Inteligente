import os
from dotenv import load_dotenv
from vector_store import inicializar_banco_vetorial
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def executar_copiloto():
    print("🤖 Inicializando o Agente Copiloto de Delivery...")
    
    vectorstore = inicializar_banco_vetorial()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

    prompt = ChatPromptTemplate.from_template("""
Você é o Copiloto de Delivery Inteligente do iFood. Sua missão é recomendar as melhores opções de refeição com base no perfil, contexto e opções disponíveis no cardápio.

**Contexto do Usuário:**
{contexto_usuario}

**Opções encontradas no Cardápio:**
{opcoes_cardapio}

**Instruções:**
1. Analise o contexto do usuário (orçamento, clima, restrições alimentares, momento do dia).
2. Apresente as opções que melhor atendem ao pedido explicando o PORQUÊ da recomendação.
3. Seja amigável, direto e mencione o preço e o nome do restaurante.

**Sua Recomendação:**
""")

    contexto_usuario = """
    - Horário: 13:00 (Almoço)
    - Clima: Dia quente e ensolarado
    - Restrição/Preferência: Quer algo leve e sem lactose
    - Orçamento máximo: R$ 50,00
    - Pedido em linguagem natural: "Tô querendo comer algo bem leve no almoço hoje porque tá muito quente, mas não posso com lactose."
    """

    print("\n🔍 Buscando as melhores opções no banco vetorial...")
    docs_relevantes = retriever.invoke("prato leve almoço dia quente sem lactose")
    opcoes_formatadas = "\n\n".join([doc.page_content for doc in docs_relevantes])

    chain = prompt | llm
    resposta = chain.invoke({
        "contexto_usuario": contexto_usuario,
        "opcoes_cardapio": opcoes_formatadas
    })

    print("\n---------------- RESULTADO DO AGENTE ----------------")
    print(resposta.content)
    print("-----------------------------------------------------")

if __name__ == "__main__":
    executar_copiloto()
