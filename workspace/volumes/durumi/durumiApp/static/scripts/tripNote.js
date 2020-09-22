var GlobalTripnoteList;
var GlobalTripnote;
var GlobalselctTripnoteForaddTripnoteList;
function addTripnoteListCancel() {
  $("#addTripnoteListDiv").css("display", "none");
}
function selectTripnoteForaddTripnoteOpen() {
  $("#selectTripnoteForaddTripnoteDiv").css({
    top:
      ($(window).height() -
        $("#selectTripnoteForaddTripnoteDiv").outerHeight()) /
        2 +
      $(window).scrollTop() +
      "px",
    left:
      ($(window).width() - $("#selectTripnoteForaddTripnoteDiv").outerWidth()) /
        2 +
      $(window).scrollLeft() +
      "px",
    //팝업창을 가운데로 띄우기 위해 현재 화면의 가운데 값과 스크롤 값을 계산하여 팝업창 CSS 설정
  });
  $("#selectTripnoteForaddTripnoteDiv").css("display", "block");
}
// function addTripNoteListOpen() {
//     $("#popup_mask").css("display","block");
//     $("#addTripnoteListDiv").css("display","block");
//     $("#addTripnoteListDiv").css("top","20vh");
// }

function selectTripnotePlace(item) {
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
  $("#tripnoteBackBtn").css("display", "none");
  $("#addTripNoteListBtn").css("display", "inline");

  EmptyTripnoteList(List);
  EmptyTripnote();
  for (var item in jdata) {
    //console.log(List[item]);
    var Ddata =
      '<div id ="' +
      List[item] +
      "\" class='tripNoteList' onclick='selectTripnote(\"" +
      List[item] +
      "\")'>" +
      List[item] +
      "</div>";

    $("#tripnoteDiv").html($("#tripnoteDiv").html() + Ddata);
  }
}
function EmptyTripnoteList() {
  console.log(GlobalTripnoteList);
  for (var TripnoteList in GlobalTripnoteList) {
    console.log(GlobalTripnoteList[TripnoteList]);
    if (document.getElementById(GlobalTripnoteList[TripnoteList])) {
      console.log(GlobalTripnoteList[TripnoteList] + " is deleted");
      document.getElementById(GlobalTripnoteList[TripnoteList]).remove();
    }
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
function EmptyselectTripnoteForaddTripnote() {
  for (var Tripnote in GlobalselctTripnoteForaddTripnoteList) {
    console.log(GlobalselctTripnoteForaddTripnoteList[Tripnote]);
    if (
      document.getElementById(GlobalselctTripnoteForaddTripnoteList[Tripnote])
    ) {
      document
        .getElementById(GlobalselctTripnoteForaddTripnoteList[Tripnote])
        .remove();
    }
  }
}
function showTripnote(jdata) {
  GlobalTripnote = jdata;
  List = jdata;
  console.log(jdata);
  EmptyTripnote();
  EmptyTripnoteList();
  $("#addTripNoteListBtn").css("display", "none");
  $("#tripnoteBackBtn").css("display", "inline");

  for (var item in jdata) {
    console.log(List[item].iconAddr);
    console.log(List[item]);
    var Ddata =
      "<div id =" +
      List[item].code +
      " class='tripNoteItems' onclick='selectTripnotePlace(\"" +
      item +
      "\")'>" +
      List[item].dest +
      "<img src = " +
      List[item].cat +
      "> </div>";

    $("#tripnoteDiv").html($("#tripnoteDiv").html() + Ddata);
    console.log(List[item]);

    SetMarkerTripnote(List[item]);
  }
}

function showselectTripnoteForaddTripnote(jdata, contentid) {
  GlobalselctTripnoteForaddTripnoteList = jdata;
  List = jdata;
  console.log(jdata);
  EmptyselectTripnoteForaddTripnote();

  for (var item in jdata) {
    //console.log(List[item]);
    var Ddata =
      '<div id ="' +
      List[item] +
      "\" class='tripNoteList' onclick=\"addTripnote('" +
      List[item] +
      "'," +
      contentid +
      ')">' +
      List[item] +
      "</div>";

    $("#selectTripnoteForaddTripnoteDiv").html(
      $("#selectTripnoteForaddTripnoteDiv").html() + Ddata
    );
  }

  selectTripnoteForaddTripnoteOpen();
}

function selectTripnoteForaddTripnoteCancel() {
  $("#selectTripnoteForaddTripnoteDiv").css("display", "none");
}
