// import React, { useState } from "react";
// import 'bootstrap/dist/css/bootstrap.min.css';

// import {Button, Modal, Form } from 'react-bootstrap';
// import {Link, useHistory} from 'react-router-dom';

// import {axios} from 'axios';



// function SignUpForm() {

    

//     //Functional states - Forms
//     const [formFields, setFormFields] = useState({
//         username: "",
//         password: "",
//         confirmPassword: "",
//         DOB: "",
//         email: "",
//     });

//     const history = useHistory();
//     const [newUser, setNewUser] = useState(null);
//     const [isLoading, setIsLoading] = useState(false); 

//     //Functional states - Modals
//     const [show, setShow] = useState(false);
//     const handleClose = () => setShow(false);
//     const handleShow = () => setShow(true);



//     //Validations
//     function validateUsername(user) {
//         console.log(user);
//         return ((user == formFields.username) ? true : false)
//     }

//     function validateEmail(response){
//         return ((response.status !== 200) ? false : (response.data.Email_free))
//     }

//     function validateBirth18(dob) {
//         //format yyyy-mm-dd as string
//         const myDateString = dob.split("-");
//         return new Date(parseInt(myDateString[0])+18, parseInt(myDateString[1])-1, parseInt(myDateString[2])) <= new Date();

//     }


    
//     function handleValidation(){
//         // const api_url = "http://localhost:8000/api";

//         // const valUsernameLength = (formFields.username.length > 0);

//         // // //check if exists: api_url/user/<username> 
//         // // const valUser = axios.get(api_url+"/user/"+formFields.username)
//         // //     .then((response) => { validateUsername(response.data.username)});

//         //             //check if exists: api_url/user/<username> 
//         // axios.get('http://localhost:8000/api/user/Admin')
//         //     .then((response) => { 
//         //         validateUsername(response.data.username)
//         //     });


//         // //check if exists: api_url/email/<email@email> rather than <email@email.com>
//         // var shortEmail = formFields.email.match(/((\S)+|(\S\.)+)@(\w+)/);
//         // const valEmailFree = axios.get(api_url+"/email/"+shortEmail)
//         //     .then((response) => {validateEmail(response)});

//         // const valEmailLength = (formFields.email.length > 0);

//         // const valPasswordLength = (formFields.password.length > 0);
//         // const valConfirmPassword = (formFields.confirmPassword.length > 0);
//         // const valSamePassword = (formFields.password === formFields.confirmPassword);

//         // //check if date of birth produces 18+ years old
//         // const valDOB = validateBirth18(formFields.DOB);


//         // return (valUsernameLength && valUser && valEmailFree && 
//         //                 valEmailLength && valPasswordLength && 
//                         // valConfirmPassword && valSamePassword && valDOB);

//     }




//     return (
//         <div>
//             <Button variant="primary" onClick={handleValidation()}>
//                 Test Me
//             </Button>
//         </div>
//     )
// }

// export default SignUpForm
