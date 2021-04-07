import {useState, useEffect} from 'react';
import {Button, Modal, Form } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom';

import axios from 'axios';

function SignUp() {
    

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    // const [formData, setFormData] = useState({
    //     username: "",
    //     password: "",
    //     confirmed_password: "",
    //     date_of_birth: "",
    //     email: "",

    // })

    const [username, setUsername] = useState("");
    const [origPassword, setOrigPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [dateOfBirth, setDateOfBirth] = useState("");
    const [userEmail, setUserEmail] = useState("");

    const [validated, setValidated] = useState(false);
    // const [subForm, setSubForm] = useState(false);



  
    const api_url = ("/api/make-user/");
    



    const handleSubmit = e => {
        e.preventDefault();

        async function postUser(){
            const result = await axios.post(api_url, {
                username: username,
                password: origPassword,
                confirmed_password: confirmPassword,
                date_of_birth: dateOfBirth, 
                email: userEmail, 
            }).then((response) => {
                console.log(response);

            }, (error) => {
                console.log(error);

            });
        };
        
        setValidated(true);
        postUser();

    //     async function postUser () {
    //         const result = await axios.post(api_url, user);
    //     };



    //     postUser();

    };


    // const handleStateUpdate = (e) => {

    //     console.log([e.target.name], e.target.value);
    //     setFormData({
    //         ...formData,
    //         [e.target.name]: e.target.value
    //     });

    // };




    return (
        <>
            <Button variant="primary" onClick={handleShow}> Sign Up </Button>
            <Modal show={show} onHide={handleClose}>

                <Modal.Header closeButton>
                    <Modal.Title> Sign Up </Modal.Title>
                </Modal.Header>

                <Modal.Body>
                    <Form noValidate validated={validated}  onSubmit={handleSubmit}>

                        {/* Username Form Input */}
                        <Form.Group controlId="formUsername">
                            <Form.Label>Username</Form.Label>
                            <Form.Control
                                required
                                type="text"
                                placeholder="Enter username"
                                value={username}
                                onChange={(e) => {setUsername(e.target.value)}}
                            />
                            <Form.Text className="text-muted">
                                This is the username that others will see in LiveChat.
                            </Form.Text>
                        </Form.Group>

                        {/* Password Form Input */}
                        <Form.Group controlId="formPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                required
                                type="password"
                                placeholder="Enter Password"
                                value={origPassword}
                                onChange={(e) => {setOrigPassword(e.target.value)}}
                            />
                        </Form.Group>

                        {/* Password 2 Form Input */}
                        <Form.Group controlId="formConfirmPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                required
                                type="password"
                                placeholder="Confirm Password"
                                value={confirmPassword}
                                onChange={(e) => {setConfirmPassword(e.target.value)}}
                            />
                        </Form.Group>

                         {/* DOB Form Input */}
                        <Form.Group controlId="formDateOfBirth">
                            <Form.Label>Date of Birth</Form.Label>
                            <Form.Control
                                required
                                type="date"
                                placeholder="Select Date of Birth"
                                value={dateOfBirth}
                                onChange={(e) => {setDateOfBirth(e.target.value)}}
                            />
                        </Form.Group>

                        <Form.Group controlId="formEmail">
                            <Form.Label>Email</Form.Label>
                            <Form.Control
                                required
                                type="email"
                                placeholder="Enter email"
                                value={userEmail}
                                onChange={(e) => {setUserEmail(e.target.value)}}
                            />
                            <Form.Text className="text-muted">
                                We'll never share your email with anyone else.
                            </Form.Text>
                        </Form.Group>


                        <Form.Group controlId="formTOS">
                            <Form.Check 
                                required
                                type="checkbox"
                                label="Confirm above information"
                                feedback="You must agree before completing the sign up form."
                            />
                            <Form.Text className="text-muted">
                                By clicking Sign Up, you are indicating that you have read and acknowledge the <Link to='p/tos'>Terms of Service</Link> and <Link to='p/Privacy'>Privacy Notice</Link>.
                            </Form.Text>

                        </Form.Group>


                       
                        <Button variant="primary" type="submit" disabled={validated}> 
                            Create Account 
                        </Button> 

                    </Form>
                </Modal.Body>

            </Modal>

        </>
        
    );

}

export default SignUp
