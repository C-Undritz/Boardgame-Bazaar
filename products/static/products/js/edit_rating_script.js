/* 
<----------  Below functions are associated with the review_rate.html page when editing a review ---------->
These functions allow the user to rate the viewed product out of five using an interactive display of an array of
five stars.  The stars go from displaying as clear to the bootstrap warning colour as the user mouses over them.  
Once the user clicks on a star to indicate their chosen score, the star clicked and those before it will remain filled. 
The stars can be reset by moving the mouse cursor over the stars array and then moving the cursor away. Governing this 
is a variable 'ratingSelected' that changes the behaviour whether it is 'true' or 'false'.
*/
let ratingValue = parseInt(document.querySelector(`#rating_value`).value); //Previous review rating
let oneStars = document.getElementById('star1');
let twoStars = document.getElementById('star2');
let threeStars = document.getElementById('star3');
let fourStars = document.getElementById('star4');
let fiveStars = document.getElementById('star5');
let starPanel = document.getElementById('star-panel');
let ratingSelected = false;

document.addEventListener("DOMContentLoaded", function () {
    oneStars.setAttribute('class', 'fas fa-star rating-star');
    twoStars.setAttribute('class', 'fas fa-star rating-star');
    threeStars.setAttribute('class', 'fas fa-star rating-star');
    fourStars.setAttribute('class', 'fas fa-star rating-star');
    fiveStars.setAttribute('class', 'fas fa-star rating-star');
    oneStars.style.textShadow = '-1px 1px 2px #FFC107, 1px 1px 2px #FFC107, 1px -1px 0 #FFC107, -1px -1px 0 #FFC107';
    oneStars.style.color = '#F8F9FA';
    twoStars.style.textShadow = '-1px 1px 2px #FFC107, 1px 1px 2px #FFC107, 1px -1px 0 #FFC107, -1px -1px 0 #FFC107';
    twoStars.style.color = '#F8F9FA';
    threeStars.style.textShadow = '-1px 1px 2px #FFC107, 1px 1px 2px #FFC107, 1px -1px 0 #FFC107, -1px -1px 0 #FFC107';
    threeStars.style.color = '#F8F9FA';
    fourStars.style.textShadow = '-1px 1px 2px #FFC107, 1px 1px 2px #FFC107, 1px -1px 0 #FFC107, -1px -1px 0 #FFC107';
    fourStars.style.color = '#F8F9FA';
    fiveStars.style.textShadow = '-1px 1px 2px #FFC107, 1px 1px 2px #FFC107, 1px -1px 0 #FFC107, -1px -1px 0 #FFC107';
    fiveStars.style.color = '#F8F9FA';
    
    // If a product has been reviewed befpre then the below code prefills the stars with the ratingValue.
    if (ratingValue === 1) {
        oneStars.style.color = '#FFC107';
    } else if (ratingValue === 2) {
        oneStars.style.color = '#FFC107';
        twoStars.style.color = '#FFC107';
    } else if (ratingValue === 3) {
        oneStars.style.color = '#FFC107';
        twoStars.style.color = '#FFC107';
        threeStars.style.color = '#FFC107';
    } else if (ratingValue === 4) {
        oneStars.style.color = '#FFC107';
        twoStars.style.color = '#FFC107';
        threeStars.style.color = '#FFC107';
        fourStars.style.color = '#FFC107';
    } else if (ratingValue === 5) {
        oneStars.style.color = '#FFC107';
        twoStars.style.color = '#FFC107';
        threeStars.style.color = '#FFC107';
        fourStars.style.color = '#FFC107';
        fiveStars.style.color = '#FFC107';
    }
});

// The following functions temporarily change the current star to orange along with any preceeding stars when called.
let mouseOverFunctionOne = function () {
    this.style.color = '#FFC107';
};

let mouseOutFunctionOne = function () {
    if (ratingSelected == false) {
        this.style.color = '#F8F9FA';
    }
};

let mouseOverFunctionTwo = function () {
    this.style.color = '#FFC107';
    oneStars.style.color = '#FFC107';
};

let mouseOutFunctionTwo = function () {
    if (ratingSelected == false) {
        this.style.color = '#F8F9FA';
        oneStars.style.color = '#F8F9FA';
    }
};

