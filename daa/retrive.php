<html><head>
<style> 
form {border:orange; border-width:2px;padding:10px; border-style:solid;}
body {padding: 0px 200px 0px 200px;}
</style></head>
<body>
<?php 
$conn = mysqli_connect('localhost','root','','test');

$s = "SELECT * FROM reg";
$ins = mysqli_query($conn, $s);
?>

<form>
<table border="1px" style="width:600px;line:height:40px" >
<tr>
	<th>First Name</th>
	<th>Last Name</th>
	<th>Email</th>
<th>Age</th>
<th>Password</th>
<th>Mobile No</th>
<th>Adderess</th>
<th>State</th>
</tr>
<?php 
while($row=mysqli_fetch_assoc($ins)){?>
<tr>  
        <td><?php echo $row['firstname']?></td>
        <td><?php echo $row['lastname']?></td>
        <td><?php echo $row['email']?></td>
      <td><?php echo $row['Age']?></td>
      <td><?php echo $row['password']?></td>
      <td><?php echo $row['mob']?></td>
      <td><?php echo $row['adder']?></td>
      <td><?php echo $row['state']?></td>

</tr>
<?php } ?>
</form>
</body>
</html>
