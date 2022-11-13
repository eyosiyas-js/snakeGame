import firebase from 'firebase'

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDXZmehEb5inXJqoyiEEfyqzsHtb0lJ9s4",
  authDomain: "netflix-2580.firebaseapp.com",
  projectId: "netflix-2580",
  storageBucket: "netflix-2580.appspot.com",
  messagingSenderId: "53327925679",
  appId: "1:53327925679:web:27f8d74b23e8bb420cdf5a",
  measurementId: "G-TTGF3R2WHE"
};
const firebaseApp = firebase.initializeApp(firebaseConfig);
const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

export {auth,db}