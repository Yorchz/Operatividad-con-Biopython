import os

Config = {
    "email": {
        "address": "tucorreo@example.com"
    },
    "data": {
        "search_term": "Homo sapiens[Organism]",  # Término de búsqueda para recuperar identificadores
        "count": 3,  # Número de archivos a descargar (opcional)
        "ids": ["NM_001301717", "NM_001374413", "NM_001301720"]  # Identificadores específicos (opcional)
    },
    "download": {
        "db": "nucleotide",
        "rettype": "fasta",
        "retmode": "text",
        "download_directory": os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                           "download_fasta"))  # Ruta al directorio de descarga
    }
}
