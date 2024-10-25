from src.utils.BioGCContentCalculator import BioGCContentCalculator
from src.utils.GCComparator import GCComparator
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
        GCComparator.compare_gc_content(custom_gc, biopython_gc)
