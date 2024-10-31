from Bio.SeqRecord import SeqRecord


class ProteinTranslator:
    """Clase para traducir secuencias de ADN a proteínas."""

    @staticmethod
    def translate_sequences(dna_records):
        """Traduce cada secuencia de ADN en la lista a proteínas en las tres lecturas.

        Args:
            dna_records (list): Lista de objetos SeqRecord que contienen secuencias de ADN.

        Returns:
            list: Lista de objetos SeqRecord con las secuencias de proteínas.
        """
        protein_records = []
        for record in dna_records:
            # Crear una lista para almacenar las proteínas traducidas
            proteins = []
            # Traducir en las tres lecturas
            for frame in range(3):
                protein_seq = record.seq[frame:].translate(to_stop=True)  # Traducir hasta el primer codón de parada
                proteins.append(protein_seq)

            # Crear un objeto SeqRecord para cada proteína traducida
            for i, protein_seq in enumerate(proteins):
                protein_record = SeqRecord(
                    protein_seq,
                    id=f"{record.id}_frame_{i + 1}",
                    description=record.description
                )
                protein_records.append(protein_record)

        return protein_records
