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
    """Aqui irá sua implementação"""
