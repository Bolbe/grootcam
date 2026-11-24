<?php

include 'dbconnect.php';
if (!isset($_POST['angle']) || !is_numeric($_POST['angle'])) {
    http_response_code(400);
    die;
}
$angle = intval($_POST['angle']);
if ($angle<-90 || $angle>90) {
    http_response_code(400);
    die;
}

$now = new DateTime('now');
$sql = "UPDATE grootcam SET grootcam_angle='".$angle."', grootcam_write_date='".$now->format("Y-m-d H:i:s")."' WHERE grootcam_index=1";
mysqli_query($db, $sql);

// read date
$result = mysqli_query($db,"SELECT * FROM `grootcam` WHERE `grootcam_index`=1");
$row = $result->fetch_assoc();
$read_date = $row['grootcam_read_date'];

echo $read_date;
http_response_code(200);
include 'dbdisconnect.php';
