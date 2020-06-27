import os
res='''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>草图收藏夹</title>
</head>
<body>
{0}
</body>
</html>
'''
node=""
for root,dirs,files in os.walk(r"."):
    for file in files:
        x=os.path.join(root,file)
        if file.endswith('.webp'):
            node+="<img src='%s' alt='%s'></img>"%(file,file[0:-5])

open('index.html',"w",encoding='utf-8').write(res.format(node))