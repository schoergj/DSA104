import pandas as pd
import numpy as np

from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdFingerprintGenerator

from sklearn.model_selection import train_test_split


def compute_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return pd.Series({
        "MolWt": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol), 
        "EState_VSA5": Descriptors.EState_VSA5(mol),
        "TPSA": Descriptors.TPSA(mol),
        "NumHAcc": Descriptors.NumHAcceptors(mol),
        "NumAromaticRings":Descriptors.NumAromaticRings(mol),
        "HeavyAtomCount":Descriptors.HeavyAtomCount(mol),
        "RingCount":Descriptors.RingCount(mol),
        "qed":Descriptors.qed(mol),
        "NumHDonors":Descriptors.NumHDonors(mol),
        "NOCount":Descriptors.NOCount(mol),

    })

def smiles_to_mol(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return mol

def morgan_fp(mols):
    fps = []
    for mol in mols:
        fpg = rdFingerprintGenerator.GetMorganGenerator(fpSize=2048, radius=2)
        fp = fpg.GetFingerprint(mol)
        fps.append(fp)
    X = np.array(fps)
    return X


def apply_descriptors(df_full):
    # Apply to dataframe
    descriptor_df = df_full["smiles"].apply(compute_descriptors)

    # Combine descriptors with original data
    df_full = pd.concat([df_full, descriptor_df], axis=1)

    # Remove rows where descriptor calculation failed
    df_full = df_full.dropna()
    
    # split into features and target
    X = df_full.drop(columns=["logS", "smiles"], axis=1)
    y = df_full["logS"]

    # train test split
    ML_X_train, ML_X_test, ML_y_train, ML_y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return ML_X_train, ML_X_test, ML_y_train, ML_y_test

def calculate_mfp(df):
    df["mol"] = df["smiles"].apply(smiles_to_mol)
    mols = df["mol"].to_numpy()
    X = morgan_fp(mols)
    y = df["logS"].to_numpy()

    # train test split
    ML_X_train, ML_X_test, ML_y_train, ML_y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return ML_X_train, ML_X_test, ML_y_train, ML_y_test


def generate_descriptors_sample(df_full, sample_size):
    # use same function as above, but introduce samplesize
    if sample_size == 0:
        return apply_descriptors(df_full)
    else:
        df = df_full.sample(sample_size, random_state=42)
        return apply_descriptors(df)


def generate_mfp_sample(df_full, sample_size):
    # use same function as above, but introduce samplesize
    if sample_size == 0:
        return calculate_mfp(df_full)
    else:
        df = df_full.sample(sample_size, random_state=42)
        return calculate_mfp(df)
        
