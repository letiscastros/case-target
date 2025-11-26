import json
import uuid

estoque_json = '''
{
    "estoque": [
        { "codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150 },
        { "codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75 },
        { "codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200 },
        { "codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320 },
        { "codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90 }
    ]
}
'''

class GestorEstoque:
    def __init__(self, dados_json):
        self.dados = json.loads(dados_json)
        self.historico_movimentacoes = []

    def buscar_produto(self, codigo):
        for produto in self.dados['estoque']:
            if produto['codigoProduto'] == codigo:
                return produto
        return None

    def lancar_movimentacao(self, codigo_produto, tipo, quantidade, descricao_mov):
        """
        Lança uma movimentação de estoque.
        tipo: 'entrada' ou 'saida'
        """
        produto = self.buscar_produto(codigo_produto)
        
        if not produto:
            return f"Erro: Produto código {codigo_produto} não encontrado."

        if quantidade <= 0:
            return "Erro: A quantidade deve ser maior que zero."


        if tipo.lower() == 'saida':
            if produto['estoque'] < quantidade:
                return f"Erro: Estoque insuficiente. Atual: {produto['estoque']}"
            produto['estoque'] -= quantidade
        elif tipo.lower() == 'entrada':
            produto['estoque'] += quantidade
        else:
            return "Erro: Tipo de movimentação inválida (use 'entrada' ou 'saida')."

        
        registro = {
            "id_transacao": str(uuid.uuid4()), 
            "codigo_produto": codigo_produto,
            "produto": produto['descricaoProduto'],
            "tipo": tipo,
            "quantidade": quantidade,
            "descricao": descricao_mov,
            "estoque_final": produto['estoque']
        }
        
        self.historico_movimentacoes.append(registro)
        
        return registro

    def exibir_estoque_atual(self):
        print("\n--- ESTOQUE ATUAL ---")
        for p in self.dados['estoque']:
            print(f"[{p['codigoProduto']}] {p['descricaoProduto']}: {p['estoque']} un.")


gestor = GestorEstoque(estoque_json)


print("Situação Inicial:")
gestor.exibir_estoque_atual()

print("\n--- Realizando Movimentações ---")


resultado1 = gestor.lancar_movimentacao(101, "entrada", 50, "Reposição de fornecedor")
print(f"Movimentação 1: {resultado1}")


resultado2 = gestor.lancar_movimentacao(102, "saida", 10, "Venda para cliente A")
print(f"Movimentação 2: {resultado2}")


resultado3 = gestor.lancar_movimentacao(105, "saida", 500, "Erro de digitação")
print(f"Movimentação 3: {resultado3}")

print("\nSituação Final:")
gestor.exibir_estoque_atual()
