<?php

$x = intval(fgets(STDIN));


for($i = 1; $i < 10000; $i++){
    if($i % $x == 2){
        echo "$i\n";
    }
}
?>
