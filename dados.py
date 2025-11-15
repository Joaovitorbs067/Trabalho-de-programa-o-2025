# Base de dados (dicionário) com os traços de referência

TRACOS = {
    "concreto_magro": {
        "descricao": "Concreto Magro (para lastro/regularização)",
        "cimento_kg_m3": 130.0,
        "areia_m3_m3": 0.65,
        "brita_m3_m3": 0.85,
        "cal_kg_m3": 0.0,
        "agua_litros_m3": 160.0,
    },
    "concreto_c15": {
        "descricao": "Concreto C15 (ex: calçadas, contrapisos)",
        "cimento_kg_m3": 240.0,
        "areia_m3_m3": 0.60,
        "brita_m3_m3": 0.80,
        "cal_kg_m3": 0.0,
        "agua_litros_m3": 170.0,
    },
    "concreto_c25": {
        "descricao": "Concreto C25 (ex: vigas, pilares, lajes)",
        "cimento_kg_m3": 320.0,
        "areia_m3_m3": 0.55,
        "brita_m3_m3": 0.75,
        "cal_kg_m3": 0.0,
        "agua_litros_m3": 175.0,
    },
    "concreto_c30": {
        "descricao": "Concreto C30 (ex: estruturas de alta solicitação)",
        "cimento_kg_m3": 360.0,
        "areia_m3_m3": 0.50,
        "brita_m3_m3": 0.70,
        "cal_kg_m3": 0.0,
        "agua_litros_m3": 180.0,
    },
    "argamassa_chapisco": {
        "descricao": "Argamassa para Chapisco (Traço 1:3 volumétrico)",
        "cimento_kg_m3": 400.0,
        "areia_m3_m3": 1.0,
        "brita_m3_m3": 0.0,
        "cal_kg_m3": 0.0,
        "agua_litros_m3": 220.0,
    },
    "argamassa_assentamento": {
        "descricao": "Argamassa de Assentamento (Traço 1:2:8 volumétrico, cimento:cal:areia)",
        "cimento_kg_m3": 180.0,
        "areia_m3_m3": 0.95,
        "brita_m3_m3": 0.0,
        "cal_kg_m3": 90.0,
        "agua_litros_m3": 200.0,
    },
    "argamassa_reboco_interno": {
        "descricao": "Argamassa de Reboco Interno (Traço recomendado 1:1:6 volumétrico)",
        "cimento_kg_m3": 210.0,
        "areia_m3_m3": 1.00,
        "brita_m3_m3": 0.0,
        "cal_kg_m3": 160.0,
        "agua_litros_m3": 200.0,
    },
}


# dados auxiliares para conversão
DADOS_AUXILIARES = {"peso_saco_cimento_kg": 50.0, "peso_saco_cal_kg": 20.0}
