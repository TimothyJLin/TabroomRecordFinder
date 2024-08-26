<?php
//header('Content-Type: application/json');
header('Content-Type: text/plain');
 //$item1=$_GET['test'];
//echo $item1.text();

//echo post
$name=$_GET['name'];
$URL=$_GET['url'];
$debaterInformation = array(
    'name' => 'John',
    'school' => 30,
    'url' => 'New York'
  );

echo $debaterInformation;
//echo 'test';
exit;
//json_encode($debaterInformation);
//echo "<script>console.log('This will be logged to the console');</script>";

?>
