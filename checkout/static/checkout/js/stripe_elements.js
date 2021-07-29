var stripePublicKeyGS = $('#id_stripe_public_key_gs').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKeyGS);
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
cardInput.addEventListener('change', function (event) { var errorElement = document.getElementById('error-element');
    if (event.error) { var html = `<i class="fas fa-exclamation-triangle highlight"></i> <span class="altFont">${event.error.message}</span>`; $(errorElement).html(html); }
    else { errorElement.textContent = ''; }
});

// Handle form submit
var form = document.getElementById('form-payment');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    cardInput.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, { payment_method: { card: cardInput, }
    }).then(function(result) {
        if (result.error) {
            var errorElement = document.getElementById('error-element');
            var html = `<i class="fas fa-exclamation-triangle highlight"></i> <span class="altFont">${event.error.message}</span>`; $(errorElement).html(html);
            cardInput.update({ 'disabled': false}); $('#submit-button').attr('disabled', false);
        } 
        else { if (result.paymentIntent.status === 'succeeded') { form.submit(); } }
    });
});