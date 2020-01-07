import os
import commands
from PIL import Image

def get_file_list(path):
    left_list = []
    small_file_list = os.listdir(path + '/small')
    all_file_list = os.listdir(path)
    for file_name in all_file_list:
        if 'cover_' not in file_name and 'py' not in file_name and 'small' not in file_name and 'raw' not in file_name:
            left_list.append(file_name)
    return left_list, len(small_file_list)

def change_pic(file_name, index):
    print 'change %s' %file_name
    back_fix = file_name.split('.')[-1]
    img = Image.open(file_name)
    resize_img = img.resize((1366, 768))
    resize_img.save('small/cover_%d.%s' %(index, back_fix))
    mv_cmd = 'mv %s ./raw/' %file_name
    #print mv_cmd
    status, out = commands.getstatusoutput(mv_cmd)
    if status:
        print 'mv failed'
    

if __name__ == '__main__':
    #path = '/home/blackmax/Blog/BlackMax_Blog/source/_posts/cover'
    path = './'
    left_list, index = get_file_list(path)
    i = 0
    for left in left_list:
        change_pic(left, index + i)
        i += 1