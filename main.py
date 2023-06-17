from utils import open_file_in_zip
from classes.operations import Operations


def main() -> None:
    """
    Основная функция программы.
    Открывает ZIP-архив, инициализирует объект класса Operations,
    и выводит информацию о последних операциях.
    """
    operations = open_file_in_zip('operations.zip')
    operations = Operations(operations)
    operations.output_last_operations()


if __name__ == '__main__':
    main()