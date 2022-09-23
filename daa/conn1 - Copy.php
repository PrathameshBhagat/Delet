<?php 
$conn = mysqli_connect('localhost','root','','Drones');
$fname= $_POST["name"];
$email = $_POST["email"];
$quantity = $_POST["qty"];
$salary = $_POST["salary"];
$insert = "INSERT INTO orders(name,email,quantity,salary) VALUES('$fname','$email','$quantity','$salary')";
$ins = mysqli_query($conn, $insert);
if($ins)
        echo "<br>inserted successfully";
?>