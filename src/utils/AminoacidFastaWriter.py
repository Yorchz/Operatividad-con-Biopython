from Bio import SeqIO

from src.config.Config import Config


class AminoacidFastaWriter:
    """Clase para escribir secuencias de aminoácidos en un archivo FASTA."""

    def __init__(self, output_file):
        self.output_file = output_file

    def write_aminoacid_fasta(self, aminoacid_records):
        """Escribe las secuencias de aminoácidos en un archivo FASTA de salida.

        Args:
            aminoacid_records (list): Lista de objetos SeqRecord con secuencias de aminoácidos.
        """
        try:
            SeqIO.write(aminoacid_records, self.output_file, "fasta")
            print(f"Archivo FASTA de aminoácidos creado en: {self.output_file}")
        except Exception as e:
            print(f"Error al escribir el archivo FASTA de salida: {e}")
