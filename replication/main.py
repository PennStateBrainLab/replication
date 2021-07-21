#!/usr/bin/env python
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:

import os
import sqlite3
import wosfile


def main():

    articles_db = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "../data/processed/database/articles.db",
    )

    wosdata = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "../data/processed/web_of_science/all_records.tsv",
    )

    wosrecords = list(wosfile.records_from(wosdata))

    conn = sqlite3.connect(articles_db)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS wosraw (
    hid INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id TEXT,
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
        'PT': 'TEXT',
        'AU': 'TEXT',
        'BA': 'TEXT',
        'BE': 'TEXT',
        'GP': 'TEXT',
        'AF': 'TEXT',
        'BF': 'TEXT',
        'CA': 'TEXT',
        'TI': 'TEXT',
        'SO': 'TEXT',
        'SE': 'TEXT',
        'BS': 'TEXT',
        'LA': 'TEXT',
        'DT': 'TEXT',
        'CT': 'TEXT',
        'CY': 'TEXT',
        'CL': 'TEXT',
        'SP': 'TEXT',
        'HO': 'TEXT',
        'DE': 'TEXT',
        'ID': 'TEXT',
        'AB': 'TEXT',
        'C1': 'TEXT',
        'RP': 'TEXT',
        'EM': 'TEXT',
        'RI': 'TEXT',
        'OI': 'TEXT',
        'FU': 'TEXT',
        'FX': 'TEXT',
        'CR': 'TEXT',
        'NR': 'INTEGER',
        'TC': 'INTEGER',
        'Z9': 'INTEGER',
        'U1': 'INTEGER',
        'U2': 'INTEGER',
        'PU': 'TEXT',
        'PI': 'TEXT',
        'PA': 'TEXT',
        'SN': 'TEXT',
        'EI': 'TEXT',
        'BN': 'TEXT',
        'J9': 'TEXT',
        'JI': 'TEXT',
        'PD': 'TEXT',
        'PY': 'TEXT',
        'VL': 'TEXT',
        'IS': 'TEXT',
        'PN': 'TEXT',
        'SU': 'TEXT',
        'SI': 'TEXT',
        'MA': 'TEXT',
        'BP': 'TEXT',
        'EP': 'TEXT',
        'AR': 'TEXT',
        'DI': 'TEXT',
        'D2': 'TEXT',
        'EA': 'TEXT',
        'PG': 'INTEGER',
        'WC': 'TEXT',
        'SC': 'TEXT',
        'GA': 'TEXT',
        'UT': 'TEXT',
        'PM': 'TEXT',
        'OA': 'TEXT',
        'HC': 'TEXT',
        'HP': 'TEXT',
        'DA': 'TEXT'
    }

    sql = ''' INSERT INTO wosraw
    values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    '''

    for rec in wosrecords:
        for key in rec.keys():
            if wos_columns[key] is None:
                rec[key] = 'None'
            elif wos_columns[key] == 'INTEGER':
                rec[key] = int(rec[key])
            else:
                rec[key] = str(rec[key])
        values = [str(None), rec.record_id]
        values.extend([str(rec.get(x)) for x in wos_columns.keys()])

        c.execute(sql, values)
    conn.close()


if __name__ == "__main__":
    main()
