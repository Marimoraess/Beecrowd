<?php

$p = trim(readline());

$conso = array('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z');
$n = str_replace($conso, "", $p);

if($n == strrev($n)){
    echo "S\n";
} else {
    echo "N\n";
}

?>
