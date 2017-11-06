/**
 *   Function to sort inlines in project forms
 *   @see https://www.djangosnippets.org/snippets/1053/
 */

jQuery(function($) {
    $('[data-formset-prefix="models-image-content_type-object_id"] table').sortable(
    {
        items: 'tr',
        update: function() {
            $(this).find('tr').each(function(i) {
                if ($(this).find('input[class$=vTextField]').val()) {
                    $(this).find('input[id$=position]').val(i);
                }
            });
        }
    });
});
