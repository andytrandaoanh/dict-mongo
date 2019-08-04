import os, configparser


class ConfigHandler:
    config = configparser.ConfigParser()
    #do not remove this line - needed to preserve case
    config.optionxform = str

    CONFIG_FILE = "lexicon.ini"
    RECENT = 'RECENTS'
    RECENT_OPEN_FILE = 'RecentOpenFilePath'
    RECENT_OUTPUT_DIR = 'RecentOutputDirectory'
    RECENT_OPEN_FILE2 = 'RecentOpenFilePath2'
    RECENT_OUTPUT_DIR2 = 'RecentOutputDirectory2'
    
    
    RECENT_DATA = {}



    def prepare_default_config(self):

        self.RECENT_DATA[self.RECENT_OPEN_FILE] = os.path.join(os.getcwd(), self.CONFIG_FILE)
        self.RECENT_DATA[self.RECENT_OUTPUT_DIR] = os.getcwd()
        self.RECENT_DATA[self.RECENT_OPEN_FILE2] = os.path.join(os.getcwd(), self.CONFIG_FILE)
        self.RECENT_DATA[self.RECENT_OUTPUT_DIR2] = os.getcwd()


    def read_config(self):
        try:
            self.config.read(self.CONFIG_FILE)
            options = self.config.options(self.RECENT)
            for opt in options:
                self.RECENT_DATA[opt] = self.config.get(self.RECENT, opt)
        except Exception as e:
            self.reset_config_file()


    def write_config(self):
        cfgfile = open(self.CONFIG_FILE,'w')
        
        try:
            if not self.config.has_section(self.RECENT): 
                self.config.add_section(self.RECENT)
        
            for key, value in self.RECENT_DATA.items():
                self.config.set(self.RECENT, key, value)

            self.config.write(cfgfile)
        except Exception as e:
            print(e)

        cfgfile.close()


    def reset_config_file(self):
        self.prepare_default_config()
        self.write_config()



    def get_config_value(self, key):
        exists = os.path.isfile(self.CONFIG_FILE)
        if exists:
            self.read_config()

        else:
            self.prepare_default_config()
            
        return self.RECENT_DATA[key]



    def set_config_value(self, key, value):
        exists = os.path.isfile(self.CONFIG_FILE)
        if exists:
            self.read_config()
        else:
            self.prepare_default_config()

        self.RECENT_DATA[key] = value

        self.write_config()






def main():
    cf = ConfigHandler()
    cf.reset_config_file()

#cf.set_config_value(cf.RECENT_OUTPUT_DIR, "D:\\PYTHON")

#print(cf.get_config_value(cf.RECENT_OUTPUT_DIR))