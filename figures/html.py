import os 

# 设置要处理的文件夹路径  
folder_path = './'  # 替换为你的图片文件夹路径  
output_html = '../main.html'           # 输出的 HTML 文件名  

# 获取该文件夹下的所有图片文件  
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]  

# 生成 HTML 内容  
html_content = '''  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Image Gallery</title>  
    <style>  
        body {  
            font-family: Arial, sans-serif;  
            margin: 20px;  
        }  
        .gallery {  
            display: flex;  
            flex-wrap: wrap;  
            justify-content: space-between;  
        }  
        .gallery img {  
            width: 32%; /* 每行三个图片 */  
            margin-bottom: 10px;  
        }  
    </style>  
</head>  
<body>  
    <h1>Image Gallery</h1>  
    <div class="gallery">  
'''  

# 添加图像到 HTML 内容  
for image_file in image_files:  
    image_path = os.path.join(folder_path, image_file)  
    html_content += f'        <img src="figures/{image_path}" alt="{image_file}">\n'  

# 结束 HTML 内容  
html_content += '''  
    </div>  
</body>  
</html>  
'''  

# 将内容写入 HTML 文件  
with open(output_html, 'w') as f:  
    f.write(html_content)  

print(f'HTML gallery has been created: {output_html}')
