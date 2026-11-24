<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="style.css">
<link rel="shortcut icon" href="grootcam.ico" />
</head>
<body style='color:#AAA;'>
<table><tr><td><img src="grootcam.png"></td><td><h2 style='color:white;'>Grootcam Control</h2>
<?php
    include 'dbconnect.php';
    if (isset($_POST['angle']) && is_numeric($_POST['angle'])) {
        $angle = intval($_POST['angle']);
        if ($angle>=-90 && $angle<=90) {
            $now = new DateTime('now');
            $sql = "UPDATE grootcam SET grootcam_angle='".$angle."', grootcam_write_date='".$now->format("Y-m-d H:i:s")."' WHERE grootcam_index=1";
            mysqli_query($db, $sql);
        }
    }
    $result = mysqli_query($db,"SELECT * FROM `grootcam` WHERE `grootcam_index`=1");
    $row = $result->fetch_assoc();
    $angle = $row['grootcam_angle'];
    $read_date = $row['grootcam_read_date'];
    $poll_date = new Datetime($read_date);
    $now = new DateTime();
    $elasped = $now->getTimestamp()-$poll_date->getTimestamp();
    if ($elasped>55) {
        echo "<p style='color:red;'>Turret OFF</p>";
    }
    else {
        echo "<p style='color:green;'>Turret ON</p>";
    }
    include 'dbdisconnect.php';
?>
</td></tr></table>
Current angle: <?php echo $angle; ?><br>
Last poll from the turret: <?php echo $read_date; ?>
<br><br>
<input type="range" min="-90" max="90" value="0" class="slider" id="slider">
<br><br>

<center>
<form action="index.php" method="post" id="form1">
    <input style="text-align: center;" type="text" id="angle" name="angle" size="3">
</form>
</center>

</body>

<script>
    var slider = document.getElementById("slider");
    var angleBox = document.getElementById("angle");

    slider.value = "<?php echo $angle; ?>";
    angleBox.value = "<?php echo $angle; ?>";

    slider.oninput = function() {
        angleBox.value = this.value;
    }

    slider.onchange = function() {
        document.getElementById("form1").requestSubmit();
    }

</script>

</html>
