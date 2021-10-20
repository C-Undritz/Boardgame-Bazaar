// The below script controls the display of the mobile search input at mobile resolutions

let searchBtn = document.getElementById('mobile-search-btn')
let searchInput = document.getElementById('search-input')

document.addEventListener("DOMContentLoaded", function () {
    searchInput.style.display = "none"
});

searchBtn.addEventListener('click', function () {
    if (searchInput.style.display === "none") {
        searchInput.style.display = "block";
    } else {
        searchInput.style.display = "none"
    };
});