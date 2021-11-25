window.onload=function(){
    // Disable submit button on page load
    document.getElementById("btnSubmit").disabled=true;
    // enable & disbale button on dropdown option selected
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