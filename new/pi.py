from PIL import Image,ImageDraw,ImageFont
i=0
a=[31,28,31,30,31,30,31,31,30,31,30,31]
m=1
d=1
while m%13!=0:
    mon=str(m)
    day=str(d)
    str1=mon+"月"+day+"日"
    str2="今天老马依然是那么强！"
    img=Image.open("q.jpg")
    draw=ImageDraw.Draw(img)
    font=ImageFont.truetype("msyh.ttc",24)
    draw.text((10,240),str1,fill=(0,0,0),font=font)
    draw.text((10,280),str2,fill=(0,0,0),font=font)
    name=mon+"-"+day+".jpg"
    img.save(name)
    if d >= a[m-1]:
        d = 1
        m = m + 1
    else:
        d = d + 1

