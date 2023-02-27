#!/usr/bin/env python3

import subprocess
import argparse
from PIL import Image, ImageOps

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("s1", type=float)
ap.add_argument("s2", type=float)
ap.add_argument("pattern", type=str)

args = ap.parse_args()

## DEALING WITH RGB= > grayscale conversion.
im = Image.open('input_0.png')
(ImageOps.grayscale(im)).save('input_0.png')


## CONTRAST ADJUSTEMENT
p = subprocess.run(['balance', 'irgb', str(args.s1), str(args.s2), 'input_0.png','input_0.sel_normalized.png'])

##MAIN PROGRAM CALL

if args.pattern == 'Columns':
    p = subprocess.run(['demo_MIRE', 'input_0.sel_normalized.png', 'output.png'])
    
else:
    im = Image.open('input_0.sel_normalized.png')
    (im.rotate(90)).save('input_0.sel_rot.png')

    p = subprocess.run(['demo_MIRE', 'input_0.sel_rot.png', 'output.png'])
    im = Image.open('output.png')
    (im.rotate(-90)).save('output.png')
    

    
    
    


@cherrypy.expose
@init_app
def result(self):
"""
display the algo results
"""
return self.tmpl_out("result.html",
                        height=image(self.work_dir
                                    + 'output.png').size[1])
