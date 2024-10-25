

class GCComparator:
    @staticmethod
    def compare_gc_content(custom_gc_content: str, biopython_gc_content: str):
        """Compare GC content results from two different calculators."""

        if custom_gc_content == biopython_gc_content:
            print(f"Ambos métodos producen resultados idénticos -> resultado biopython ({biopython_gc_content}), "
                  f"resultado implementación ({custom_gc_content})")
        elif abs(custom_gc_content - biopython_gc_content) < 1:
            print(f"Ambos métodos producen resultados similares -> resultado biopython ({biopython_gc_content}), "
                  f"resultado implementación ({custom_gc_content})")
        else:
            print(f"Ambos métodos producen resultados diferentes -> resultado biopython ({biopython_gc_content}), "
                  f"resultado implementación ({custom_gc_content})")
