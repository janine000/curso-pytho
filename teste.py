class Carro:
    def __init__(self, modelo, cor, valor, ano):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.ano = ano

    def calcular_valor_com_desconto(self, percentual_desconto):
        """"""
        desconto = (percentual_desconto / 100) * self.valor
        valor_com_desconto = self.valor - desconto
        return valor_com_desconto

    def calcular_valor_parcelado(self, numero_parcelas):
        """
        Calcula o valor de cada parcela para um pagamento parcelado.

        :param numero_parcelas: Número de parcelas para o pagamento.
        :return: Valor de cada parcela.
        """
        if numero_parcelas <= 0:
            raise ValueError("O número de parcelas deve ser maior que zero.")
        valor_parcelado = self.valor / numero_parcelas
        return valor_parcelado

# Exemplo de uso da classe Carro:
carro = Carro(modelo="Fusca", cor="azul", valor=30000, ano=2024)

# Calculando o valor com desconto
valor_com_desconto = carro.calcular_valor_com_desconto(20)
print(f"Valor com 20% de desconto: R${valor_com_desconto:.2f}")

# Calculando o valor parcelado em 12 vezes
valor_parcelado = carro.calcular_valor_parcelado(12)
print(f"Valor de cada parcela (12x): R${valor_parcelado:.2f}")
