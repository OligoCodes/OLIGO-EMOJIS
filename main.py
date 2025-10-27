"""Demo for oligo-emojis library."""

from oligoemojis import Emojis

def main():
    e = Emojis(default_count=3)
    print("Package version:", getattr(__import__('oligoemojis'), '__version__', '<no version>'))
    print("Categories:", e.list_categories())
    print("Sample smileys:", e.smileys())
    print("Random animal:", e.animals_random())
    print("Two random objects:", e.objects(q=2))

if __name__ == "__main__":
    main()