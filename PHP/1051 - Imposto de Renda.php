<?php
$x = floatval(fgets(STDIN));

$taxes = [
    0 => ['min' => 00.00, 'max' => 2000.00, 'tax' => 0],
    1 => ['min' => 2000.01, 'max' => 3000.00, 'tax' => 0.08],
    2 => ['min' => 3000.01, 'max' => 4500.00, 'tax' => 0.18],
    3 => ['min' => 4500.01, 'max' => PHP_FLOAT_MAX, 'tax' => 0.28],
];

$total_tax = 0;

if($x > 2000.00) {
    $max_tax = count($taxes);

    while ($max_tax > 0) {
        foreach($taxes as $key => $salary) {
            if ($x >= $salary['min'] && $x <= $salary['max'] && $key > 0) {
                $y = $taxes[$key-1]['max'];

                $total_tax += ($x-$y)*$salary['tax'];

                $x = $y;
            }
        }
        
        $max_tax--;
    }

    $total_tax = "R$ " . sprintf('%.2f', $total_tax);
}else{
    $total_tax = "Isento";

}
echo  $total_tax . "\n";



?>
