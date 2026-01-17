<?php

$qntd_test = intval(fgets(STDIN));

$numbers = [];
for ($i = 0; $i < $qntd_test; $i++) {
  $numbers[] = intval(fgets(STDIN));
}

[$in, $out] = 0;

foreach($numbers as $number){
    if($number >= 10 && $number <= 20){
        $in++;
    }else{
        $out++;
    }
}

echo "$in in\n";
echo "$out out\n";
?>
