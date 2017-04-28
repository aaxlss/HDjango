/**
 * Created by aaxlss on 4/26/17.
 */
$(document).ready(function () {
    $(document).on('click', '#renderByAjax', function (e) {
        e.preventDefault();
       $.ajax({
           url: $(this).attr('href'),
           success: function (data) {
               x=window.open();
               x.document.open().write(data);
           }

       });
    });
});
