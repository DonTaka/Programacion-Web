function validar() {
    /* 
        username: min 5 max 30 
        password: largo min 8 
    */

    const user = document.getElementById("username").value;
    const pass = document.getElementById("pass").value;
    if (String(user).length >= 5 && String(user).length <= 30) {
        var res = document.getElementById("username");
        res.style.border = "1px solid green"
        if (String(pass).length >= 8) {
            /* Correcto */
            var res = document.getElementById("pass");
            res.style.border = "1px solid green"
            document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>" +
                "Acceso Concedido</div>"
        } else {
            /* Error pass */

            var res = document.getElementById("pass");
            res.style.border = "1px solid red"
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
                "Contraseña debe tener minimo 8 caracteres</div>"
        }
    } else {
        /* Error User */
        var res = document.getElementById("username");
        res.style.border = "1px solid red"
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
            "Usuario debe tener minimo 5 y maximo 30 caracteres</div>";
    }
}