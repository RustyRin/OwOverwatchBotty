import json
import os.path


class BotSettingsDefault:
    def __init__(
            self,
            prefix="!ow",
            admin_ids=None,
            logging_channel_id="1103036573404110989"
    ):
        if admin_ids is None:
            admin_ids = ["183680648408465408"]

        self.prefix = prefix
        self.admin_ids = admin_ids
        self.logging_channel_id = logging_channel_id


class BotSettings(BotSettingsDefault):
    def __int__(self):
        pass

    def save(self):
        """Saves the current version of bot settings to JSON file"""

        # for whatever reason, dumps returns a string form of json
        # so i turn it from string to dict
        # there has to be a better way, but im tired
        json_object = json.dumps(self.__dict__)
        json_object = json.loads(json_object)
        f = open("./database/bot_info/bot_settings.json", mode="w")
        json.dump(json_object, f, indent=4)
        f.close()

    def set_prefix_bot(self, new_prefix: str):
        """Sets the bots default prefix"""
        self.prefix = new_prefix

    def add_amin_id(self, admin_id: str | int):
        """Appends a Discord User ID to the list of bot admins"""

        if isinstance(admin_id, int):
            admin_id = str(admin_id)
        elif isinstance(admin_id, str):
            pass
        else:
            raise ValueError("You can only supply admin_id in either str or int")

        self.admin_ids.append(admin_id)

    def set_logging_channel_id(self, channel_id):
        """Sets the channel that *bot* logs will be posted"""
        if isinstance(channel_id, int):
            channel_id = str(channel_id)
        elif isinstance(channel_id, str):
            pass
        else:
            raise ValueError("You can only supply channel_id in either str or int")

        self.logging_channel_id = channel_id


def load():
    if os.path.exists("./database/bot_info/bot_settings.json"):
        with open("./database/bot_info/bot_settings.json", encoding="utf-8") as f:
            json_file = json.load(f)

        return BotSettings(**json_file)

    else:
        return BotSettings()
