# Development Log & Architectural Decisions

## Phase 1: Project Initialization & Privacy Controls (Nov 10, 2026)
* **Core Stack Selected:** Streamlit (Python prototyping frontend) + Power BI Desktop (Local BI 
  engineering layer).
* **Infrastructure Strategy:** Opted for a single-repository architecture connected to Streamlit 
  Cloud and GitHub Pages to maximize recruiter visibility and minimize hosting overhead.
* **Data Governance Policy:** Prior to importing any genomic data, established a strict `.gitignore` 
  protocol masking the `raw_dna/` directory. This guarantees that commercial AncestryDNA and 
  FamilyTreeDNA profiles remain localized and never leak to the public cloud, mirroring enterprise 
  HIPAA data integrity expectations.

## Phase 2: Schema Audit & Flat File Parsing (Nov 10, 2026)
* **Data Footprint Discovered:** Verified that the AncestryDNA files utilize a standard 5-column 
  schema (`rsid`, `chromosome`, `position`, `allele1`, `allele2`) separated by raw TAB delimiters.
* **Reference Genome Verification:** Explicitly audited the vendor file comments and confirmed that 
  both 2023 and 2026 profiles align perfectly on the **Human Reference Build 37.1 (hg19)** 
  coordinate assembly. This locks down a unified spatial matrix for downstream lookup mappings.
* **Engineering Resolution:** Authored a modular, low-memory Python parser function 
  (`parse_ancestry_file`) that strips vendor header metadata, aggregates isolated alleles into 
  uniform 2-character genotype strings, and automatically normalizes missing variant call fields.
* **Compliance Protocol Executed:** Integrated a clinical-style string filter (`profile_id`) 
  during ingestion to immediately decouple biological data rows from personal family nomenclature.

