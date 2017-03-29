<?php
	session_start();
	if(!isset($_SESSION["doctor_id"]))
		header("refresh:0.1 ;url=index.php");
	$patient_id=$_GET["q"];	
	echo "Patient Id: ".$patient_id;
?>