def treat_input(input_json):
    treated = dict()
    for key, value in input_json.items():
        if key[0] == 'Q':
            treated[value] = 1
        else:
            treated[key] = 1
    return treated
