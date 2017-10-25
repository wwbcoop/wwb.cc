/**
 * js.js
 * Common scripts to be used throughout the site
 */

// Vanilla JS equivalent of jQuery document.ready
document.addEventListener("DOMContentLoaded", function(){

  //Show navigation -- hamburguer icon in toolbar
  document.querySelector('.hamburguer-icon').onclick = function(){
      document.body.classList.toggle('navigation-open');
  };

  // FOUC
  document.querySelector('.region-content').style.display = 'block';
  
})
