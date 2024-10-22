from Bio import SeqIO

from api_connection_download.utils.FilePathHelper import FilePathHelper


class NonEmptyValidator:
    @staticmethod
    def validate(file_name: str) -> bool:
        """Comprueba que el archivo FASTA no esté vacío."""
        try:
            with open(file_name, "r") as file_handle:
                records = list(SeqIO.parse(file_handle, "fasta"))
                if records:
                    print(f"{FilePathHelper.get_filename_only(file_name)} no está vacío.")
                    return True
                else:
                    print(f"{FilePathHelper.get_filename_only(file_name)} está vacío.")
                    return False
        except Exception as e:
            print(f"Error al validar el archivo {FilePathHelper.get_filename_only(file_name)}: {e}")
            return False
