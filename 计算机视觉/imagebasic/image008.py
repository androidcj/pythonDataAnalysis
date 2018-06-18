#coding:utf-8

'''
Created on 2018年4月5日

@author: win7
'''
import cognitive_face as CF
import os

def run_main():
    key = '762e85b7f4c24c4b81f7b7f60211a31a'
    CF.Key.set(key)
    image_path = './images/big-bang-theory-group.jpg'
    face_list = CF.face.detect(image_path)
    print(face_list)
    print('检测出{}张人脸'.format(len(face_list)))
    return ''
    


if __name__ == '__main__':
    run_main()