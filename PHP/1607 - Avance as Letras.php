<?php


function min_operacoes($a, $b) {
    $n = strlen($a);
    $ops = 0;
    for ($i = 0; $i < $n; $i++) {
        
        $diff = ord($b[$i]) - ord($a[$i]);
     
        if ($diff < 0) {
            $diff += 26;
        }
        $ops += $diff;
    }
    return $ops;
}

$T = intval(fgets(STDIN));

for ($i = 0; $i < $T; $i++) {
    // Lê as duas strings
    list($a, $b) = explode(" ", trim(fgets(STDIN)));

    echo min_operacoes($a, $b) . PHP_EOL;
}
?>