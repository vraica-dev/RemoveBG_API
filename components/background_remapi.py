"""
idea - using the API from https://www.remove.bg/ process each pic in selected folder;
https://www.remove.bg/ comes with a free API key for 50 pic proc / month;
"""
from time import sleep
import os
import requests
from components.path_extracter import PathExtracter
from components.config import REMOVE_BACKGROUND_API_KEY
from components.utils import time_it_out


class BackgroundRemapi:
    API_ADD = r'https://api.remove.bg/v1.0/removebg'
    __extractor = PathExtracter()

    def __init__(self):
        self.pic_list = self.__extractor.get_list_pics_path()

    def process_pic(self, pic_path: str):
        """
        sends the request to the API;
        contains picturea path the secret key;
        """
        api_resp = requests.post(
            self.API_ADD,
            files={'image_file': open(pic_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': REMOVE_BACKGROUND_API_KEY}
        )

        try:
            if api_resp.status_code == 402:
                raise NameError("Insufficient credits")
        except NameError:
            print("Insufficient credits.")
            return False
        else:
            if api_resp.status_code == 200:
                no_bg_name = os.path.join(self.__extractor.no_bg_folder_path, pic_path.split('\\')[-1])
                with open(no_bg_name, 'wb') as no_bg_pic:
                    no_bg_pic.write(api_resp.content)
                return True
            else:
                print(f"Error occured when processing pic - {pic_path}")
                return False

    @time_it_out
    def mass_processing(self):
        """
        proceses all the files; since there's a rate limit, concurrent downloading won't fit;
        api could process 500 pics per minue - sleeps for ~8 seconds between the pics;
        """

        continue_iter = True
        for pic_path in self.pic_list:

            while continue_iter:
                status_ = self.process_pic(pic_path)
                continue_iter = status_

                if continue_iter:
                    sleep(500 / 60)

