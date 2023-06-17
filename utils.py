from zipfile import ZipFile
import json

def open_file_in_zip(path_zip: str) -> list[dict]:
    """
    Открывает файл внутри ZIP-архива и возвращает его содержимое в формате JSON
    """
    with ZipFile(path_zip, "r") as myzip:
        for item in myzip.infolist():
            if item.filename.endswith(".json"):
                with myzip.open(item.filename, "r") as f:
                    return json.load(f)
