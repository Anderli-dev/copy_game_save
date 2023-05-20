import os
import shutil
import time

from check_if_game_running import check_if_process_running
from path import original, target
    # original - path to the file to be copied
    # target - path to where it will be copied (with the name of the copy file)

if __name__ == '__main__':

    last_modified_time = os.path.getmtime(original)
    try:
        while True:
            if check_if_process_running('hoi4'):
                current_modified_time = os.path.getmtime(original)
                # checking  if need to copy by creation time
                if current_modified_time > last_modified_time:
                    time.sleep(20)
                    file_stats = os.stat(original)
                    # if file is damaged (weight 0 bits), deletes it and does not copy it
                    if file_stats.st_size == 0:
                        os.remove(original)
                    else:
                    # if file is okay, it will wait until the game writes all data and copies it
                        time.sleep(30)
                        shutil.copyfile(original, target)

                    last_modified_time = current_modified_time
            else:
                time.sleep(90)
    except KeyboardInterrupt:
        print('\n')
