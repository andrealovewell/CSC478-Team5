<!DOCTYPE html>

<html>
    <head>
        <title>JAM</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" href="loginStyles0.1.css">
        <!-- load scripts -->
        <script src="script.js"></script>
        <script src="https://unpkg.com/react@17/umd/react.development.js" crossorigin></script>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    </head>
    <body>
        <header>
            <div id="title" class="form-title"><b>JAM</b></div>
            <div id="title" class="form-subscript">the Job Application Manager</div>
        </header>
        <div class ="login-page">
            <?php
            
            if($_SERVER['REQUEST_METHOD'] == "POST") {
                
                
                $login = (object) [
                    'email' => $_POST['email'],
                    'password' => $_POST['password']
                ];
                
                $login = json_encode($login);
                
                $url = "https://accxsx6g7g.execute-api.us-west-2.amazonaws.com/Beta/signin";
                $curl = curl_init($url);
                curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
                curl_setopt($curl, CURLOPT_POST, true);
                curl_setopt($curl, CURLOPT_POSTFIELDS, $login);
                curl_setopt($curl, CURLOPT_HTTPHEADER, [
                    'Accept: application/json'
                ]);

                $response = curl_exec($curl);
                curl_close($curl);
                
                print "Welcome! The site is under development, come back soon. :)";
                
            }
            ?>
        </div>
</html>