### Branch

- 분기점을 생성하여 독립적으로 코드를 변경할 수 있도록 도와주는 모델

### 📌 새로운 프로젝트에 들어갈 때 루틴

**# 팀원일 때(우리는 신입이니까 이 경우만 작성하겠습니다 🥸)**

1. **가장 먼저 어떤 작업을 할 지를 적기 위해** **Issue를 작성합니다.**  
>> 팀장(상사)가 만든 repository > issues > New issue > issue 작성 > Submit

2.  **Fork 하고 clone을 합니다.** 

**‼️ 주의 ‼️ **팀원은 main branch에서 작업하면 안됩니다 ! ~~회사에서 이러면 호온~나요~~** 

1. **git-flow 사용을 위해 초기화합니다.** 
>> **git flow init** 
2. **'develop' 브랜치에서 작업을 바로 시작하기 보다는 feature branch를 만들어 작업을 진행합니다.
>> git flow feature start 브랜치명**
3. **작업 후, git add > git commit > git push** 
*참고로 commit은 기능의 최소 단위로 올리는 연습을 하는 것이 좋습니다.* 
4. **브랜치를 'develop'에 병합(merge) 후 기능 브랜치를 삭제합니다. 삭제가 완료되면 'develop' 브랜치로 
전환합니다.**
>> **git flow feature finish 브랜치명**
5. **push 작업**
>> **git push -u origin develop**
6. **fork한 레파지토리 > Pull requests > New pull request**

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c337b28-b2c0-478b-b595-0178b03255a0/스크린샷_2021-07-28_오후_11.31.24.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1c337b28-b2c0-478b-b595-0178b03255a0/스크린샷_2021-07-28_오후_11.31.24.png)

    **위 사진처럼 나의 레파지토리의 develop에서 팀장(상사)의 레파지토리 develop로 가게해야합니다.** 
    ~~main으로 보내면 호온~납니다.~~

7. **내가 작업을 끝낸 issue가 무엇인지 title에 작성합니다. 내용에는 미리 작성했던 issue 번호를 입력하여 issue #1과 지금 작성하는 Pull requests가 연결되어 유기적으로 동작됩니다.** 

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/867897a9-0909-4adf-9789-e2da93af47f2/스크린샷_2021-07-28_오후_11.35.47.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/867897a9-0909-4adf-9789-e2da93af47f2/스크린샷_2021-07-28_오후_11.35.47.png)

8. **팀원은 Approve가 날 때까지 기다립니다.** 

### develop로 puch할 때 충돌이 일어나는 경우 😵

팀 작업을 할 때 일어나는 흔한 문제입니다. 충돌이 일어나는 이유는 branch를 병합할 때 main branch가 변화되어 있을 때 위 같은 에러가 나게 됩니다. 이럴 때는 2가지 방법이 있습니다. 

1. 충돌이 일어나는 둘 중에 하나를 선택
2. 두 개를 조합

이 2가지 모두 팀원과 상의를 하여 충돌을 해결합니다. 

### 충돌 해결 후 커밋 메시지 작성

어떻게 해결했는지 자세히 작성 후 커밋하는 것이 좋습니다. 

### merge 히스토리는 남는다.

insights > Network > merge 내역 확인 

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/277a7302-9e77-475a-988b-d574abb2c012/스크린샷_2021-07-28_오후_1.49.28.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/277a7302-9e77-475a-988b-d574abb2c012/스크린샷_2021-07-28_오후_1.49.28.png)

### 💩 Git requested URL returned Error 403 해결방법

### **발생이유**

`git the requested URL returend error : 403`이 발생하는 이유는 다양한 편입니다. 저의 경우 코드를 작성하고 깃허브에 세팅하고 첫 푸쉬를 실행할 때 403 에러가 발생했습니다.

### **해결방법**

아래의 코드를 통해 깃허브 레퍼지토리에 대한 접근 권한/인증을 받으면 됩니다.

> git remote set-url origin https:*//github-username@github.com/github-username/github-repository-name.git*

1. 터미널 창을 실행하고 명령어 입력하여 깃헙 레퍼지토리와 연결
2. github-username -> github 에서 사용하는 username
3. github-repository-name -> github에 코드를 추가하고자 하는 repository name 명

이 포스트에서 사용하는 명령어는 원격 저장소와 작성한 코드를 연결하기 위한 것과 연관이 되어 있습니다. [깃 학습 사이트](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-%EB%B2%84%EC%A0%84-%EA%B4%80%EB%A6%AC%EB%9E%80%3F)를 이용하세요
