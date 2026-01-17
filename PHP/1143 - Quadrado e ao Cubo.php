<?php

$input = intval(fgets(STDIN));

for($x = 1; $x <= $input; $x++){

    for($j = 1; $j <= 3; $j++){
        echo ($j != 3)  ? pow($x, $j) . " " : pow($x, $j);
    } 
    echo "\n";
}