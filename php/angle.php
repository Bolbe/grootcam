<?php
// update time stamp only if request comes from camera. In this case myangle is set.

include 'dbconnect.php';

$myangle = 180;
if (isset($_GET['myangle']) && is_numeric($_GET['myangle'])) {   // if set then the request comes from the camera. It is online.
    $myangle = intval($_GET['myangle']);
    if ($myangle>=-90 && $myangle<=90) {
        // update field with timestamp.
        $now = new DateTime('now');
        $sql = "UPDATE grootcam SET grootcam_read_date='".$now->format("Y-m-d H:i:s")."' WHERE grootcam_index=1";
        mysqli_query($db, $sql);
    }
}

$loop = 0;
$angle = 0;
$read_date = "";

while (true) {
    $loop++;
    $result = mysqli_query($db,"SELECT * FROM `grootcam` WHERE `grootcam_index`=1");
    $row = $result->fetch_assoc();
    $angle = $row['grootcam_angle'];
    $read_date = $row['grootcam_read_date'];
    if ($myangle!=$angle || $loop>25) break;
    sleep(2);
}

http_response_code(200);
echo $angle."|".$read_date;
include 'dbdisconnect.php';
