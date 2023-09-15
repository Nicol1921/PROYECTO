// regla de validacion

const number=/^[0-9]{5,15}$/ 
const text=/[a-z Ñ ñ á-ú Á-Ú A-Z 0-9]{3,50}/
const pass=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()\-_=+{};:,<.>]).{4,}$/

let flag

// Acceder a los elementos que se van a alterar
const form=document.getElementById("validacion")
console.log(form)

// Acceder al valor digitado en el campo
const Nom=form.Nom.value
const Apl=form.Apl.value
const User=form.User.value
const Pass=form.Pass.value
const confirmm=form.confirmm.value

const f1=document.querySelector("#campoName .feedback")
const f2=document.querySelector("#campoLast .feedback")
const f3=document.querySelector("#user .feedback")
const f4=document.querySelector("#pass .feedback")
const f5=document.querySelector("#conPass .feedback")



// Nombre
form.Nom.addEventListener('input', (e)=>{
    e.preventDefault()

    if (text.test(e.target.value)) {
        //Regla pasa la validacion
        form.Nom.setAttribute("class","succes")
        f1.style.setProperty("visibility","hidden")
        f1.style.setProperty("opacity","0")


    }else{
        form.Nom.setAttribute("class","error")
        f1.textContent="Ingrese los caracteres alfanúmericos que desee (mínimo 3)"
        f1.style.setProperty("visibility","visible")
        f1.style.setProperty("opacity","1")

    }
})

// Apellido
form.Apl.addEventListener('input', (e)=>{
    e.preventDefault()

    if (text.test(e.target.value)) {
        //Regla pasa la validacion
        form.Apl.setAttribute("class","succes")
        f2.style.setProperty("visibility","hidden")
        f2.style.setProperty("opacity","0")

    }else{
        form.Apl.setAttribute("class","error")
        f2.textContent="Ingrese los caracteres alfanúmericos que desee (mínimo 3)"
        f2.style.setProperty("visibility","visible")
        f2.style.setProperty("opacity","1")

    }
})
 

// Correo
form.User.addEventListener('input', (e)=>{
    e.preventDefault()

    if (User.test(e.target.value)) {
        //Regla pasa la validacion
        form.ema.setAttribute("class","succes")
        f3.style.setProperty("visibility","hidden")
        f3.style.setProperty("opacity","0")

    }else{
        form.ema.setAttribute("class","error")
        f3.textContent="Ingrese los caracteres alfanúmericos que desee (mínimo 3)"
        f3.style.setProperty("visibility","visible")
        f3.style.setProperty("opacity","1")

    }
})

// contraseña
form.Pass.addEventListener('input', (e)=>{
    e.preventDefault()

    if (pass.test(e.target.value)) {
        //Regla pasa la validacion
        form.Pass.setAttribute("class","succes")
        f4.style.setProperty("visibility","hidden")
        f4.style.setProperty("opacity","0")

    }else{
        form.Pass.setAttribute("class","error")
        f4.textContent="Ingrese mínimo una letra mayúscula, un número, una letra minúscula y un caracter especial(mínimo 10 caracteres)"
        f4.style.setProperty("visibility","visible")
        f4.style.setProperty("opacity","1")
    }
})

///confirmar contraseña
form.confirmm.addEventListener('input', (e)=>{
    e.preventDefault()

    if (form.confirmm.value === form.Pass.value) {
        //Regla pasa la validacion
        form.confirmm.setAttribute("class","succes")
        f5.style.setProperty("visibility","hidden")
        f5.style.setProperty("opacity","0")
    }else{
        form.confirmm.setAttribute("class","error")
        f5.textContent="Las contraseñas deben ser iguales"
        f5.style.setProperty("visibility","visible")
        f5.style.setProperty("opacity","1")
    }
})

    // alerta de validacion con focus en el campo vacio
    form.addEventListener('submit', (e)=>{
        e.preventDefault()
        flag= true
       
            //Nombre
        if (form.Nom.value==null ||form.Nom.value==0 || !text.test(form.Nom.value)) {
            alert("Debe ingresar un nombre valido")
            form.Nom.focus()
            form.Nom.setAttribute("class","error")
            flag=false
        }
        //Apellido
        if (form.Apl.value==null ||form.Apl.value==0 || !text.test(form.Apl.value)) {
            alert("Debe ingresar un apellido valido")
            form.Apl.focus()
            form.Apl.setAttribute("class","error")
            flag=false
        }
       
        // email
          if (form.User.value==null ||form.User.value==0 ||!text.test(form.User.value)) {
            alert("Debe ingresar un usuario valido")
            form.User.focus()
            form.User.setAttribute("class","error")
            flag=false
        }
        //contraseña
        if (form.Pass.value==null ||form.Pass.value==0 || !pass.test(form.Pass.value)) {
            alert("Debe ingresar una contraseña valida")
            form.Pass.focus()
            form.Pass.setAttribute("class","error")
            flag=falsae
        }
        //confirmacion de contraseña
        if (form.confirmm.value==null ||form.confirmm.value==0 ||!pass.test(form.confirmm.value)||form.confirmm.value != form.Pass.value) {
            alert("Debe ingresar la misma contraseña para la confirmación")
            form.confirmm.focus()
            form.confirmm.setAttribute("class","error")
            flag=false
        }
   
    })