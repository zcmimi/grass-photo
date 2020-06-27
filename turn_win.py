import os
for root,dirs,files in os.walk(r"."):
      for file in files:
        x=os.path.join(root,file)
        if file.endswith('.jpg'):
            os.system("wt\cwebp %s -o %s.webp"%(x,x[0:-4]))
            os.remove(x)
        if file.endswith('.png'):
            os.system("wt\cwebp %s -o %s.webp"%(x,x[0:-4]))
            os.remove(x)
        if file.endswith('.gif'):
            os.system("wt\gif2webp %s -o %s.webp"%(x,x[0:-4]))
            os.remove(x)

print('finish')
input()