window.onload=function(){
        
    document.getElementById("btnSubmit").disabled=true;

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