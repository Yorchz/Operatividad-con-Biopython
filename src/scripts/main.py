from io import StringIO
from Bio import SeqIO
from src.config.Config import Config
from src.orchestrator.MainOrchestrator import MainOrchestrator
from src.utils.aminoacid_translator import AminoAcidTranslator
from src.utils.aminoacid_fasta_writer import AminoacidFastaWriter

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

        # Comprobar cuántas secuencias de ADN se han leído
        print(f"Número de secuencias de ADN leídas: {len(dna_records)}")

        # Calcular y comparar contenido de GC
        orchestrator.calculate_and_compare_gc_content(filename)

        # Traducir secuencias de ADN a aminoácidos en los seis marcos de lectura
        all_aminoacid_records = []
        for dna_record in dna_records:
            aminoacid_records = AminoAcidTranslator.translate_all_frames(dna_record)
            all_aminoacid_records.extend(aminoacid_records)

        # Comprobar cuántas secuencias de aminoácidos se han generado
        print(f"Número de secuencias de aminoácidos generadas: {len(all_aminoacid_records)}")

        # Escribir las secuencias de aminoácidos en un archivo FASTA
        aminoacid_output_file = "output_aminoacids.fasta"  # Cambia el nombre del archivo de salida si es necesario
        fasta_writer = AminoacidFastaWriter(aminoacid_output_file)
        fasta_writer.write_aminoacid_fasta(all_aminoacid_records)

    else:
        orchestrator.execute_read_all()


# Llamar a la función principal
if __name__ == "__main__":
    main("sequence.fasta", False)
