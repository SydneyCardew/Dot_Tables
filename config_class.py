import os
import configparser as conf


class Configuration:
    """stores the config settings as a convenient object so that reading the config file can be minimised"""
    def __init__(self):
        try:
            self.retrieve_settings()
        except ValueError:
            print("Fatal Error: Bad Settings")

    def retrieve_settings(self):
        self.config = conf.ConfigParser()
        self.config.read(os.getcwd() + '/Settings/Config.ini')
        self.program_name = self.config['MAIN']['program_name']
        self.version = self.config['MAIN']['version']
        self.output_path = self.config['MAIN']['output_path']
        self.output_name = self.config['MAIN']['output_name']
        self.simple_header = self.config.getboolean('SIMPLE', 'header')
        self.advanced_header = self.config.getboolean('ADVANCED', 'header')
        self.advanced_border = self.config['ADVANCED']['border']
        self.advanced_background_color = self.config['ADVANCED']['background-color']
        self.advanced_header_color = self.config['ADVANCED']['header-color']

    def header_override(self, args):
        if args.header:
            self.simple_header = True
            self.advanced_header = True
        elif args.noheader:
            self.simple_header = False
            self.advanced_header = False

    def store_target(self, args):
        self.target = args.source

    def view(self):
        """generates the config output string and passes it to __repr__ and __str__"""
        string = f"Current configuration settings for {self.program_name} v.{self.version}.\n" \
                 f"Consult README.md for more details.\n\n"
        return string

    def __repr__(self):
        return self.view()

    def __str__(self):
        return self.view()
