import bios
api_key_file="/tmp/api_keys.yaml"
api_name="contextual_news"


class Config(object):

    def __init__(self) :
        
        try:
            self.app_settings=bios.read(api_key_file)[api_name]
            print(self.app_settings)
        except:
            raise Exception(f"can't read settings from {api_key_file}")

        try:
            self.secret_key=self.app_settings["secret_key"]
            if self.secret_key is None or self.secret_key == '' :
                raise Exception("Secret not set in config ")
        except:
            raise Exception(f"can't read secret key from {api_key_file}")

        
    


