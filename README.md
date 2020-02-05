# Python_AutomationClass_Lec3

세 번째 수업은 직접 마우스로 파일을 옮기거나 삭제하는 것이 아닌 Python코드로 이와 같은 동작을 어떻게 하는지 학습했다.

코드 원본 파일은 [https://github.com/dbsghtmd99/Python_AutomationClass_Lec3](https://github.com/dbsghtmd99/Python_AutomationClass_Lec3) 에서 확인 가능하다.

## 1. 라이브러리 설명

1. shutil, os: 폴더 생성 또는 파일경로를 이용한 파일을 복사/이동/삭제/이름 변경의 기능을 제공

2. zipfile : 파일을 압축하거나 압축된 파일을 압축 해제하는 기능을 제공
   
## 2. 수업때 다루었던 모듈의 메소드

1. 폴더/파일의 존재 여부를 확인 (True 또는 False 반환)
```python
os.path.isdir('찾고자 하는 폴더명')
os.path.isfile('찾고자 하는 파일')
```

2. 새로운 폴더 생성
```python
os.mkdir('새로운 폴더 이름')
```

3. 폴더/파일의 이름 변경
```python
os.rename('before', 'after')
```

4. 파일을 복사/삭제/이동
```python
shutil.copy('복사 시킬 파일경로', '복사 될 경로')
shutil.remove('삭제할 파일 경로')
shutil.move('옮길 파일 경로', '옮길 경로')
```

5. 해당 디렉토리의 파일/폴더를 가져와 list로 반환
```python
os.listdir('경로')
```

6. zipfile 객체 생성후 압축파일 생성
```python
zip = zipfile.ZipFile('new.zip', 'w') # 이름, 모드
zip.write('temp.py', compress_type = zip.ZIP_DEFLATED)
zip.close()
```

7. 압축 풀기
```python
zip = zipfile.ZipFile('new.zip')
zip.extractall()
zip.close()
```


## 3. 연습문제
```Python
# 1 압축 푼다
# 2 새로운 폴더 만든다
# 3 ZIP파일만 새로운 폴더에 다 넣는다
# 4 위의 ZIP파일들을 각각 압축푼다
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
        shutil.move('C:\\Users\\HS YUN\\Desktop\\Project\\' + i, 
                    'C:\\Users\\HS YUN\\Desktop\\Project\\hw\\'+i)
    elif temp[-1] == 'txt':
        path = 'C:\\Users\\HS YUN\\Desktop\\Project\\'
        os.remove(path + i)


file = os.listdir('C:\\Users\\HS YUN\\Desktop\\Project\\hw')
os.mkdir('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip')
for i in file:
    temp = i.split('_')
    shutil.move('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\' + i, 
                'C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + i)
    os.rename('C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + i, 
                'C:\\Users\\HS YUN\\Desktop\\Project\\hw\\hw_zip\\' + \
                temp[-2] + '_' + temp[-1])



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

```
