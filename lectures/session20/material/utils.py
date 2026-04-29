import numpy as np
from rdkit import Chem
from rdkit.Chem import MACCSkeys


def maccs_fp_from_smiles(smiles_list):
    fps = []
    valid_idx = []

    for i, smi in enumerate(smiles_list):
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            continue
        fp = MACCSkeys.GenMACCSKeys(mol)
        fps.append(np.array(fp))
        valid_idx.append(i)

    return np.array(fps), valid_idx

def maccs_fp_from_smiles_as_bitvectors(smiles_list):
    fps = []
    for i, smi in enumerate(smiles_list):
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            continue
        fp = MACCSkeys.GenMACCSKeys(mol)
        fps.append(fp)
    return fps