<?php
	session_start();
	if(!isset($_SESSION["doctor_id"]))
		header("refresh:0.01 ;url=6.php");
?>
<!DOCTYPE html>
<html>
<head>
	<title>SUSHRUT-RECORD</title>
</head>
<?php
        echo "Hello Dr.".$_SESSION["doctor_name"];
?>
<body bgcolor=#2ECC71>
	<form method="POST" action="7.php">
		PATIENT-ID:<input type="text" name="patient_id" placeholder="PATIENT-ID" required><br><br>
		<input type="submit" value="SUBMIT"><br><br>
	</form>
	<a href="2.php">NEW PATIENT</a><br><br>
	<a href="10.php">PATIENT SEARCH</a><br><br>
	<a href="logout.php">LOGOUT</a>
</body>
</html>