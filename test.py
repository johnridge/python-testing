modelType = 'SEIRDS'
initialValues = ['N - I_0', 0, 'I_0'] + [0 if x != 'S' else None for x in modelType[1:]]
print(initialValues)