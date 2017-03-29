<!DOCTYPE html>
<html>
<head>
	<title>Sushrut</title>
</head>
<body bgcolor=#2ECC71>
	<form method="POST" action="4.php">
		DOCTOR NAME:<input type="text" name="doctor_name" placeholder="NAME" required><br><br>
		DOCTOR EMAIL:<input type="email" name="doctor_email" placeholder="EMAIL"
		required><br><br>
		DOCTOR CONTACT:<input type="text" name="doctor_contact" placeholder="CONTACT" required><br><br>
		DOCTOR ADDRESS:<input type="text" name="doctor_address" placeholder="ADDRESS" required><br><br>
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
DOCTOR STATE:<select name="state" onclick="showHint(this.value)">
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
DOCTOR CITY:<span id="txtHint"></span><br><br>
		DOCTOR AADHAR NO:<input type="text" name="doctor_adhar" placeholder="AADHAR" required><br><br>
		DOCTOR REG. NO.:<input type="text" name="doctor_reg" placeholder="REGISTRATION NUMBER" required><br><br>
		DOCTOR DEGREE:<input type="text" name="doctor_deg" placeholder="DEGREE" required><br><br>
		DOCTOR SPECIALIZATION:<input type="text" name="doctor_spec" placeholder="SPECIALIZATION" required><br><br>
		DOCTOR DOB:<input type="date" name="doctor_dob" required><br><br>
		DOCTOR GENDER:<select name="doctor_gender" required>
			<option value="MALE">MALE</option>
			<option value="FEMALE">FEMALE</option>
			<option value="OTHER">OTHER</option>
		</select><br><br>
		PASSWORD:<input type="password" name="doctor_password" placeholder="PASSWORD" required><br><br>
		<input type="submit" value="REGISTER DOCTOR">
	</form>
</body>
</html>