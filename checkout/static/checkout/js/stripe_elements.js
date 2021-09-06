/*
Logic and instructions for the below can be found here:
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

This closely follows the Boutique Ado Project stripe payments sections
*/

// Gets public key and client secret from the template.
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Variables required to set up stripe.
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
      color: "#212529",
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


