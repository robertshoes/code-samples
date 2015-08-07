<html>

    <head>

	
            <script type="text/javascript">
            
            function validate() {
                var form_firstname=document.getElementById("thefirstname");
                var form_lastname=document.getElementById("thelastname");
                var form_email=document.getElementById("theemail");
                var form_password=document.getElementById("pwd");
                     
                if (form_email.value==""||form_password.value==""||form_firstname.value==""||form_lastname.value=="") {                    
                   alert("All fields are mandatory.  Your form has one or more mandatory fields empty.  Please correct this.");
                   return false;
                }else{
                   return true;
                }
            
                
            }
            
        </script>
            
        
    </head>

<body>

<h1>Welcome to the user registration page!</h1>
<hr>    
<h2>Fill the quick form bellow and create your new account!</h3>



<form action="validate_user.php" method="post" onsubmit="return validate()">
<table border="4">
<tr><td>First Name:</td><td><input type="text" name="firstname" id="thefirstname"></td></tr>
<tr><td>Last Name:</td><td><input type="text" name="lastname" id="thelastname"></td></tr>
<tr><td>email:</td><td><input type="text" name="email" id="theemail"></td></tr>
<tr><td>Password:</td><td><input type="password" name="password" id="pwd"></td></tr>
<tr><td colspan=2 align="center"><input type="reset" value="erase"><input type="submit"></td></tr>
</table>
</form>


</body>


    
</html>
