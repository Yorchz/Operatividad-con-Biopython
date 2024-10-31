from io import StringIO

from Bio import SeqIO

from src.orchestrator.GCOrchestrator import GCOrchestrator
from src.utils.GCContentCalculator import GCContentCalculator
from src.orchestrator.DownloaderOrchestrator import DownloaderOrchestrator
from src.orchestrator.ReaderOrchestrator import ReaderOrchestrator
from src.utils.AminoacidFastaWriter import AminoacidFastaWriter
from src.utils.AminoAcidTranslator import AminoAcidTranslator


class MainOrchestrator:
    def __init__(self, config):
        self.download_orchestrator = DownloaderOrchestrator(config)
        self.reader_orchestrator = ReaderOrchestrator(config)

    def execute_download(self, file_ids):
        self.download_orchestrator.download_files(file_ids)

    def execute_read_single(self, filename):
        return self.reader_orchestrator.read_single_fasta(filename)

    def execute_read_all(self):
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

    def translate_dna_to_aminoacids(self, dna_records):
        all_aminoacid_records = []
        for dna_record in dna_records:
            aminoacid_records = AminoAcidTranslator.translate_all_frames(dna_record)
            all_aminoacid_records.extend(aminoacid_records)
        print(f"Número de secuencias de aminoácidos generadas: {len(all_aminoacid_records)}")
        return all_aminoacid_records

    def write_aminoacids_to_fasta(self, all_aminoacid_records, output_file="output_proteins.fasta"):
        fasta_writer = AminoacidFastaWriter(output_file)
        fasta_writer.write_aminoacid_fasta(all_aminoacid_records)


