from io import StringIO

from Bio import SeqIO

from src.orchestrator.GCOrchestrator import GCOrchestrator
from src.utils.GCContentCalculator import GCContentCalculator
from src.orchestrator.DownloaderOrchestrator import DownloaderOrchestrator
from src.orchestrator.ReaderOrchestrator import ReaderOrchestrator
from src.utils.ProteinFastaWriter import ProteinFastaWriter
from src.utils.ProteinTranslator import ProteinTranslator


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
        return self.reader_orchestrator.read_single_fasta(filename)

    def execute_read_all(self):
        """Execute the reading of all FASTA files."""
        return self.reader_orchestrator.read_all_fastas()

    def calculate_gc_custom(self, filename):
        record_id, sequence = self.execute_read_single(filename)
        gc_content = GCOrchestrator.calculate_gc_custom(str(sequence))
        print(f"Custom GC Content for {record_id}: {gc_content:.2f}%")
        return gc_content

    def calculate_gc_biopython(self, filename):
        record_id, sequence = self.execute_read_single(filename)
        gc_content = GCOrchestrator.calculate_gc_biopython(str(sequence))
        print(f"Biopython GC Content for {record_id}: {gc_content:.2f}%")
        return gc_content

    def calculate_and_compare_gc_content(self, filename):
        record_id, sequence = self.execute_read_single(filename)
        custom_gc = self.calculate_gc_custom(filename)
        biopython_gc = self.calculate_gc_biopython(filename)
        GCOrchestrator.compare_gc_methods(custom_gc, biopython_gc)

    def create_fasta_content(self, record_id, sequence):
        fasta_content = f">{record_id}\n{sequence}\n"
        return fasta_content

    def read_dna_sequences(self, fasta_content):
        dna_records = list(SeqIO.parse(StringIO(fasta_content), "fasta"))
        print(f"Número de secuencias de ADN leídas: {len(dna_records)}")
        return dna_records

    def translate_dna_to_proteins(self, dna_records):
        protein_records = ProteinTranslator.translate_sequences(dna_records)
        print(f"Número de secuencias de proteínas generadas: {len(protein_records)}")
        return protein_records

    def write_proteins_to_fasta(self, protein_records, output_file="output_proteins.fasta"):
        fasta_writer = ProteinFastaWriter(output_file)
        fasta_writer.write_protein_fasta(protein_records)


