<?php
	session_start();
	$prescription=$_POST["prescription"];
	require("conn.php");
	$patient_id=$_SESSION["patient_id"];
	$doctor_id=$_SESSION["doctor_id"];
	$query="INSERT into record(patient_id,doctor_id,prescription) values('$patient_id','$doctor_id','$prescription')";
	if(mysqli_query($conn,$query))
	{
		header("refresh:0.1 ;url=9.php");
	}
	else
		echo "Failed";
?>