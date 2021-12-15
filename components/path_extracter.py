import os


class PathExtracter:

    __ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def __init__(self):
        self.__param_file_path = os.path.join(self.__ROOT, 'folder_path.txt')
        self.__pic_folder_path = self.__extract_pic_folder_path()
        self.__pic_path_list = self.__read_paths()

        self.__create_no_bg_folder()

    def __extract_pic_folder_path(self):
        """
        reads the path of the folder containing the pictures to be processed
        """
        with open(self.__param_file_path, 'r') as f_add:
            return f_add.readline().strip('"')


    def __read_paths(self):
        """
        searches through all the file and if they are jpg then the full path is appended to the output list
        """
        all_pics = []
        for file_found in os.listdir(self.__pic_folder_path):
            if file_found.split('.')[-1] == 'jpg':
                all_pics.append(os.path.join(self.__pic_folder_path, file_found))

        return all_pics

    def __create_no_bg_folder(self):
        if os.path.exists(os.path.join(self.__pic_folder_path, 'no_bg_pics')):
            pass
        else:
            os.mkdir(os.path.join(self.__pic_folder_path, 'no_bg_pics'))

    @property
    def no_bg_folder_path(self):
        return os.path.join(self.__pic_folder_path, 'no_bg_pics')


    def get_list_pics_path(self):
        """
        provides the entire list of the pics to be processed
        """
        return self.__pic_path_list

