from run_one import Th2Processor
from run_one import Config
from run_one import read_csv_matrix

if __name__ == '__main__':
    config = Config.read_config('config.yaml')
    actions = read_csv_matrix(config.matrix_path, config)
    th2_processor = Th2Processor(config)
    try:
        th2_processor.process(actions)
    finally:
        th2_processor.close()
