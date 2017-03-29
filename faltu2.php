<?php
    $q = $_GET["q"];
    require("conn.php");
    $query="SELECT city_name from cities where city_state='$q' order by city_name ASC";
    $result=mysqli_query($conn,$query);
    $rows=mysqli_num_rows($result);
    $row=mysqli_fetch_all($result,MYSQLI_ASSOC);
    echo "<select name='city'>";
    for($i=0;$i<$rows;$i++)
    {
        echo "<option>".$row[$i]['city_name']."</option>";
    }
    echo "</select>";
?>