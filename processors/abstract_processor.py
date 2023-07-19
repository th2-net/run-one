from importlib import import_module
from typing import Type

from action_handlers.abstract_action_handler import AbstractActionHandler
from util.util import Action


class AbstractProcessor:

    def load_action_handlers(self, processed_actions_mapping: dict) -> dict[str, Type[AbstractActionHandler]]:
        result = {}
        for action, handler_name in processed_actions_mapping.items():
            action_handler_module = import_module(f'action_handlers.{handler_name}')
            action_handler_class = getattr(action_handler_module, handler_name)
            result[action] = action_handler_class
        return result

    def process(self, test_cases: dict[str, list[Action]]):
        """
        Process test cases
        :param test_cases: collection of test cases: test case name to list of its actions
        """
        pass


if __name__ == '__main__':
    ap = AbstractProcessor()
    r = ap.load_action_handlers({'send1': 'TH2ActHandler', 'send2': 'TH2ActHandler'})
    print()
