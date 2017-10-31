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

function show(cat){
    if(cat=='all'){
        document.querySelectorAll('[class*="cat-"]').forEach( function(i){
            i.classList.add('active');
        });
    } else {
        document.querySelectorAll('[class*="cat-"]').forEach( function(i){
            i.classList.remove('active');
        });
        document.querySelectorAll('.cat-' + cat).forEach( function(i){
            i.classList.add('active');
        });
    }
}

// Vanilla JS equivalent of jQuery document.ready
document.addEventListener("DOMContentLoaded", function(){

  // Show navigation -- hamburguer icon in toolbar
  document.querySelector('.hamburguer-icon').onclick = function(){
      document.body.classList.toggle('navigation-open');
  };

  // Detect scroll on frontpage
  var sections = document.querySelectorAll('.featured-projects__item');
  var anchors = document.querySelectorAll('.featured-projects-browser__anchor');
  var h       = window.pageYOffset;
  var vh      = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
  var current = Math.floor(h/vh);
  window.addEventListener('scroll', function() {
      h       = window.pageYOffset;
      vh      = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
      current = Math.floor(h/vh);
      if(!anchors[current].classList.contains('active')){
          anchors.forEach( function(i){ i.classList.remove('active'); });
          anchors[current].classList.add('active')
      }
  });
  function slideshow(){
      setTimeout(function() {
          requestAnimationFrame(slideshow);
          scrollTo(sections[(current+1)%sections.length], 1000, function(t){ return t < 0.5 ? 2*t*t : (4-2*t)*t - 1; });
      }, 5000);
  }
  requestAnimationFrame(slideshow);

  // FOUC
  document.querySelector('.region-content').style.display = 'block';

})
