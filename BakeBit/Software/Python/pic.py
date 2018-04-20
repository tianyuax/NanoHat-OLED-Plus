#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image,ImageDraw,ImageFont

def drawPic(num):
    width = 750
    height = 750
    bgcolor = (255,255,255)
    image = Image.new('RGB',(width,height),bgcolor)
    font = ImageFont.truetype('HATTEN.TTF',500)
    fontcolor = (0,0,0)
    draw = ImageDraw.Draw(image)
    draw.text((100,110),num+'%',font=font,fill=fontcolor)
    image.save('pic.png')
    del draw
    del image

if __name__ == '__main__':
     n="30"
     drawPic(n)
