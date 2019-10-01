import os
import shutil
del_extension = ['.tmp', '._mp', '.log', '.gid', '.chk', '.old', '.xlk', '.bak','.wbk','.xlk','.syd','.$$$','.@@@','.`*']
del_userprofile = ['cookies', 'recent', 'Temporary Internet Files', 'Temp']
del_windir = ['prefetch', 'temp']
root_sys_drive = os.environ['systemdrive'] + '\\'
root_user_profile = os.environ['userprofile']
root_win_dir = os.environ['windir']
def del_dir_or_file(root):
    try:
        if os.path.isfile(root):
            os.remove(root)
            print ('file: ' + root + ' removed')
        elif os.path.isdir(root):
            shutil.rmtree(root)
            print ('directory: ' + root + ' removed')
    except WindowsError:
        print ('failure: ' + root + " can't remove")
for roots, dirs, files in os.walk(root_sys_drive, topdown=False):
    for every_file in files:
        file_extension = os.path.splitext(every_file)[1]
        if file_extension in del_extension:
            full_path = os.path.join(roots, every_file)
            del_dir_or_file(full_path)
for every_dir in del_userprofile:
    full_path = os.path.join(root_user_profile, every_dir)
    del_dir_or_file(full_path)
for every_dir in del_windir:
    full_path = os.path.join(root_win_dir, every_dir)
    del_dir_or_file(full_path)
print ('\nfinished')
