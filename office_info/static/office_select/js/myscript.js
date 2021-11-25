window.onload=function(){
    // Disable the Submit button on page load
    document.getElementById("btnSubmit").disabled=true;
    
    // Enable Disable the Submit button based on the dropdown option
    document.getElementById("dropdown").onchange=function()
    {
        if(this.options[this.selectedIndex].value=="Select Office location")
        {
            document.getElementById("btnSubmit").disabled=true;
        }
        else
        {
            document.getElementById("btnSubmit").disabled=false;
        }
    }
}