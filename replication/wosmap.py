#!/usr/bin/env python
# Some notes:
# 'UT' is the WOS unique ID
# 'CR' is the Cited References
# 'DI' is the DOI
# there are 1481 papers in the dataset without a DI
# there are 4 papers in the dataset that the record_id method fails with KeyError
#   3 of which are reports:
#     "Alzheimer's Association Report 2011 Alzheimer's disease facts and figures",
#     "Alzheimer's Association Report 2015 Alzheimer's disease facts and figures",
#     "2012 Alzheimer's disease facts and figures"
#   1 is an article
#     'Tackling in Youth Football',
#   All have UT and DI
# there is 1 paper in the dataset without a UT
#   That paper's UT is in SU? (WOS:000337092900018)
#   That paper's DI is in J9?
#   This is also the only paper without a DI and UT

import pathlib
import re

import networkx as nx

import wosfile


def create_record_id(record):
    try:
        return record.record_id
    except KeyError:
        # don't use get method below, want an error if this fails
        return f"{record['UT']}, {record['DI']}"


def get_doi_from_cr(ref):
    doi_match = re.compile(r"^\s*DOI.*$")
    ref = ref.split(",")
    for item in ref:
        if re.match(doi_match, item):
            return item.lstrip()


def reliable_doi(paper):
    return paper.get("DI", paper.get("UT", paper.get("SU")))


def main():
    G = nx.DiGraph()
    nodes_in_data = set()

    data = list(
        wosfile.records_from(
            (pathlib.Path(__file__).parent / ".." / "data" / "raw" / "web_of_science_2021_06_21").resolve().glob("*.txt")
        )
    )
    output_data = (pathlib.Path(__file__).parent / ".." / "data" / "processed" / "web_of_science").resolve() / "reference.net"

    record_ids = [create_record_id(x) for x in data]

    for idx, paper in enumerate(data):
        paper_node = reliable_doi(data[idx])
        # print(f"working on {paper_node=}")
        print(nx.info(G))
        nodes_in_data.add(paper_node)
        for reference in paper.get("CR", []):
            # print(f"working on {reference=}")
            if reference in record_ids:
                reference_doi = reliable_doi(data[record_ids.index(reference)])
                G.add_edge(paper_node, reference_doi)
                G.nodes[paper_node].update(
                    {
                        "Abstract": str(paper.get("AB")),
                        "Title": str(paper.get("TI")),
                        "JournalName": str(paper.get("SO")),
                        "Keywords": str(paper.get("ID")),
                        "Year": str(paper.get("PY")),
                    }
                )

    G.remove_nodes_from(set(G) - nodes_in_data)
    nx.write_pajek(G, output_data)


if __name__ == "__main__":
    main()
