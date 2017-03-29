<?php
	session_start();
	if(!isset($_SESSION["doctor_id"]))
		header("refresh:0.01 ;url=6.php");
	$patient_name=$_GET["q"];
	require("conn.php");
	$query="SELECT * from patient where patient_name like '%$patient_name%'";
	$result=mysqli_query($conn,$query);
	$row=mysqli_fetch_all($result,MYSQLI_ASSOC);
	echo "<table style='width:50%' border='1px solid black' border-collapse='collapse'>
  <tr>
  	<th>Sr.No</th>
    <th>Name</th>
    <th>City</th> 
    <th>Link</th>
  </tr>";
	for($i=0;$i<mysqli_num_rows($result);$i++)
		echo "<tr><td>".($i+1)."</td><td>".$row[$i]["patient_name"]."</td><td>".$row[$i]["patient_city"]."</td><td><a href=11.php?q=".$row[$i]["patient_id"].">View</a>"."</td></tr>";
	echo "</table></html>";
?>