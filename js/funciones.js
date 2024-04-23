function validar() {
    /* Validar los siguientes campos:
        username: min 6 max 15 
        password: min 8 
    */
    let user = document.getElementById("username").value;
    let pass = document.getElementById("pass").value;
    if (String(user).length >= 6 && String(user).length <= 15) {
        if (String(pass).length >= 8) {
            /* Credenciales correctas */
            document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>" +
                "Acceso Concedido </div>"
        } else {
            /* Pass Error */
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
                "Contraseña debe tener minimo 8 caracteres </div>"
        }
    } else {
        /* Usuario error */
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
            "Usuario debe tener minimo 6 y maximo 15 caracteres </div>"
    }
}