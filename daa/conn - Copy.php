<?php 
$conn = mysqli_connect('localhost','root','','Drones');
$fname= $_POST["firstname"];

$email = $_POST["email"];
$pwd = $_POST["pwd"];
$mob = $_POST["mob"];
$adder= $_POST["adder"];
$msg = $_POST["message"];
$age = $_POST["age"];
$insert = "INSERT INTO reg1(FirstName,Email,Password,Mob,Adder,State,Age) VALUES('Prathamesh','Bhagat@me.com','Pass','Mobile','AAddwer','State','10')"
$ins = mysqli_query($conn, $insert);
if($ins)
        echo "<br>inserted successfully";
?>
/*('$fname','$email','$pwd','$mob','$adder','$state','$age')"; */