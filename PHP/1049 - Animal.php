<?php
$x = trim(fgets(STDIN));
$y = trim(fgets(STDIN));
$z = trim(fgets(STDIN));

$three = [
    'vertebrado' => [
        'ave' => [
            'carnivoro' => 'aguia',
            'onivoro' => 'pomba'
        ],
        'mamifero' => [
            'onivoro' => 'homem',
            'herbivoro' => 'vaca'
        ],
    ],
    'invertebrado' => [
        'inseto' => [
            'hematofago' => 'pulga',
            'herbivoro' => 'lagarta'
        ],
        'anelideo' => [
            'hematofago' => 'sanguessuga',
            'onivoro' => 'minhoca'
        ],
    ],
];

echo $three[$x][$y][$z]."\n";



?>
