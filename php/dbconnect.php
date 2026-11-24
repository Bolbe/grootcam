<?php
        include 'conf.php';
	$db=mysqli_connect("localhost",$dbuser,$dbpassword,"grootcam");
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
		die();
	}
?>
