from Bio import SeqIO

class BaseFastaReader:
    def read_fasta(self, file_path):
        """Read a single FASTA file and return a generator with each sequence."""
        with open(file_path, 'r') as fasta_file:
            for record in SeqIO.parse(fasta_file, 'fasta'):
                yield record
