from fonction_math import setup_data

def test_data_name(setup_data):
    assert setup_data[1]['name'] == 'Elise'

def test_data_age(setup_data):
    assert setup_data[1]['age'] == 23
