from src.utils.BioGCContentCalculator import BioGCContentCalculator
from src.utils.GCContentCalculator import GCContentCalculator


class GCComparator:
    @staticmethod
    def compare_gc_content(sequence: str):
        """Compare GC content results from two different calculators."""
        custom_gc_content = GCContentCalculator.calculate_gc_content(sequence)
        biopython_gc_content = BioGCContentCalculator.calculate_gc_content(sequence)

        print(f"Custom GC Content: {custom_gc_content:.2f}%")
        print(f"Biopython GC Content: {biopython_gc_content:.2f}%")

        if abs(custom_gc_content - biopython_gc_content) < 1e-5:
            print("Both methods produce similar results.")
        else:
            print("The methods produce different results.")
