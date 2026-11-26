import os
from PIL import Image, ImageDraw, ImageFont
F='/usr/share/fonts/opentype/inter/'; M='/usr/share/fonts/truetype/jetbrains-mono/'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','site','assets','share','')
face=Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','site','assets','img','ben-fung-400.jpg'))
def circ(im,size,xy,ring=None):
    f=face.resize((size,size),Image.LANCZOS); m=Image.new('L',(size,size),0); ImageDraw.Draw(m).ellipse((0,0,size-1,size-1),fill=255)
    if ring: ImageDraw.Draw(im).ellipse((xy[0]-8,xy[1]-8,xy[0]+size+8,xy[1]+size+8),fill=ring)
    im.paste(f,xy,m)

def save(im,n): im.save(OUT+n,quality=85,optimize=True,progressive=True)
# departures
im=Image.new('RGB',(1200,630),(11,12,14)); d=ImageDraw.Draw(im)
fm=ImageFont.truetype(M+'JetBrainsMono-Bold.ttf',92); fs=ImageFont.truetype(M+'JetBrainsMono-Regular.ttf',26)
d.text((70,60),'DEPARTURES · TECHNOLOGY DELIVERY',font=fs,fill=(255,194,61))
x=70
for ch in 'BEN FUNG':
    if ch==' ': x+=40; continue
    d.rounded_rectangle((x,110,x+96,250),8,fill=(38,42,49)); d.rectangle((x,178,x+96,182),fill=(11,12,14))
    d.text((x+48,180),ch,font=fm,fill=(243,241,234),anchor='mm'); x+=104
d.line((70,290,1130,290),fill=(255,194,61),width=3)
rows=[('2026','GATWICK AIRPORT','£1M AVOIDED'),('2023','EASYJET','ON DEADLINE'),('2022','LSEG','ON SCHEDULE')]
for i,(a,b,c) in enumerate(rows):
    y=315+i*70; d.rounded_rectangle((70,y,1130,y+58),6,fill=(31,34,40))
    d.text((90,y+29),a,font=fs,fill=(255,194,61),anchor='lm'); d.text((240,y+29),b,font=fs,fill=(243,241,234),anchor='lm')
    d.text((1110,y+29),c,font=fs,fill=(95,224,143),anchor='rm')
circ(im,150,(1000,85),ring=(255,194,61))
save(im,'card-departures.jpg')
# programme plan
im=Image.new('RGB',(1200,630),(238,241,245)); d=ImageDraw.Draw(im)
d.rounded_rectangle((40,40,1160,590),16,fill=(255,255,255),outline=(213,219,228),width=2)
fb=ImageFont.truetype(F+'InterDisplay-Bold.otf',80); fl=ImageFont.truetype(F+'Inter-SemiBold.otf',22); fr=ImageFont.truetype(F+'Inter-Regular.otf' if False else F+'InterDisplay-Medium.otf',30)
circ(im,130,(80,80))
d.text((240,85),'CAREER PROGRAMME · HIGHLIGHT REPORT',font=fl,fill=(71,85,105)); d.text((236,115),'Ben Fung',font=fb,fill=(20,33,61))
yrs=list(range(1997,2027)); x0,x1=120,1100; w=(x1-x0)/360
for i,y in enumerate(yrs):
    xx=x0+i*12*w; d.line((xx,300,xx,540),fill=(230,234,240),width=1)
    if y%5==0: d.text((xx+4,280),str(y),font=fl,fill=(71,85,105))
P=lambda s:tuple(map(int,s.split('-')))
bars=[[('1997-03','2000-10'),('2000-11','2003-02'),('2003-05','2006-10'),('2006-11','2007-04'),('2007-06','2008-05'),('2008-04','2009-03')],
      [('2009-04','2009-11'),('2010-02','2011-06'),('2011-11','2013-12'),('2014-03','2015-09'),('2015-10','2016-10')],
      [('2018-01','2018-10'),('2019-01','2019-04'),('2019-05','2019-08'),('2019-08','2020-01'),('2020-02','2020-05'),('2020-04','2020-11'),('2021-01','2021-03'),('2022-01','2022-02')],
      [('2022-05','2023-05'),('2023-09','2024-12'),('2025-02','2025-06'),('2026-01','2026-08')]]
cols=[(51,78,125),(74,111,165),(47,127,134),(29,78,216)]
for i,grp in enumerate(bars):
    for a_,b_ in grp:
        a,b=P(a_),P(b_); s=x0+((a[0]-1997)*12+a[1]-1)*w; e=x0+((b[0]-1997)*12+b[1])*w; y=330+i*52; d.rounded_rectangle((s,y,e,y+34),6,fill=cols[i])
d.text((120,555),'Technology programme and project delivery · since 1997',font=fl,fill=(20,33,61))
save(im,'card-programme-plan.jpg')
# line map
im=Image.new('RGB',(1200,630),(251,251,253)); d=ImageDraw.Draw(im)
for xx in range(0,1200,24):
    for yy in range(0,630,24): d.point((xx,yy),fill=(220,216,230))
P=(91,45,142); O=(179,71,0)
fb=ImageFont.truetype(F+'InterDisplay-Bold.otf',84); fn=ImageFont.truetype(F+'InterDisplay-Bold.otf',24); fz=ImageFont.truetype(F+'Inter-SemiBold.otf',18)
d.ellipse((70,60,150,140),outline=P,width=14); d.text((110,100),'BF',font=fn,fill=(22,20,31),anchor='mm')
d.text((180,55),'The Ben Fung Line',font=fb,fill=(22,20,31))
d.line((90,360,1110,360),fill=P,width=16)
st=[(90,'BACKGROUND','undated'),(290,'FINYX','2009'),(490,'EASYJET','2023'),(690,'TESSIANT · HX','2025'),(890,'GATWICK','2026')]
for x,n,z in st:
    d.ellipse((x-17,343,x+17,377),fill=(255,255,255),outline=(22,20,31),width=7); an='ls' if x==90 else 'ms'; xo=x-17 if x==90 else x; d.text((xo,320),n,font=fn,fill=(22,20,31),anchor=an); d.text((xo,410),z.upper(),font=fz,fill=(78,74,92),anchor=an)
d.rounded_rectangle((1080,334,1132,386),8,fill=P); d.text((1110,320),'NEXT',font=fn,fill=(22,20,31),anchor='ms')
d.line((200,500,1000,500),fill=O,width=10)
for x in (260,460,660,860): d.ellipse((x-12,488,x+12,512),fill=(255,255,255),outline=O,width=5)
d.text((200,470),'THE ASSIGNMENTS LOOP',font=fz,fill=O)
circ(im,120,(1010,55),ring=P)
save(im,'card-line-map.jpg')
