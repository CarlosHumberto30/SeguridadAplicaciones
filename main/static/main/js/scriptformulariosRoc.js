var formularionuevo1=0;
var formularionuevo2=0;
var formularionuevo3=0;
// instanciar ckeditor para los textareas



$(document).ready(function(){
document.getElementById("main").style.marginLeft = "250px";

$('textarea').each(function(e){
         CKEDITOR.disableAutoInline = true;

         CKEDITOR.inline( this.id,{
        'height': 100,
         'resize_enabled': false,

} );
    });



validarinput();

 $('#id_imagen').change(function () {
        var val = $(this).val().toLowerCase(),
            regex = new RegExp("(.*?)\.(jpg|png)$");

        if (!(regex.test(val))) {
            $(this).val('');
            $(".alert-success").hide();
            $(".alert-danger").show();

        }else{
        $(".alert-danger").hide();
        $(".alert-success").show();
        }
    });

// verificando la cantidad de filas de la tabla para ocultar el boton de eliminar fila
var total1 = $("#id_form1-TOTAL_FORMS").val();
var total2 = $("#id_form2-TOTAL_FORMS").val();
var total3 = $("#id_form3-TOTAL_FORMS").val();

if(total1 == 1){
 $(".remove-item--form1").hide();
 // seccion de apendixC ocultar el boton borrar
 $(".borrar").hide();
}
if(total2 == 1){
 $(".remove-item--form2").hide();
}
if(total3 == 1){
 $(".remove-item--form3").hide();
}
    });


 var frm = $('#FORM-ID');
    frm.submit(function () {
         for (instance in CKEDITOR.instances) {

        CKEDITOR.instances[instance].updateElement();
    }
        $.ajax({
            type: 'POST',
            url: frm.attr('.'),
            data: frm.serialize(),
            success: function (data) {
            if (data.is_taken) {
             $('#modal').modal('hide')


             }
            },
            error: function(data) {

            }
        });
        validarinput();
        return false;
    });



$('#id_descripcion').change(function () {
          if( $('#id_descripcion').val().length >= 1) {
           $("#id_imagen").attr("required", true);
            } else{
             $("#id_imagen").removeAttr('required');
            }
    });

 $("#formulario").on('submit', function(evt){

 $('#modal').modal('show');

 });


