<?php
	session_start();
	session_destroy();
	header("refresh:0.01 ;url=index.php");
?>