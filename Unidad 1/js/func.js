$(document).ready(function () {

    $("#btnEnviar").click(function () {
        $("#formulario").submit();
    })
    
    $("#btnGenerar").click(function () {
        let rut = $("#txtRut").val();
        let nombre = $("#txtNombre").val();
        let appaterno = $("#txtAppaterno").val();
        let apmaterno = $("#txtApmaterno").val();
        let fecha = $("#txtFecha").val();
        let edad = $("#txtEdad").val();
        let genero = $("input[name=optGenero]:checked").val();
        let mail = $("#txtMail").val();
        let telefono = $("#txtTelefono").val();
        let profesion = $("#txtProf").val();
        let comentario = $("#txtComentario").val();
        let res = validarDatos(rut, nombre, appaterno, apmaterno, edad, genero, telefono)
        if (res) {
            $("#exampleModal").modal("show");
            $("#res").html("")
            $("#res").append("<p>");
            $("#res").append("Rut: " + rut + "<br>");
            $("#res").append("Nombre Completo: " + nombre + " " + appaterno + " " + apmaterno + "<br>");
            $("#res").append("Fecha: " + fecha + "<br>");
            $("#res").append("Edad: " + edad + "<br>");
            $("#res").append("Genero: " + genero + "<br>");
            $("#res").append("Correo: " + mail + "<br>");
            $("#res").append("Telefono: " + telefono + "<br>");
            $("#res").append("Profesion: " + profesion + "<br>");
            $("#res").append("Aspiraciones: " + comentario + "<br>");
            $("#res").append("</p>");
        }
    })

    function validarDatos(rut, nombre, appaterno, apmaterno, edad, genero, celular) {

        if (String(rut).length < 9 || String(rut).length > 10) {
            /* Validacion Rut */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Rut debe tener largo entre 9 y 10 caracteres</div>");
        } else if (String(nombre).length < 3 || String(nombre).length > 20) {
            /* Validacion Nombre */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Nombre debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(appaterno).length <= 3 || String(appaterno).length >= 20) {
            /* Validacion Apellido Paterno */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Paterno debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(apmaterno).length <= 3 || String(apmaterno).length >= 20) {
            /* Validacion Apellido Materno */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Materno debe tener largo entre 3 y 20 caracteres</div>");
        } else if (Number(edad) < 18 && Number(edad) > 30) {
            /* Validacion Edad */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Edad debe estar entre 18 y 30 años</div>");
        } else if (genero != "Masculino" && genero != "Femenino" && genero != "Otro") {
            /* Validacion Genero */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Debe seleccionar un genero valido</div>");

        } else if (String(celular).length < 9 || String(celular).length > 12) {
            /* Validacion Edad */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Telefono debe tener entre 9 y 12 digitos</div>");
        } else {
            /* Confirmacion */
            return true;
        }

    }
});