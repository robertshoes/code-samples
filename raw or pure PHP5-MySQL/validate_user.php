
<?php
session_start();

include("./myclasses.php");

//load queries
$q = new Queries();
//Get connection to the DB
$connObj = new MySQLConn();
$connObj->getConnection();

if(isset($_GET['userId'])){
    /*Handling the case when the user need to be activated
    */
    $id = $_GET['userId'];
    $query_str = sprintf($q->updActivateUser(), $id);
    //echo "This is the formatted string:<br>";
    //echo $query_str."<br>";
    $connObj->executeQuery($query_str);
    
    echo "<h1>Account activated!</h1><hr>";
    echo "Your account has been activated!<br>";
    echo "Please go to this <a href='http://localhost/login.php'>link</a> to login!";
   
}else{
    
$userObj = new User();
$userObj->setFirstName($_POST["firstname"]);
$userObj->setLastName($_POST["lastname"]);
$userObj->setEmail($_POST["email"]);
$userObj->setPassword($_POST["password"]);
$userObj->setUserActivated(0); //by default

//echo "The name you sent is:  ". $userObj->getFirstName() . "!!!";

/*Validate if the user exists.  If it does, then just check if its already activated by checking this field in the DB, if not
 *then resend an activation email to the email of the user and redirect the user to a page where it tells that an email has been sent to
 *activate the account.  If the user doesn't exist then create it and put the activated field in the DB
 *in 0 and send activation email to the user's email account and redirect it to the screen that tells that an email has been sent to his/her account
 *to activate the account.
 *If the account already exists and is activated then redirect the user to the dashboard.
*/

//execute query to see if the user exist
$email = $connObj->escapeMe($userObj->getEmail());
$result = $connObj->executeQuery($q->getUserByEmail()."'$email'");

$usersCount = $connObj->getNumRows();
//echo "You selected ".$usersCount." users<br>"."select * from `user` where `email`=".$userObj->getEmail();


if($usersCount <= 0){
    /*First case: a new user needs to be created
     *We need to create the user in the DB with the user_activated flag with 0 and send an email
     *with a url like this: localhost/validate_user?userID=id&hash_email=hash&userActivated=1;
    */
    
    $query_str = sprintf($q->insInsertNewUser(), $userObj->getFirstName(), $userObj->getLastName(), $userObj->getEmail(), $userObj->getPassword(),
                   $userObj->getUserActivated());
    //echo "This is the formatted string:<br>";
    //echo $query_str;
    
    $result = $connObj->executeQuery($query_str);
    $lastId = $connObj->getLastId();
    $connObj->commit();
    
    //echo "This is my last id inserted: ". $lastId;
    
    //Send email to the user
    /*This part will have to be emulated with only an echo in this very same page
     *because I need to set a mail server for this.
    */
    /*
    $msg = "New user account created for usefulapps!\n
           username: ".$userObj->getEmail()."\n".
           "password: ".$userObj->getPassword()."\n".
           "To activate your account go to this <a href='http://localhost/validate.php?userId='.$lastId>link</a>.";
    mail($userObj->getEmail(),"Account validation from usefulapps!", $msg);
    */
    echo "<h1>Account created!</h1><hr>";
    echo "<br><h4>An email has been sent to you in order to activate the account created.</h4><br>";
    echo "<h4>To activate your account please go to this <a href=http://localhost/validate_user.php?userId=$lastId>link</a></h4><br>";

}else{
    /*Two possible scenarios here: the first one is that the user already exists but is not activated.  We tell the user that
     *he/she need to check his/her email acccount in order to activate our account.
     *The second one is that the user already exists and is activated.  We validate that the username and password match
     *and redirect the user to the dashboard.  This scenario will be
     *applied to the login.php too.
    */
    $arr = $connObj->fetchArray();
    $userId = $arr["user_id"];
    //First scenario
    if($arr['user_activated']==0){
        echo "This user is already created.  Please go to your email account and activate this user or
              go to this <a href=http://localhost/validate_user.php?userId=$userId>link</a>";
    }else{
        //Second scenario
        if($userObj->getEmail() == $arr["email"] && $userObj->getPassword() == $arr["password"]){
            //setting a session for this validated user
            $_SESSION["username"] = $arr["name"];
            $_SESSION["email"] = $arr["email"];
            $_SESSION["userId"] = $arr["user_id"];
            //now I redirect the user to the dashboard
            header('Location: ' . "http://localhost/dashboard.php", true, 301);
        }else{
            echo "Email and password do not match.  Please <a href=http://localhost/login.php>check</a> again.";
        }
    }
    
}

}

//At the end close mysql connection
$connObj->closeConnection();

?>