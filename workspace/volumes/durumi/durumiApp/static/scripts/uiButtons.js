// UI 버튼 관련 스크립트 

function closeMenu(){
    $("#popup_mask").css("display","none"); //팝업창 뒷배경 display none
    $("#menuDiv").css("left","140vw");
    $("#openMenu").css("left","88vw");
    checkMenu = checkMenu * -1;
}

$("#popup_mask").click(function(){
    if( checkMenu == 1 ) { //메뉴 닫기 
        closeMenu();
    }
    if( checkLoginPage == 1){ //로그인페이지 닫기 
        checkLoginPage = -1
        closeLoginPage();
    }
});


function openLoginPage(){
    closeMenu();
    $("#popup_mask").css("display","block");
    $("#loginPage").css("display","block");
    $("#loginPage").css("top","20vh");
    checkLoginPage = 1;
    
}

function closeLoginPage(){
    $("#popup_mask").css("display","none");
    $("#loginPage").css("top","120vh");
    checkLoginPage = -1;
}