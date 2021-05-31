
function validarMiFormulario() { 
    nombrePlanta = document.getElementById('txtNombrePlanta').value;
    descripcionPlanta = document.getElementById('txtDescripcionPlanta').value;
    if(nombrePlanta == '' || descripcionPlanta == '') { 
        alert("Recuerda que ambos campos deben ser llenados"); returnToPreviousPage(); return false; 
    } 
    alert("validations passed"); return true; 
}


