$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#contact-ajax .modal-content").html("");
        $("#contact-ajax").modal("show");
      },
      success: function (data) {
        $("#contact-ajax .modal-content").html(data.html_form);
      }
    });
  };

  var sendForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#contact-ajax").modal("hide");
        }
        else {
          $("#contact-ajax .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create contact
  $(".js-contact-ajax").click(loadForm);
  $("#contact-ajax").on("submit", ".js-contact-form-ajax", sendForm);

});