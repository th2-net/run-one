import time

from action_handlers.abstract_action_handler import AbstractActionHandler
from util.util import Action


class SleepHandler(AbstractActionHandler):

    def process(self, action: Action):
        time.sleep(int(action.extra_data.get('Time', 0)) / 1000)
