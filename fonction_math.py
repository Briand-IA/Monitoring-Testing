import pytest

#test_math.py
def add(x, y):
    return x + y

# test_classe.py
class Calculator:
    def add(self, x, y):
        return x + y
    
#test_fixture.py
@pytest.fixture
def setup_data():
    data = [
        {'name': 'John', 'age': 30},
        {'name': 'Elise', 'age': 23},
        {'name': 'Paul', 'age': 29},
        {'name': 'Alex', 'age': 12},
    ]
    return data

# fichier: test_parametrize.py
def add(x, y):
    return x + y

# fichier: test_exceptions.py
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# fichier: test_async.py
import asyncio

async def async_function():
    await asyncio.sleep(3)
    return 42