from src.fasta_reader.reader.BaseFastaReader import BaseFastaReader
from src.utils.FilePathHelper import FilePathHelper


class FastaBatchReader:
    def __init__(self, file_handler):
        """Initialize with a FastaFileHandler instance."""
        self.file_handler = file_handler
        self.base_reader = BaseFastaReader()

    def read_fasta_by_name(self, filename):
        """Read a specific FASTA file by its name."""
        filenames = self.file_handler.get_filenames_only()
        if filename in filenames:
            file_path = next(f for f in self.file_handler.get_fasta_files() if FilePathHelper.get_filename_only(f) == filename)
            yield from self.base_reader.read_fasta(file_path)
        else:
            raise FileNotFoundError(f"No FASTA file named '{filename}' found in the directory.")

    def read_all_fastas(self):
        """Read all FASTA files provided by the file handler."""
        fasta_files = self.file_handler.get_fasta_files()
        for fasta_file in fasta_files:
            yield from self.base_reader.read_fasta(fasta_file)
