<?php
	$doctor_adhar=$_POST["doctor_adhar"];
	$doctor_email=$_POST["doctor_email"];
	require("conn.php");
	$query="SELECT * from doctor where doctor_adhar='$doctor_adhar' and doctor_email='$doctor_email'";
	$result=mysqli_query($conn,$query);
	if(mysqli_num_rows($result)>0)
	{
		$row=mysqli_fetch_array($result,MYSQLI_ASSOC);
		mail($doctor_email,"PASSWORD FOR LOGIN on sushrut.000webhostapp.com","Your Password for Login : 
".$row["doctor_password"],"FROM:sushrut.webhostapp.com");
		header("refresh:0.01 ;url=6.php");
	}
	else
		header("refresh:0.01 ;url=forgotpassword.php");
?>