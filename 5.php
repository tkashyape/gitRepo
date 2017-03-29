<?php
	$patient_name=$_POST["patient_name"];
	$patient_email=$_POST["patient_email"];
	$patient_contact=$_POST["patient_contact"];
	$patient_address=$_POST["patient_address"];
	$patient_city=$_POST["city"];
	$patient_state=$_POST["state"];
	$patient_adhar=$_POST["patient_adhar"];
	$patient_dob=$_POST["patient_dob"];
	$patient_gender=$_POST["patient_gender"];
	$patient_bg=$_POST["patient_bg"];
	$patient_password=$_POST["patient_password"];
	require("conn.php");
	$query="INSERT into patient(patient_name,patient_email,patient_contact,patient_address,patient_state,patient_city,patient_adhar,patient_dob,patient_gender,patient_bg,patient_password) values('$patient_name','$patient_email','$patient_contact','$patient_address','$patient_state','$patient_city','$patient_adhar','$patient_dob','$patient_gender','$patient_bg','$patient_password')";
	if(mysqli_query($conn,$query))
	{
		$query1="SELECT * from patient where patient_adhar='$patient_adhar'";
		$result=mysqli_query($conn,$query1);
		$row=mysqli_fetch_array($result,MYSQLI_ASSOC);
        mail($patient_email,"PATIENT ID FOR LOGIN on sushrut.000webhostapp.com","Your PATIENT ID for Login : ".$row["patient_id"],"FROM:sushrut.webhostapp.com");
		echo "<script>alert('Congrats...!!!Check your mail for ID.')</script>";
		header("refresh:0.01 ;url=9.php");
	}
	else
		echo "ENTER CREDENTIALS AGAIN";
?>