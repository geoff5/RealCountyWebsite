function registrationValidation()
{
    var password = document.getElementById("password").value;
    var cPassword = document.getElementById("cpassword").value;

    document.getElementById("error1").style.visibility = "hidden";
    document.getElementById("error2").style.visibility = "hidden";

    if(password != cPassword)
    {
        document.getElementById("error1").style.visibility = "visible";
        document.getElementById("error2").style.visibility = "visible";
        return false;
    }

}