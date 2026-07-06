import { initializeApp } from "https://www.gstatic.com/firebasejs/12.2.1/firebase-app.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/12.2.1/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyB7urkO_bJsfKkD0t_4W0HMybe_XlS7oOQ",
  authDomain: "veb-projekat-bf2ad.firebaseapp.com",
  projectId: "veb-projekat-bf2ad",
  storageBucket: "veb-projekat-bf2ad.firebasestorage.app",
  messagingSenderId: "167297100093",
  appId: "1:167297100093:web:d9812b8c480822ae6f7d54",
  measurementId: "G-P2MY8PWFVR"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app)

export { db }