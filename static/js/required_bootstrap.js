// Required Javascript to display toasts

// This stackoverflow post helped with interpreting the bootstrap instructions:
// https://stackoverflow.com/questions/63515279/how-to-initialize-toasts-with-javascript-in-bootstrap-5
let option = {
    autohide: true,
    delay: 12000,
}

var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl, option)
})
toastList.forEach(toast => toast.show());


// Required Javascript to display bootstrap offcanvas
var offcanvasElementList = [].slice.call(document.querySelectorAll('.offcanvas'))
var offcanvasList = offcanvasElementList.map(function (offcanvasEl) {
    return new bootstrap.Offcanvas(offcanvasEl)
})
offcanvasList.forEach(offcanvas => offcanvas.show());


