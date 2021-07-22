#!/usr/bin/env python
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import os
import shutil
import gzip
import tempfile
import sqlite3

import wosfile


def main():

    articles_db = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "../data/processed/database/articles.db",
    )

    wosdata = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "../data/processed/web_of_science/all_records.tsv.gz",
    )

    conn = sqlite3.connect(articles_db, isolation_level=None)
    conn.execute('PRAGMA journal_mode = OFF;')
    conn.execute('PRAGMA synchronous = 0;')
    conn.execute('PRAGMA cache_size = 1000000;')  # give it a GB
    conn.execute('PRAGMA locking_mode = EXCLUSIVE;')
    conn.execute('PRAGMA temp_store = MEMORY;')
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS wosraw (
    hid INTEGER PRIMARY KEY AUTOINCREMENT,
    PT TEXT,
    AU TEXT,
    BA TEXT,
    BE TEXT,
    GP TEXT,
    AF TEXT,
    BF TEXT,
    CA TEXT,
    TI TEXT,
    SO TEXT,
    SE TEXT,
    BS TEXT,
    LA TEXT,
    DT TEXT,
    CT TEXT,
    CY TEXT,
    CL TEXT,
    SP TEXT,
    HO TEXT,
    DE TEXT,
    ID TEXT,
    AB TEXT,
    C1 TEXT,
    RP TEXT,
    EM TEXT,
    RI TEXT,
    OI TEXT,
    FU TEXT,
    FX TEXT,
    CR TEXT,
    NR INTEGER,
    TC INTEGER,
    Z9 INTEGER,
    U1 INTEGER,
    U2 INTEGER,
    PU TEXT,
    PI TEXT,
    PA TEXT,
    SN TEXT,
    EI TEXT,
    BN TEXT,
    J9 TEXT,
    JI TEXT,
    PD TEXT,
    PY TEXT,
    VL TEXT,
    wosIS TEXT,
    PN TEXT,
    SU TEXT,
    SI TEXT,
    MA TEXT,
    BP TEXT,
    EP TEXT,
    AR TEXT,
    DI TEXT,
    D2 TEXT,
    EA TEXT,
    PG INTEGER,
    WC TEXT,
    SC TEXT,
    GA TEXT,
    UT TEXT,
    PM TEXT,
    OA TEXT,
    HC TEXT,
    HP TEXT,
    DA TEXT
    );"""
    )

    wos_columns = {
        "PT": "TEXT",
        "AU": "TEXT",
        "BA": "TEXT",
        "BE": "TEXT",
        "GP": "TEXT",
        "AF": "TEXT",
        "BF": "TEXT",
        "CA": "TEXT",
        "TI": "TEXT",
        "SO": "TEXT",
        "SE": "TEXT",
        "BS": "TEXT",
        "LA": "TEXT",
        "DT": "TEXT",
        "CT": "TEXT",
        "CY": "TEXT",
        "CL": "TEXT",
        "SP": "TEXT",
        "HO": "TEXT",
        "DE": "TEXT",
        "ID": "TEXT",
        "AB": "TEXT",
        "C1": "TEXT",
        "RP": "TEXT",
        "EM": "TEXT",
        "RI": "TEXT",
        "OI": "TEXT",
        "FU": "TEXT",
        "FX": "TEXT",
        "CR": "TEXT",
        "NR": "INTEGER",
        "TC": "INTEGER",
        "Z9": "INTEGER",
        "U1": "INTEGER",
        "U2": "INTEGER",
        "PU": "TEXT",
        "PI": "TEXT",
        "PA": "TEXT",
        "SN": "TEXT",
        "EI": "TEXT",
        "BN": "TEXT",
        "J9": "TEXT",
        "JI": "TEXT",
        "PD": "TEXT",
        "PY": "TEXT",
        "VL": "TEXT",
        "IS": "TEXT",
        "PN": "TEXT",
        "SU": "TEXT",
        "SI": "TEXT",
        "MA": "TEXT",
        "BP": "TEXT",
        "EP": "TEXT",
        "AR": "TEXT",
        "DI": "TEXT",
        "D2": "TEXT",
        "EA": "TEXT",
        "PG": "INTEGER",
        "WC": "TEXT",
        "SC": "TEXT",
        "GA": "TEXT",
        "UT": "TEXT",
        "PM": "TEXT",
        "OA": "TEXT",
        "HC": "TEXT",
        "HP": "TEXT",
        "DA": "TEXT",
    }

    sql = f""" INSERT INTO wosraw
    values({",".join(["?"] * 68)})
    """
    wosrecords = []
    with tempfile.TemporaryDirectory() as temp_dir:
        with gzip.open(wosdata, "rb") as f_in, open(
            os.path.join(temp_dir, "wosfile.tsv"), "wb"
        ) as f_out:
            rawdata = f_in.read()
            f_out.write(rawdata)
        wosrecords = list(wosfile.records_from(os.path.join(temp_dir, "wosfile.tsv")))

    for rec in wosrecords:
        record_dict = {}
        for key in rec.keys():
            if wos_columns[key] == "TEXT" and rec[key] is not None:
                record_dict[key] = str(rec[key])
            else:
                try:
                    record_dict[key] = int(rec[key])
                except ValueError:
                    pass
                    print(f"{len(rec)}\n {rec=} {rec[key]=}")
        values = [None]
        values.extend([record_dict.get(x, "NULL") for x in wos_columns.keys()])
        c.execute(sql, values)
        conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
