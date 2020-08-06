// UI 버튼 관련 스크립트 

function openTripNote(){
    console.log(checkNote);
    if (checkNote == 1){ //노트 올라와 있는 상태 
        $("#noteDiv").css("top","130vh");
        $("#openNote").css("top","95vh");
        // $(".midCatDiv").css("display","block");
    }
    else if(checkNote == -1){//노트 내려와 있는 상태 
        $("#noteDiv").css("display","block"); //팝업창 display block
        $("#noteDiv").load("tripnote/");
        $("#noteDiv").css("top","70vh");
        $("#openNote").css("top","68vh");
        // $(".midCatDiv").css("display","none");
    }

    //다른 ui 숨기기
    $("#catDiv").slideToggle(10);
    $("#searchDiv").slideToggle();
    $("#modeChange").slideToggle();
    $("#openMenu").slideToggle();
    checkNote = checkNote * -1; 
       // alert("note")
}


function closeMenu(){
    $("#popup_mask").css("display","none"); //팝업창 뒷배경 display none
    $("#menuDiv").css("left","140vw");
    $("#openMenu").css("left","88vw");
    checkMenu = checkMenu * -1;
}

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