/*
Logic and instructions for the below can be found here:
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

This closely follows the Boutique Ado Project stripe payments sections
*/

// Gets public key and client secret from the template.
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Variables required to set up stripe.
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
      color: "#212529",
      fontfamily: '"Amatic SC", cursive, Helvitica, sans-serif',
      fontsmoothing: 'antialiased',
      fontSize: '16px',
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
  };
  
var card = elements.create('card', { style: style });
// Mounts card to the correct div element in template.
card.mount('#card-element');

// Handles realtime validation errors on the card element.
card.on('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
      displayError.textContent = event.error.message;
    } else {
      displayError.textContent = '';
    }
});

// Handle form submit.
// includes form data for stripe payment intent succeeded webhook as it will be coming from stripe.
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({'disabled': true}); // disables card element
    $('#submit-button').attr('disabled', true); // disables submit button
    $('#adjust-cart-btn').attr('disabled', true); // disables adjust cart button
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // get value of the save_info check box by looking at checked status
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // gets csrf token from the {% csrf_token %} in the checkout.html payment-form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // object to pass this information to the view 'cache_checkout_data'
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'save_info': saveInfo,
        'client_secret': clientSecret,
    };

    // url to call view assigned to variable
    var url = '/checkout/cache_checkout_data/';

    // posts data to view using JQuery post method and waits for response that payment is updated and 
    // then executes the confirmed payment method
    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    state: $.trim(form.county.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                }
            }
        }).then(function(result) {
            if (result.error) {
                var displayError = document.getElementById('card-errors');
                displayError.textContent = result.error.message;
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({'disabled': false}); // enables card element
                $('#submit-button').attr('disabled', false); // enables submit button
                $('#adjust-cart-btn').attr('disabled', false); // enables adjust cart button
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // reloads page with error shown in django messages; customer not charged.
        location.reload();
    });
});
