from io import StringIO
from Bio import SeqIO
from src.config.Config import Config
from src.orchestrator.MainOrchestrator import MainOrchestrator
from src.utils.ProteinTranslator import ProteinTranslator
from src.utils.ProteinFastaWriter import ProteinFastaWriter


def main(filename=None, download=None, file_ids=None):
    orchestrator = MainOrchestrator(Config)

    # Descargar archivos si se especifica
    if download and file_ids:
        orchestrator.execute_download(file_ids)

    # Leer secuencias de ADN desde el archivo FASTA
    if filename:
        # Llamar a read_single_fasta para obtener ID y contenido
        id, content = orchestrator.execute_read_single(filename)

        # Crear contenido FASTA
        fasta_content = f">{id}\n{content}\n"  # Asegurarse de que haya una nueva línea al final

        # Leer secuencias de ADN desde el contenido del archivo FASTA
        dna_records = list(SeqIO.parse(StringIO(fasta_content), "fasta"))

        # Comprobar cuántas secuencias se han leído
        print(f"Número de secuencias de ADN leídas: {len(dna_records)}")

        # Calcular y comparar contenido de GC
        orchestrator.calculate_and_compare_gc_content(filename)

        # Traducir secuencias de ADN a proteínas
        protein_records = ProteinTranslator.translate_sequences(dna_records)

        # Comprobar cuántas secuencias de proteínas se han generado
        print(f"Número de secuencias de proteínas generadas: {len(protein_records)}")

        # Escribir las secuencias de proteínas en un archivo FASTA
        protein_output_file = "output_proteins.fasta"  # Cambia el nombre del archivo de salida si es necesario
        fasta_writer = ProteinFastaWriter(protein_output_file)
        fasta_writer.write_protein_fasta(protein_records)

    else:
        orchestrator.execute_read_all()


# Llamar a la función principal
if __name__ == "__main__":
    main("NM_001301717.fasta", False)
