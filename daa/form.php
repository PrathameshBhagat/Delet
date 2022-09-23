<html><head>
<title>registration FORM</title>
<style> 
form {border:orange; border-width:2px;padding:10px; border-style:solid;}
body {padding: 0px 200px 0px 200px;}
</style></head>
<body>
<FORM action="conn.php" method="post"><center>
<legend style="color:blue;"><b> <i>Genral Information</i></b></legend></center>
<p><b>First name: </b><input type="text" name="firstname" placeholder="Mahatma"required >&nbsp&nbsp&nbsp
<b> Last name: </b> <input type="text" name="lastname"placeholder="Ghandhi" required></p> 
</table>
<p> <b> Email*:</b> <td><IMG SRC="http://pngimg.com/uploads/email/email_PNG11.png" HEIGHT="20PX" WIDTH="30PX" ></i></h4></td>
<td><input type="email" name="email" placeholder="your@gamil.com " required><br>
<table>

<td><b>Enter Password&nbsp&nbsp<b></td>
<td><IMG SRC="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Password.svg/1024px-Password.svg.png" HEIGHT="25PX" WIDTH="25PX"></td>
<td><input type="password" name="pwd"value="Enter Password"><br></td>
</table>
<p><b>Mobile no.</b> <input type="number" name="mob"placeholder="123456789" required >
</p><b> Age</b> <input type="number" name="age" placeholder="enter your Age" required ><p >
<p><b>Permanant Address:</b><br><textarea required name="adder" cols="50">Enter your address required</textarea></p> <p>
<p> <b> State:</b> <input type="text" name="state" placeholder="Maharashtra" required>
<p><b> Did you have any Disability</b> <input type="radio" name="r1"> Yes <input type="radio" name="r1">No<p>
<p><b> Date</b> <input type "Date"> <p>
<p><b> Gender <b>
<input type="radio"name="r2"> Male <input type="radio" name="r2">Female <input
type ="radio"name="r2"> Other</p>
<Button id="sl1">Submit</button>
<input type="Reset" id="sl"></input></form>
</Body>
</html>