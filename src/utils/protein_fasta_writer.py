from Bio import SeqIO

class ProteinFastaWriter:
    """Clase para escribir secuencias de proteínas en un archivo FASTA."""

    def __init__(self, output_file):
        self.output_file = output_file

    def write_protein_fasta(self, protein_records):
        """Escribe las secuencias de proteínas en un archivo FASTA de salida.

        Args:
            protein_records (list): Lista de objetos SeqRecord con secuencias de proteínas.
        """
        try:
            SeqIO.write(protein_records, self.output_file, "fasta")
            print(f"Archivo FASTA de proteínas creado en: {self.output_file}")
        except Exception as e:
            print(f"Error al escribir el archivo FASTA de salida: {e}")
