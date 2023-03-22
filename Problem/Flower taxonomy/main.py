iris = {}

def add_iris(id_n, species, petal_lenght, petal_width, **kwargs):
    iris[id_n] = {'species': species, 'petal_length': petal_lenght, 'petal_width': petal_width, **kwargs}



# def add_iris(id_n, species, petal_length, petal_width, **kwargs):
#     iris.update({id_n: {'species': species, 'petal_length': petal_length, 'petal_width': petal_width, **kwargs}})

def add_iris(*args, **kwargs):
    keys = ['species', 'petal_length', 'petal_width']
    iris[args[0]] = dict(zip(keys, args[1:]))
    iris[args[0]].update(kwargs)
    return iris


def add_iris(id_n, species, petal_length, petal_width, **additional_features):
    iris[id_n] = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    # if kwargs:
    for k, v in additional_features.items():
        iris[id_n][k] = v
# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    global iris
    dict1 = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    dict1.update(kwargs)
    iris = {id_n: dict1}

def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    iris.setdefault(id_n, {
        'species': species,
        'petal_length': petal_length,
        'petal_width': petal_width,
        **kwargs
    })
