from src.reader.FastaBatchReader import FastaBatchReader
from src.utils.FastaFileHandler import FastaFileHandler


class ReaderOrchestrator:
    def __init__(self, config):
        """Initialize with the directory where FASTA files are located."""
        self.fasta_handler = FastaFileHandler(config["download"]["download_directory"])
        self.reader = FastaBatchReader(self.fasta_handler)

    def read_single_fasta(self, filename):
        """Read a single FASTA file by its name."""
        for seq_record in self.reader.read_fasta_by_name(filename):
            print(seq_record.id, seq_record.seq)

    def read_all_fastas(self):
        """Read all FASTA files in the directory."""
        for seq_record in self.reader.read_all_fastas():
            print(seq_record.id, seq_record.seq)
