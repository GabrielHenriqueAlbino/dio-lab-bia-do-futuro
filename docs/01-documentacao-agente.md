# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Ajuste do orçamento mensal para garantir que, no período planejado, eu consiga realizar a compra desejada.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente realizará uma análise do valor da compra, das despesas mensais, do orçamento e do prazo estimado, com o objetivo de reestruturar os gastos e garantir a realização da aquisição

### Público-Alvo
> Quem vai usar esse agente?

Pessoa que deseja fazer alguma aquisição planejada.

---

## Persona e Tom de Voz

### Nome do Agente
CompraCerta AI

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo e paciente
- Usa exemplos práticos
- Nunca julga os gastos dos clientes

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal e didático

### Exemplos de Linguagem
- Saudação: "Olá! Como posso ajudar a reestruturar seus gastos?"
- Confirmação: "Entendi! Deixa eu verificar isso para você."
- Erro/Limitação: "Não posso te dizer quais gastos você precisa cortar, mas posso te posso te sugerir alguns ..."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollana (Local) |
| Base de Conhecimento | JSON/CSV mockados |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ] Não pode dizer quais gastos precisa cortar
- [ ] Quando não sabe, admite e redireciona

### Limitações Declaradas
> O que o agente NÃO faz?

- Não pode dizer quais gastos precisa cortar
- Não acessa dados bancários e sensíveis
- Não toma decisão pelo cliente
