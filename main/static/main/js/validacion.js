var formularionuevo1=0;
$(document).ready(function(){
//        $("#add-item").on("click", addItem);
//        $("#remove-item").on("click", removeItem);
var totalformularios = $("#id_form-TOTAL_FORMS").val();

if(totalformularios == 1){
 $("#remove-item").hide();
 $(".remove-item--form").hide();
}


        $('[data-toggle="tooltip"]').tooltip();
        $(".help-block").hide();

        $("#submit").on("click",function(){
            if(validar()){
                return true;
            } else {
                alert("formulario no valido");
                return false;
            }
        });
        $("#id_form1-nombre_organizacion").keyup(validar_nombre);
        $("#id_form1-pais").keyup(validar_pais);
        $("#id_form1-direccion").keyup(validar_direccion);



function actividad() {
alert("entro");
    var t;
    window.onload = resetTimer;
    // DOM Events
    document.onmousemove = resetTimer;
    document.onkeypress = resetTimer;

    function logout() {
        alert("You are now logged out.")
        //location.href = 'logout.php'
    }

    function resetTimer() {
        clearTimeout(t);
        t = setTimeout(logout, 3000)
        // 1000 milisec = 1 sec
    }
};

mensajeusuarioinactivo();

    });

 function mensajeusuarioinactivo() {
    var t;
    window.onload = resetTimer;
    // DOM Events
    document.onmousemove = resetTimer;
    document.onkeypress = resetTimer;
    document.onscroll = resetTimer;

    function logout() {
       $('#msginactividad').modal({backdrop: 'static', keyboard: false})
 $('#msginactividad').modal('show');
    }

    function resetTimer() {
        clearTimeout(t);
        t = setTimeout(logout, 900000)
        // 1000 milisec = 1 sec
    }
};




//validar campos
function validartexto(id){
var input = document.getElementById(id);
var txtid="#"+id;
    if (!/^[ @.a-z0-9áéíóúüñ_-]*$/i.test(input.value)) {
        input.value = input.value.replace(/[^ @.a-z0-9áéíóúüñ_-]+/ig,"");
        $(txtid).parent().siblings(".help-block").text("caracter no permitido");
         $(txtid).parent().siblings(".help-block").show();

    }else{
     $(txtid).parent().siblings(".help-block").hide();
    }
}

function validaridrequerimiento(id){
var input = document.getElementById(id);
var txtid="#"+id;
    if (!/^ [A-Za-z0-9.-]*$/i.test(input.value)) {
        input.value = input.value.replace(/[^ A-Za-z0-9.-]+/ig,"");
        $(txtid).parent().siblings(".help-block").text("caracter no permitido");
         $(txtid).parent().siblings(".help-block").show();

    }else{
     $(txtid).parent().siblings(".help-block").hide();
    }
}


function validarprioridad(id){
var input = document.getElementById(id);
var txtid="#"+id;
    if (!/^[0-9]*$/i.test(input.value)) {
        input.value = input.value.replace(/[^0-9]+/ig,"");
        $(txtid).parent().siblings(".help-block").text("caracter no permitido");
         $(txtid).parent().siblings(".help-block").show();

    }else{
     $(txtid).parent().siblings(".help-block").hide();
    }
}



    function addItem(){

        // Clonamos la ultima fila de la tabla
        var newElement = $(".table tr:last").clone(true);
        // Necesitamos aumentar en 1 el total de los formularios
        // por eso obtenemos el total actual, debería ser 4
        var total = $("#id_form-TOTAL_FORMS").val();
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
        $("#id_form-TOTAL_FORMS").val(total);
        // Insertamos el nueva formulario al final
        $(".table tr:last").after(newElement);
        // Solo mostramos el botón para quitar si hay mas de un formulario
        if (total > 1) {
            $("#remove-item").show();
        }
    }

    function removeItem(){
        // Obtenemos el último formulario de la tabla
        var lastElement = $(".table tr:last");
        // Obtenemos el total de formularios ya que ahora tenemos
        // que descontar un formulario
        var total = $("#id_form-TOTAL_FORMS").val();
        $(lastElement).remove();
        // Actualizamos el total de los formularios
        total--;
        $("#id_form-TOTAL_FORMS").val(total);
        // Solo mostrar el botón si existe por lo menos un formulario
        if (total < 2) {
            $("#remove-item").hide();
        }
    }


    function validar_campo_obligatorio(campo){
        if(campo == null || campo.length == 0 || /^\s+$/.test(campo)){
            return true;
        }
        return false;
    }




    function validar_nombre(){
        var nombre = document.getElementById("id_form1-nombre_organizacion").value;
        if (validar_campo_obligatorio(nombre)){
            $("#id_form1-nombre_organizacion").parent().children(".glyphicon").remove();
            $("#id_form1-nombre_organizacion").parent().parent().attr("class","form-group has-error has-feedback");
            $("#id_form1-nombre_organizacion").parent().append("<span class='glyphicon glyphicon-remove form-control-feedback'></span>");
            $("#id_form1-nombre_organizacion").parent().parent().children(".help-block").text("debe ingresar algun caracter");
            $("#id_form1-nombre_organizacion").parent().parent().children(".help-block").show();
            return false;
        } else {
            $("#id_form1-nombre_organizacion").parent().children(".glyphicon").remove();
            $("#id_form1-nombre_organizacion").parent().parent().attr("class","form-group has-success has-feedback");
            $("#id_form1-nombre_organizacion").parent().append("<span class='glyphicon glyphicon-ok form-control-feedback'></span>");
            $("#id_form1-nombre_organizacion").parent().parent().children(".help-block").text("");
            $("#id_form1-nombre_organizacion").parent().parent().children(".help-block").hide();
            return true;
        }
    }

    function validar_pais(){
        var pais = document.getElementById("id_form1-pais").value;
        if (validar_campo_obligatorio(pais)){
            $("#id_form1-pais").parent().children(".glyphicon").remove();
            $("#id_form1-pais").parent().parent().attr("class","form-group has-error has-feedback");
            $("#id_form1-pais").parent().append("<span class='glyphicon glyphicon-remove form-control-feedback'></span>");
            $("#id_form1-pais").parent().parent().children(".help-block").text("debe ingresar algun caracter");
            $("#id_form1-pais").parent().parent().children(".help-block").show();
            return false;
        } else {
            $("#id_form1-pais").parent().children(".glyphicon").remove();
            $("#id_form1-pais").parent().parent().attr("class","form-group has-success has-feedback");
            $("#id_form1-pais").parent().append("<span class='glyphicon glyphicon-ok form-control-feedback'></span>");
            $("#id_form1-pais").parent().parent().children(".help-block").text("");
            $("#id_form1-pais").parent().parent().children(".help-block").hide();
            return true;
        }
    }
    
    function validar_direccion(){
        var direccion = document.getElementById("id_form1-direccion").value;
        if (validar_campo_obligatorio(direccion)){
            $("#id_form1-direccion").parent().children(".glyphicon").remove();
            $("#id_form1-direccion").parent().parent().attr("class","form-group has-error has-feedback");
            $("#id_form1-direccion").parent().append("<span class='glyphicon glyphicon-remove form-control-feedback'></span>");
            $("#id_form1-direccion").parent().parent().children(".help-block").text("debe ingresar algun caracter");
            $("#id_form1-direccion").parent().parent().children(".help-block").show();
            return false;
        } else {
            $("#id_form1-direccion").parent().children(".glyphicon").remove();
            $("#id_form1-direccion").parent().parent().attr("class","form-group has-success has-feedback");
            $("#id_form1-direccion").parent().append("<span class='glyphicon glyphicon-ok form-control-feedback'></span>");
            $("#id_form1-direccion").parent().parent().children(".help-block").text("");
            $("#id_form1-direccion").parent().parent().children(".help-block").hide();
            return true;
        }
    }

    function validar(){
        validar_nombre()
        validar_pais()
        validar_direccion()
        if(validar_nombre()&&validar_pais()&&validar_direccion())
            return true;

        return false;
    }

