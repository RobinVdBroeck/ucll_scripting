def any_adults(persons):
    for p in persons:
        if p.age >= 18:
            return True

    return False
