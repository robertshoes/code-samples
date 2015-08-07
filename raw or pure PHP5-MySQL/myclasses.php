<?php

class User {
    
    private $firstName;
    private $lastName;
    private $email;
    private $password;
    private $userActivated;
    private $creationDate;
    
    public function setFirstName($firstName){
        $this->firstName = $firstName;
    }
    public function getFirstName(){
        return $this->firstName;
    }
    public function setLastName($lastName){
        $this->lastName = $lastName;
    }
    public function getLastName(){
        return $this->lastName;
    }
    public function setEmail($email){
        $this->email = $email;
    }
    public function getEmail(){
        return $this->email;
    }
    public function setPassword($password){
        $this->password = $password;
    }
    public function getPassword(){
        return $this->password;
    }
    public function setUserActivated($userActivated){
        $this->userActivated = $userActivated;
    }
    public function getUserActivated(){
        return $this->userActivated;
    }
    
}


/*This class will handle the connection to the DB
 *It will return a connection handler to manipulate the tables
*/
class MySQLConn {
    /*Wrapper class for mysqli
    */
    
    private $username = "root";
    private $password = "xxxxx";
    private $dbname = "usefulapps";
    private $theConn;
    private $resultSet;
    
    public function getConnection(){
        
        $this->theConn = new mysqli("localhost",$this->username,$this->password, $this->dbname);
        
        if(!$this->theConn){
           die("The connection couldn't be done! " .mysqli_connect_error());
        }    
    }
    
    public function closeConnection(){
        $this->theConn->close();    
    }
    
    public function escapeMe($str){
        return $this->theConn->real_escape_string($str);
    }
    
    public function executeQuery($query){        
        $this->resultSet = $this->theConn->query($query);
        if($this->resultSet === false) {
           trigger_error('Syntax error: ' . $query . ' Error: ' . $this->theConn->error, E_USER_ERROR);
        }
        return $this->resultSet;
    }
    
    public function getNumRows(){
        return $this->resultSet->num_rows;
    }
    
    public function commit(){
        $this->theConn->commit();
    }
    
    public function fetchArray(){
        $this->resultSet->data_seek(0);
        return $this->resultSet->fetch_array(MYSQLI_ASSOC);
    }
    
    public function getLastId(){
        return $this->theConn->insert_id;
    }
    
}



class Queries {
    //Query to get the user count by email
    private $userCountByEmail = "select count(*) from `user` where `email` = ";
    //Query to get the user fields by email
    private $userByEmail = "select * from `user` where `email`= ";
    //insert a new user
    private $insertNewUser = "insert into `user`(`name`, `last_name`, `email`, `password`, `user_activated`) values('%s', '%s', '%s', '%s', '%d')";
    //activate a new user
    private $activateUser = "update `user` set `user_activated`=1 where `user_id`='%d'";
    //insert image
    private $insertImg = "insert into `users_images`(`user_id_img`, `img`, `name_img`, `size`) values ('%s','%s', '%s', '%s')";
    //get images by user
    private $getImgByUserId = "select * from `users_images` where `user_id_img`=%s";
    
    public function getUserCountByEmail(){
        return $this->userCountByEmail;
    }
    public function getUserByEmail(){
        return $this->userByEmail;
    }
    public function insInsertNewUser(){
        return $this->insertNewUser;
    }
    public function updActivateUser(){
        return $this->activateUser;
    }
    public function insInsertImg(){
        return $this->insertImg;
    }
    public function getImgByUserId(){
        return $this->getImgByUserId;
    }
}






?>