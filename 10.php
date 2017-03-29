<html>
<head>
<script>
	function showHint(str) {
    if (str.length == 0) { 
        document.getElementById("txtHint").innerHTML = "";
        return;
    } else {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("txtHint").innerHTML = this.responseText;
            }
        };
        xmlhttp.open("GET", "faltu1.php?q=" + str, true);
        xmlhttp.send();
    }
}
</script>
</head>
<body>
<form> 
Patient Search: <input type="text" placeholder="PATIENT SEARCH" onkeyup="showHint(this.value)">
</form>
<p><span id="txtHint"></span></p>
</body>
</html>