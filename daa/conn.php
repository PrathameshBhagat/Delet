<?php 
$conn = mysqli_connect('localhost','root','','test');
$fname= $_POST["firstname"];
$lname= $_POST["lastname"];
$email = $_POST["email"];
$pwd = $_POST["pwd"];
$mob = $_POST["mob"];
$adder= $_POST["adder"];
$state = $_POST["state"];
$age = $_POST["age"];
$insert = "INSERT INTO reg(firstname,lastname,email,password,mob,adder,state,Age) VALUES('$fname','$lname','$email','$pwd','$mob','$adder','$state','$age')";
$ins = mysqli_query($conn, $insert);
if($ins)
        echo "<br>inserted successfully";
?>