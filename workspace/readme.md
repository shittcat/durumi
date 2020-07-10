### 구성 파일 디렉토리 구조

volumes : docker 서비스 구성 파일 모음
- durumi
	- static : css, js , image 등 위치할 디렉토리
	- apitest / durumi / polls : 앱 구성 파일 위치할 디렉토리 
		- apicodes : 파이썬 코드 위치
		- Models : 모델 설정 위치
		- templates : html 파일 위치 

volumes-nginx : nginx 서비스 구성 파일 모음

css , javascript는 작성하여 static 디렉토리로 분리하여 위치시킬 것 . 
