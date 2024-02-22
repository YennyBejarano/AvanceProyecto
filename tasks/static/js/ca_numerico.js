// archivo: agregar_usuario.js
document.addEventListener("DOMContentLoaded", function() {
    var cedulaInput = document.getElementById("cedula");
    var celularInput = document.getElementById("celular");
    var nombreInput = document.getElementById("nombre");

    // Configura la validación para cédula
    cedulaInput.addEventListener("input", function() {
        this.value = this.value.replace(/\D/g, ''); // Elimina caracteres no numéricos
        if (this.value.length > 10) {
            this.value = this.value.slice(0, 10); // Limita a 10 dígitos
        }
    });

    // Configura la validación para celular
    celularInput.addEventListener("input", function() {
        this.value = this.value.replace(/\D/g, ''); // Elimina caracteres no numéricos
        if (this.value.length > 10) {
            this.value = this.value.slice(0, 10); // Limita a 10 dígitos
        }
    });

    // Configura la validación para nombre de usuario con espacios
    nombreInput.addEventListener("input", function() {
        this.value = this.value.replace(/[^a-zA-Z\s]/g, ''); // Solo permite letras y espacios
    });

    // Configura validación general para campos vacíos y caracteres especiales
    var form = document.querySelector(".user-form");
    form.addEventListener("submit", function(event) {
        var cedulaValue = cedulaInput.value.trim();
        var celularValue = celularInput.value.trim();
        var nombreValue = nombreInput.value.trim();

        if (cedulaValue === "" || celularValue === "" || nombreValue === "") {
            alert("Todos los campos son obligatorios.");
            event.preventDefault();
        } else if (!/^[a-zA-Z\s]+$/.test(nombreValue)) {
            alert("El nombre solo debe contener letras y espacios.");
            event.preventDefault();
        }
    });
});
