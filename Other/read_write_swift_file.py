# -*- coding:UTF-8 -*-

import os

def get_file_name(path):
    fileList = os.listdir(path)
    for sublist in fileList:
        subPath = os.path.join(path, sublist)
        if os.path.isdir(subPath):
            get_file_name(subPath)
        else:
            if os.path.splitext(sublist)[1] == '.swift':
                print(subPath)
        
if __name__ == '__main__':

    PATH = '/Users/Hanson/Desktop/ios-svn/ios-app/dingdong'
    get_file_name(PATH)