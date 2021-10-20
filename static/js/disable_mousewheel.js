// Disables mousewheel. Solution from: https://stackoverflow.com/questions/9712295/disable-scrolling-on-input-type-number

$(document).on("wheel", "input[type=number]", function (e) {
    $(this).blur();
});