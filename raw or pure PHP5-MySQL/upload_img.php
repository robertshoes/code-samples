<?php
session_start();

include("./myclasses.php");

//load queries
$q = new Queries();
//Get connection to the DB
$connObj = new MySQLConn();
$connObj->getConnection();

if(isset($_SESSION['username'])){

     //3 scenarios: upload the image, view images and delete image
     //First
     if($_GET['act']=="uimg"){
        
        //TODO: put more restrictions like file size, type of file, etc
        $filename = $connObj->escapeMe($_FILES['imgfile']['name']);
        $fileSize = $_FILES["imgfile"]["size"];
        $fileObj = $_FILES["imgfile"]["tmp_name"];
        $userId = $_SESSION["userId"];
        $sql = sprintf($q->insInsertImg(), $userId, $fileObj, $filename, $fileSize);
        $connObj->executeQuery($sql);
        
        echo "<h1>Your image has been saved!!!</h1>";
        echo "<hr><h3>Please go to the main <a href=http://localhost/dashboard.php>menu</a> for more options.</h3>";
     }
     //Second
     if($_GET['act']=="viewimg"){
        
        $userId = $_SESSION["userId"];
        $connObj->escapeMe($userId);
        $sql = sprintf($q->getImgByUserId(), $userId);
        
        $connObj->executeQuery($sql);
        $result = $connObj->fetchArray();
        
        foreach($result as $img){
            echo '<img src='.$img.'/>';
        }
        
        
        
        echo "<hr><h3>Please go to the main <a href=http://localhost/dashboard.php>menu</a> for more options.</h3>";
     }

}else{
    echo "<h1>Hello there!</h1><hr>";
    
    echo "<h4>If you want to user our services please create an account <a href=http://localhost/new_user.php>here</a>.  Thanks!</h4>";
}


?>