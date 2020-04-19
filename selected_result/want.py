import os 
filelist = os.listdir("C:\\Users\\Phoenix\\Desktop\\selected_result")
filelist = [x for x in filelist if "jpg" in x]
for i in range(1,len(filelist)+1):
    os.rename("C:\\Users\\Phoenix\\Desktop\\selected_result\\"+filelist[i-1],"C:\\Users\\Phoenix\\Desktop\\selected_result\\{}.jpg".format(i))
print(filelist)