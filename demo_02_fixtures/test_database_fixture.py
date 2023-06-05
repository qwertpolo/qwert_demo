import pytest
from database import Database 


@pytest.fixture
def fixture_db():
    db = Database()
    db.insert_data('test', 'value')
    return db


def test_insert_data(fixture_db):
    fixture_db.insert_data('key', 'another_value')
    assert fixture_db.get_data('key') == 'another_value'


def test_get_data(fixture_db):
    assert fixture_db.get_data('test') == 'value'
