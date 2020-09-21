### 구성 파일 디렉토리 구조 가이드 

volumes : docker 서비스 구성 파일 모음
- durumiApp
	- static : css, js , image 등 위치할 디렉토리. manifest.json 위치함. 
	- apicodes : 백엔드 파이썬 코드 위치
	- Models : 모델 설정 위치
	- templates : html 파일 위치 
	- Views : 뷰 파일 위치 

volumes-nginx : nginx 서비스 구성 파일 모음

css , js는 우선 html 파일에서 개발하면서 테스트 하고, 기능 추가 및 테스트 완료되면 파일 분리하여 static 디렉토리로 위치시킬 것 . 
> html 코드 상 수정은 서버 재시작 불필요하지만, 그 외 부분에 대한 수정은 서버를 재시작 해야 반영됨. 
> js는 map.html의 <script> 태그 내에서 테스트 하다가, 테스트 완료된 부분 그대로 복사해서 스태틱 디렉토리로 옮기면 됨. 
> css는 <style> 태그 내에서 테스트 하다가 js와 동일하게 적용하면 됨. 

파이썬 코드는 apicodes 에 모듈화하여 넣어서 사용. 
> view의 경우는 class 형 view는 views.py에 직접 추가하고, 함수형 view는 apicodes에 추가하여 모듈 형태로 imports 시킬 것. 



--------
### 서비스 구성요소

- #### main view 
	- URL : /Map  , View : apicodes/MapView.MapView
	- tripnote
	- 상세 view 
		- picture 
		- place 
	- menu
	- decision 
	- searchKeyword -> apicodes/Keyword.py 

---------
### 웹 페이지 제작 가이드

1. 반응형 웹 기반이므로 절대로 사이즈나 해상도 하드코딩 금지 
	> meta 태그에서 viewport 기반으로 고정/절대값 사용 말것. 퍼센트나 스케일 단위사용
	> 다만, 몇몇 크기의 경우 하드코딩 필요한 경우 있음 염두해둘것. 
2. 웹 페이지 로드시 한번에 모든 페이지를 미리 로드 해놓고, 사용자 선택에 따라 제일 앞에 보일 뷰만 교체하는 식으로 진행해야함.
	> 웹 로딩시 A, B, C 한번에 미리 로드해놓고, z-index 조절하는 식으로 제일 앞에 보일 페이지 교체. 
3. 각 메뉴가 독립적인 페이지를 가지게 제작. 
4. static 파일에서는 {% url } 로 파일 가져오는것 불가능하므로, 하드코딩으로 경로 넣을것. (url에 등록된 대로)
5. 테마 색상 코드 : 2196F3 / 9e9e9e , 8597aa , 44336, 9c27b0, 4caf50, ff5722 / f5f6f8

-------
### CSS / 자바스크립트 파일 정리 
카테고리 - catDiv.css

검색 결과창 , view, 지도 마커 - overlays.css

로그인 페이지, 기타 웹 페이지 - pageView.css

검색 div 관련, 우측메뉴 - searchMenuDiv.css

트립노트 - tripNote.css


------

