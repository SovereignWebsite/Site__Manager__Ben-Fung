import os
from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/opentype/inter/'
W,H=1200,630
bg=(14,32,44); teal=(94,200,170); ink=(236,240,238); muted=(160,178,184)
im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
# path motif: a line with five stops
y=560
d.line((80,y,1120,y),fill=(40,70,84),width=6)
for i,x in enumerate([80,340,600,860,1120]):
    r=14 if i==4 else 10
    d.ellipse((x-r,y-r,x+r,y+r),fill=teal if i==4 else bg,outline=teal,width=5)
face=Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','site','assets','img','ben-fung-400.jpg')).resize((330,330),Image.LANCZOS)
m=Image.new('L',(330,330),0); ImageDraw.Draw(m).ellipse((0,0,329,329),fill=255)
d.ellipse((72,82,418,428),fill=teal)
im.paste(face,(80,90),m)
f1=ImageFont.truetype(F+'InterDisplay-Bold.otf',104)
f2=ImageFont.truetype(F+'InterDisplay-Medium.otf',34)
f3=ImageFont.truetype(F+'Inter-SemiBold.otf',24)
d.text((480,100),'TECHNOLOGY DELIVERY',font=f3,fill=teal,spacing=0)
d.text((474,140),'Ben Fung',font=f1,fill=ink)
d.multiline_text((480,262),'Technology project and programme\nmanager. 25+ years in technology,\n~20 in project management and\ndelivery leadership.',font=f2,fill=muted,spacing=12)
d.text((80,488),'ben-fung.manager.sovereignweb.site',font=f3,fill=muted)
im.save(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','site','assets','share','card-1200x630.jpg'),quality=86,optimize=True,progressive=True)
