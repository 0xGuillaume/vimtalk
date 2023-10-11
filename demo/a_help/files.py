"""Vim talk demo."""
import csv
import json
import yaml


class Csv:
    """Custom methods to interract with csv files."""

    def __init__(self):
        """Inits Csv class."""

    @classmethod
    def read(cls, file:str) -> list:
        """Read csv file."""

        with open(file, "r", encoding="UTF-8") as file_:
            reader = csv.reader(file_)

            return list(reader)

    @classmethod
    def write(cls, file:str, fields:list, content:list) -> None:
        """Put headers and list down into a csv file."""

        with open(file, "w", encoding="UTF-8", newline='') as file_:
            writer = csv.writer(file_)
            writer.writerow(fields)
            writer.writerows(content)

    @classmethod
    def write_dict(cls, file:str, fields:list, content:dict) -> None:
        """Put headers and dictionnary down into a csv file."""

        with open(file, "w", encoding="UTF-8") as file_:
            writer = csv.DictWriter(file_, fieldnames=fields)
            writer.writeheader()
            writer.writerows(content)
