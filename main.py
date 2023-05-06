import os
import shutil
import time

from check_if_game_running import check_if_process_running
from path import original, target

if __name__ == '__main__':

    last_modified_time = os.path.getmtime(original)
    try:
        while True:
            if check_if_process_running('hoi4'):
                current_modified_time = os.path.getmtime(original)
                if current_modified_time > last_modified_time:
                    time.sleep(20)
                    file_stats = os.stat(original)
                    if file_stats.st_size == 0:
                        os.remove(original)
                    else:
                        time.sleep(30)
                        shutil.copyfile(original, target)

                    last_modified_time = current_modified_time
            else:
                time.sleep(60)
    except KeyboardInterrupt:
        print('\n')
