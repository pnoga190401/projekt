<?php
    $data1 = "Paulina Noga";
    $data2 = "Paulina Nogax";
    echo hash('md5', $data);
    echo '\n\r';
    echo hash('sha256', $data2);
    echo '\n\r';
    echo hash('haval256,5', $data2);
?>

