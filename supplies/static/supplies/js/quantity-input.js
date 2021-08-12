// Credit for adapted quantity buttons script from the Boutique Ado project
// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`#qty-dec_${itemId}`).prop('disabled', minusDisabled);
    $(`#qty-inc_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty-input');
for(var i = 0; i < allQtyInputs.length; i++) { var itemId = $(allQtyInputs[i]).data('item_id'); handleEnableDisable(itemId); }

// Check enable/disable every time the input is changed
$('.qty-input').change(function() { var itemId = $(this).data('item_id'); handleEnableDisable(itemId); });

// Increment quantity
$('.qty-inc').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty-input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Decrement quantity
$('.qty-dec').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty-input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});