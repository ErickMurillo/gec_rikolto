(function($){
	$(document).ready( function()
	{
    valor = $('#id_indicador').val();
    if (valor == 1) {
        $('#objind1_set-group').show();
        $('#objind2_set-group').hide();
        $('#objind3_set-group').hide();
        $('#objind4_set-group').hide();
      } else if (valor == 2){
        $('#objind1_set-group').hide();
        $('#objind2_set-group').show();
        $('#objind3_set-group').hide();
        $('#objind4_set-group').hide();
      } else if (valor == 3){
        $('#objind1_set-group').hide();
        $('#objind2_set-group').hide();
        $('#objind3_set-group').show();
        $('#objind4_set-group').hide();
      } else if (valor == 4){
        $('#objind1_set-group').hide();
        $('#objind2_set-group').hide();
        $('#objind3_set-group').hide();
        $('#objind4_set-group').show();
      } else {
        $('#objind1_set-group').hide();
        $('#objind2_set-group').hide();
        $('#objind3_set-group').hide();
        $('#objind4_set-group').hide();
      }

    $('#id_indicador').change(function(){
      valor = $('#id_indicador').val();
      if (valor == 1) {
        $('#objind1_set-group').show();
        $('#objind2_set-group').hide();
        $('#objind3_set-group').hide();
        $('#objind4_set-group').hide();
      } else if (valor == 2){
        $('#objind1_set-group').hide();
        $('#objind2_set-group').show();
        $('#objind3_set-group').hide();
        $('#objind4_set-group').hide();
      } else if (valor == 3){
        $('#objind1_set-group').hide();
        $('#objind2_set-group').hide();
        $('#objind3_set-group').show();
        $('#objind4_set-group').hide();
      } else if (valor == 4){
        $('#objind1_set-group').hide();
        $('#objind2_set-group').hide();
        $('#objind3_set-group').hide();
        $('#objind4_set-group').show();
      }
    });

  });
})(jQuery || django.jQuery);