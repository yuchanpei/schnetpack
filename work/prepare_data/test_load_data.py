#%%
from schnetpack.data import load_dataset
from schnetpack.data import AtomsDataFormat
#%%
data_loaded = load_dataset("/pubhome/ycpei02/git/schnetpack/work/prepare_data/new_dataset.db",AtomsDataFormat.ASE)
# %%
count_idx = 0
for data_item in data_loaded:
    #print(type(data_item))
    for k,v in data_item.items():
        print("-", k, ":", v)
    count_idx += 1
    if count_idx > 3:
        break
#%%
data_loaded[0]
# %%
print('Number of reference calculations:', len(data_loaded))
print('Available properties:')

for p in data_loaded.available_properties:
    print('-', p)
print()

example = data_loaded[0]
print('Properties of molecule with id 0:')

for k, v in example.items():
    print('-', k, ':', v.shape)
#%%
for k, v in example.items():
    print('-', k, ':', v)
# %%
data_loaded = load_dataset("/pubhome/ycpei02/git/schnetpack/work/spk_qm9_workdir/data/qm9.db",AtomsDataFormat.ASE)
#%%
count_idx = 0
for data_item in data_loaded:
    #print(type(data_item))
    for k,v in data_item.items():
        print("-", k, ":", v)
    count_idx += 1
    if count_idx > 3:
        break
# %%
data_loaded = load_dataset("/pubhome/ycpei02/git/schnetpack/work/prepare_data/test_ligand_pocket.db",AtomsDataFormat.ASE)
#%%
count_idx = 0
for data_item in data_loaded:
    #print(type(data_item))
    for k,v in data_item.items():
        print("-", k, ":", v)
    count_idx += 1
    if count_idx > 3:
        break
# %%
data_loaded = load_dataset("/pubhome/ycpei02/git/schnetpack/work/spk_md17_workdir/forcetut/ethanol.db",AtomsDataFormat.ASE)
print(len(data_loaded))
# %%
