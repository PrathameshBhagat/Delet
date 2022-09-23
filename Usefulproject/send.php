<?php 
include "conn.php";
$name=  $_POST["name"];
$sname= $_POST["sname"];
$mname= $_POST["mname"];
$fname= $_POST["fname"];
$pno= $_POST["pno"];
$fno= $_POST["fno"];
$mno= $_POST["mno"];
$eno= $_POST["eno"];
$Place= $_POST["Place"];
$Instituiton= $_POST["Instituiton"];
$cInstituiton=$_POST["cInstitution"];
$fInstituiton=$_POST["fInstitution"];
$d1= $_POST["d1"];
$d2= $_POST["d2"];
$m1= $_POST["m1"];
$m2= $_POST["m2"];
$y1= $_POST["y1"];
$y2= $_POST["y2"];
$y3= $_POST["y3"];
$y4= $_POST["y4"];
/*$index= $_POST["index"];*/
$date=$y1.$y2.$y3.$y4."-".$m1.$m2."-".$d1.$d2;
echo $date;
$index=45;
$i=NULL;
$insert = "INSERT INTO indivisual(id, Indexe, Name, Father, Surname, Mother, Phone, PFather,PMother,PExtra,DOB,CPlaces,PInstitutions,CInstitution,FInstitution) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
$stmt = mysqli_prepare($conn,$insert);
mysqli_stmt_bind_param($stmt,'sisssssssssssss',$i ,$index,$name,$fname,$sname,$mname,$pno,$fno,$mno,$eno,$date,$Place,$Instituiton,$cInstituiton,$fInstituiton);
$result = mysqli_stmt_execute($stmt);

?>
