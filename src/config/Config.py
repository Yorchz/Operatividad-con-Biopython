import os

Config = {
    "email": {
        "address": "tucorreo@example.com"
    },
    "data": {
        "search_term": "Homo sapiens[Organism]",
        "count": 3,
        "ids": ["NM_001301717", "NM_001374413", "NM_001301720"]
    },
    "download": {
        "db": "nucleotide",
        "rettype": "fasta",
        "retmode": "text",
        "download_directory": os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                                                           "data", "download_fasta"))
    }
}
