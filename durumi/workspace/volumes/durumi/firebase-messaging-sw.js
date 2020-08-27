// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here, other Firebase libraries
// are not available in the service worker.
importScripts("https://www.gstatic.com/firebasejs/7.17.2/firebase-app.js");
importScripts(
  "https://www.gstatic.com/firebasejs/7.17.2/firebase-messaging.js"
);

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
  apiKey: "AIzaSyAZD8fSFfofedCXhMHHgtAf3XfFVOO7ixs",
  authDomain: "durumi-66072.firebaseapp.com",
  databaseURL: "https://durumi-66072.firebaseio.com",
  projectId: "durumi-66072",
  storageBucket: "durumi-66072.appspot.com",
  messagingSenderId: "648983791536",
  appId: "1:648983791536:web:369da7d0e19df097423875",
  measurementId: "G-JDDRFBHHP2",
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();
