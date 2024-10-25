from Bio.SeqUtils import gc_fraction


class BioGCContentCalculator:
    @staticmethod
    def calculate_gc_content(sequence: str) -> float:
        """Calculate the GC content using Biopython's gc_fraction function."""
        return gc_fraction(sequence) * 100
