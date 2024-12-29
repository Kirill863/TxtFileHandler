class TxtFileHandler:
    """
    Класс для работы с текстовыми файлами.

    Методы:
        read_file(filepath: str) -> str: Чтение данных из TXT файла.
        write_file(filepath: str, *data: str) -> None: Запись данных в TXT файл.
        append_file(filepath: str, *data: str) -> None: Дописывание данных в TXT файл.
    """

    @staticmethod
    def read_file(filepath: str) -> str:        
        """Метод для чтения данных из TXT файла.
                Args:
                    filepath (str): Путь к файлу.
                Returns:
                    str: Содержимое файла или пустая строка, если файл не существует.
                """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return ""
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return ""
    @staticmethod
    def write_file(filepath: str, *data: str) -> None:
        """
        Метод для записи данных в TXT файл.

        Args:
            filepath (str): Путь к файлу.
            *data (str): Строки для записи в файл.
        """
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                for line in data:
                    file.write(line)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")
    @staticmethod
    def append_file(filepath: str, *data: str) -> None:
        """
        Метод для дописывания данных в TXT файл.

        Args:
            filepath (str): Путь к файлу.
            *data (str): Строки для добавления в файл.
        """
        try:
            with open(filepath, 'a', encoding='utf-8') as file:
                for line in data:
                    file.write(line)
        except Exception as e:
            print(f"Ошибка при добавлении данных в файл: {e}")