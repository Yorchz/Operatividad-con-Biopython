import json

from Bio import Entrez
from typing import List


class IdFetcher:
    def __init__(self, config: json):
        Entrez.email = config["email"]["address"]
        self.db = config["download"]["db"]
        self.search_term = config["data"]["search_term"]

    def fetch_ids(self, count: int) -> List[str]:
        """Recuperar una lista de identificadores de la base de datos NCBI."""
        try:
            with Entrez.esearch(db=self.db, term=self.search_term, retmax=count) as handle:
                record = Entrez.read(handle)
                return record["IdList"]
        except Exception as e:
            print(f"Ocurrió un error al recuperar los identificadores: {e}")
            return []
