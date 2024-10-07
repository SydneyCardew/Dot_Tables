import os
import configparser as conf


class Configuration:
    """stores the config settings as a convenient object so that reading the config file can be minimised"""
    def __init__(self, config_seg):
        self.config_seg = config_seg
        try:
            self.retrieve_settings(config_seg)
        except ValueError:
            print("Fatal Error: Bad Settings")

    def retrieve_settings(self, config_seg):
        self.config = conf.ConfigParser()
        self.config.read(os.getcwd() + '\\Settings\\Config.ini')
        self.program_name = self.config[(config_seg)]['program_name']
        self.version = self.config[(config_seg)]['version']

    def view(self):
        """generates the config output string and passes it to __repr__ and __str__"""
        string = f"Current configuration settings for {self.program_name} v.{self.version}.\n" \
                 f"Consult README.md for more details.\n\n"
        return string

    def __repr__(self):
        return self.view()

    def __str__(self):
        return self.view()
