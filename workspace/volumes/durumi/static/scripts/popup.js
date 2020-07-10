var SaveDiv;
var GlobalList;

function SelectPlace(inum){  //지역 선택 시 화면 전환 함수 
    
    var list = $.parseJSON(GlobalList[inum]);
    PopUpClose();
    panTo(list['mapy'],list['mapx']);
}

function PopUpClose(){
    $("#popup_mask").css("display","none"); //팝업창 뒷배경 display none
    $("#popupDiv").css("display","none"); //팝업창 display none
    $("body").css("overflow","auto");//body 스크롤바 생성
}

function popup(jdata){ //지역 검색시 팝업 및 검색결과 리스트 출력 함수 
    $("#popupDiv").html( //새로운 지역 검색시 팝업창 내용 초기화 
        SaveDiv
    );
    
    GlobalList = jdata;
    for(var item in jdata){
        var list = $.parseJSON(jdata[item])
        var Ddata = "<div id ="+item+" class='items' onclick='SelectPlace(\"" + item + "\")'>"+list['title']+"</div>"
        
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
        PopUpClose(); 
    });
}