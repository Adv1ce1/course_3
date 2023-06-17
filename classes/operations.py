from typing import Any


class Operations:
    """
    Базовый классс Operations - предоставляет информацию о 5 последних банковских операциях
        Args:
            all_operations (list[dict]) - передает все банковские операции
        Attributes:
            self.__last_operations (list[dict]) - получает 5 последних банковский операций

    """

    def __init__(self, all_operations: list[dict]) -> None:
        """Инициализирует Operations объект со списком всех операций"""
        self.all_operations: list[dict] = all_operations
        self.__last_operations: list[dict] = self.__set_last_operations()