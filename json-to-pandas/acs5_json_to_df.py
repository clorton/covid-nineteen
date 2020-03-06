#! /usr/bin/env python3

"""
A quick python script that makes acs5_variable_listing.json into a pandas dataframe
with table IDs (BXXXXX) and concept.
"""

from argparse import ArgumentParser
import json
import pandas


def acs5_data_to_dataframe(data):

    variables = data["variables"]
    select = lambda k, v: (k.startswith("B") or k.startswith("C")) and "concept" in v
    tuples = [(key, value["concept"]) for key, value in variables.items() if select(key, value)]
    ids, concepts = zip(*tuples)

    df = pandas.DataFrame.from_dict({"id": ids, "concept": concepts}, orient="columns", columns=None) # columns=None means use all keys as columns

    return df


def acs5_file_to_dataframe(filename):

    with open(filename, "r") as input:
        data = json.load(input)

    df = acs5_data_to_dataframe(data)

    return df


def main(filename):

    df = acs5_file_to_dataframe(filename)

    print(f"{df.head(10)}")

    return


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--source", default="acs5_variable_listing.json")
    args = parser.parse_args()

    main(args.source)
