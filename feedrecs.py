import os
import json


class FeedrecsEnv(object):

    def __init__(self, config_file='~/.feedrecs.json'):

        self.env_config = self.get_env_config(config_file)
        self.data_dir = self.get_data_dir()
        self.model_cache = None

    def get_env_config(self, config_location='~/.classer.json'):

        if '~' in config_location:
            config_location = os.path.expanduser(config_location)

        with open(config_location, 'r') as env_config_file:
            env_config = json.load(env_config_file)

        return env_config

    def get_data_dir(self):

        data_dir = self.env_config.get('data_dir')

        if '~' in data_dir:
            data_dir = os.path.expanduser(data_dir)

        if data_dir[-1] != '/':
            data_dir += '/'

        return data_dir

    def get_profiles():
        raise NotImplemented

    def add_profile(profile_name):
        raise NotImplemented
