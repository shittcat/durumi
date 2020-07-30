var SaveDiv;
var GlobalList;

// 마커 이미지의 이미지 주소입니다
var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 

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
        image : markerImage // 마커 이미지 
    });
    
    var content = '<div class="wrap">' + 
    '    <div class="info">' + 
    '        <div class="title">' + 
    '            '+ list['title'] + 
    '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' + 
    '        </div>' + 
    '        <div class="body">' + 
    '            <div class="img">' +
    '                <img src="https://cfile181.uf.daum.net/image/250649365602043421936D" width="73" height="70">' +
    '           </div>' + 
    '            <div class="desc">' + 
    '                <div class="ellipsis">'+list['addr1']+'</div>' + 
    '                <div class="jibun ellipsis">'+list['addr2']+'</div>' + 
    '                <div><a href="https://www.kakaocorp.com/main" target="_blank" class="link">홈페이지</a></div>' + 
    '            </div>' + 
    '        </div>' + 
    '    </div>' +    
    '</div>';

    var overlay = new kakao.maps.CustomOverlay({
        content: content,  // 오버레이에 표시할 내용
        map: null,
        position: marker.getPosition(),   
    });

    // 마커를 클릭했을 때 커스텀 오버레이를 표시합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        overlay.setMap(map);
    });
}

function closeOverlay() {
    overlay.setMap(null);     
}

function selectPlace(inum){  //지역 선택 시 화면 전환 함수 
    var list = $.parseJSON(GlobalList[inum]);
    popUpClose();
    panTo(list['mapy'],list['mapx']);
}

function popUpClose(){
    $("#popup_mask").css("display","none"); //팝업창 뒷배경 display none
    $("#popupDiv").css("display","none"); //팝업창 display none
    $("body").css("overflow","auto");//body 스크롤바 생성
}

function keywordSearch(jdata){ //지역 검색시 팝업 및 검색결과 리스트 출력 함수 
    
    hideOverlays();
    hideMarkers();
    
    markers = [];
    overlays = [];
    
    
    $("#popupDiv").html( //새로운 지역 검색시 팝업창 내용 초기화 
        SaveDiv
    );
    
    GlobalList = jdata;
    for(var item in jdata){
        var list = $.parseJSON(jdata[item]);
        SetMarker(item);
        var Ddata = "<div id ="+item+" class='items' onclick='selectPlace(\"" + item + "\")'>"+list['title']+"</div>";
        
        $("#popupDiv").html(
            $("#popupDiv").html()+Ddata
        );    
        console.log(item);
    }

    $("#popupDiv").css({
            "top": (($(window).height()-$("#popupDiv").outerHeight())/2+$(window).scrollTop())+"px",
            "left": (($(window).width()-$("#popupDiv").outerWidth())/2+$(window).scrollLeft())+"px"
            //팝업창을 가운데로 띄우기 위해 현재 화면의 가운데 값과 스크롤 값을 계산하여 팝업창 CSS 설정
     }); 
        
    $("#popup_mask").css("display","block"); //팝업 뒷배경 display block
    $("#popupDiv").css("display","block"); //팝업창 display block
    
    $("#popCloseBtn").click(function(event){
        popUpClose(); 
    });
}



