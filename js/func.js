function verInfo() {
    var user = document.getElementById("user").value;
    var pass = document.getElementById("pass").value;
    console.log("User: " + user + " Pass:" + pass);

    if (user == 'user1' && pass == 'pass1234') {
        document.getElementById("resultado").innerHTML = "<div class='alert alert-success col-4 mx-auto h-50'>" +
            "<p>Conexion Exitosa</p></div>";

    } else {
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger col-4 mx-auto h-50'>" +
            "<p>Usuario y/o contraseña incorrecto</p></div>";
    }

}

function clearButton() {
    document.getElementById("resultado").innerHTML = "";
}