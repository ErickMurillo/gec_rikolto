(function($){
	$(document).ready( function()
	{
        $('#id_indicador').change(function(){
            id = $('#id_indicador').val();
            $.getJSON('/ajax/admin/producto/?id='+id, function(data){
                if(data){
                    
                    indicador = data[0].split('.').join('_');
                    $('.inline-group').hide();
                    $('#indproducto'+indicador+'_set-group').show(); 
                }
            });
        }); 

        id = $('#id_indicador').val();
        if(id != null){
            $.getJSON('/ajax/admin/producto/?id='+id, function(data){
                if(data){
                    
                    indicador = data[0].split('.').join('_');
                    $('.inline-group').hide();
                    $('#indproducto'+indicador+'_set-group').show(); 
                }
            });
        } else {
            $('.inline-group').hide();
        }

    });
})(jQuery || django.jQuery);