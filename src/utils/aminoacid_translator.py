from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


class AminoAcidTranslator:
    """Clase para traducir secuencias de ADN en los seis marcos de lectura posibles a aminoácidos."""

    @staticmethod
    def translate_all_frames(dna_record):
        """Traduce la secuencia de ADN en los seis marcos de lectura posibles a aminoácidos.

        Args:
            dna_record (SeqRecord): Objeto SeqRecord que contiene una secuencia de ADN.

        Returns:
            list: Lista de objetos SeqRecord con secuencias de aminoácidos de los seis marcos de lectura.
        """
        aminoacid_records = []

        # Traducción de los tres marcos de lectura en la secuencia original
        for frame in range(3):
            # Ajustar la secuencia para que sea un múltiplo de tres
            seq_to_translate = dna_record.seq[frame:]
            seq_to_translate = seq_to_translate[:len(seq_to_translate) - len(seq_to_translate) % 3]
            aminoacid_seq = seq_to_translate.translate(to_stop=True)

            frame_id = f"{dna_record.id}_frame_{frame + 1}_forward"
            aminoacid_record = SeqRecord(aminoacid_seq, id=frame_id, description=dna_record.description)
            aminoacid_records.append(aminoacid_record)

        # Traducción de los tres marcos de lectura en la cadena complementaria inversa
        reverse_seq = dna_record.seq.reverse_complement()
        for frame in range(3):
            # Ajustar la secuencia complementaria inversa para que sea un múltiplo de tres
            seq_to_translate = reverse_seq[frame:]
            seq_to_translate = seq_to_translate[:len(seq_to_translate) - len(seq_to_translate) % 3]
            aminoacid_seq = seq_to_translate.translate(to_stop=True)

            frame_id = f"{dna_record.id}_frame_{frame + 1}_reverse"
            aminoacid_record = SeqRecord(aminoacid_seq, id=frame_id, description=dna_record.description)
            aminoacid_records.append(aminoacid_record)

        return aminoacid_records
