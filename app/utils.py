import pandas as pd
import numpy as np


def parse_ancestry_file(file_path, subject_id):
    """
    Parses a raw AncestryDNA text file natively.
    - Automatically skips rows starting with '#'
    - Combines allele1 and allele2 into a standardized 2-character genotype
    - Strips vendor metadata and applies an anonymized subject_id string
    """
    # Read the tab-delimited file, skipping comment lines automatically
    df = pd.read_csv(file_path, sep="\t", comment="#", low_memory=False)

    # Force columns to lowercase just in case of any platform anomalies
    df.columns = df.columns.str.lower()

    # Combine individual alleles into a single string (e.g., 'A' + 'G' -> 'AG')
    df["genotype"] = df["allele1"].astype(str) + df["allele2"].astype(str)

    # Convert missing data markers (like '00', '--', '??') to a clean NaN format
    df["genotype"] = df["genotype"].replace(["--", "00", "??", "nan", "NN"], np.nan)

    # Assign our anonymized research ID to decouple personal identity
    df["profile_id"] = subject_id
    df["vendor"] = "AncestryDNA"

    # Filter out the raw individual alleles to keep the master dataset slim and uniform
    return df[["profile_id", "rsid", "chromosome", "position", "genotype", "vendor"]]

