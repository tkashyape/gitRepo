<?php
	$doctor_name=$_POST["doctor_name"];
	$doctor_email=$_POST["doctor_email"];
	$doctor_contact=$_POST["doctor_contact"];
	$doctor_address=$_POST["doctor_address"];
	$doctor_city=$_POST["city"];
	$doctor_state=$_POST["state"];
	$doctor_adhar=$_POST["doctor_adhar"];
	$doctor_reg=$_POST["doctor_reg"];
	$doctor_deg=$_POST["doctor_deg"];
	$doctor_spec=$_POST["doctor_spec"];
	$doctor_dob=$_POST["doctor_dob"];
	$doctor_gender=$_POST["doctor_gender"];
	$doctor_password=$_POST["doctor_password"];
	require("conn.php");
	$query="INSERT into doctor(doctor_name,doctor_email,doctor_contact,doctor_address,doctor_city,doctor_state,doctor_adhar,doctor_reg,doctor_deg,doctor_spec,doctor_dob,doctor_gender,doctor_password) values ('$doctor_name','$doctor_email','$doctor_contact','$doctor_address','$doctor_city','$doctor_state','$doctor_adhar','$doctor_reg','$doctor_deg','$doctor_spec','$doctor_dob','$doctor_gender','$doctor_password')";
	if(mysqli_query($conn,$query))
	{
		$query1="SELECT * from doctor where doctor_adhar='$doctor_adhar'";
		$result=mysqli_query($conn,$query1);
		$row=mysqli_fetch_array($result,MYSQLI_ASSOC);
		mail($doctor_email,"Your DOCTOR ID for Login : ".$row["doctor_id"],"FROM:sushrut.webhostapp.com");
		echo "<script>alert('Congrats...!!!Check your mail for ID.')</script>";
		header("refresh:0.1 ;url=6.php");
	}
	else
		echo "ENTER CREDENTIALS AGAIN";
?>