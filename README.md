Developed algorithm for searching of degenerate repeats.
My algorithm can search for four types (direct, complementary, mirror, inverted) repeats of any length and degeneracy in a circular genome.
Algorithm described in the BMC Genomics paper https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-5536-1

Main scrips:
_degrephunter_20230207.py - searchin 10-length repeats and merging to long repeats
TandCleaner.py - fixing bug with tandem repeats (merging to normal repeat)