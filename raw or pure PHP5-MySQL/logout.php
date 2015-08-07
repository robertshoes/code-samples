<?php
session_start();
if(isset($_SESSION['username'])){
     echo "<h1>Thanks for using our services ".$_SESSION['username']."</h1>";
     echo "<h2>Come back soon!</h2>";
     session_destroy();
     
}else{
    echo "<h1>Hello there!</h1><hr>";
    
    echo "<h4>If you want to user our services please create an account <a href=http://localhost/new_user.php>here</a>.  Thanks!</h4>";
}


?>