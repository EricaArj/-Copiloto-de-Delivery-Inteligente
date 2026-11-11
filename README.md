

# 🤖 Copiloto de Delivery Inteligente (RAG + LLM)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-000000?style=for-the-badge&logo=chainlink)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-orange?style=for-the-badge)
![Gemini AI](https://img.shields.io/badge/Google_Gemini-2.5_Flash-4285F4?style=for-the-badge&logo=google)

Um agente conversacional de alta performance e hiper-personalizado projetado para solucionar o problema prático de escolha de refeições em plataformas de delivery (como o iFood). 

O projeto aplica uma **arquitetura híbrida de RAG (Retrieval-Augmented Generation)**, unindo a velocidade da **busca semântica em base de dados vetorial** com a flexibilidade de raciocínio de um **Modelo de Linguagem (LLM)**.

---

## 📌 Principais Recursos

- 🔍 **Busca Semântica por Contexto:** Compreende intenções subjetivas como *"dia quente"*, *"comida leve"* ou *"algo para a noite"* via embeddings vetoriais.
- 🎯 **Filtros e Restrições Alimentares:** Considera restrições (ex: sem lactose, vegetariano), horário e orçamento máximo do usuário.
- 💬 **Interface Conversacional em Linguagem Natural:** Traduz a dúvida do cliente em recomendações claras e justificadas.
- 🚀 **Arquitetura Leve e Escalável:** Utiliza armazenamento de vetores em memória com o ChromaDB e conexões via API otimizadas.

---

## 🏗️ Arquitetura do Sistema

```text
  [ Usuário / Prompt ] 
           │
           ▼
  [ Contexto & Pedido em Linguagem Natural ]
           │
           ├───► [ 1. Embeddings (Google Text-Embedding-004) ]
           │              │
           │              ▼
           │     [ 2. Busca Semântica no ChromaDB ]
           │              │
           └──────────────┼──────────────┐
                          ▼              ▼
           [ 3. Pratos Relevantes Recuperados ]
                          │
                          ▼
        [ 4. LLM (Gemini 2.5 Flash + Prompt Engineering) ]
                          │
                          ▼
            [ Recomendação Personalizada ]
```

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Função |
| :--- | :--- | :--- |
| **Lógica do Agente** | **Python** + **LangChain** | Orquestração do pipeline, gestão de contexto e engenharia de prompts. |
| **Base Vetorial** | **ChromaDB** | Armazenamento de vetores em memória para busca semântica veloz. |
| **Embeddings** | **Google Text-Embedding-004** | Vetorização de textos e tags dos pratos. |
| **Modelo de IA** | **Google Gemini 2.5 Flash** | Processamento de linguagem natural e geração da resposta final. |

---

## 📁 Estrutura do Repositório

```text
copiloto-delivery/
├── data/
│   └── cardapio.json       # Base de dados simulada de pratos e restaurantes
├── vector_store.py          # Processamento, embeddings e indexação vetorial
├── main.py                  # Agente principal, prompt template e orquestração
├── .env.example             # Modelo para configuração das chaves de API
├── requirements.txt         # Dependências de bibliotecas Python
└── README.md                # Documentação do projeto
```

---

## ⚙️ Como Executar o Projeto

### Pró-requisitos
- **Python 3.10+** instalado.
- Uma chave de API do **Google Gemini** ([Obter chave no Google AI Studio](https://aistudio.google.com/)).

### Passo a Passo

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/seu-usuario/copiloto-delivery.git
   cd copiloto-delivery
   ```

2. **Instalar as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar as Variáveis de Ambiente:**
   Crie um arquivo `.env` na raiz do projeto (com base no `.env.example`):
   ```env
   GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
   ```

4. **Executar a Aplicação:**
   ```bash
   python main.py
   ```

---


## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
