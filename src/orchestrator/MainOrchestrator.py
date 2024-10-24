from src.orchestrator.DownloaderOrchestrator import DownloaderOrchestrator
from src.orchestrator.ReaderOrchestrator import ReaderOrchestrator


class MainOrchestrator:
    def __init__(self, config):
        """Initialize with the download orchestrator and the reader orchestrator."""
        self.download_orchestrator = DownloaderOrchestrator(config)
        self.reader_orchestrator = ReaderOrchestrator(config)

    def execute_download(self, file_ids):
        """Execute the download of files."""
        self.download_orchestrator.download_files(file_ids)

    def execute_read_single(self, filename):
        """Execute the reading of a single FASTA file."""
        self.reader_orchestrator.read_single_fasta(filename)

    def execute_read_all(self):
        """Execute the reading of all FASTA files."""
        self.reader_orchestrator.read_all_fastas()