import os
import pandas as pd
import streamlit as st
from utils import parse_ancestry_file

st.set_page_config(
    page_title="SNP Decoder | Clinical Informatics MVP",
    page_icon="🧬",
    layout="wide",
)

st.title("🧬 SNP Decoder: Clinical Genomics Pipeline")
st.markdown(
    "Harmonizing multi-vendor commercial DNA files into a de-identified research schema."
)
st.markdown("---")

st.subheader("1. Local Raw Data Audit")
st.write("Scanning local `raw_dna/` directory for source profiles:")

# Map your local files to anonymized research identifiers
profile_map = [
    {"id": "Subject-01", "file": "AncestryDNA_dad.txt"},
    {"id": "Subject-02", "file": "AncestryDNA_mom.txt"},
    {"id": "Subject-03", "file": "AncestryDNA_grace.txt"},
]

cols = st.columns(3)
valid_files = []

for idx, item in enumerate(profile_map):
    filepath = os.path.join("raw_dna", item["file"])
    with cols[idx]:
        if os.path.exists(filepath):
            st.success(f"**{item['id']}**\n\nStatus: Ready")
            valid_files.append((filepath, item["id"]))
        else:
            st.error(f"**{item['id']}**\n\nMissing: `{item['file']}`")

st.markdown("---")
st.subheader("2. Execute Anonymization & Harmonization")

if st.button("Run Pipeline Engine", disabled=len(valid_files) == 0, type="primary"):
    with st.spinner("Parsing and de-identifying genomic records..."):
        dfs = []
        for path, sub_id in valid_files:
            df = parse_ancestry_file(path, sub_id)
            dfs.append(df)

        master_df = pd.concat(dfs, ignore_index=True)

        st.success(
            f"Harmonized **{len(master_df):,}** total SNP records "
            f"across **{len(valid_files)}** profiles!"
        )

        # Display top rows to verify anonymization worked
        st.dataframe(master_df.head(50), width="stretch")

        # Save local output for Power BI Desktop testing
        out_path = os.path.join("data", "processed", "mvp_harmonized_snps.csv")
        master_df.to_csv(out_path, index=False)
        st.info(f"Saved clean dataset locally to `{out_path}`.")

