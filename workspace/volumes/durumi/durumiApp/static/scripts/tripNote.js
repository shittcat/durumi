function showTripnote(jdata) {
  GlobalList = jdata;
  console.log("showTripnote");
  for (var item in jdata) {
    var Ddate =
      "<div id =" +
      item +
      " class='items' onclick='selcectTripnote(\"" +
      item +
      "\")'>" +
      item +
      "</div>";

    $("#tripnoteDiv").html($("#tripnoteDiv").html() + Ddata);
    console.log("showTripnote");
  }
}
