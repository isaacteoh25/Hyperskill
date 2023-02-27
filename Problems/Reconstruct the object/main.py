import pickle


def reconstruct_data(a, b):
    # music_instruments = ['Acoustic piano', 'Electric piano', 'Synthesizer']
    # with open(a, 'rb') as pickled_file:
    unpickled_data = pickle.loads(a)
    # with open(b, 'rb') as pickled_file_b:
    unpickled_data_b = pickle.loads(b)

    return  unpickled_data + unpickled_data_b