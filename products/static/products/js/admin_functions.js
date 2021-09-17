let adminReveal = document.querySelector('#admin-reveal');
let adminFunctions = document.querySelector('#admin-functions');

document.addEventListener("DOMContentLoaded", function () {
    adminFunctions.style.display = "none";
});

adminReveal.addEventListener('click', function () {
    if (adminFunctions.style.display === "none") {
        adminFunctions.style.display = "block";
    } else if (adminFunctions.style.display === "block")  {
        adminFunctions.style.display = "none";
    };
});