def revert_string(value):
    reverted = ''
    listed_value = list(value)
    for i in range(len(listed_value) - 1, -1, -1):
        reverted += value[i]

    print(reverted)

revert_string('olecram')