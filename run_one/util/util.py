from collections import defaultdict
from datetime import datetime
from itertools import tee
import json
from typing import Callable
import uuid

import pandas as pd

from run_one.util.config import Config


uid = str(uuid.uuid1())
counter = 0


class Action:

    def __init__(self, row: dict, extra_data: dict) -> None:
        self.row = row
        self.extra_data = extra_data

    def __repr__(self) -> str:
        return f'row={self.row}\nextra_data={self.extra_data}'


def generate_random_id(value: str = ''):
    global counter
    counter += 1
    if not value:
        return str(uuid.uuid1())
    return f'{uid[:len(value) - len(str(counter))]}{counter}'


def generate_time(time_format: str = '%Y-%m-%dT%H:%M:%S.%fZ'):
    return datetime.utcnow().strftime(time_format)


def read_csv_matrix(filepath: str,
                    config: Config,
                    id_function: Callable = generate_random_id,
                    time_function: Callable = generate_time) -> dict[str, list[Action]]:
    """
    Read matrix file
    :param str filepath: path to matrix file
    :param config: configuration class instance
    :param id_function: function to transform ID-like fields
    :param time_function: function to transform Time-like fields
    :return: Collection of filtered action_handlers combined by test cases
    """

    file = pd.read_csv(filepath)

    result = defaultdict(list)
    test_case_name = ''
    id_mapping, time_mapping = {}, {}

    for index, row in file.iterrows():

        seq = row.get('Seq')
        if seq == 'TEST_CASE_START':
            test_case_name = row.get('CaseName')
            continue
        elif seq == 'TEST_CASE_END':
            id_mapping.clear()
            time_mapping.clear()
            continue

        action = row.get('Action')

        if action in config.processed_actions:
            row.dropna(inplace=True)
            extracted_fields = row.get([field for field in config.fields_to_extract if field in row], [])
            row.drop(config.fields_to_drop + config.fields_to_extract, errors='ignore', inplace=True)
            row.rename(config.field_mapping, inplace=True)

            for field in config.nested_fields:
                if field in row and row[field] != '*':
                    row[field] = json.loads(row[field].replace("'", '"'))

            if id_function is not None:
                for field in config.regenerate_id_fields:
                    if field in row and row[field] != '*':
                        field_value = row[field]
                        if field_value.startswith('!='):
                            key = field_value[2:]
                            row[field] = f'!={id_mapping.setdefault(key, generate_random_id(key))}'
                        else:
                            row[field] = id_mapping.setdefault(field_value, generate_random_id(field_value))

            if time_function is not None:
                for field in config.regenerate_time_fields:
                    if field in row and row[field] != '*':
                        row[field] = time_mapping.setdefault(row[field], time_function())

            result[test_case_name].append(Action(row.to_dict(), extracted_fields.to_dict()))

    return result


def pairwise(iterable):
    """
    Return successive overlapping pairs taken from the input iterable.
    pairwise('ABCDEFG') --> AB BC CD DE EF FG
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
