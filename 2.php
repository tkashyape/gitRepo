<?php
	session_start(); 
	if(!isset($_SESSION["doctor_id"]))
		header("refresh:0.01 ;url=6.php");
?>
<!DOCTYPE html>
<html>
<head>
	<title>Sushrut</title>
</head>
<body bgcolor=#2ECC71>
	<form method="POST" action="5.php">
		PATIENT NAME:<input type="text" name="patient_name" placeholder="NAME" required><br><br>
		PATIENT EMAIL:<input type="email" name="patient_email" placeholder="EMAIL"
		required><br><br>
		PATIENT CONTACT:<input type="text" name="patient_contact" placeholder="CONTACT" required><br><br>
		PATIENT ADDRESS:<input type="text" name="patient_address" placeholder="ADDRESS" required><br><br>
<script>
		function showHint(str) {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("txtHint").innerHTML = this.responseText;
            }
        };
        xmlhttp.open("GET", "faltu2.php?q="+str, true);
        xmlhttp.send();
}
</script>
PATIENT STATE:<select name="state" onclick="showHint(this.value)">
<option>SELECT</option>
<?php
    require("conn.php");
    $query="SELECT distinct city_state from cities order by city_state ASC";
    $result=mysqli_query($conn,$query);
    $row=mysqli_fetch_all($result,MYSQLI_ASSOC);
    for($i=0;$i<mysqli_num_rows($result);$i++)
        echo "<option value=".$row[$i]['city_state'].">".$row[$i]['city_state']."</option>";
?>
    </select><br><br>
PATIENT CITY:<span id="txtHint"></span><br><br>
		PATIENT AADHAR NO:<input type="text" name="patient_adhar" placeholder="AADHAR" required><br><br>
		PATIENT DOB:<input type="date" name="patient_dob" required><br><br>
		PATIENT GENDER:<select name="patient_gender" required>
			<option value="MALE">MALE</option>
			<option value="FEMALE">FEMALE</option>
			<option value="OTHER">OTHER</option>
		</select><br><br>
		PATIENT BLOOD GROUP:<select name="patient_bg" required>
			<option value="AB+">AB+</option>
			<option value="AB-">AB-</option>
			<option value="A+">A+</option>
			<option value="A-">A-</option>
			<option value="B+">B+</option>
			<option value="B-">B-</option>
			<option value="O+">O+</option>
			<option value="O-">O-</option>
		</select><br><br>
		PASSWORD:<input type="password" name="patient_password" placeholder="PASSWORD" required><br><br>
		<input type="submit" value="REGISTER patient">
	</form>
</body>
</html>