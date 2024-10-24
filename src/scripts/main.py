from src.conections.Connection import NCBIConnection  # Usando tu conexión ya implementada
from src.orchestrator.MainOrchestrator import MainOrchestrator


def main(filename=None, download=False, file_ids=None):

    connection = NCBIConnection()
    fasta_dir = 'ruta_a_tu_directorio_fasta'

    orchestrator = MainOrchestrator(connection, fasta_dir)

    if download and file_ids:
        orchestrator.execute_download(file_ids)

    if filename:
        orchestrator.execute_read_single(filename)
    else:
        orchestrator.execute_read_all()


if __name__ == "__main__":
    main(filename="NM_001301717.fasta", download=False, file_ids=None)
