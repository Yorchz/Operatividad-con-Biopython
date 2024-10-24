from typing import List, Optional
from src.fasta_downloader.downloader.SingleFastaDownloader import SingleFastaDownloader


class FastaDownloader:
    def __init__(self, single_fasta_downloader: SingleFastaDownloader):
        self.single_fasta_downloader = single_fasta_downloader

    def download_fasta_files(self, identifiers: List[str]) -> List[Optional[str]]:
        """Descargar múltiples archivos FASTA dado una lista de identificadores."""
        return [self.single_fasta_downloader.download(identifier) for identifier in identifiers]
