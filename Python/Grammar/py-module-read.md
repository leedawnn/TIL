### 모듈 활용하기

```python
from <py파일 경로> import <변수, 함수 혹은 클래스명>
```

### 예제

```python
from my_email import Email
from my_news import News
from my_excel import Excel

m_email = Email()
m_news = News()
m_excel = Excel()
```

### import만 사용하기

- 모듈 안의 클래스, 함수 등을 명시하지 않고 모듈 자체만 가져옵니다.
- 모듈 안의 클래스, 함수 등을 사용할 때 모듈을 명시해야합니다.

```python
from my_email import Email 
import my_news
from my_excel import Excel 

m_email = Email()
m_news = my_news.News()
m_excel = Excel()
```

### from ~ import 심화

my_email.py가 testlib 폴더 밑에 있을 때 사용하고 싶은 경우 

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/06871489-6670-4b89-8e22-cad382d42ef5/스크린샷_2021-08-05_오후_4.57.43.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/06871489-6670-4b89-8e22-cad382d42ef5/스크린샷_2021-08-05_오후_4.57.43.png)

```python
from testlib.my_email import Email
from my_news import News
from my_excel import Excel
```

### __**name__내장변수 활용**

- 파이썬에는 기본적으로 여러 내장변수, 내장함수가 있습니다.
- 그 중 __name__은 해당 클래스를 어디에서 실행했는지 나타냅니다.
- import했을 때와 실행했을 때 차이가 있습니다. 
import 했을 때는 __name__변수가 __main__이 아닙니다. 직접 파일을 실행했을 때 __main__변수를 가집니다.

### 파일 입출력

# **파일 읽기 - read()**

- read() 함수를 통해 파일을 읽을 수 있습니다. 그러나 파일의 모든 내용을 가져오기 때문에 파일의 용량이 너무 크다면 파이썬 프로그램에 문제가 생길 수도 있습니다.

```python
datafile = open('data.txt', 'r')
data = datafile.read()
print(data)
```

# **파일 읽기 - readline()**

- readline() 함수를 이용해 파일의 내용을 한 줄씩 읽을 수도 있습니다.

```python
datafile = open('data.txt', 'r')

line = datafile.readline()
print(line) 

# print()는 자동 개행을 하기 때문에 한 줄 개행이 되어 출력됩니다. 
# 공백을 지우고 싶다면 strip()을 이용하여 detafile.readline().strip() 이렇게 사용해주면 됩니다.
```
