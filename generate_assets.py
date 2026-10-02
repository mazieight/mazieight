"""Generate original profile artwork. Requires Python and Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).parent / 'assets'
OUT.mkdir(exist_ok=True)
W, H = 1280, 300
font_dir = Path('C:/Windows/Fonts')
def font(name, size):
    return ImageFont.truetype(str(font_dir / name), size)

def frame(t):
    im = Image.new('RGB', (W, H), '#0c1627')
    d = ImageDraw.Draw(im)
    for x in range(0, W, 40):
        for y in range(0, H, 40):
            d.ellipse((x,y,x+2,y+2), fill='#1c2c40')
    d.rounded_rectangle((20,20,W-20,H-20), radius=22, outline='#2a4054', width=2)
    d.text((62,51), 'BUILD WITH INTENT.', font=font('segoeuib.ttf', 55), fill='#f3f7fc')
    d.text((66,137), 'Interface. Systems. Automation.', font=font('segoeui.ttf', 28), fill='#c1ccd9')
    d.line((66,206,600,206), fill='#32465a', width=2)
    d.text((66,229), 'MAZEIGHT  /  SAAD LAMAIZI', font=font('consola.ttf', 20), fill='#70e2ce')
    paths = [((830,70),(1030,70),(1100,140)), ((780,145),(920,145),(990,235),(1170,235)), ((850,245),(920,175),(1120,175))]
    for i, points in enumerate(paths):
        d.line(points, fill='#305666', width=3)
        for x,y in points:
            d.ellipse((x-5,y-5,x+5,y+5), fill='#6c9caa')
        lengths=[math.dist(a,b) for a,b in zip(points,points[1:])]
        distance=((t+i/3)%1)*sum(lengths)
        for a,b,length in zip(points,points[1:],lengths):
            if distance<=length:
                u=distance/length; x=a[0]+u*(b[0]-a[0]); y=a[1]+u*(b[1]-a[1])
                d.ellipse((x-8,y-8,x+8,y+8),fill='#244b53')
                d.ellipse((x-4,y-4,x+4,y+4),fill='#70e2ce')
                break
            distance-=length
    return im

frames=[frame(i/36) for i in range(36)]
frames[0].save(OUT/'header.png', optimize=True)
# Short finite animation: two cycles, with no flashing or moving text.
frames[0].save(OUT/'header.gif',save_all=True,append_images=frames[1:],duration=100,loop=1,optimize=True)
print({p.name:p.stat().st_size for p in OUT.iterdir()})
