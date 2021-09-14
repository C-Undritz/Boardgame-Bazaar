// From the Boutique Ado project. Controls the color of the country drop downvalue to ensure
// that if value is selected that is valid (a country) then the value is shown in Font
// color Bootstrap 'dark', and shown as the placeholder grey if a country is not selected.

let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#212529');
    }
});