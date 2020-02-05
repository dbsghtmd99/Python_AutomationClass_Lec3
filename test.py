# 1 압축 푼다
# 2 새로운 폴더 만든다
# 3 ZIP파일만 다 넣는다 새로운 폴더에는 ZIP파일만
# 4 위의 ZIP파일들을 각각 압축풀기
# 5 학번_이름으로 바꾸기
# 6 이 안에다 .cpp파일만 나머지 삭제
import zipfile
import os
import shutil
newZip = zipfile.ZipFile('C:\\Users\\HS YUN\\Desktop\\Project\\gradebook.zip')
newZip.extractall('C:\\Users\\HS YUN\\Desktop\\Project')
newZip.close()
os.remove('C:\\Users\\HS YUN\\Desktop\\Project\\gradebook.zip')

file = os.listdir('C:\\Users\\HS YUN\\Desktop\\Project')
os.mkdir('C:\\Users\\HS YUN\\Desktop\\Project\\hw')
for i in file:
    temp = i.split('.')
    if temp[-1] == 'zip':
        shutil.move('C:\\Users\\HS YUN\\Desktop\\Project\\' + i, 'C:\\Users\\HS YUN\\Desktop\\Project\\hw\\'+i)
    elif temp[-1] == 'txt':
        path = 'C:\\Users\\HS YUN\\Desktop\\Project\\'
        os.remove(path + i)


file = os.listdir('C:\\Users\\HS YUN\\Desktop\\Project\\hw')
os.mkdir('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip')
for i in file:
    temp = i.split('_')
    shutil.move('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\' + i, 'C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + i)
    os.rename('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + i, 'C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + temp[-2] + '_' + temp[-1])



file = os.listdir('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip')
for i in file:
    print(i)
    temp = zipfile.ZipFile('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + i)
    temp.extractall(path='C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip')
    temp.close()

file = os.listdir('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip')
for i in file:
    if os.path.isdir('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + i) == False:
        temp = i.split('.')
        print(temp)
        if temp[-1] == 'cpp':
            pass
        else:
            os.remove('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + i)
