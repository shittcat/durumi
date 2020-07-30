
function openTripNote(){
    console.log(checkNote);
    if (checkNote == 1){ //노트 올라와 있는 상태 
        $("#noteDiv").css("top","130vh");
        $("#openNote").css("top","95vh");
    }
    else if(checkNote == -1){//노트 내려와 있는 상태 
        $("#noteDiv").css("display","block"); //팝업창 display block
        $("#noteDiv").load("tripnote/");
        $("#noteDiv").css("top","70vh");
        $("#openNote").css("top","68vh");
    }
    
    checkNote = checkNote * -1; 
   // alert("note")
}

function openMenu(){
    if (checkMenu == -1){ //메뉴 나와 있는 상태 
        $("#popup_mask").css("display","block"); //팝업창 뒷배경 display none
        $("#menuDiv").css("display","block"); //팝업창 display block
        $("#menuDiv").load("hamburgerMenu/");
        $("#menuDiv").css("left","70vw");
        $("#openMenu").css("left","68vw");
        checkMenu = checkMenu * -1; 
    }
   // alert("note")
}

function closeMenu(){
    $("#popup_mask").css("display","none"); //팝업창 뒷배경 display none
    $("#menuDiv").css("left","140vw");
    $("#openMenu").css("left","88vw");
    checkMenu = checkMenu * -1;
}

function modeChange(){
    if(viewMode == 1){ //place -> picture 전환
        $("itemOverlays.place").css("transform","rotateY(180deg)");
        $("itemOverlays.picture").css("transform","rotateY(0deg)");
    }
    else if(viewMode == -1){ //picture -> place 전환 
        $("itemOverlays.place").css("transform","rotateY(0deg)");
        $("itemOverlays.picture").css("transform","rotateY(180deg)");
    }
    viewMode *= -1;
}

// function SetMarker(inum){
//     var list = $.parseJSON(GlobalList[inum]);
//     // 마커 이미지의 이미지 크기 입니다
//     var imageSize = new kakao.maps.Size(24, 35); 
//     // 마커 이미지를 생성합니다    
//     var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
//     // 마커를 생성합니다
//     var marker = new kakao.maps.Marker({
//         map: map, // 마커를 표시할 지도
//         position: new kakao.maps.LatLng(list['mapy'],list['mapx']), // 마커를 표시할 위치
//         title : list['title'], // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
//         image : markerImage // 마커 이미지 
//     });
    
//     var content = '<div id=\"'+inum+'Overlay\" class=\"itemOverlays place\"> place view </div>'+
//             '<div id=\"'+inum+'Overlay\" class=\"itemOverlays picture\"> picture view </div>'

//     var overlay = new kakao.maps.CustomOverlay({
//         content: content,  // 오버레이에 표시할 내용
//         map: null,
//         position: marker.getPosition(),   
//     });

//     markers.push(marker);
//     overlays.push(overlay);
//     // 마커를 클릭했을 때 커스텀 오버레이를 표시합니다
//     kakao.maps.event.addListener(marker, 'click', function() {
//         overlay.setMap(map);
//         // overlay.setContent(
//         //     '<div id=\"'+inum+'Overlay\" class=\"itemOverlays place\"> place view </div>'+
//         //     '<div id=\"'+inum+'Overlay\" class=\"itemOverlays picture\"> picture view </div>'
//         // )
//     });
// }

function hideMarkers(map) {
    for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(null);
    }            
}

function hideOverlays(map) {
    for (var i = 0; i < markers.length; i++) {
            overlays[i].setMap(null);
    }            
}

$("#popup_mask").click(function(){
    if( checkMenu == 1 ) { //메뉴 닫기 
        closeMenu();
    }
});