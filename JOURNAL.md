# Development Log & Architectural Decisions

## Phase 1: Project Initialization & Privacy Controls (Nov 2026)
*   **Core Stack Selected:** Streamlit (Python prototyping frontend) + Power BI Desktop (Local BI engineering layer).
*   **Infrastructure Strategy:** Opted for a single-repository architecture connected to Streamlit Cloud and GitHub Pages to maximize recruiter visibility and minimize hosting overhead.
*   **Data Governance Policy:** Prior to importing any genomic data, established a strict `.gitignore` protocol masking the `raw_dna/` directory. This guarantees that commercial AncestryDNA and FamilyTreeDNA patient profiles remain localized and never leak to the public cloud, mirroring enterprise HIPAA/GDPR data integrity expectations.

