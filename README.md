# Scientific reproducibility in the clinical neurosciences: if replication is the answer, then what are the questions?

This is the companion repository for the paper "Scientific reproducibility in the clinical neurosciences: if replication is the answer, then what are the questions?"  Including ALL data, code, and support material for the methods used there-in.  Not for open publication, due to restrictions on sharing of proprietary data.

## Repository Structure

Based on [Edward Ma's DS project template](https://github.com/makcedward/ds_project_template)

Here is the explantation of folder strucure:
  .
  ├── data                              # All source data
  │   ├── processed                     # Any data resulting from processing, automatic or manual
  │   │   ├── database                  # sqlite3 database for articles
  │   │   └── vosviewer                 # processed data created with VOSviewer
  │   └── raw                           # All untouched data
  │       ├── s2_2021_06_01             # Semantic Scholar data
  │       └── webofscience_2021_06_21   # Web of Science data
  ├── docs                              # Documentation / Drafts
  ├── notebook                          # Jupyter / R Notebooks
  │   └── eda                           # Exploratory data analysis
  ├── replication                       # All source code
  │   ├── preparation                   # Source code for data processing
  │   └── processing                    # Source code for data preparation
  └── test                              # All software testing goes here

