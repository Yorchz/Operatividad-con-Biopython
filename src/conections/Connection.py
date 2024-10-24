from Bio import Entrez


class NCBIConnection:
    def __init__(self, email: str):
        self.email = email
        Entrez.email = email

    def connect(self) -> None:
        """Simula la conexión al API para asegurar que se configure correctamente."""
        print(f"Conexión a la API de NCBI establecida con el email: {self.email} \n")
