### 구성 파일 디렉토리 구조 가이드 

-------

volumes : docker 서비스 구성 파일 모음
- durumi
	- static : css, js , image 등 위치할 디렉토리
	- apitest / durumi / polls : 앱 구성 파일 위치할 디렉토리 
		- apicodes : 파이썬 코드 위치
		- Models : 모델 설정 위치
		- templates : html 파일 위치 

volumes-nginx : nginx 서비스 구성 파일 모음

css , js는 우선 html 파일에서 개발하면서 테스트 하고, 기능 추가 및 테스트 완료되면 파일 분리하여 static 디렉토리로 위치시킬 것 . 
> html 코드 상 수정은 서버 재시작 불필요하지만, 그 외 부분에 대한 수정은 서버를 재시작 해야 반영됨. 

파이썬 코드는 apicodes 에 모듈화하여 넣어서 사용. 
> view의 경우는 class 형 view는 views.py에 직접 추가하고, 함수형 view는 apicodes에 추가하여 모듈 형태로 imports 시킬 것. 



--------
### 서비스 구성요소