function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
}




    function addItem1(){

        // Clonamos la ultima fila de la tabla
        var newElement = $("#tabla1 tr:last").clone(true);
        // Necesitamos aumentar en 1 el total de los formularios
        // por eso obtenemos el total actual, debería ser 4
        var total = $("#id_form1-TOTAL_FORMS").val();
        // Cuando se usan formsets, los elementos del formulario
        // son enumerados (id_form-0-rate, id_form-1-rate, etc.)
        // entonces necesitamos que el nuevo elemento siga esa
        // numeración
        newElement.find(":input").each(function() {
            var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
            var id = "id_" + name;
            // Seteamos los atributos y limpiamos los valores
            $(this).attr({"name": name, "id": id}).val("");

        }

        );

        newElement.find(":checkbox").each(function() {
            var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
            var id = "id_" + name;
            // Seteamos los atributos y limpiamos los valores
            $(this).attr({"name": name, "id": id}).val("");
            $(this).removeAttr('checked');
            $(this).val("x");
        }

        );
        // Aumentamos en 1 la cantidad de formularios en el formset
        total++;
        $("#id_form1-TOTAL_FORMS").val(total);
       // eliminamos el diveditable que se creo al clonar
        newElement.find("textarea").each(function() {

          $(this).siblings('div').remove();
          $(this).removeAttr("style");
          $(this).removeAttr("data-config");
          $(this).removeAttr("data-processed");
          $(this).removeAttr("data-external-plugin-resources");
          $(this).removeAttr("data-id");
          $(this).removeAttr("data-type");


        }
          );
         // Insertamos el nueva formulario al final
        $("#tabla1 tr:last").after(newElement);

        // instancio otro ckeditor
        $('#tabla1 tr:last textarea').each(function(e){

        CKEDITOR.disableAutoInline = true;
         CKEDITOR.inline( this.id,{
        'height': 100,



} );
    });
        // Solo mostramos el botón para quitar si hay mas de un formulario
        if (total > 1) {
            $(".remove-item--form1").show();
        }


        validarinput();
        formularionuevo1++;
    }

    function removeItem1(id,tabla, seccion){

        // Obtenemos el último formulario de la tabla

        // Obtenemos el total de formularios ya que ahora tenemos
        // que descontar un formulario
        var total = $("#id_form1-TOTAL_FORMS").val();
        var idformulario = $("#"+id).val();
         var inicial = $("#id_form1-INITIAL_FORMS").val();
         inicial=(inicial-1);
         if(formularionuevo1==0){
         $("#id_form1-INITIAL_FORMS").val(inicial);
         }else{
         formularionuevo1--;
         }

        eliminarenbd(idformulario,tabla,seccion);
        $("#"+id).closest('tr').remove();
        // Actualizamos el total de los formularios
        total--;
        $("#id_form1-TOTAL_FORMS").val(total);


        // Solo mostrar el botón si existe por lo menos un formulario
        if (total < 2) {
            $(".remove-item--form1").hide();
        }
        updateFormElementIndices("tabla1");
    }

     // manejo de talbladinamica 2

      function addItem2(){

        // Clonamos la ultima fila de la tabla
        var newElement = $("#tabla2 tr:last").clone(true);
        // Necesitamos aumentar en 1 el total de los formularios
        // por eso obtenemos el total actual, debería ser 4
        var total = $("#id_form2-TOTAL_FORMS").val();
        // Cuando se usan formsets, los elementos del formulario
        // son enumerados (id_form-0-rate, id_form-1-rate, etc.)
        // entonces necesitamos que el nuevo elemento siga esa
        // numeración
        newElement.find(":input").each(function() {
            var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
            var id = "id_" + name;
            // Seteamos los atributos y limpiamos los valores
            $(this).attr({"name": name, "id": id}).val("");
        });
        // Aumentamos en 1 la cantidad de formularios en el formset
        total++;
        $("#id_form2-TOTAL_FORMS").val(total);

        // removemos el div de ckeditor que se creo al clonar
         newElement.find("textarea").each(function() {

          $(this).siblings('div').remove();
          $(this).removeAttr("style");
          $(this).removeAttr("data-config");
          $(this).removeAttr("data-processed");
          $(this).removeAttr("data-external-plugin-resources");
          $(this).removeAttr("data-id");
          $(this).removeAttr("data-type");


        }
          );

        // Insertamos el nueva formulario al final
        $("#tabla2 tr:last").after(newElement);

        // instancio otro ckeditor
        $('#tabla2 tr:last textarea').each(function(e){

        CKEDITOR.disableAutoInline = true;
         CKEDITOR.inline( this.id,{
        'height': 100,

} );
    });

        // Solo mostramos el botón para quitar si hay mas de un formulario
        if (total > 1) {
            $(".remove-item--form2").show();
        }
        validarinput();
        formularionuevo2++;
    }




    function removeItem2(id,tabla, seccion){
        // Obtenemos el último formulario de la tabla

        // Obtenemos el total de formularios ya que ahora tenemos
        // que descontar un formulario
        var total = $("#id_form2-TOTAL_FORMS").val();
        var idformulario = $("#"+id).val();
         var inicial = $("#id_form2-INITIAL_FORMS").val();
         inicial=(inicial-1);
         if(formularionuevo2==0){
         $("#id_form2-INITIAL_FORMS").val(inicial);
         }else{
         formularionuevo2--;
         }

        eliminarenbd(idformulario,tabla,seccion);
        $("#"+id).closest('tr').remove();
        // Actualizamos el total de los formularios
        total--;
        $("#id_form2-TOTAL_FORMS").val(total);
        // Solo mostrar el botón si existe por lo menos un formulario
        if (total < 2) {
            $(".remove-item--form2").hide();
        }
        updateFormElementIndices("tabla2");
    }

    // manejo de talbladinamica 3

      function addItem3(){

        // Clonamos la ultima fila de la tabla
        var newElement = $("#tabla3 tr:last").clone(true);
        // Necesitamos aumentar en 1 el total de los formularios
        // por eso obtenemos el total actual, debería ser 4
        var total = $("#id_form3-TOTAL_FORMS").val();
        // Cuando se usan formsets, los elementos del formulario
        // son enumerados (id_form-0-rate, id_form-1-rate, etc.)
        // entonces necesitamos que el nuevo elemento siga esa
        // numeración
        newElement.find(":input").each(function() {
            var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
            var id = "id_" + name;
            // Seteamos los atributos y limpiamos los valores
            $(this).attr({"name": name, "id": id}).val("");
        });
        // Aumentamos en 1 la cantidad de formularios en el formset
        total++;
        $("#id_form3-TOTAL_FORMS").val(total);

         // removemos el div de ckeditor que se creo al clonar
         newElement.find("textarea").each(function() {

          $(this).siblings('div').remove();
          $(this).removeAttr("style");
          $(this).removeAttr("data-config");
          $(this).removeAttr("data-processed");
          $(this).removeAttr("data-external-plugin-resources");
          $(this).removeAttr("data-id");
          $(this).removeAttr("data-type");


        }
          );

        // Insertamos el nueva formulario al final
        $("#tabla3 tr:last").after(newElement);

           // instancio otro ckeditor
        $('#tabla3 tr:last textarea').each(function(e){

        CKEDITOR.disableAutoInline = true;
         CKEDITOR.inline( this.id,{
        'height': 100,


} );
    });

        // Solo mostramos el botón para quitar si hay mas de un formulario
        if (total > 1) {
            $(".remove-item--form3").show();
        }
        validarinput();
        formularionuevo3++;
    }

    function removeItem3(id,tabla, seccion){
        // Obtenemos el último formulario de la tabla

        // Obtenemos el total de formularios ya que ahora tenemos
        // que descontar un formulario
        var total = $("#id_form3-TOTAL_FORMS").val();
        var idformulario = $("#"+id).val();
         var inicial = $("#id_form3-INITIAL_FORMS").val();
         inicial=(inicial-1);
         if(formularionuevo3==0){
         $("#id_form3-INITIAL_FORMS").val(inicial);
         }else{
         formularionuevo3--;
         }

        eliminarenbd(idformulario,tabla,seccion);
        $("#"+id).closest('tr').remove();
        // Actualizamos el total de los formularios
        total--;
        $("#id_form3-TOTAL_FORMS").val(total);
        // Solo mostrar el botón si existe por lo menos un formulario
        if (total < 2) {
            $(".remove-item--form3").hide();
        }
        updateFormElementIndices("tabla3");
    }



