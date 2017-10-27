/**
 *    Creates a thumbnail from a html file input using HTML5 File API
 */


/**
 *  Slugify function
 *  @see https://gist.github.com/mathewbyrne/1280286
 */

 function slugify(text)
 {
   return text.toString().toLowerCase()
     .replace(/\s+/g, '-')           // Replace spaces with -
     .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
     .replace(/\-\-+/g, '-')         // Replace multiple - with single -
     .replace(/^-+/, '')             // Trim - from start of text
     .replace(/-+$/, '');            // Trim - from end of text
 }

+(function()
{
    var slug_source = document.querySelector('#slug-source');
    var source      = slug_source.getAttribute('data-source');
    var input       = document.querySelector('input[name="' + source + '"]');
    input.addEventListener(
        'keyup',
        function(e) {
            var text = input.value;
            document.querySelector('input[name="slug"]').value = slugify(text);
        },
    false);
})();
