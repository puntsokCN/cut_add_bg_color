from PIL import Image

# 去除背景后的图片
# 白 w  （255，255，255）
# 蓝 b  (67 ,142, 219)
# 红 r  (255, 0, 0 )
path = '%s\\'%os.getcwd() + filename
def add_bg_color():
    color = input('请输入需要的背景颜色： \n')
    if color is 'w': 
        img = Image.open(r'test.jpg_no_bg.png').convert("RGBA")
        x, y = img.size
        card = Image.new("RGBA", img.size, (255, 255, 255))
        card.paste(img, (0, 0, x, y), img)
        card.save("rere.jpg", format="png")
    if color is 'b': 
        img = Image.open(r'test.jpg_no_bg.png').convert("RGBA")
        x, y = img.size
        card = Image.new("RGBA", img.size, (67, 142, 219))
        card.paste(img, (0, 0, x, y), img)
        card.save("rere.jpg", format="png")
    if color is 'r': 
        img = Image.open(r'test.jpg_no_bg.png').convert("RGBA")
        x, y = img.size
        card = Image.new("RGBA", img.size, (255, 0, 0))
        card.paste(img, (0, 0, x, y), img)
        card.save("rere.jpg", format="png")
