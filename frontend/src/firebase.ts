import firebase from 'firebase/app';
import 'firebase/analytics';
import 'firebase/performance';

const firebaseConfig = {
    apiKey: 'AIzaSyDhGQYjbTh7dRIZ45tlDB1F7UxaexOR5x8',
    authDomain: 'wasletztepreis-1.firebaseapp.com',
    projectId: 'wasletztepreis-1',
    storageBucket: 'wasletztepreis-1.appspot.com',
    messagingSenderId: '1030531345753',
    appId: '1:1030531345753:web:ba31243c6ae7d1593bf048',
    measurementId: 'G-GF0Q275NP1',
  };

firebase.initializeApp(firebaseConfig);
export const FB_ANALYTICS = firebase.analytics();
export const FB_PERFORMANCE = firebase.performance();
