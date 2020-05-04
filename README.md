# biozernike-validation
Data and scripts used for training and benchmarking of [BioZernike method](https://github.com/biocryst/biozernike)

## Datasets
There are 3 datasets in tar.xz bundles with .pdb files. Use `tar xf` to extract.
- [Assemblies](datasets/assemblies.tar.xz) : 500 biological assemblies randomly selected from all PDB entries (2019) such that no two assemblies have density correlation score larger than 0.5. Additional conformations by normal mode analysis can be obtained with [this python script](scripts/assemblies_nma.py).
- [CATH](datasets/cath.tar.xz) : a non-redundant subset of CATH domains. 2685 structures divided among 151 families.
- [ECOD](datasets/ecod.tar.xz) : a non-redundant subset of ECOD domains

## Optimized weights
The implementation at rcsb.org exposes two search profiles:
- "strict" : corresponding to profile 0
- "relaxed" : corresponding to profile 1

The weights for each profile are annotated in [this file](datasets/weights.properties).