from scrapy.cmdline import execute
import os
import sys

def main():
    current_file_path = os.path.abspath(__file__)
    startup_folder = get_startup_folder()
    save_path = os.path.join(startup_folder, 'scrapy.bat')
    if not os.path.exists(save_path):
        bat_content = f'''
        @echo off
        python "{current_file_path}"
        '''
        with open(save_path, 'w') as file:
            file.write(bat_content)
    os.chdir(os.path.dirname(current_file_path))
    execute("scrapy crawl cq".split())



def get_startup_folder():
    if sys.platform == 'win32':
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        return startup_folder
    else:
        print("Unsupported platform.")
        return None
    



if __name__ == '__main__':
    main()