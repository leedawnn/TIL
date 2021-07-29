### git ignore 설정

**안하면 clone 할 때 용량이 너무 커져서 다운받을 때 시간이 엄청 오래 걸리게 됩니다.** ~~팀원이 욕할 수 있음ㅋ..~~ 아래 웹사이트에서 개발환경에 맞는 git ignore파일을 긁어서 해당 레파지토리에 있는 .gitignore에 붙여넣기 해주면 됩니다. 

[gitignore.io](http://gitignore.io)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6fe4bbd5-43ac-4a59-99d0-7b85f1a9f506/스크린샷_2021-07-28_오후_3.30.01.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6fe4bbd5-43ac-4a59-99d0-7b85f1a9f506/스크린샷_2021-07-28_오후_3.30.01.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/582b7211-72ba-4391-bc40-e949a60c1c96/스크린샷_2021-07-28_오후_3.37.24.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/582b7211-72ba-4391-bc40-e949a60c1c96/스크린샷_2021-07-28_오후_3.37.24.png)

위에서 음영된 부분이 main stream입니다. 보통 PM이 main branch를 만들면, fork로 main을 clone하여develop에서 작업합니다. feature은 develop를 clone해서 우리 같은 신입이 작업해서 팀장한테 넘겨줍니다. hotfix는 긴급패치가 이루어집니다. 이름처럼 아주 뜨거운 이슈에 대해서 fix하는 곳이라고 알아두면 되겠습니다. release에서는 개발이 이루어지지 않습니다. release를 하면 local에서 작업한 것 !! 깃헙까지 보내려면 push를 반드시 해야합니다 !! 

>> git push -u origin develop(이 과정은 한번만 하면 됩니다.)

### tagging도 push 해야한다

>> **git push --tags**

아래와 같이 tag에서는 release 버전을 확인 할 수 있습니다. 

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ef35aab2-df52-4f3a-b3e7-f8332688e392/스크린샷_2021-07-28_오후_4.39.43.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ef35aab2-df52-4f3a-b3e7-f8332688e392/스크린샷_2021-07-28_오후_4.39.43.png)

### 버전 네이밍

보통 v1.0 or v1.0.0 같이 2자리 혹은 3자리로 씁니다.(팀 by 팀, 회사 by 회사) 

v0.1로 시작해서 발전을 시키다가 v1.0이 되었을 때 정식버전으로 출시하는 게 일반적입니다. 

- 뒷 자리(끝자리) 올릴 때 : 마이너한 기능변화가 있을 때(디자인, 버그 수정 등)
- 앞 자리를 올릴 때 : 큰 기능의 변화가 있을 때

### 되돌리기(Revert)

레포 안에서 파일 이동 or 파일 이름바꾸기 하려면 mv로 하면 안됩니다.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d568307-b270-43df-9357-9b6f29e8e8bb/스크린샷_2021-07-28_오후_4.44.02.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d568307-b270-43df-9357-9b6f29e8e8bb/스크린샷_2021-07-28_오후_4.44.02.png)

mv로 이름을 바꾸게 되면 위의 사진처럼 원래 파일을 삭제하고, 추적을 하지 않는 파일로 되어 연속성을 깨지기 때문에, 어떤 오브젝트의 히스토리를 볼 때 방해가 됩니다. **그러므로, git mv [hello.py](http://hello.py/) [world.py](http://world.py/) 이런식으로 하는 것이 좋습니다.**

### Undoing(작업 취소)

변경사항을 취소하고 싶을 때 사용하는 명령어 

>> **git restore** 파일명

** 모든 파일을 add하고 싶을 때 사용하는 명령어 

>> **git add .**

### Unstaging(스테이지에서 내리는 것)

>> **git reset HEAD** 파일명

### Commit 수정하기

commit이라는 건 타임 스탬프같은 쌓여있는 것이기 때문에, 중간에 커밋을 삭제할 수는 없습니다. 대신에 직전 커밋을 수정할 수는 있습니다. 

>> **git commit --amend(단, push하기 전일 때 수정할 수 있음 !!)**

### 이전 커밋으로 돌아가기(그러나 이전 버전으로 돌아가야합니다^^..)

**>> git rebase -i <commit>**

commit을 했는데, 잘못 적어서 이력을 남기지 않기 위해 

### Reset Commit

- Worst case: Reset

    ex) 직전 3개의 commit을 삭제한 후, remote에 강제 push

    >> **git reset —hard HEAD~3**

    >> **git push -f origin <branch>**

협업 시 다른 cloned repo에 존재하던 commit log로 인해 파일이 살아나거나, 과거 이력이 깔끔히 사라져 commit log tracking이 힘들어집니다. 

**solution: 잘못한 이력도 commit으로 박제하고 수정한 이력을 남기자!**

- Best case: Revert
ex) 현재 HEAD에서 직전의 3개의 commit을 순서대로 거슬러 올라가 해당 내역에 대해 commit, push 수행

>> **git revert —no-commit HEAD~3**

>> **git commit**

>> **git push origin <branch>**

잘못하기 전 과거로 돌아가 최신을 유지하면서 되돌렸다는 이력을 commit으로 남겨 모든 팀원이 이 사항을 공유하고 주지시킬 수 있음. 특히 어떤 파일을 삭제할 때는 revert를 이용해서 삭제하는 것이 좋습니다. reset을 사용하여 commit을 남겨놓지 않으면 삭제 해야될 파일인데 팀원 중 누가 이 파일을 가지고 작업하는 불상사가 일어날 수 있습니다. ~~만약 그것이 팀장이었다면 우리는..~~

### Milestones - 일주일 단위로 마쳐야 하는 기능 할 일을 만드는 것

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/25aaa43f-4aae-4529-9733-ecd51d82d177/스크린샷_2021-07-28_오후_5.42.15.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/25aaa43f-4aae-4529-9733-ecd51d82d177/스크린샷_2021-07-28_오후_5.42.15.png)

**Labels는 할 일이 어떤 카테고리에 속하는지 정하는 것입니다.**
