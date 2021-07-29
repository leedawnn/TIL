### 📌 hexo를 활용한 github pages에 blog 생성과 포스트 작성

**매번 블로그에 글을 올릴 때,** **static page라서 generate를 할 때 마다, 아래의 명령어를 수행해야 합니다.**

찌꺼기 파일들을 다 지우고 generate해주는 것이 좋습니다. 이렇게 해도 md파일은 지워지지 않습니다 ☺️

>> **hexo clean && hexo generate**

### 📌 hexo 사용법

페이지를 수정하고 적용할 때 clean, generate하고 hexo server로 확인한 다음에 괜찮다면 clean, deploy 해서 배포하는 사이클입니다. 

- hexo post >> 글쓰고
- hexo server >> 로컬에서 어떻게 보여지는지 먼저 확인해서 마음에 들면
- hexo deploy >> 배포 ~

### **Create a new post**

**$ hexo new "My New Post"**

More info: [Writing](https://hexo.io/docs/writing.html)

### **Run server**

**$ hexo server**

More info: [Server](https://hexo.io/docs/server.html)

### **Generate static files**

**$ hexo generate**

More info: [Generating](https://hexo.io/docs/generating.html)

### **Deploy to remote sites**

**$ hexo deploy**

More info: [Deployment](https://hexo.io/docs/one-command-deployment.html)

** **command + shift + R** >> 이렇게 해야 예전 캐시파일을 지우고 새로 페이지를 업로드합니다. 프로젝트 하면서 새로고침할 때 이렇게 하는 것이 좋습니다.
