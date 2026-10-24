def age_assignment(*args, **kwargs):
    people = {}
    for name in args:
        people[name] = kwargs[name[0]]
    return people

