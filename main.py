# Arquivo: main.py
# Programa principal que controla o menu e chama as funções.

import funcoes  # Importa nosso arquivo de funções


def menu_principal():
    """
    Função principal que roda o menu.
    Usa um LOOP (while True) para continuar rodando até o usuário sair.
    """

    # Bloco try-except para evitar que o programa quebre
    # se o usuário digitar texto onde deveria ser um número.
    try:
        while True:
            print("\n=====  CALCULADORA DE TRAÇO DE CONCRETO/ARGAMASSA =====")
            print("1. Ver traços disponíveis")
            print("2. Calcular materiais para um traço")
            print("0. Sair do programa")

            escolha = input("Digite sua opção: ")

            # --- Opção 1: Ver Traços ---
            if escolha == "1":
                funcoes.mostrar_tracos_disponiveis()

            # --- Opção 2: Calcular ---
            elif escolha == "2":
                print("\nVamos calcular os materiais...")
                funcoes.mostrar_tracos_disponiveis()  # Mostra as opções

                traco_escolhido = (
                    input("Digite o NOME do traço (ex: concreto_c25): ").strip().lower()
                )
                volume_desejado = float(
                    input("Digite o volume total em m³ (ex: 2.5): ")
                )

                # --- Passo 1: Calcular totais em kg/m³ ---
                resultado_base = funcoes.calcular_materiais_base(
                    traco_escolhido, volume_desejado
                )

                if resultado_base is None:
                    print(f"Erro: O traço '{traco_escolhido}' não foi encontrado.")
                else:
                    # --- Passo 2: Converter para unidades de compra (sacos) ---
                    resultado_final = funcoes.calcular_unidades_compra(resultado_base)

                    # --- Passo 3: Mostrar o resultado ---
                    print("\n" + "--- 💰 ORÇAMENTO DE MATERIAIS ---")
                    print(f"Para {volume_desejado} m³ de '{traco_escolhido}':\n")

                    # Imprime Cimento (se existir no resultado)
                    if "cimento_sacos" in resultado_final:
                        print(f"  Cimento: {resultado_final['cimento_sacos']} saco(s)")
                        print(
                            f"     (Total exato: {resultado_final['cimento_kg_total']:.2f} kg)"
                        )

                    # Imprime Cal (se existir no resultado)
                    if "cal_sacos" in resultado_final:
                        print(f"  Cal: {resultado_final['cal_sacos']} saco(s)")
                        print(
                            f"     (Total exato: {resultado_final['cal_kg_total']:.2f} kg)"
                        )

                    # Imprime Areia (se for maior que zero)
                    if resultado_final.get("areia_m3_total", 0) > 0:
                        print(f"  Areia: {resultado_final['areia_m3_total']:.2f} m³")

                    # Imprime Brita (se for maior que zero)
                    if resultado_final.get("brita_m3_total", 0) > 0:
                        print(f"  Brita: {resultado_final['brita_m3_total']:.2f} m³")

                    if resultado_final.get("agua_litros_total", 0) > 0:
                        print(
                            f"  Água: {resultado_final['agua_litros_total']:.2f} Litros (valor aprox.)"
                        )
                    print("------------------------------------")

            # --- Opção 0: Sair ---
            elif escolha == "0":
                print("Saindo... Bom trabalho!")
                break

            else:
                print("Opção inválida! Por favor, escolha 1, 2 ou 0.")

    except ValueError:
        print("\nErro! Você digitou um valor não numérico para o volume.")
        print("Reiniciando o programa...")
        menu_principal()  # Reinicia o menu
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


# --- Esta é a linha que inicia o programa ---
if __name__ == "__main__":
    menu_principal()
