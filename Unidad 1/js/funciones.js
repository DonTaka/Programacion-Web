function validar() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("pass").value;
    /* 
        username: min 5 max 20
        password: min 8    
    */
    if (String(user).length >= 5 && String(user).length <= 20) {
        if (String(pass).length >= 8) {
            /* Funciono */
            document.getElementById("username").style.border = "1px solid lightgrey";
            document.getElementById("pass").style.border = "1px solid lightgrey";
            /* Alerta */
            document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>" +
                "Acceso Concedido</div>"
        } else {
            /* Pass error */
            /* Borde */
            document.getElementById("pass").style.border = "1px solid red";
            /* Alerta */
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
                "Contraseña debe tener minimo 8 caracteres</div>"

        }
    } else {
        /* User Error */
        /* 
            1.- Alerta
            2.- Label
            3.- animaciones
            4.- letras rojo
            5.- borde en rojo 
        */
        /* Borde */
        document.getElementById("username").style.border = "1px solid red";
        /* Alerta */
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>Usuario debe tener minimo 5 y maximo 20 caracteres</div>"
    }
}