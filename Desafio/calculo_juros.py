from datetime import datetime

def calcular_divida_atualizada():
    print("CÁLCULO DE JUROS POR ATRASO")
    
    try:
        
        valor_original = float(input("Digite o valor original do título (R$): "))
        data_vencimento_str = input("Digite a data de vencimento (DD/MM/AAAA): ")
        
    
        data_vencimento = datetime.strptime(data_vencimento_str, "%d/%m/%Y")
        hoje = datetime.now()
        
       
        diferenca = hoje - data_vencimento
        dias_atraso = diferenca.days
        
        if dias_atraso <= 0:
            print("\nO título não está vencido. Não há juros a calcular.")
        else:
            # Regra: 2,5% ao dia (Juros Simples)
            # J = P * i * n
            taxa_diaria_percentual = 2.5
            taxa_decimal = taxa_diaria_percentual / 100
            
            valor_juros = valor_original * taxa_decimal * dias_atraso
            valor_total = valor_original + valor_juros
            
            print("\nRESULTADO")
            print(f"Data Atual: {hoje.strftime('%d/%m/%Y')}")
            print(f"Dias de atraso: {dias_atraso} dias")
            print(f"Taxa de juros: {taxa_diaria_percentual}% ao dia")
            print("-" * 30)
            print(f"Valor Original: R$ {valor_original:.2f}")
            print(f"Valor dos Juros: R$ {valor_juros:.2f}")
            print(f"TOTAL A PAGAR:  R$ {valor_total:.2f}")
            
    except ValueError:
        print("Erro: Certifique-se de digitar o valor com ponto (ex: 100.50) e a data no formato correto.")

if __name__ == "__main__":
    calcular_divida_atualizada()
