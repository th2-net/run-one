from processors.th2_processor import Th2Processor
from util.config import Config
from util.util import read_csv_matrix

if __name__ == '__main__':
    config = Config.read_config('config.yaml')
    actions = read_csv_matrix(config.matrix_path, config)
    th2_processor = Th2Processor(config)
    try:
        th2_processor.process(actions)
    finally:
        th2_processor.close()
