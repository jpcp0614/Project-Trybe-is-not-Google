def exists_word(word, instance):
    occurrences = list()

    for element in instance.list:
        occurrences_lines = list()

        occurrences.append({
            'palavra': word,
            'arquivo': element['nome_do_arquivo'],
            'ocorrencias': occurrences_lines
        })

        for index, line in enumerate(element['linhas_do_arquivo']):
            word_lower = word.lower()
            line_lower = line.lower()

            if word_lower in line_lower:
                occurrences_lines.append({
                    'linha': index + 1
                })

        if len(occurrences_lines) == 0:
            occurrences.pop()

    return occurrences


def search_by_word(word, instance):
    occurrences = []
    for element in instance.list:
        data = {
            'palavra': word,
            'arquivo': element['nome_do_arquivo'],
            'ocorrencias': []
        }

        for index, line in enumerate(element['linhas_do_arquivo']):
            line_minus_period = line.replace('.', '').lower().split()
            word_lower = word.lower()

            if word_lower in line_minus_period:
                data['ocorrencias'].append({
                    'linha': index + 1,
                    'conteudo': line
                })

        if len(data['ocorrencias']) > 0:
            occurrences.append(data)

    return occurrences
