import os


class FilePathHelper:
    @staticmethod
    def get_filename_only(file_path: str) -> str:
        """Devuelve solo el nombre del archivo a partir de la ruta completa."""
        return os.path.basename(file_path)
