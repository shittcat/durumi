// 지도 오버레이 마커/뷰 관련 스크립트 

function SetMarker(inum){
    var list = $.parseJSON(GlobalList[inum]);
    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(24, 35); 
    // 마커 이미지를 생성합니다    
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: new kakao.maps.LatLng(list['mapy'],list['mapx']), // 마커를 표시할 위치
        title : list['title'], // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image : markerImage, // 마커 이미지 
        mnum : inum
    });
    
    var content = 
            $('.itemOverlays').html()

    var overlay = new kakao.maps.CustomOverlay({
        content: content,  // 오버레이에 표시할 내용
        map: null,
        position: marker.getPosition(),   
    });

    markers.push(marker);
    overlays.push(overlay);
    
    kakao.maps.event.addListener(marker, 'click', function() {
        // markerClicked();
        var mtitle = marker.getTitle()
        var tmpcont = overlay.getContent().replace(/itemOverlays noMark/gi,'itemOverlays setMark');
        
        // 마커가 지도위에 처음으로 노출될 때의 스타일 설정 
       
        if(viewMode == 1){ //place view 일때
            tmpcont = tmpcont.replace(/place/,'place" style="width: 70vw; height: 40vh;"')              
        }
        else if(viewMode == -1){ //picture 일때
            tmpcont = tmpcont.replace(/place/,'place" style="transform: rotateY(0deg);"')
            tmpcont = tmpcont.replace(/picture/,'picture" style="width: 70vw; height: 40vh; transform: rotateY(0deg);"')  
        }

        var list = $.parseJSON(GlobalList[findListByTitle(mtitle)]);
        
        mtitle += "<br/> 도로명 주소 :"+list['addr1']
        mtitle += "<br/> 지번 주소 :"+list['addr2']
        
        tmpcont = tmpcont.replace(/placeContent/,mtitle);

        console.log(list);
        overlay.setContent(tmpcont);
        overlay.setMap(map);
    });
}    

function markerClicked() {
    $('.itemOverlays').css("display","block");
}

function findListByTitle(title){ //장소 이름으로 특정 JSON 리스트 찾아오기 
    for(idx in GlobalList){
        if($.parseJSON(GlobalList[idx])["title"] == title){
            return idx;
        }
    }
    return "fail" ;
}
    
    
function modeChange(){
    if(viewMode == 1){ //place -> picture 전환
        $(".place").css("width","0");
        $(".place").css("height","0");
        $(".place").css("transform","rotateY(180deg)");
        $(".picture").css("width","70vw");
        $(".picture").css("height","40vh");
        $(".picture").css("transform","rotateY(0deg)");
    }
    else if(viewMode == -1){ //picture -> place 전환 
        $(".place").css("width","70vw");
        $(".place").css("height","40vh");
        $(".place").css("transform","rotateY(0deg)");
        $(".picture").css("width","0");
        $(".picture").css("height","0");
        $(".picture").css("transform","rotateY(180deg)");
    }
    console.log(viewMode)
    viewMode *= -1;
}