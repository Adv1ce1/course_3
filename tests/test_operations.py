import pytest

from classes.operations import Operations


def test_operations_repr():
    operations = Operations([{'id': 1, 'date': '2022-01-01T12:00:00', 'description': 'Operation 1'}])
    expected_repr = [{'id': 1, 'date': '2022-01-01T12:00:00', 'description': 'Operation 1'}]
    assert operations.__repr__() == f"Operations({expected_repr})"


def test_operations_set_last_operations():
    all_operations = [
        {'id': 1, 'date': '2022-01-01T12:00:00', 'description': 'Operation 1'},
        {'id': 2, 'date': '2022-01-02T12:00:00', 'description': 'Operation 2'},
        {'id': 3, 'description': 'Operation 3'}
    ]
    operations = Operations(all_operations)
    assert len(operations._Operations__last_operations) == 2
    assert operations._Operations__last_operations[0]['id'] == 2
    assert operations._Operations__last_operations[1]['id'] == 1


def test_date_reversed():
    assert Operations._Operations__date_reversed('2022-01-01T12:00:00') == "01.01.2022"


@pytest.fixture
def operations_instance():
    all_operations = [
        {
            'id': 1,
            'date': '2017-01-01T12:00:00',
            'description': 'Operation 2',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'

        },
        {
            'id': 2,
            'date': '2018-01-01T12:00:00',
            'description': 'Operation 2',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {
            'id': 3,
            'date': '2015-01-01T12:00:00',
            'description': 'Operation 3',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {
            'id': 4,
            'date': '2020-01-01T12:00:00',
            'description': 'Operation 4',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        },
        {},
        {
            'id': 5,
            'date': '2021-01-01T12:00:00',
            'description': 'Operation 5',
            'operationAmount': {'amount': 100, 'currency': {'name': 'RUB'}},
            'state': 'EXECUTED'
        },
        {
            'id': 6,
            'date': '2022-01-01T12:00:00',
            'description': 'Operation 6',
            'from': 'Account A',
            'to': 'Account B',
            'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
            'state': 'EXECUTED'
        }

    ]
    return Operations(all_operations)


def test_operations_output_last_operations(operations_instance, capsys):
    operations_instance.output_last_operations()
    captured = capsys.readouterr()
    assert 'Операция: 2' in captured.out
    assert '01.01.2022 Operation 6' in captured.out
    assert 'Операция: 3' not in captured.out