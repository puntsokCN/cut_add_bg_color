
from removebg import RemoveBg
from PIL import Image
import os, sys, time, show_process

readme = ('使用方法：\n' + 
'1. 本程序需要联网执行！\n' + 
'2. 将待抠图的图片 与本程序存放在同一文件夹下\n'+
'3. 运行程序，输入IDkey，输入图片文件名，请加上的对应的后缀名（例如 1.jpg）\n'+
'4. 可在该网址申领IDkey： https://www.remove.bg/api  每个账号可免费处理50张抠图\n' +
'5. 程序里的颜色选项： 白色--w   红色--r  黑色--b\n'
'备注：\n' +
'试用IDkey:  iGJuJtVhvPHZjVHLQdcdXHRp   若IDkey 已失效请前往上述网址邮箱注册申领！！\n' +
'在程序中选中key值 右键一下即可复制， 再到输入位置 右键可粘贴\n'
'如果无法复制粘贴可到 https://zhidao.baidu.com/question/509849100.html 查看解决方案\n' +
'by ： 阿甘整理\n')

print('-'*30, '欢迎使用本程序', '-'*30, '\n')
print('-'*20, '请将图片与本程序放在同一目录下', '-'*20, '\n')
print('-'*70)
print(readme)
print('-'*70)

idkey = input('>>>请输入IDkey，注意大小写：')
rmbg = RemoveBg(idkey, "error.log")
filename = input('>>>请输入图片的名称(请加上后缀名)：') 
path = '%s\\'%os.getcwd() + filename

# for pic in os.listdir(path) :
#     # rmbg.remove_background_from_img_file("%s\%s"%(path, pic))
#     rmbg.remove_background_from_img_file(path, pic)
print('*****  开始抠图!  *****')
rmbg.remove_background_from_img_file(path)


## 显示进度
max_steps = 100
process_bar = show_process.ShowProcess(max_steps, 'OK')
for i in range(max_steps):
    process_bar.show_process()
    time.sleep(0.01)


# 去除背景后的图片
# 白 w  （255，255，255）
# 蓝 b  (67 ,142, 219)
# 红 r  (255, 0, 0 )
bg_path = '%s\\'%os.getcwd() + filename + '_no_bg.png'
def add_bg_color():
    color = input('>>>请输入需要的背景颜色： \n')
    if color is 'w':
        print('开始为图片设置背景色：') 
        img = Image.open(r'%s'%bg_path).convert("RGBA")
        x, y = img.size
        card = Image.new("RGBA", img.size, (255, 255, 255))
        card.paste(img, (0, 0, x, y), img)
        card.save("re.jpg", format="png")
    if color is 'b':
        print('开始为图片设置背景色：') 
        img = Image.open(r'%s'%bg_path).convert("RGBA")
        x, y = img.size
        card = Image.new("RGBA", img.size, (67, 142, 219))
        card.paste(img, (0, 0, x, y), img)
        card.save("re.jpg", format="png")
    if color is 'r': 
        print('开始为图片设置背景色：')
        img = Image.open(r'%s'%bg_path).convert("RGBA")
        x, y = img.size
        card = Image.new("RGBA", img.size, (255, 0, 0))
        card.paste(img, (0, 0, x, y), img)
        card.save("re.jpg", format="png")

need_bg = input('*****' + '是否需要为您上背景色！y/n')

colors = ['w', 'r', 'b']

if need_bg is 'y'  :
    
    add_bg_color()
    ## 显示进度
    max_steps = 100
    process_bar = show_process.ShowProcess(max_steps, 'OK')
    for i in range(max_steps):
        process_bar.show_process()
        time.sleep(0.01)
else :
    print('-'*30 + '感谢使用' + '-'*30)

