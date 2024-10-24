from Bio import SeqIO
from src.utils.FilePathHelper import FilePathHelper


class FormatValidator:
    @staticmethod
    def validate(file_name: str) -> bool:
        """Comprueba que el archivo tenga al menos una secuencia en formato FASTA."""
        try:
            with open(file_name, "r") as file_handle:
                records = list(SeqIO.parse(file_handle, "fasta"))
                if len(records) > 0:
                    print(f"\n{FilePathHelper.get_filename_only(file_name)} tiene un formato FASTA válido.")
                    return True
                else:
                    print(f"\n{FilePathHelper.get_filename_only(file_name)} no tiene un formato FASTA válido.")
                    return False
        except Exception as e:
            print(f"\nError al validar el formato de {FilePathHelper.get_filename_only(file_name)}: {e}")
            return False
