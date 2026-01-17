<?php

    function sequencia_espelho($inicio, $fim) {

        $sequencia = "";
        for ($i = $inicio; $i <= $fim; $i++) {
            $sequencia .= $i;
        }
        
  
        echo $sequencia . strrev($sequencia) . PHP_EOL;
    }
    
    $casos = intval(fgets(STDIN));
    
 
    for ($i = 0; $i < $casos; $i++) {
     
        list($inicio, $fim) = array_map('intval', explode(" ", fgets(STDIN)));
      
        sequencia_espelho($inicio, $fim);
    }
?>