# Scientific reproducibility in the clinical neurosciences: if replication is the answer, then what are the questions?

This is the companion repository for the paper "Scientific reproducibility in the clinical neurosciences: if replication is the answer, then what are the questions?"  Including ALL data, code, and support material for the methods used there-in.  Not for open publication, due to restrictions on sharing of proprietary data.

## Repository Structure

Based on [Edward Ma's DS project template](https://github.com/makcedward/ds_project_template)

Here is the explantation of folder strucure:
```bash
  .
  ├── data                              # All source data
  │   ├── processed                     # Any data resulting from processing, automatic or manual
  │   │   ├── database                  # sqlite3 database for articles
  │   │   └── vosviewer                 # processed data created with VOSviewer
  │   └── raw                           # All untouched data
  │       ├── s2_2021_06_01             # Semantic Scholar data
  │       └── web_of_science_2021_06_21 # Web of Science data
  ├── docs                              # Documentation / Drafts
  ├── notebook                          # Jupyter / R Notebooks
  │   └── eda                           # Exploratory data analysis
  ├── replication                       # All source code
  │   ├── preparation                   # Source code for data processing
  │   └── processing                    # Source code for data preparation
  └── test                              # All software testing goes here
```

## Web of Science

| Column name | Description     |
|-------------|-----------------|
| FN | File Name       |
| VR | Version Number  |
| PT | Publication Type (J=Journal; B=Book; S=Series; P=Patent) |
| AU | Authors         |
| AF | Author Full Name |
| BA | Book Authors    |
| BF | Book Authors Full Name |
| CA | Group Authors |
| GP | Book Group Authors |
| BE | Editors |
| TI | Document Title |
| SO | Publication Name |
| SE | Book Series Title |
| BS | Book Series Subtitle |
| LA | Language |
| DT | Document Type |
| CT | Conference Title |
| CY | Conference Date |
| CL | Conference Location |
| SP | Conference Sponsors |
| HO | Conference Host |
| DE | Author Keywords |
| ID | Keywords Plus® |
| AB | Abstract |
| C1 | Author Address |
| RP | Reprint Address |
| EM | E-mail Address |
| RI | ResearcherID Number |
| OI | ORCID Identifier (Open Researcher and Contributor ID) |
| FU | Funding Agency and Grant Number |
| FX | Funding Text |
| CR | Cited References |
| NR | Cited Reference Count |
| TC | Web of Science Core Collection Times Cited Count |
| Z9 | Total Times Cited Count (Web of Science Core Collection, Arabic Citation Index, BIOSIS Citation Index, Chinese Science Citation Database, Data Citation Index, Russian Science Citation Index, SciELO Citation Index) |
| U1 | Usage Count (Last 180 Days) |
| U2 | Usage Count (Since 2013) |
| PU | Publisher |
| PI | Publisher City |
| PA | Publisher Address |
| SN | International Standard Serial Number (ISSN) |
| EI | Electronic International Standard Serial Number (eISSN) |
| BN | International Standard Book Number (ISBN) |
| J9 | 29-Character Source Abbreviation |
| JI | ISO Source Abbreviation |
| PD | Publication Date |
| PY | Year Published |
| VL | Volume |
| IS | Issue |
| SI | Special Issue |
| PN | Part Number |
| SU | Supplement |
| MA | Meeting Abstract |
| BP | Beginning Page |
| EP | Ending Page |
| AR | Article Number |
| DI | Digital Object Identifier (DOI) |
| D2 | Book Digital Object Identifier (DOI) |
| EA | Early access date |
| EY | Early access year |
| PG | Page Count |
| P2 | Chapter Count (Book Citation Index) |
| WC | Web of Science Categories |
| SC | Research Areas |
| GA | Document Delivery Number |
| PM | PubMed ID |
| UT | Accession Number |
| OA | Open Access Indicator |
| HP | ESI Hot Paper. Note that this field is valued only for ESI subscribers. |
| HC | ESI Highly Cited Paper. Note that this field is valued only for ESI subscribers. |
| DA | Date this report was generated. |
| ER | End of Record |
| EF | End of File |
--------------------
