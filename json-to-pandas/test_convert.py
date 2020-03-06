#! /usr/bin/env python3

from acs5_json_to_df import acs5_file_to_dataframe as convert

df = convert("acs5_variable_listing.json")
print(f"{df.head(5)}")
