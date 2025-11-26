import json

json_data = '''
{
  "vendas": [
    { "vendedor": "João Silva", "valor": 1200.50 },
    { "vendedor": "João Silva", "valor": 950.75 },
    { "vendedor": "João Silva", "valor": 1800.00 },
    { "vendedor": "João Silva", "valor": 1400.30 },
    { "vendedor": "João Silva", "valor": 1100.90 },
    { "vendedor": "João Silva", "valor": 1550.00 },
    { "vendedor": "João Silva", "valor": 1700.80 },
    { "vendedor": "João Silva", "valor": 250.30 },
    { "vendedor": "João Silva", "valor": 480.75 },
    { "vendedor": "João Silva", "valor": 320.40 },
    { "vendedor": "Maria Souza", "valor": 2100.40 },
    { "vendedor": "Maria Souza", "valor": 1350.60 },
    { "vendedor": "Maria Souza", "valor": 950.20 },
    { "vendedor": "Maria Souza", "valor": 1600.75 },
    { "vendedor": "Maria Souza", "valor": 1750.00 },
    { "vendedor": "Maria Souza", "valor": 1450.90 },
    { "vendedor": "Maria Souza", "valor": 400.50 },
    { "vendedor": "Maria Souza", "valor": 180.20 },
    { "vendedor": "Maria Souza", "valor": 90.75 },
    { "vendedor": "Carlos Oliveira", "valor": 800.50 },
    { "vendedor": "Carlos Oliveira", "valor": 1200.00 },
    { "vendedor": "Carlos Oliveira", "valor": 1950.30 },
    { "vendedor": "Carlos Oliveira", "valor": 1750.80 },
    { "vendedor": "Carlos Oliveira", "valor": 1300.60 },
    { "vendedor": "Carlos Oliveira", "valor": 300.40 },
    { "vendedor": "Carlos Oliveira", "valor": 500.00 },
    { "vendedor": "Carlos Oliveira", "valor": 125.75 },
    { "vendedor": "Ana Lima", "valor": 1000.00 },
    { "vendedor": "Ana Lima", "valor": 1100.50 },
    { "vendedor": "Ana Lima", "valor": 1250.75 },
    { "vendedor": "Ana Lima", "valor": 1400.20 },
    { "vendedor": "Ana Lima", "valor": 1550.90 },
    { "vendedor": "Ana Lima", "valor": 1650.00 },
    { "vendedor": "Ana Lima", "valor": 75.30 },
    { "vendedor": "Ana Lima", "valor": 420.90 },
    { "vendedor": "Ana Lima", "valor": 315.40 }
  ]
}
'''

def calcular_comissao(dados):
    data = json.loads(dados)
    resumo_vendedores = {}

    print(f"{'VENDEDOR':<20} | {'VENDA':<10} | {'COMISSÃO':<10} | {'% APLICADO'}")
    print("-" * 60)

    for venda in data['vendas']:
        vendedor = venda['vendedor']
        valor = venda['valor']
        comissao = 0.0
        taxa = "0%"

        
        if valor < 100.00:
            comissao = 0.0
            taxa = "0%"
        elif valor < 500.00:
            comissao = valor * 0.01
            taxa = "1%"
        else:
            comissao = valor * 0.05
            taxa = "5%"

        
        print(f"{vendedor:<20} | R$ {valor:>8.2f} | R$ {comissao:>8.2f} | {taxa}")

        
        if vendedor not in resumo_vendedores:
            resumo_vendedores[vendedor] = {'total_vendas': 0, 'total_comissao': 0}
        
        resumo_vendedores[vendedor]['total_vendas'] += valor
        resumo_vendedores[vendedor]['total_comissao'] += comissao

    print("\n" + "="*40)
    print("RESUMO FINAL POR VENDEDOR")
    print("="*40)
    for nome, dados in resumo_vendedores.items():
        print(f"Vendedor: {nome}")
        print(f"  Total Vendido:   R$ {dados['total_vendas']:.2f}")
        print(f"  Total Comissão:  R$ {dados['total_comissao']:.2f}")
        print("-" * 20)

if __name__ == "__main__":
    calcular_comissao(json_data)
