from src.reader.FastaBatchReader import FastaBatchReader
from src.utils.FastaFileHandler import FastaFileHandler


def main(filename=None):
    # Inicializar el manejador de archivos con el directorio de FASTA
    fasta_handler = FastaFileHandler('/data/download_fasta')

    # Inicializar el lector de archivos FASTA
    fasta_batch_reader = FastaBatchReader(fasta_handler)

    # Si se proporciona un nombre de archivo, leer solo ese archivo
    if filename:
        for seq_record in fasta_batch_reader.read_fasta_by_name(filename):
            print(seq_record.id, seq_record.seq)
    else:
        # Leer todas las secuencias de todos los archivos FASTA
        for seq_record in fasta_batch_reader.read_all_fastas():
            print(seq_record.id, seq_record.seq)


if __name__ == "__main__":
    # Puedes pasar el nombre del archivo aquí
    main(filename="NM_001301717.fasta")
