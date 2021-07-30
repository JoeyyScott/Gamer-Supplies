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
    $('#form-payment').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: { 
                card: cardInput,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.contact_number.value),
                    address: {
                        line1: $.trim(form.address_line_1.value),
                        line2: $.trim(form.address_line_2.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.contact_number.value),
                address: {
                    line1: $.trim(form.address_line_1.value),
                    line2: $.trim(form.address_line_2.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorElement = document.getElementById('error-element');
                var html = `<i class="fas fa-exclamation-triangle highlight"></i> <span class="altFont">${result.error.message}</span>`; $(errorElement).html(html);
                $('#form-payment').fadeToggle(100); $('#loading-overlay').fadeToggle(100); cardInput.update({ 'disabled': false}); $('#submit-button').attr('disabled', false); 
            } 
            else { if (result.paymentIntent.status === 'succeeded') { form.submit(); } }
        });
    }).fail(function () {
        // Reload the page, django messages will handle the error
        location.reload();
    });
});