// validaciones.js
function validarFormulario() {
    // Validar cédula
    var cedulaInput = document.getElementById("cedula");
    var mensajeCedula = document.getElementById("mensajeCedula");
    var cedula = cedulaInput.value.trim();

    // Expresión regular para validar cédula en formato específico
    var regexCedula = /^[0-9]{10}$/;

    if (!regexCedula.test(cedula)) {
        mensajeCedula.innerText = "La cédula debe contener exactamente 10 dígitos numéricos.";
        return false;
    } else {
        mensajeCedula.innerText = "";
    }

    // Otras validaciones para cédula según sea necesario

    // Resto del código de validación para otros campos del formulario

    return true;
}