function addItem1(){

        // Clonamos la ultima fila de la tabla
        var newElement = $("#tabla1 tr:last").clone(true);
        // Necesitamos aumentar en 1 el total de los formularios
        // por eso obtenemos el total actual, debería ser 4
        var total = $("#id_form-TOTAL_FORMS").val();
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
        // seteamos el valor del select auditable de instrucciones en 1
        newElement.find("select").each(function() {
           $(this).val("1");
        });



        $('input:radio');
        // Aumentamos en 1 la cantidad de formularios en el formset
        total++;
        $("#id_form-TOTAL_FORMS").val(total);

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
         $('.table tr:last textarea').each(function(e){

        CKEDITOR.disableAutoInline = true;
         CKEDITOR.inline( this.id,{
        'height': 100,

} );
    });
        // Solo mostramos el botón para quitar si hay mas de un formulario
        if (total > 1) {
            $("#remove-item").show();
             $(".remove-item--form").show();
        }


        formularionuevo1++;
    }


 function eliminarenbd(id, tabla) {

        $.ajax({
            type: 'GET',
            url: '/administracion/eliminarfila/',
            data: {'id':id,'tabla': tabla},
            success: function (data) {
            if (data.is_taken) {

             }
            },
            error: function(data) {

            }
        });
        return false;
    }


function removeItem1(id,tabla){
        // Obtenemos el último formulario de la tabla

        // Obtenemos el total de formularios ya que ahora tenemos
        // que descontar un formulario
        var total = $("#id_form-TOTAL_FORMS").val();
        var idformulario = $("#"+id).val();

         var inicial = $("#id_form-INITIAL_FORMS").val();
         inicial=(inicial-1);
         if(formularionuevo1==0){
         $("#id_form-INITIAL_FORMS").val(inicial);
         }else{
         formularionuevo1--;
         }
        eliminarenbd(idformulario,tabla);
        $("#"+id).closest('tr').remove();
        // Actualizamos el total de los formularios
        total--;
        $("#id_form-TOTAL_FORMS").val(total);


        // Solo mostrar el botón si existe por lo menos un formulario
        if (total < 2) {
            $(".remove-item--form").hide();
        }
        updateFormElementIndices("tabla1");
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

function validarnombreusuario(nombre) {

        $.ajax({
            type: 'GET',
            url: '/administracion/validarnombreusuario/',
            data: {'nombre':nombre},
            success: function (data) {
            if (data.existe == 1) {
             $('#submit').attr("disabled", true);
             $("#labelusername").text("Nombre de usuario ya existe");
             $("#labelusername").show();
             $('#labelusername').parents('.form-group').addClass( "has-error" );

             }
              if(data.existe == 0){
              $('#submit').attr("disabled", false);
              $("#labelusername").hide();
              $('#labelusername').parents('.form-group').removeClass( "has-error" );
              }
            },
            error: function(data) {

            }
        });
        return false;
    }