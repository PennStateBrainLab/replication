#!/usr/bin/env python
import os
import logging
import sqlite3
import json

logging.basicConfig(level=logging.INFO)

articles_db = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "../data/processed/database/articles.db",
)

conn = sqlite3.connect(articles_db, isolation_level=None)

conn.execute("PRAGMA journal_mode = OFF;")
conn.execute("PRAGMA synchronous = 0;")
conn.execute("PRAGMA cache_size = 1000000;")  # give it a GB
conn.execute("PRAGMA locking_mode = EXCLUSIVE;")
conn.execute("PRAGMA temp_store = MEMORY;")
c = conn.cursor()
c.execute(
    """
    CREATE TABLE IF NOT EXISTS s2raw (
    id TEXT,
    title TEXT,
    paperAbstract TEXT,
    authors TEXT,
    inCitations TEXT,
    outCitations TEXT,
    year INTEGER,
    s2Url TEXT,
    sources TEXT,
    pdfUrls TEXT,
    venue TEXT,
    journalName TEXT,
    journalVolume TEXT,
    journalPages TEXT,
    doi TEXT,
    doiUrl TEXT,
    pmid TEXT,
    fieldsOfStudy TEXT,
    magId TEXT,
    s2PdfUrl TEXT,
    entities TEXT
    );
    """
)
s2papers = json.load(open('../data/raw/s2_2021_06_01/downselected.json', 'r'))
sql = f""" INSERT INTO s2raw
    values({",".join(["?"] * 21)})
    """

for paper in s2papers:
    data = [str(x) for x in paper.values()]
    c.execute(sql, data)

c.execute(
    """
    CREATE TABLE IF NOT EXISTS s2authors (
    hid INTEGER PRIMARY KEY AUTOINCREMENT,
    id TEXT,
    name TEXT
    )
    """
)

conn.commit()
conn.close()
