import yaml


class Config:

    def __init__(self, **kwargs) -> None:

        self.matrix_path = '../test.csv'
        if 'matrix_path' in kwargs:
            self.matrix_path = kwargs['matrix_path']

        self.processed_actions = {'sleep': 'SleepHandler'}
        if 'processed_actions' in kwargs:
            self.processed_actions = kwargs['processed_actions']

        self.field_mapping = {}
        if 'field_mapping' in kwargs:
            self.field_mapping = kwargs['field_mapping']

        self.nested_fields = []
        if 'nested_fields' in kwargs:
            self.nested_fields = kwargs['nested_fields']

        self.fields_to_drop = []
        if 'fields_to_drop' in kwargs:
            self.fields_to_drop = kwargs['fields_to_drop']

        self.fields_to_extract = []
        if 'fields_to_extract' in kwargs:
            self.fields_to_extract = kwargs['fields_to_extract']

        self.regenerate_id_fields = []
        if 'regenerate_id_fields' in kwargs:
            self.regenerate_id_fields = kwargs['regenerate_id_fields']

        self.regenerate_time_fields = []
        if 'regenerate_time_fields' in kwargs:
            self.regenerate_time_fields = kwargs['regenerate_time_fields']

        if 'processor_config' in kwargs:
            self.processor_config = kwargs['processor_config']

    @staticmethod
    def read_config(filepath: str) -> 'Config':
        with open(filepath) as file:
            data = yaml.safe_load(file)

        return Config(**data)
