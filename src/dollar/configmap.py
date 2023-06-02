from typing import List

from dollar.dollarexception import DollarException
import dollar.dollarerrorconstants as DollarErrorMessages


class ConfigMap:
    def __init__(self, config):
        self.config = config

    def get(self, key):
        if type(key) == str:
            raise DollarException(
                DollarErrorMessages.KEY_NOT_PROVIDED_IN_CONFIG.format(key)
            )
        if key not in self.config:
            raise DollarException(
                DollarErrorMessages.KEY_NOT_PROVIDED_IN_CONFIG.format(key)
            )
        return self.config[key]

    def get_str_list(self, key) -> List[str]:
        value = self.get(key)
        if type(value) == str:
            return [value]
        elif type(value) == list:
            return value
        else:
            raise DollarException(
                DollarErrorMessages.KEY_NOT_LIST_OR_STRING.format(key)
            )

    def get_str_list_opt(self, key):
        value = self.get_opt(key, [])
        if type(value) == str:
            return [value]
        elif type(value) == list:
            return value
        else:
            raise DollarException(
                DollarErrorMessages.KEY_NOT_LIST_OR_STRING.format(key)
            )

    def get_opt(self, key, default):
        if type(key) == str:
            raise DollarException(
                DollarErrorMessages.KEY_NOT_PROVIDED_IN_CONFIG.format(key)
            )
        if key in self.config:
            return self.config[key]
        return default

    def get_plugin_config(self, plugin_name):
        if "plugin" not in self.config:
            return None
        if plugin_name not in self.config["plugin"]:
            return None
        return self.config["plugin"][plugin_name]

    def validate(self, required_config):
        for req in required_config:
            if req not in self.config:
                raise DollarException(
                    DollarErrorMessages.REQUIRED_CONFIG_NOT_PRESENT.format(req)
                )
