class TxtFileHandler
    @staticmethod
    def read_file(filepath: str) -> str:
        """Метод для чтения данных из TXT файла."""
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
        """Метод для записи данных в TXT файл."""
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                for line in data:
                    file.write(line)
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")