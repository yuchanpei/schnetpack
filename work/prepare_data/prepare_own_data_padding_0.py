#%%
from ase import Atoms
import numpy as np
from schnetpack.data import ASEAtomsData
#%%
data = np.load('/pubhome/ycpei02/git/PhysNet/data/test_ligand_pocket.npz')
#%%
#data["N"]
#numbers = data["Z"]
atoms_list = []
property_list = []
for numbers, positions, energies in zip(data["Z"], data["R"], data["E"]):
    ats = Atoms(positions=positions, numbers=numbers)
    energy_in_np = np.array([energies])
    properties = {'energy': energy_in_np}
    property_list.append(properties)
    atoms_list.append(ats)
#%%
print('Properties:', property_list[0])
# %%
ligand_pocket_dataset = ASEAtomsData.create(
    './test_ligand_pocket.db',
    distance_unit='Ang',
    property_unit_dict={'energy':'kcal/mol'}
)
ligand_pocket_dataset.add_systems(property_list, atoms_list)
#%%

for p in ligand_pocket_dataset.available_properties:
    print('-', p)
print()
# %%
example = ligand_pocket_dataset[0]
print('Properties of molecule with id 0:')

for k, v in example.items():
    print('-', k, ':', v.shape)
# %%
