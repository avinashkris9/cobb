import os
import logging

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from .slack import register_listeners


logging.basicConfig(level=logging.DEBUG)


def slack_starter():
    # Initialization
    app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

    # Register Listeners
    register_listeners(app)
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()


if __name__ == "__main__":
    slack_starter()
