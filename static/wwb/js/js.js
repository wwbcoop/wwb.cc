/**
 * js.js
 * Common scripts to be used throughout the site
 */

 /**
  *  scrollTo
  *  Scrolls window to given Y-coord
  *  @see https://pawelgrzybek.com/page-scroll-in-vanilla-javascript/
  *  Simplified and adapted to ECMA2015 to avoid some nasty crossbrowsing issues
  */

 function scrollTo(destination, duration = 200, easing, callback)
 {
     var start = window.pageYOffset;
     var startTime = 'now' in window.performance ? performance.now() : new Date().getTime();
     var documentHeight = Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);
     var windowHeight = window.innerHeight || document.documentElement.clientHeight || document.getElementsByTagName('body')[0].clientHeight;
     var destinationOffset = typeof destination === 'number' ? destination : destination.offsetTop;
     var destinationOffsetToScroll = Math.round(documentHeight - destinationOffset < windowHeight ? documentHeight - windowHeight : destinationOffset);

     if ('requestAnimationFrame' in window === false) {
         window.scroll(0, destinationOffsetToScroll);
         if (callback) {
           callback();
         }
         return;
     }

     function scroll() {
         var now = 'now' in window.performance ? performance.now() : new Date().getTime();
         var time = Math.min(1, ((now - startTime) / duration));
         var timeFunction = easing(time);
         window.scroll(0, Math.ceil((timeFunction * (destinationOffsetToScroll - start)) + start));

         if (window.pageYOffset === destinationOffsetToScroll) {
           if (callback) {
             callback();
           }
           return;
         }

         requestAnimationFrame(scroll);
     }
     scroll();
 }

function go(el, target){
  document.querySelectorAll('.featured-projects-browser__anchor').forEach( function(i){
      i.classList.remove('active');
  } );
  el.classList.add('active');
  scrollTo( document.querySelector(target), 1000, function(t){ return t < 0.5 ? 2*t*t : (4-2*t)*t - 1; })
}

// Vanilla JS equivalent of jQuery document.ready
document.addEventListener("DOMContentLoaded", function(){

  // Show navigation -- hamburguer icon in toolbar
  document.querySelector('.hamburguer-icon').onclick = function(){
      document.body.classList.toggle('navigation-open');
  };

  // FOUC
  document.querySelector('.region-content').style.display = 'block';

})
