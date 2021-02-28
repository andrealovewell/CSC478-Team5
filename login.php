<!DOCTYPE html>
<html>
    <head>
        <title>JAM Log in</title>
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
            <div class ="form">
                <!--register new user-->
                <form class="register" action="index.php" method="post">
                    <input type="text" id="firstName" name="firstName" placeholder = "First Name"/>
                    <input type="text" id="lastName" name="lastName" placeholder = "Last Name"/>
                    <input type="email" id="email" name="email" placeholder = "email@example.com"/>
                    <input type="number" id="phoneNumber" name="phoneNumber" placeholder = "1234567890"/>
                    <input type="password" id="password" name="password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" placeholder = "choose a password"/>
                    <!--check pw for validity-->
                    <ul id="message">
                        <h5>Password must contain the following:</h5>
                        <div id="lowercase" class="invalid">A <b>lowercase</b> letter</div>
                        <div id="capital" class="invalid">A <b>capital (uppercase)</b> letter</div>
                        <div id="number" class="invalid">A <b>number</b></div>
                        <div id="length" class="invalid">Minimum <b>8 characters</b></div>
                    </ul>
                    <button id="regBtn" type="submit">Register</button>
                    <p class="message">Already registered? <a href="#">Log In</a></p>
                </form>
                <!--log in, returning user-->
                <form class="login" action="main.php" method="post">
                    <h3>Welcome Back!</h3>
                    <input type="email" name="email" placeholder = "email@example.com"/>
                    <input type="password" name="password" id="current-password" placeholder = "password"/>
                    <button id="logBtn" type="submit">Log In</button>
                    <!--commented out for now--/ <p class="message"><a href="#">Forgot Password? </a></p> /---->
                    <p class="message">Not registered? <a href="#">Create New Account</a></p>
                </form>
            </div>	
        </div>
        
        <!--PHP-->
        <?php
        
            if($_SERVER['REQUEST_METHOD'] == 'POST') {


                $name = $_POST['firstName']." ".$_POST['lastName'];
                $email = $_POST['email'];
                $password = $_POST['password'];
                $phone_number= "+".$_POST['phoneNumber'];

                $registration = (object) [
                    'name' => $name,
                    'email' => $email,
                    'password' => $password,
                    'phone_number' => $phone_number
                ];
                
                $registration = json_encode($registration);


                $url = "https://accxsx6g7g.execute-api.us-west-2.amazonaws.com/Beta/signup";
                $curl = curl_init($url);
                curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
                curl_setopt($curl, CURLOPT_POST, true);
                curl_setopt($curl, CURLOPT_POSTFIELDS, $registration);
                curl_setopt($curl, CURLOPT_HTTPHEADER, [
                    'Accept: application/json'
                ]);

                $response = curl_exec($curl);
                curl_close($curl);
                
            }
        ?>
        
        <!--javascript-->
        <script>
            //hides registration form
            $('.message a').click(function () {
                $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
            });

            //password requirement validation
            var myInput = document.getElementById("password");
            var letter = document.getElementById("lowercase");
            var capital = document.getElementById("capital");
            var number = document.getElementById("number");
            var length = document.getElementById("length");

// show message when user clicks inside of pw box
            myInput.onfocus = function () {
                document.getElementById("message").style.display = "block";
            }

// hide message when clicked outside of pw box
            myInput.onblur = function () {
                document.getElementById("message").style.display = "none";
            }

// pw validation message appears with password input
            myInput.onkeyup = function () {
                // pw lowercase letter
                var lowerCaseLetters = /[a-z]/g;
                if (myInput.value.match(lowerCaseLetters)) {
                    letter.classList.remove("invalid");
                    letter.classList.add("valid");
                } else {
                    letter.classList.remove("valid");
                    letter.classList.add("invalid");
                }

                // pw capital letter
                var upperCaseLetters = /[A-Z]/g;
                if (myInput.value.match(upperCaseLetters)) {
                    capital.classList.remove("invalid");
                    capital.classList.add("valid");
                } else {
                    capital.classList.remove("valid");
                    capital.classList.add("invalid");
                }

                // pw numbers
                var numbers = /[0-9]/g;
                if (myInput.value.match(numbers)) {
                    number.classList.remove("invalid");
                    number.classList.add("valid");
                } else {
                    number.classList.remove("valid");
                    number.classList.add("invalid");
                }

                // pw length
                if (myInput.value.length >= 8) {
                    length.classList.remove("invalid");
                    length.classList.add("valid");
                } else {
                    length.classList.remove("valid");
                    length.classList.add("invalid");
                }
            }
        </script>
    </body>
</html>