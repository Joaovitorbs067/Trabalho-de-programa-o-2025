# Arquivo: funcoes.py
# cálculos do nosso programa.

import dados  # Importa nosso dicionário
import math  # Importa a biblioteca de matemática para arredondar


def mostrar_tracos_disponiveis():
    """
    Usa um LOOP (for) para ler o dicionário em 'dados.py'
    e mostrar as opções para o usuário de forma organizada.
    """
    print("\n--- Traços Disponíveis ---")

    for chave, valor in dados.TRACOS.items():
        print(f"Nome: {chave}")
        print(f"   Descrição: {valor['descricao']}")

    print("----------------------------")


def calcular_materiais_base(traco_nome, volume_m3):
    """
    Recebe o nome do traço e o volume, faz o cálculo
    e retorna um dicionário com os totais em kg e m³.
    """

    if traco_nome not in dados.TRACOS:
        return None

    receita_base = dados.TRACOS[traco_nome]

    resultados_base = {}

    # O uso de .get(chave, 0) garante que, se um material não
    # existir no traço (ex: 'cal' no concreto), ele usa 0 e não dá erro.
    resultados_base["cimento_kg_total"] = (
        receita_base.get("cimento_kg_m3", 0) * volume_m3
    )
    resultados_base["areia_m3_total"] = receita_base.get("areia_m3_m3", 0) * volume_m3
    resultados_base["brita_m3_total"] = receita_base.get("brita_m3_m3", 0) * volume_m3
    resultados_base["cal_kg_total"] = receita_base.get("cal_kg_m3", 0) * volume_m3
    resultados_base["agua_litros_total"] = (
        receita_base.get("agua_litros_m3", 0) * volume_m3
    )

    return resultados_base


def calcular_unidades_compra(resultados_base):
    """
    NOVA FUNÇÃO: Converte os resultados de kg/m3 para
    unidades de compra (sacos), arredondando para cima.
    """
    unidades_finais = {}

    # Pega os pesos dos sacos do arquivo de dados
    peso_saco_cimento = dados.DADOS_AUXILIARES["peso_saco_cimento_kg"]
    peso_saco_cal = dados.DADOS_AUXILIARES["peso_saco_cal_kg"]

    # Copia valores que não mudam (m³ e litros)
    unidades_finais["areia_m3_total"] = resultados_base.get("areia_m3_total", 0)
    unidades_finais["brita_m3_total"] = resultados_base.get("brita_m3_total", 0)
    unidades_finais["agua_litros_total"] = resultados_base.get("agua_litros_total", 0)

    # Converte Cimento (kg -> sacos)
    kg_cimento = resultados_base.get("cimento_kg_total", 0)
    if kg_cimento > 0:
        # math.ceil() arredonda para o próximo número inteiro
        unidades_finais["cimento_sacos"] = math.ceil(kg_cimento / peso_saco_cimento)
        unidades_finais["cimento_kg_total"] = kg_cimento  # Mantém o kg para informação

    # Converte Cal (kg -> sacos)
    kg_cal = resultados_base.get("cal_kg_total", 0)
    if kg_cal > 0:
        unidades_finais["cal_sacos"] = math.ceil(kg_cal / peso_saco_cal)
        unidades_finais["cal_kg_total"] = kg_cal  # Mantém o kg para informação

    return unidades_finais
