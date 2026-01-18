<?php

$x = fgets(STDIN);

$readjustment = [
    0 => ['min' => 00.00, 'max' => 400.00, 'readjustment' => 0.15],
    1 => ['min' => 400.01, 'max' => 800.00, 'readjustment' => 0.12],
    2 => ['min' => 800.01, 'max' => 1200.00, 'readjustment' => 0.10],
    3 => ['min' => 1200.01,'max' => 2000.00, 'readjustment' => 0.07],
    4 => ['min' => 2000.01, 'max' => PHP_FLOAT_MAX, 'readjustment' => 0.04],
];

foreach($readjustment as $salary) {
    if ($x >= $salary['min'] && $x <= $salary['max']) {
        $increase = sprintf("%.2f", ($x*$salary['readjustment']));
        $new_salary = sprintf("%.2f", ($x+$increase));
        $percent = ($salary['readjustment']*100). " %";

        echo "Novo salario: $new_salary\n";
        echo "Reajuste ganho: $increase\n";
        echo "Em percentual: $percent\n";

        break;
    }
}


?>
