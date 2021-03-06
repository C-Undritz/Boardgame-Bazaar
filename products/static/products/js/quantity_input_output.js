// Disables the ability for the customer to type in a quantity into the quantity input box
$("[type='number']").keypress(function (evt) {
    evt.preventDefault();
});

/* 
Below is pure JS version of the Boutique Ado Jquery for the handling of the quantity select functionality.
How to disable here: http://www.java2s.com/example/javascript/dom-html-element/disable-a-button-with-setattributedisabled-and-removeattributedi.html
*/

// Handles enabling and disabling of the buttons based on the value of input that they are controlling
function handleEnabledDisabled(itemId) {
    let plusDisabled;
    let currentValue = parseInt(document.querySelector(`#id_qty_${itemId}`).value);
    let currentStock = parseInt(document.querySelector(`#stock_${itemId}`).value);
    let minusDisabled = currentValue < 2;
    if (currentStock < 10) {
        plusDisabled = currentValue > (currentStock - 1);
    } else {
        plusDisabled = currentValue > 9;
    }
    let minusBtn = document.querySelector(`#minus-qty_${itemId}`);
    let plusBtn = document.querySelector(`#plus-qty_${itemId}`);
    minusBtn.removeAttribute("disabled");
    plusBtn.removeAttribute("disabled");
    if (minusDisabled) {
        minusBtn.setAttribute("disabled", "disabled");
    }
    if (plusDisabled) {
        plusBtn.setAttribute("disabled", "disabled");
    }
}

// On page load, loops through all input fields and calls the handleEnabledDisabled function
// to ensure proper enabling/disabling of all inputs on the page
let allQtyInputs = document.querySelectorAll('.qty-input');
if (allQtyInputs) {
    for (let i = 0; i < allQtyInputs.length; i++) {
        let itemId = allQtyInputs[i].dataset.item_id;
        handleEnabledDisabled(itemId);
    }
}

// Increase quantity
document.querySelectorAll('.plus-btn').forEach(item => {
    item.addEventListener('click', event => {
        event.preventDefault();
        let closestInput = item.closest('.input-group').querySelectorAll('.qty-input')[0];
        let currentValue = parseInt(closestInput.value);
        closestInput.value = currentValue + 1;
        let itemId = item.dataset.item_id;
        handleEnabledDisabled(itemId);
    });
});

// Decrease quantity
document.querySelectorAll('.minus-btn').forEach(item => {
    item.addEventListener('click', event => {
        event.preventDefault();
        let closestInput = item.closest('.input-group').querySelectorAll('.qty-input')[0];
        let currentValue = parseInt(closestInput.value);
        closestInput.value = currentValue - 1;
        let itemId = item.dataset.item_id;
        handleEnabledDisabled(itemId);
    });
});