let mouseOverFunctionThree = function () {
    this.style.color = '#FFC107';
    oneStars.style.color = '#FFC107';
    twoStars.style.color = '#FFC107';
};

let mouseOutFunctionThree = function () {
    if (ratingSelected == false) {
        this.style.color = '#F8F9FA';
        oneStars.style.color = '#F8F9FA';
        twoStars.style.color = '#F8F9FA';
    }
};

let mouseOverFunctionFour = function () {
    this.style.color = '#FFC107';
    oneStars.style.color = '#FFC107';
    twoStars.style.color = '#FFC107';
    threeStars.style.color = '#FFC107';
};

let mouseOutFunctionFour = function () {
    if (ratingSelected == false) {
        this.style.color = '#F8F9FA';
        oneStars.style.color = '#F8F9FA';
        twoStars.style.color = '#F8F9FA';
        threeStars.style.color = '#F8F9FA';
    }
};

let mouseOverFunctionFive = function () {
    this.style.color = '#FFC107';
    oneStars.style.color = '#FFC107';
    twoStars.style.color = '#FFC107';
    threeStars.style.color = '#FFC107';
    fourStars.style.color = '#FFC107';
};

let mouseOutFunctionFive = function () {
    if (ratingSelected == false) {
        this.style.color = '#F8F9FA';
        oneStars.style.color = '#F8F9FA';
        twoStars.style.color = '#F8F9FA';
        threeStars.style.color = '#F8F9FA';
        fourStars.style.color = '#F8F9FA';
    }
};

// Reset the star rating to false and therefore the stars colours to clear. Rating button also disabled.
let resetRating = function () {
    ratingSelected = false;
};

// Calls the functions to change the stars colours when moused over.
oneStars.onmouseover = mouseOverFunctionOne;
oneStars.onmouseout = mouseOutFunctionOne;

twoStars.onmouseover = mouseOverFunctionTwo;
twoStars.onmouseout = mouseOutFunctionTwo;

threeStars.onmouseover = mouseOverFunctionThree;
threeStars.onmouseout = mouseOutFunctionThree;

fourStars.onmouseover = mouseOverFunctionFour;
fourStars.onmouseout = mouseOutFunctionFour;

fiveStars.onmouseover = mouseOverFunctionFive;
fiveStars.onmouseout = mouseOutFunctionFive;

// Calls the function to reset rating prior to submission on mouse enter
starPanel.onmouseenter = resetRating;

/* The following functions changes the current star to filled along with any preceeding stars when they are clicked.
This is when a rating value has been selected in the HTML. ratingSelected is then true and the resetRating() function 
is then required to reset the stars.*/
oneStars.addEventListener('click', function () {
    oneStars.style.color = '#FFC107';
    twoStars.style.color = '#F8F9FA';
    threeStars.style.color = '#F8F9FA';
    fourStars.style.color = '#F8F9FA';
    fiveStars.style.color = '#F8F9FA';
    ratingSelected = true;
});

twoStars.addEventListener('click', function () {
    oneStars.style.color = '#FFC107';
    twoStars.style.color = '#FFC107';
    threeStars.style.color = '#F8F9FA';
    fourStars.style.color = '#F8F9FA';
    fiveStars.style.color = '#F8F9FA';
    ratingSelected = true;
});

threeStars.addEventListener('click', function () {
    oneStars.style.color = '#FFC107';
    twoStars.style.color = '#FFC107';
    threeStars.style.color = '#FFC107';
    fourStars.style.color = '#F8F9FA';
    fiveStars.style.color = '#F8F9FA';
    ratingSelected = true;
});

fourStars.addEventListener('click', function () {
    oneStars.style.color = '#FFC107';
    twoStars.style.color = '#FFC107';
    threeStars.style.color = '#FFC107';
    fourStars.style.color = '#FFC107';
    fiveStars.style.color = '#F8F9FA';
    ratingSelected = true;
});

fiveStars.addEventListener('click', function () {
    oneStars.style.color = '#FFC107';
    twoStars.style.color = '#FFC107';
    threeStars.style.color = '#FFC107';
    fourStars.style.color = '#FFC107';
    fiveStars.style.color = '#FFC107';
    ratingSelected = true;
});