const _version = "v2";
const cacheName = "v1";
const cacheList = ["images/1.jpg", "images/2.jpg"];

const log = (msg) => {
  console.log("[ServiceWorker " + _version + "]" + msg);
};
/*
self.addEventListener("install", (event) => {
  //self.skipWaiting(); // 기존에 Install된 서비스워커가 있더라도 Waiting 하지 않고 Install해줌

  log("INSTALL");
});
*/
self.addEventListener("install", function (event) {
  //self.skipWaiting(); // 기존에 Install된 서비스워커가 있더라도 Waiting 하지 않고 Install해줌

  console.log("[service Worker] Installing Service Worker " + _version, event);
});

self.addEventListener("activate", function (event) {
  console.log("[Service Worker] Activating Service Worker " + _version, event);
  return self.clients.claim();
});

self.addEventListener("fetch", function (event) {
  console.log("[Service Worker] Fetching something " + _version, event);
  event.respondWith(fetch(event.request));
  /* 
  // .jpg 파일을 모두 /images/2.jps 파일로 바꿔주는 코드
  if (event.request.url.indexOf(".jps") != -1) {
    event.respondWith(fetch("/images/2.jsp"));
  }
  */
});

self.addEventListener("sync", function (event) {
  self.addEventListener("notificationclick", function (event) {
    var notification = event.notification;
    var action = event.action;

    console.log(notification);

    if (action === "confirm") {
      console.log("Confirm was chosen");
      notification.close();
    } else {
      console.log("Not confirm button clicked");
      notification.close();
    }
  });
  self.addEventListener("notificationclose", function (event) {
    console.log("Notification was closed &", event);
  });
});
