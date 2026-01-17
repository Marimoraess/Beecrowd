<?php

$x = intval(fgets(STDIN));

for($i = 1; $i <= $x; $i++){
    if($i % 2 == 0){
        $power = pow($i, 2);
        echo "$i^2 = $power\n";
    }
}
?>
