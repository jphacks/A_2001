import firebase from 'firebase'

if (!firebase.apps.length) {
  firebase.initializeApp(
    {
        apiKey: "AIzaSyARAh-X9znEbHAHrl2wyVDvLOUc6GaboO8",
        authDomain: "a-2001.firebaseapp.com",
        databaseURL: "https://a-2001.firebaseio.com",
    projectId: 'a-2001',
        storageBucket: "a-2001.appspot.com",
        messagingSenderId: "507907244331",
        appId: "1:507907244331:web:42e02dec127493e8e3056e",
        measurementId: "G-RKETVZ8C7K"
    
    })

}

export default firebase