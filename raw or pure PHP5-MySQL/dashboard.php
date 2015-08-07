<?php
session_start();

if(isset($_SESSION['username'])){
    $username = $_SESSION['username'];
    $email = $_SESSION['email'];
    $userId = $_SESSION['userId'];

    echo "<h1>Welcome to your dashboard ".$username."!!!<br>";
    echo "Your email address is ".$email;
    
    echo "<h3>Menu</h3>";
    echo "<ul><li><a href=http://localhost/upload_form.php>Upload an image</a></li>
              <li><a href=http://localhost/upload_img.php?act=viewimg>View all images</a></li>
              <li><a href=http://localhost/upload_img.php?act=dimg>Delete an image</a></li>
              <li><a href=http://localhost/logout.php>Logout</a></li>
          </ul>";
}else{
    echo "<h1>Hello there!</h1><hr>";
    
    echo "<h4>If you want to user our services please create an account <a href=http://localhost/new_user.php>here</a>.  Thanks!</h4>";
}

?>