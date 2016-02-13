# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:29:51 2016

@author: shreez
"""

import Image
import os
import glob

def crop(infile,height,width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(imgheight//height):
        for j in range(imgwidth//width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)

if __name__=='__main__':
    height, width = 92, 92    
    sat_dir = '/home/shreez/Documents/ML/NAIP/NAIP_LABELING/test/sat/*.tiff'
    map_dir = '/home/shreez/Documents/ML/NAIP/NAIP_LABELING/test/map/*.tiff'
    start_num = 100
    
    for fn in glob.glob(sat_dir):
        for k,piece in enumerate(crop(fn,height,width),start_num):
            img=Image.new('RGBA', (height,width))
            img.paste(piece)
            path1=os.path.join('/home/shreez/Documents/ML/NAIP/NAIP_LABELING/test/sat/tmp',"IMG-%s.tif" % k)
            path1=os.path.join('/home/shreez/Documents/ML/NAIP/NAIP_LABELING/test/sat/tmp',"IMG-%s.tif" % k)  
            img.save(path1)
            img.save(path2)
        
    
    sat_file='/home/shreez/Documents/ML/NAIP/NAIP_LABELING/test/sat/IMG_1.tif'
    map_file='/home/shreez/Documents/ML/NAIP/NAIP_LABELING/test/sat/IMG_1.tif'
    height=92
    width=92
    start_num=100
    for k,piece in enumerate(crop(infile,height,width),start_num):
        img=Image.new('RGBA', (height,width))
        img.paste(piece)
        path1=os.path.join('/home/shreez/Documents/ML/NAIP/NAIP_LABELING/test/sat/tmp',"IMG-%s.png" % k)
        path2=os.path.join('/home/shreez/Documents/ML/NAIP/NAIP_LABELING/test/sat/tmp',"IMG-%s.tif" % k)        
        img.save(path1)
        img.save(path2)