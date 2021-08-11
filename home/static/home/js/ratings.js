// Logic to generate 5 stars with the amount of the rating.innerText highlighted
const stars = document.querySelectorAll('.ratings');
stars.forEach(rating => {
    amount = rating.innerText;
    rating.innerText = '';
    for (i = 1; i < 6; i++) {
        if (i <= amount) { rating.innerHTML += '<i class="fa fa-star highlight"></i>'; }
        else { rating.innerHTML += '<i class="fa fa-star "></i>'; }
    }
})