let revealReviews = document.getElementById('reveal-all-reviews');
let hideReviews = document.getElementById('hide-all-reviews');
let allReviewsText  = document.getElementById('all-reviews');

/* Event Listeners for the display of the reviews.  The display of features depends on the amount of reviews 
against the product.  Therefore the 'if' statements test for when the elements are included in the html before 
determining how they are displayed.*/
document.addEventListener("DOMContentLoaded", function () {
    if ((allReviewsText) && (hideReviews)) {
        allReviewsText.style.display = "none";
        hideReviews.style.display = "none";
    }
});

// Determines what is displayed in the reviews section of a product detail view when the text 'See all reviews' is clicked.
if (revealReviews) { 
    revealReviews.addEventListener('click', function () {
        revealReviews.style.display = "none";
        hideReviews.style.display = "block";
        allReviewsText.style.display = "block";
    });
}

// Determines what is displayed in the reviews section of a product detail view when the text 'Close' is clicked.
if (hideReviews) {
    hideReviews.addEventListener('click', function() {
        revealReviews.style.display = "block";
        hideReviews.style.display = "none";
        allReviewsText.style.display = "none";
    });
}