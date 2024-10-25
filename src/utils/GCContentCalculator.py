class GCContentCalculator:
    @staticmethod
    def calculate_gc_content(sequence: str) -> float:
        """Calculate the GC content of a given DNA sequence."""
        if not sequence:
            return 0.0
        g_count = sequence.upper().count('G')
        c_count = sequence.upper().count('C')
        gc_count = g_count + c_count
        return (gc_count / len(sequence)) * 100
