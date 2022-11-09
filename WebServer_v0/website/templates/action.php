<!DOCTYPE html>
    <html>
        <Head>
            <title>Search Results</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='css/search.css') }}">
            
        </Head>
        <body style="background-color: white;">
            <!-- Header section-->
            <header>
                <section id = "header" class = "header">
                   <!-- <h1>GPU Web Scraper</h1> -->
                </section>
            </header>
            {% extends "base.html" %} {% block title %}Home{% endblock %}
            {% block content %}

            <table>
                <tr>
                    <th>Price</th>
                    <th>GPU Name</th>
                    <th>Memory</th>
                </tr>
                
                <?php
                    $host        = "host = 127.0.0.1";
                    $port        = "port = 5432";
                    $dbname      = "dbname = postgres";
                    $credentials = "user = postgres password=Csc394ishard";

                    $db = pg_connect( "$host $port $dbname $credentials"  );
                    if(!$db) {
                        echo "Error : Unable to open database\n";
                    } else {
                        echo "Opened database successfully\n";
                    }

                    $sql =<<<EOF
                        SELECT * from GPUS;
                    EOF;

                    $ret = pg_query($db, $sql);
                    if(!$ret) {
                        echo pg_last_error($db);
                        exit;
                    } 
                    while($row = pg_fetch_row($ret)) {
                        echo "<tr><td>".$row[0]."<td><td>".$row[2]."<td><td>".$row[1]."<td><td>".$row[3]."<td><td>".$row[4]."<td><tr>".;
                    }
                    echo "Operation done successfully\n";
                    pg_close($db);
                ?>
                
                

            </table>
            
            {% endblock %}
        </body>
    </html>