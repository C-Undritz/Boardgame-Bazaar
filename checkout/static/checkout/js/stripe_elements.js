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

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({'disabled': true}); // disables card element
    $('#submit-button').attr('disabled', true); // disables submit button
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        } 
    }).then(function(result) {
        if (result.error) {
            var displayError = document.getElementById('card-errors');
            displayError.textContent = result.error.message;
            card.update({'disabled': false}); // enables card element
            $('#submit-button').attr('disabled', false); // enables submit button
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
