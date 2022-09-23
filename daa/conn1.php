<?php 
$server = "localhost";
$username ="root";
$password = "";
$db ="drones";
$conn = mysqli_connect($server,$username,$password,$db) or die("Not conneted");
 if(isset($_POST['submit']))
 {    $fname= $_POST['fname'];
    $lname= $_POST['lname'];
    $num=$_POST['num'];
    $email = $_POST['email'];
    $insert = "INSERT INTO reg1(FirstName,Email,Lastname) VALUES('fname','email','pwd')";
    $ins = mysqli_query($conn, $insert) or die("NOtt");
    mysqli_close($conn);
 }?>