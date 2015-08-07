<?php
session_start();
?>
<html>
<body>

<?php
    if(isset($_SESSION['username'])){

        echo "<h1>Upload your image file ".$_SESSION['username']."</h1>";
    }else{
        echo "<h1>Hello there!</h1><hr>";
        echo "<h4>If you want to user our services please create an account <a href=http://localhost/new_user.php>here</a>.  Thanks!</h4>";
    }
?>

<form action="/upload_img.php?act=uimg" enctype="multipart/form-data" method="post">
<table border=4><tr><td>File:</td><td><input type="file" name="imgfile" id="the_img_file"><br></td></tr>
<tr><td colspan=2 align="center"><input type="submit" name="submit" value="Submit"></td></tr>
</table>
</form>

</body>
</html>

