<html>

    <head>

	<script type="text/javascript">
            
            function validate() {
                var form_email=document.getElementById("theemail");
                var form_password=document.getElementById("pwd");
                     
                if (form_email.value==""||form_password.value=="") {                    
                   alert("All fields are mandatory.  Your form has one of the two mandatory fields empty.  Please correct this.");
                   return false;
                }else{
                   return true;
                }
            
                
            }
        </script>
    </head>

<body>

<h1>Welcome to the login page!</h1>
<hr>
<h2>Enter the email and password to access your account!</h3>



<form action="validate_user.php" method="post" id="login_form" onsubmit="return validate();">
<table border="4">
<tr><td>email:</td><td><input type="text" name="email" id="theemail"></td></tr>
<tr><td>Password:</td><td><input type="password" name="password" id="pwd"></td></tr>
<tr><td colspan=2 align="center"><input type="reset" value="erase"><input type="submit"></td></tr>
</table>
</form>

<h4>Are you a new user?.  Please enter <a href="./new_user.php">here</a> to create your account!.</h4>

<?php



?>    


</body>


    
</html>
