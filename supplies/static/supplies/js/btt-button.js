// Credit for adapted scroll to top button - see README.md for details
var page = document.documentElement;
document.addEventListener("scroll", function () { 
    var btt = document.getElementById('trigger-btt');
    if (page.scrollTop > 290) { btt.classList.remove('hidden'); } else { btt.classList.add('hidden'); }
});
$('#trigger-btt').click(function(e) { window.scrollTo(0,0); });