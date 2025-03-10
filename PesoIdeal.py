import math
import streamlit as st

# Função para calcular o IMC
def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.

    :param peso: Peso da pessoa em quilogramas (kg)
    :param altura: Altura da pessoa em metros (m)
    :return: Valor do IMC
    """
    imc = peso / math.pow(altura, 2)  # Fórmula do IMC: peso / (altura * altura)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    """
    Classifica o IMC em categorias de acordo com a tabela padrão.

    :param imc: Valor do IMC calculado
    :return: Classificação do IMC
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

# Função para ajustar o IMC com base no sexo
def ajustar_imc_por_sexo(imc, sexo):
    """
    Faz um ajuste no IMC considerando diferenças entre homens e mulheres.
    Mulheres tendem a ter um percentual de gordura maior, então o IMC pode ser levemente ajustado.
    """
    if sexo.lower() == "feminino":
        return imc * 0.95  # Ajuste de -5% no IMC para mulheres
    elif sexo.lower() == "masculino":
        return imc * 1.05  # Ajuste de +5% no IMC para homens
    return imc  # Sem alteração se a entrada for inválida

# Função para calcular o peso ideal
def calcular_peso_ideal(altura, sexo):
    """
    Calcula o peso ideal com base na altura e no sexo da pessoa.

    :param altura: Altura da pessoa em metros (m)
    :param sexo: Sexo da pessoa (Masculino/Feminino)
    :return: Peso ideal em quilogramas (kg)
    """
    if sexo.lower() == "masculino":
        # Fórmula para homens: 50 + 0.91 * (altura em cm - 152.4)
        peso_ideal = 50 + 0.91 * ((altura * 100) - 152.4)
    elif sexo.lower() == "feminino":
        # Fórmula para mulheres: 45.5 + 0.91 * (altura em cm - 152.4)
        peso_ideal = 45.5 + 0.91 * ((altura * 100) - 152.4)
    else:
        return None  # Retorna None se o sexo não for válido
    return peso_ideal

# Interface do Streamlit
def main():
    st.title("Calculadora de Índice de Massa Corporal (IMC)")

    # Entrada de dados
    peso = st.number_input("Digite o seu peso em kg:", min_value=0.1, value=70.0, step=0.1)
    altura = st.number_input("Digite a sua altura em metros:", min_value=0.1, value=1.70, step=0.01)
    sexo = st.selectbox("Selecione o seu sexo:", ["Masculino", "Feminino"])

    # Botão para calcular
    if st.button("Calcular IMC e Peso Ideal"):
        if peso <= 0 or altura <= 0:
            st.error("Erro: O peso e a altura devem ser valores positivos.")
        else:
            imc = calcular_imc(peso, altura)
            imc_ajustado = ajustar_imc_por_sexo(imc, sexo)
            classificacao = classificar_imc(imc_ajustado)
            peso_ideal = calcular_peso_ideal(altura, sexo)

            # Exibe os resultados
            st.write(f"Seu IMC ajustado é: **{imc_ajustado:.2f}**")
            st.write(f"Classificação: **{classificacao}**")
            if peso_ideal is not None:
                st.write(f"Seu peso ideal é: **{peso_ideal:.2f} kg**")
            else:
                st.write("Sexo inválido. Não foi possível calcular o peso ideal.")

if __name__ == "__main__":
    main()