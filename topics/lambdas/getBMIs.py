def get_bmis(people):
    result = []

    for p in people:
        result.append(p.weight / p.height ** 2)

    return result
