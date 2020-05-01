import random
import prody as pr
import os


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


def calc_ensembles(structure_orig):
    structure_ca = structure_orig.select('ca or name P')
    structure_anm = pr.ANM('structure ca')
    structure_anm.buildHessian(structure_ca)
    structure_anm.calcModes(n_modes=5)
    structure_anm_ext, structure_all = pr.extendModel(structure_anm, structure_ca, structure_orig, norm=True)
    ens = pr.sampleModes(structure_anm_ext, atoms=structure_all.all, n_confs=1, rmsd=1.5)
    return ens, structure_all

pdb_dir = 'NR'

pdb_files = os.listdir(pdb_dir)
random.shuffle(pdb_files)
pdb_files = [os.path.join(pdb_dir,p) for p in pdb_files if len(p)==15]
for pdb_file in pdb_files:
    structure = pr.parsePDB(pdb_file)
    n_structures = 4
    for i_structure in range(n_structures):
        i_file_name = pdb_file[:-4]+'_'+str(i_structure).zfill(3)+'.pdb'

        if os.path.exists(i_file_name):
            continue

        touch(i_file_name)
	print '\n\ncalculating', i_file_name,'\n'
        ensemble, structure_new = calc_ensembles(structure.copy())
        structure_new.setCoords(ensemble.getCoordsets(0))

        for i_repeat in range(5):
            ensemble, structure_new = calc_ensembles(structure_new)
            structure_new.setCoords(ensemble.getCoordsets(0))

        pr.writePDB(i_file_name, structure_new)
