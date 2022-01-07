(function (){
    const jQueryVersion = '3.6.0';
    const siteUrl = 'https://127.0.0.1:8000/';
    const staticUrl = siteUrl + 'static/';
    const minWidth = 100;
    const minHeight = 100;

    function bookmarklet(msg){
        // bookmarklet code
    }

    // check if jQuery is loaded
    if(typeof window.jQuery != undefined){
        bookmarklet();
    }
    else{
          // check for conflicts
          const conflict = typeof window.$ != 'undefined';
          // Create the script and point to Google API
 var script = document.createElement('script');
 script.src = '//ajax.googleapis.com/ajax/libs/jquery/' +
 jquery_version + '/jquery.min.js';
 // Add the script to the 'head' for processing
 document.head.appendChild(script);
 // Create a way to wait until script loading
 var attempts = 15;
 (function(){
 // Check again if jQuery is undefined
 if(typeof window.jQuery == 'undefined') {
 if(--attempts > 0) {
 // Calls himself in a few milliseconds
 window.setTimeout(arguments.callee, 250)
 } else {
 // Too much attempts to load, send error
 alert('An error occurred while loading jQuery')
 }
 } else {
 bookmarklet();
 }
 })();
 }
})()  