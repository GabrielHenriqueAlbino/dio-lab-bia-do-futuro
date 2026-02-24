# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_adquirir.json` | JSON | Informar quais produtos cliente deseja |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Na base de dados produtos_adquirir foi anexada o valor do carro e da casa o cliente deseja comprar.
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```
- Perfil do investidor (perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}
- Produtos adquirir (produtos_adquirir.json):
[
  {
    "carro": "Honda Civic",
    "versao": "Touring",
    "valor": 265500.00
  },
  {
    "casa": "Casa de Alvenaria",
    "estilo_arquitetonico": "Contemporâneo",
    "valor": 600000.00
  }
 
]
- Transacoes do cliente (transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida
---
````
## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
