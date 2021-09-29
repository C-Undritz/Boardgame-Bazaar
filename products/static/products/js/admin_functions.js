let adminReveal = document.querySelector('#admin-reveal');
let adminFunctions = document.querySelector('#admin-functions');

// Controls the display of the Admin functions on the product detail view
document.addEventListener("DOMContentLoaded", function () {
    if (adminFunctions) {
        adminFunctions.style.display = "none";
    };
});

if (adminReveal) {
    adminReveal.addEventListener('click', function () {
        if (adminFunctions.style.display === "none") {
            adminFunctions.style.display = "block";
        } else if (adminFunctions.style.display === "block")  {
            adminFunctions.style.display = "none";
        };
    });
};