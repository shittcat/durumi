var GlobalTripnoteList;
var GlobalTripnote;
function showTripnoteList(jdata) {
  GlobalTripnoteList = jdata;
  List = jdata;
  console.log(jdata);
  for (var item in jdata) {
    console.log(List[item]);
    var Ddata =
      "<div id =" +
      List[item] +
      " class='items' onclick='selectTripnote(\"" +
      List[item] +
      "\")'>" +
      List[item] +
      "</div>";

    $("#tripnoteDiv").html($("#tripnoteDiv").html() + Ddata);
  }
}
function EmptyTripnoteList() {
  for (var TripnoteList in GlobalTripnoteList) {
    document.getElementById(GlobalTripnoteList[TripnoteList]).remove();
  }
}
function EmptyTripnote() {
  for (var Tripnote in GlobalTripnote) {
    document.getElementById(GlobalTripnote[Tripnote]).remove();
  }
}
function showTripnote(jdata) {
  GlobalTripnote = jdata;
  List = jdata;
  console.log(jdata);
  EmptyTripnoteList();
  for (var item in jdata) {
    console.log(List[item].iconAddr);
    var Ddata =
      "<div id =" +
      List[item] +
      " class='items' >" +
      List[item].dest +
      "<img src = " +
      List[item].cat +
      "> </div>";
    $("#tripnoteDiv").html($("#tripnoteDiv").html() + Ddata);
    console.log("showTripnote");

    var imageSize = new kakao.maps.Size(24, 35);
    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

    var temp = $("#gpsLoc").text().split(":");

    map.setLevel(6);

    hideOverlays();
    hideMarkers();

    markers = []; 
    overlays = [];

  }
}
