// Logic to generate 5 stars with the amount of the rating.innerText highlighted
const stars = document.querySelectorAll('.ratings');
let amount = 0;
stars.forEach(rating => {
    // Pull the data from innerText which is the amount of stars to highlight
    amount = rating.innerText;
    rating.innerText = '';
    // For loop to generate 5 stars and highlight them until i is lower than the data pulled from innerText
    for (let i = 1; i < 6; i++) {
        if (i <= amount) { rating.innerHTML += '<i class="fa fa-star highlight"></i>'; }
        else { rating.innerHTML += '<i class="fa fa-star "></i>'; }
    }
});