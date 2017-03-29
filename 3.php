<?php
	$doctor_id=$_POST["doctor_id"];
	$doctor_password=$_POST["doctor_password"];
	require("conn.php");
	$query="SELECT * from doctor where doctor_id='$doctor_id' and doctor_password='$doctor_password'";
	$result=mysqli_query($conn,$query);
	if(mysqli_num_rows($result)==0)
	{
		header("refresh:0.1 ;url=6.php");
	}
	else
	{
        $row=mysqli_fetch_array($result,MYSQLI_ASSOC);
		session_start();
		$_SESSION["doctor_id"]=$doctor_id;
                $_SESSION["doctor_name"]=$row["doctor_name"];
		header("refresh:0.1 ;url=9.php");
	}
?>