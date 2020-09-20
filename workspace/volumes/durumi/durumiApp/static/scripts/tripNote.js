var GlobalTripnoteList;
var GlobalTripnote;

function addTripNote() {
  
}

function selectPlace(item) {
  //지역 선택 시 화면 전환 함수
  place = GlobalTripnote[item];
  console.log(place.mapy, place.mapx);
  panTo(place.mapy, place.mapx);

  $("#viewDiv").css("top", "-.5em");
  $("#viewDiv").css("left", "-.5em");
}

function showTripnoteList(jdata) {
  GlobalTripnoteList = jdata;
  List = jdata;
  console.log(jdata);
  EmptyTripnoteList();
  EmptyTripnote();
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
    console.log(GlobalTripnoteList[TripnoteList]);
    if (document.getElementById(GlobalTripnoteList[TripnoteList]) != null)
      document.getElementById(GlobalTripnoteList[TripnoteList]).remove();
  }
}
function EmptyTripnote() {
  for (var Tripnote in GlobalTripnote) {
    console.log(GlobalTripnote[Tripnote]);
    if (document.getElementById(GlobalTripnote[Tripnote].code) != null)
      document.getElementById(GlobalTripnote[Tripnote].code).remove();
    hideMarkers(map);
    hideOverlays(map);
  }
}

function showTripnote(jdata) {
  GlobalTripnote = jdata;
  List = jdata;
  console.log(jdata);
  EmptyTripnote();
  EmptyTripnoteList();

  for (var item in jdata) {
    console.log(List[item].iconAddr);
    console.log(List[item]);
    var Ddata =
      "<div id =" +
      List[item].code +
      " class='items' onclick='selectPlace(\"" +
      item +
      "\")'>" +
      List[item].dest +
      "<img src = " +
      List[item].cat +
      "> </div>";

    $("#tripnoteDiv").html($("#tripnoteDiv").html() + Ddata);
    console.log(List[item]);

    SetMarkerTripnote(List[item]);
    //SetMarkerTripnote(33.450701, 126.570667);
  }
}
