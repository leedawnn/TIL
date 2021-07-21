# CLI 환경에서 git 사용하기 
## CLI 기본 명렁어
- cd
// 상위 폴더로 이동

- mkdir 폴더명 
// 새로운 폴더 생성

- rm
// 파일 삭제

- touch 파일명.확장자
// 파일 생성

- mv 이동할 파일명 이동할 경로
// 파일 이동

- cp 복사할 파일명 붙여넣을 곳
// 파일 복사

- mv 현재 파일명 바꿀 파일명
// 파일명 바꾸기

- rm server.* 
//(에시) server라는 이름을 가진 모든 파일 삭제

- rm -rf 폴더명 >> 안에 있는 모든파일을 지우고 너도 지워라
// 폴더를 삭제할 때는 반드시 폴더 안에  아무것도 없어야한다.

- ^C >> ctrl + C
// 현재 실행중인  작업 중지

## git objects 
- Blob : 파일 하나의 내용에 대한 정보(변경 사항)
- Tree : Blob이나 subtree의 메타데이터(디렉토리 위치, 속성, 이름 등)
- Commit : 커밋 순간의 스냅샷. 인터넷이 연결되지 않아도 Commit이 가능함

## git 기본 사용법 
- git status
// 리포지토리 상태 표시.

- git add 파일명
// 스테이지 영역(커밋 전 임시영역)에 파일 추가.

- git commit 
// 스테이지 영역에 기록된 시점들 파일을 실제 리포지토리에 커밋메시지와 함께 실재 내역에 반영.

- git push -u origin 브랜치명
// 로컬 리포에 있는 현재 브랜치 upstream이 origin 브랜치로 설정

## Commit Convention
- 커밋 제목은 50자 이내로 요약하여 작성한다
- 제목과 내용사이 한 칸
- prefix를 사용하여 한 눈에 커밋의 용도를 알기 쉽게 한다

feat: features
docs: documentations
conf: configurations
test: test
fix: bug-fix
refactor: refactoring
ci: Continuous Integration
build: Build
perf: Performance
