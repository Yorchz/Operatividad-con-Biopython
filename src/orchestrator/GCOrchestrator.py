from src.utils.BioGCContentCalculator import BioGCContentCalculator
from src.utils.GCContentCalculator import GCContentCalculator


class GCOrchestrator:
    @staticmethod
    def calculate_gc_custom(sequence: str) -> float:
        """Calculate GC content using the custom method."""
        return GCContentCalculator.calculate_gc_content(sequence)

    @staticmethod
    def calculate_gc_biopython(sequence: str) -> float:
        """Calculate GC content using Biopython's gc_fraction function."""
        return BioGCContentCalculator.calculate_gc_content(sequence)

    @staticmethod
    def compare_gc_methods(custom_gc: str, biopython_gc: str) -> float:
        """Compare GC content results from both methods and display them."""

        print(f"Custom GC Content: {custom_gc:.2f}%")
        print(f"Biopython GC Content: {biopython_gc:.2f}%")

        if abs(custom_gc - biopython_gc) < 1e-5:
            print("Both methods produce similar results.")
        else:
            print("The methods produce different results.")
