import os
from src.utils.FilePathHelper import FilePathHelper


class FastaFileHandler:
    def __init__(self, fasta_dir):
        self.fasta_dir = fasta_dir
        print(fasta_dir)

    def get_fasta_files(self):
        """Return a list of all fasta files in the directory."""
        fasta_files = [f for f in os.listdir(self.fasta_dir) if f.endswith('.fasta')]
        return [os.path.join(self.fasta_dir, f) for f in fasta_files]

    def get_filenames_only(self):
        """Return only the names of the fasta files (without full paths)."""
        fasta_files = self.get_fasta_files()
        return [FilePathHelper.get_filename_only(f) for f in fasta_files]
