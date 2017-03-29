<?php
	session_start();
	if(!isset($_SESSION["doctor_id"]))
		header("refresh:0.01 ;url=6.php");
	$patient_id=$_POST["patient_id"];
	require("conn.php");
	$query="SELECT * from patient where patient_id='$patient_id'";
	$result=mysqli_query($conn,$query);
	if(mysqli_num_rows($result)>0)
	{
		$_SESSION["patient_id"]=$patient_id;
		echo "<html>
		<body bgcolor=#2ECC71>
		PRESCRIPTION:<br><br>
		<form method='POST' action='8.php'>
			<textarea name='prescription' rows='10' cols='30'></textarea><br><br>
			<input type='submit' value='SUBMIT'>
		</form>
		</body>
		</html>
		";
	}
	else
		header("refresh:0.01 ;url=2.php");

?>