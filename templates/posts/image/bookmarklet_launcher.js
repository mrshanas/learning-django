// creates bookmarks to browsers

(function (){
    if(window !== undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script').src=`https://127.0.0.1:8000/static/posts/js/bookmarklet.js?r=${Math.floor(Math.random()*99999999999999999999)}`)
    }
})()