// Credit for adapted code to change colour of country field in profile form from boutique ado project - See README.md for more details
let countrySelected = $('#id_default_country').val();
if(!countrySelected) { $('#id_default_country').css('color', '#6c757d'); }
$('#id_default_country').change(function() { countrySelected = $(this).val();
    if(!countrySelected) { $(this).css('color', '#6c757d'); } else { $(this).css('color', '#4169e1'); }
});