 // Change text after 5 seconds
 setTimeout(function(){
    document.getElementById('navbar-brand').textContent = 'About Legacy';
    // Change text back after 5 seconds
    setTimeout(function(){
        document.getElementById('navbar-brand').textContent = 'Hey! I am Legacy, your trusted servant for your server.';
    }, 5000);
}, 5000);