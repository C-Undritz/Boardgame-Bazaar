/*
From the Boutique Ado project. Takes the value of the selected option from the dropdown
sort selector input and seperates the value to get a sort parameter and direction parameter
to use and update the url so as to display the results.
*/

$('#sort-selector').change(function() {
    const selector = $(this);
    const currentUrl = new URL(window.location);

    const selectedVal = selector.val();
    if(selectedVal != "reset"){
        const sort = selectedVal.split("_")[0];
        const direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});
