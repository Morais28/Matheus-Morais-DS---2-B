#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import unicodedata
from pathlib import Path

ARQUIVO_RANKING = Path("forca_ranking.json")

FORCA_DESENHOS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
]

CATEGORIAS = {
    "Animais": [
        "tucano", "onça-pintada", "tamanduá", "capivara", "boto-cor-de-rosa",
        "arara-azul", "jabuti", "lobo-guará", "mico-leão-dourado", "sucuri"
    ],
    "Frutas": [
        "açaí", "cupuaçu", "cajá", "caju", "carambola", "graviola",
        "jabuticaba", "pitanga", "seriguela", "maracujá"
    ],
    "Tecnologia": [
        "algoritmo", "firewall", "roteador", "banco de dados", "interface",
        "compilador", "python", "variável", "função", "recursão"
    ],
    "Países": [
        "brasil", "portugal", "argentina", "paraguai", "uruguai",
        "angola", "moçambique", "espanha", "frança", "itália"
    ],
}

def normalizar(txt: str) -> str:
    # remove acentos para comparação, mas mantém original para exibir
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt.lower())
        if unicodedata.category(c) != 'Mn'
    )

def carregar_ranking():
    if ARQUIVO_RANKING.exists():
        try:
            with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"melhor_streak": 0}
    return {"melhor_streak": 0}

def salvar_ranking(ranking):
    try:
        with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
            json.dump(ranking, f, ensure_ascii=False, indent=2)
    except Exception:
        pass  # se não der pra salvar, segue o jogo

def escolher_palavra():
    categoria = random.choice(list(CATEGORIAS.keys()))
    palavra = random.choice(CATEGORIAS[categoria])
    dica = f"Categoria: {categoria} (tamanho: {len(palavra)})"
    return palavra, dica

def exibir_estado(palavra, letras_certas, letras_erradas, dica, tentativas_restantes):
    print(FORCA_DESENHOS[len(FORCA_DESENHOS) - 1 - tentativas_restantes])
    exibicao = []
    for ch in palavra:
        if ch == " ":
            exibicao.append(" ")
        elif normalizar(ch) in letras_certas:
            exibicao.append(ch)  # preserva acento/maiúscula da palavra
        else:
            exibicao.append("_")
    print("Palavra:  " + " ".join(exibicao))
    print("Dica:     " + dica)
    if letras_erradas:
        print("Erradas:  " + ", ".join(sorted(letras_erradas)))
    print(f"Tentativas restantes: {tentativas_restantes}")
    print("-" * 40)

def obter_chute(letras_tentadas):
    while True:
        chute = input("Digite uma letra OU tente a palavra inteira: ").strip()
        if not chute:
            print("Entrada vazia. Tente novamente.")
            continue
        # chute de palavra
        if len(chute) > 1:
            return chute
        # chute de letra
        letra_norm = normalizar(chute)[0]
        if not letra_norm.isalpha():
            print("Digite uma letra válida (a-z).")
            continue
        if letra_norm in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        return letra_norm

def jogo_forca():
    palavra, dica = escolher_palavra()
    alvo_norm = normalizar(palavra)
    letras_certas = set()
    letras_erradas = set()
    tentativas = len(FORCA_DESENHOS) - 1  # 6 erros permitidos

    while tentativas >= 0:
        exibir_estado(palavra, letras_certas, letras_erradas, dica, tentativas)
        # checa vitória
        reveladas = [ch if normalizar(ch) in letras_certas or ch == " " else "_" for ch in palavra]
        if "_" not in reveladas:
            print("🎉 Parabéns! Você acertou a palavra:", palavra)
            return True

        chute = obter_chute(letras_certas | letras_erradas)

        # tentativa de palavra inteira
        if len(chute) > 1:
            if normalizar(chute) == alvo_norm:
                print("🎯 Acertou em cheio! A palavra era:", palavra)
                return True
            else:
                print("Palpite de palavra incorreto!")
                tentativas -= 1
                continue

        # tentativa de letra
        if chute in alvo_norm:
            letras_certas.add(chute)
            print("✔ Boa! A letra está na palavra.")
        else:
            letras_erradas.add(chute)
            tentativas -= 1
            print("✖ Não foi dessa vez.")

    print(FORCA_DESENHOS[-1])
    print("💀 Fim de jogo! A palavra era:", palavra)
    return False

def menu():
    print("=" * 40)
    print("     JOGO DA FORCA - TERMINAL EDITION")
    print("=" * 40)
    ranking = carregar_ranking()
    melhor = ranking.get("melhor_streak", 0)
    streak = 0

    while True:
        print(f"\nMelhor sequência: {melhor} | Sua sequência atual: {streak}")
        print("[1] Jogar")
        print("[2] Trocar semente aleatória (modo festa)")
        print("[3] Zerar ranking local")
        print("[0] Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            venceu = jogo_forca()
            if venceu:
                streak += 1
                if streak > melhor:
                    melhor = streak
                    ranking["melhor_streak"] = melhor
                    salvar_ranking(ranking)
                    print("🏆 Novo recorde de sequência!")
            else:
                streak = 0
        elif op == "2":
            seed = random.randrange(1_000_000)
            random.seed(seed)
            print(f"🔮 Nova semente aleatória aplicada: {seed}")
        elif op == "3":
            ranking = {"melhor_streak": 0}
            salvar_ranking(ranking)
            melhor = 0
            streak = 0
            print("🧹 Ranking zerado.")
        elif op == "0":
            print("Até a próxima! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
