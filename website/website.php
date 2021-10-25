<html>
    <head>
        <title>Alter Way</title>
    </head>

    <body>
        <h1>DevOps Test</h1>
        <ul>
            <?php

            $json = file_get_contents('http://deploy/');
            $obj = json_decode($json);

            $products = $obj->outputDiv;

            foreach ($products as $product) {
                echo "<li>$product</li>";
            }

            ?>
        </ul>
    </body>
</html>