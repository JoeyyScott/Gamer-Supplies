// Credit for slide animation for Bootstrap 5 dropdown - See README.md for more details
// Add slideDown animation to Bootstrap dropdown when expanding.
$('.dropdown').on('show.bs.dropdown', function() { $(this).find('.dropdown-menu').first().stop(true, true).slideDown(); });
// Add slideUp animation to Bootstrap dropdown when collapsing.
$('.dropdown').on('hide.bs.dropdown', function() { $(this).find('.dropdown-menu').first().stop(true, true).slideUp(); });