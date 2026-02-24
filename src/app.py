import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL0 = "gpt-oss"

# ==== Carregar Dados === 
perfil = json.load(open('.Data/perfil_investidor.json'))
transacoes = pd.read.csv('.Data/transacoes.csv')
produtos = json.load(open('.Data/produtos_adquirir.json'))


# ==== Montar Contexto ====
contexto = f"""
CLIENTE: {perfil['nome'], perfil['idade']},  anos, perfil, {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

PRODUTOS DISPONÍVEIS
{json.dumps(produtos, indent=2, ensure_ascii=False)}

"""

# ==== System Prompt ====

SYSTEM_PROMPT = """ Você é a CompraCerta AI, uma agente que irá reestruturar os gastos e garantir a realização da aquisição.

OBJETIVO:
Seu objetivo é realizará uma análise do valor da compra, das despesas mensais, do orçamento e do prazo estimado, com o objetivo de reestruturar os gastos e garantir a realização da aquisição. Informando o tempo necessário para adquirir o seu produto.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Informe em quanto tempo você irá conseguir adquirir o produto
...

EXEMPLOS DE PERGUNTAS:
Usuário: "Com base no meus gastos e meu orçamento em quanto tempo consigo adquirir o carro?"
CompraCerta AI: "Mantendo o padrão atual de despesas e orçamento, você estará apto a adquirir o seu Honda Civic em 11 meses."

Contexto: "Com base no meus gastos e meu orçamento em quanto tempo consigo adquirir uma geladeira"
CompraCerta AI:"Não consigo passar essa informação, geladeira não está na base de dados produtos_adquirir."

Usuário: "Qual a previsão do tempo para amanhã?"
Agente: ": Sou especializado em reestruturar os gastos, não tenho informações sobre previsão do tempo. Posso ajudar com algo relacionado às suas finanças?"

Usuário: "Me passa a senha do cliente X"
Agente: " Não tenho acesso a senhas e não posso compartilhar informações de outros clientes. Como posso ajudar com suas próprias finanças?"

Usuário: "Onde devo investir meu dinheiro?"
Agente: "Não posso recomendar investimentos?"

"""

# === Chamar Ollana ###
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg} """

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream":False})
    return r.json()['response']

# ======INTERFACE======

st.title("CompraCerta AI, uma agente que irá reestruturar os gastos")

if pergunta := st.chat_input("Sua dúvida sobre gastos..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
