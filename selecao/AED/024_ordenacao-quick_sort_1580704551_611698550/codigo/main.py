def quick_sort(times):
    return sorted(times, key=lambda time: (
        -time['pontos'],          # Pontos em ordem decrescente
        -time['vitorias'],        # Vitórias em ordem decrescente
        -time['saldo_gols'],      # Saldo de gols em ordem decrescente
        -time['gols_marcados'],   # Gols marcados em ordem decrescente
        time['jogos'],            # Menor número de jogos
        time['nome'].lower()      # Ordem alfabética, case-insensitive
    ))

def processar_resultados(campeonato, times, jogos):
    for jogo in jogos:
        time1, gols1, time2, gols2 = analisar_jogo(jogo)
        gols1, gols2 = int(gols1), int(gols2)

        for time, gols_feitos, gols_tomados in [(time1, gols1, gols2), (time2, gols2, gols1)]:
            times[time]['jogos'] += 1
            times[time]['gols_marcados'] += gols_feitos
            times[time]['gols_sofridos'] += gols_tomados
            times[time]['saldo_gols'] = times[time]['gols_marcados'] - times[time]['gols_sofridos']

        if gols1 > gols2:
            times[time1]['pontos'] += 3
            times[time1]['vitorias'] += 1
            times[time2]['derrotas'] += 1
        elif gols1 < gols2:
            times[time2]['pontos'] += 3
            times[time2]['vitorias'] += 1
            times[time1]['derrotas'] += 1
        else:
            times[time1]['pontos'] += 1
            times[time2]['pontos'] += 1
            times[time1]['empates'] += 1
            times[time2]['empates'] += 1

    times_ordenados = quick_sort(list(times.values()))

    resultados = [campeonato]
    for posicao, time in enumerate(times_ordenados, 1):
        resultados.append(
            f"{posicao} - {time['nome']}: {time['pontos']} pontos, {time['jogos']} jogos "
            f"({time['vitorias']}-{time['empates']}-{time['derrotas']}), d.g. {time['saldo_gols']} "
            f"({time['gols_marcados']}-{time['gols_sofridos']})"
        )
    return resultados

def analisar_jogo(jogo):
    time1, time2 = jogo.split('#')
    nome1, gols1 = time1.split(':')
    nome2, gols2 = time2.split(':')
    return nome1.strip(), gols1.strip(), nome2.strip(), gols2.strip()

def main():
    n = int(input().strip())
    resultados_finais = []

    for i in range(n):
        input()  # Linha separadora entre os campeonatos, pode ser ignorada.
        campeonato = input().strip()
        t = int(input().strip())
        times = {}
        for _ in range(t):
            nome = input().strip()
            times[nome] = {
                'nome': nome,
                'pontos': 0,
                'jogos': 0,
                'vitorias': 0,
                'empates': 0,
                'derrotas': 0,
                'gols_marcados': 0,
                'gols_sofridos': 0,
                'saldo_gols': 0
            }

        g = int(input().strip())
        jogos = [input().strip() for _ in range(g)]

        if resultados_finais:
            resultados_finais.append("")

        resultados_camp = processar_resultados(campeonato, times, jogos)
        resultados_finais.extend(resultados_camp)

    print("")
    print("\n".join(resultados_finais))

if __name__ == "__main__":
    main()
