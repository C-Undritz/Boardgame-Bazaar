/*
Logic and instructions for the below can be found here:
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements

This closely follows the Boutique Ado Project stripe payments sections but adds 
a stock check against purchase.
*/

// Gets public key and client secret from the template.
const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);

// Variables required to set up stripe.
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
      color: "#212529",
      fontFamily: 'Economica, Helvitica, sans-serif',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
  };
  
const card = elements.create('card', { style: style });
// Mounts card to the correct div element in template.
card.mount('#card-element');

// Handles realtime validation errors on the card element.
card.on('change', function(event) {
    let displayError = document.getElementById('card-errors');
    if (event.error) {
      displayError.textContent = event.error.message;
    } else {
      displayError.textContent = '';
    }
});

// Handle checkout form submit.
// Includes form data for stripe payment intent succeeded webhook
const form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#adjust-cart-btn').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    // Get value of the save_info check box by looking at checked status
    const saveInfo = Boolean($('#id-save-info').attr('checked'));
    // Gets csrf token from the {% csrf_token %} in the checkout.html payment-form
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // Object to pass this information to the view 'cache_checkout_data'
    const postData = {
        'csrfmiddlewaretoken': csrfToken,
        'save_info': saveInfo,
        'client_secret': clientSecret,
    };

    // Checks if there is enough stock to fulfill order
    const in_stock_url = '/checkout/is_in_stock/';
    $.post(in_stock_url, postData).done(function(response) {
        // If sale quantity is equal to or less than stock amount:
        if (response.result === true) {
            const cache_data_url = '/checkout/cache_checkout_data/';
            $.post(cache_data_url, postData).done(function() {
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
                        let displayError = document.getElementById('card-errors');
                        displayError.textContent = result.error.message;
                        $('#payment-form').fadeToggle(100);
                        $('#loading-overlay').fadeToggle(100);
                        card.update({'disabled': false});
                        $('#submit-button').attr('disabled', false); 
                        $('#adjust-cart-btn').attr('disabled', false); 
                    } else {
                        if (result.paymentIntent.status === 'succeeded') {
                            // form.submit();
                        }
                    }
                });
            }).fail(function() {
                // reloads page with error shown in django messages; customer not charged.
                location.reload();
            });
        } else {
            // If sale quantity is more than stock amount:
            const loc = window.location.href;
            const path = window.location.pathname;
            const newurl = loc.replace(path, '/checkout/no_sale/');
            location.replace(newurl);
        }
    });
});