// esta funcion se utiliza cuando el valor del primer campo debe de ser autoincrementable
 function addItem1seccion4_9(){

        // Clonamos la ultima fila de la tabla
        var newElement = $("#tabla1 tr:last").clone(true);
        // Necesitamos aumentar en 1 el total de los formularios
        // por eso obtenemos el total actual, debería ser 4
        var total = $("#id_form1-TOTAL_FORMS").val();
        // Cuando se usan formsets, los elementos del formulario
        // son enumerados (id_form-0-rate, id_form-1-rate, etc.)
        // entonces necesitamos que el nuevo elemento siga esa
        // numeración
        newElement.find(":input").each(function() {
            var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
            var id = "id_" + name;
            // Seteamos los atributos y limpiamos los valores
            if(id=='id_form1-'+total+'-campo1'){
            // incrementando contador de documetos
            var i=parseInt(total)+1;
            $(this).attr({"name": name, "id": id}).val("Doc-"+i);
            }else{
            $(this).attr({"name": name, "id": id}).val("");
            }


        });
        // Aumentamos en 1 la cantidad de formularios en el formset
        total++;
        $("#id_form1-TOTAL_FORMS").val(total);
        // Insertamos el nueva formulario al final
        $("#tabla1 tr:last").after(newElement);
        // Solo mostramos el botón para quitar si hay mas de un formulario
        if (total > 1) {
            $("#remove-item--form1").show();
        }


        validarinput();
        formularionuevo1++;
    }



   // esta funcion se utiliza cuando el valor del primer campo debe de ser autoincrementable
   function addItem2campoincrementable(prefijo){

        // Clonamos la ultima fila de la tabla
        var newElement = $("#tabla2 tr:last").clone(true);
        // Necesitamos aumentar en 1 el total de los formularios
        // por eso obtenemos el total actual, debería ser 4
        var total = $("#id_form2-TOTAL_FORMS").val();
        // Cuando se usan formsets, los elementos del formulario
        // son enumerados (id_form-0-rate, id_form-1-rate, etc.)
        // entonces necesitamos que el nuevo elemento siga esa
        // numeración
        newElement.find(":input").each(function() {
            var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
            var id = "id_" + name;
            // Seteamos los atributos y limpiamos los valores
            if(id=='id_form2-'+total+'-campo1'){
            // incrementando contador de documetos
            var i=parseInt(total)+1;
            $(this).attr({"name": name, "id": id}).val(prefijo+''+i);
            }else{
            $(this).attr({"name": name, "id": id}).val("");
            }
        });
        // Aumentamos en 1 la cantidad de formularios en el formset
        total++;
        $("#id_form2-TOTAL_FORMS").val(total);
        // Insertamos el nueva formulario al final
        $("#tabla2 tr:last").after(newElement);
        // Solo mostramos el botón para quitar si hay mas de un formulario
        if (total > 1) {
            $("#remove-item--form2").show();
        }
        validarinput();
        formularionuevo2++;
    }







     function eliminarenbd(id, tabla, seccion) {

        $.ajax({
            type: 'GET',
            url: '/autodoc/eliminarfila/',
            data: {'id':id,'tabla': tabla, 'seccion': seccion},
            success: function (data) {
            if (data.is_taken) {

             }
            },
            error: function(data) {

            }
        });
        return false;
    }


