var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        color: '#4169e1',
        fontFamily: '"Salsa", cursive',
        fontSize: '14px',
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var cardInput = elements.create('card', {style: style});
cardInput.mount('#card-element');

// Event listener to check for errors on the card field and display them if so
cardInput.addEventListener('change', function (event) { var errorDiv = document.getElementById('error-payment');
    if (event.error) { var html = `<i class="fas fa-exclamation-triangle highlight"></i> <span class="altFont">${event.error.message}</span>`; $(errorDiv).html(html); }
    else { errorDiv.textContent = ''; }
});