function validarinput() {
    var camposRellenados = true;
     var form = $(".validarvacio");

    form.find("textarea").each(function() {

    var $this = $(this);

            if( $this.val().length <= 0 ) {
           $this.addClass( "vacio" );
          $(this).siblings().addClass("vacio");


            } else{

              $this.removeClass("vacio")
               $(this).siblings().removeClass("vacio");
            }
    });
    if(camposRellenados == false) {
        return false;
    }
    else {
        return true;
    }
}

// para manejo de appendixc
 function addappendixc(){

        // Clonamos la ultima fila de la tabla
        var newElement = $("#tabla1 tr:last").clone(true);
        // Necesitamos aumentar en 1 el total de los formularios
        // por eso obtenemos el total actual, debería ser 4
        var total = $("#id_form1-TOTAL_FORMS").val();
        // Cuando se usan formsets, los elementos del formulario
        // son enumerados (id_form-0-rate, id_form-1-rate, etc.)
        // entonces necesitamos que el nuevo elemento siga esa
        // numeración
        newElement.find(":input").each(function() {
            var name = $(this).attr("name").replace("-" + (total-1) + "-", "-" + total + "-");
            var id = "id_" + name;
            // Seteamos los atributos y limpiamos los valores
            $(this).attr({"name": name, "id": id}).val("");

        });
        // Aumentamos en 1 la cantidad de formularios en el formset
        total++;
        $("#id_form1-TOTAL_FORMS").val(total);
         // eliminamos el diveditable que se creo al clonar
        newElement.find("textarea").each(function() {

          $(this).siblings('div').remove();
          $(this).removeAttr("style");
          $(this).removeAttr("data-config");
          $(this).removeAttr("data-processed");
          $(this).removeAttr("data-external-plugin-resources");
          $(this).removeAttr("data-id");
          $(this).removeAttr("data-type");


        }
          );
        // Insertamos el nueva formulario al final
        $("#tabla1 tr:last").after(newElement);

         $('#tabla1 tr:last textarea').each(function(e){

        CKEDITOR.disableAutoInline = true;
         CKEDITOR.inline( this.id,{
        'height': 100,

} );
    });

        // Solo mostramos el botón para quitar si hay mas de un formulario
        if (total > 1) {
            $(".borrar").show();
        }


        validarinput();
        formularionuevo1++;
    }

    function removeappendixc(tabla, seccion){
        // Obtenemos el último formulario de la tabla
        var lastElement = $("#tabla1 tr:last");
        // Obtenemos el total de formularios ya que ahora tenemos
        // que descontar un formulario
        var total = $("#id_form1-TOTAL_FORMS").val();
        var idformulario = $("#id_form1-"+(total-1)+"-id").val();
         var inicial = $("#id_form1-INITIAL_FORMS").val();
         inicial=(inicial-1);
         if(formularionuevo1==0){
         $("#id_form1-INITIAL_FORMS").val(inicial);
         }else{
         formularionuevo1--;
         }

        eliminarenbd(idformulario,tabla,seccion);
        $(lastElement).remove();
        // Actualizamos el total de los formularios
        total--;
        $("#id_form1-TOTAL_FORMS").val(total);
        // Solo mostrar el botón si existe por lo menos un formulario
        if (total < 2) {
            $("#remove-item--form1").hide();
        }
    }

function updateFormElementIndices(idtabla) {

 $('#'+idtabla).find('tbody').find('tr').each(function (i,el) {
$(el).find(":input").each(function(j,inp) {

        var curIndex = $(inp).attr('id').match(/-\d+-/)[0];
        var index= curIndex.match(/\d+/)[0];



           var name = $(inp).attr("name").replace("-" + index + "-", "-" + i + "-");
            var id = "id_" + name;

            // Seteamos los atributos y limpiamos los valores
            $(inp).attr({"name": name, "id": id});

        });
});
}