import {useState} from 'react';
import {Button, Modal, Form } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom';
// import {axios} from 'axios';

function SignUp() {
    

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const [username, setUsername] = useState("");
    const [pass1, setPass1] = useState("");
    const [pass2, setPass2] = useState("");
    const [date_of_birth, setDateOfBirth] = useState("");
    const [email, setEmail] = useState("");

    const [validated, setValidated] = useState(false);



    const handleSubmit = (e) => {

        console.log(e.currentTarget);
        setTimeout(function() {console.log(e.currentTarget)}, 1000);
        setValidated(true);

    };




    return (
        <>
            <Button variant="primary" onClick={handleShow}> Sign Up </Button>
            <Modal show={show} onHide={handleClose}>

                <Modal.Header closeButton>
                    <Modal.Title> Sign Up </Modal.Title>
                </Modal.Header>

                <Modal.Body>
                    <Form noValidate validated={validated} onSubmit={handleSubmit}>

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
                                value={pass1}
                                onChange={(e) => {setPass1(e.target.value)}}
                            />
                        </Form.Group>

                        {/* Password 2 Form Input */}
                        <Form.Group controlId="formConfirmPassword">
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                required
                                type="password"
                                placeholder="Confirm Password"
                                value={pass2}
                                onChange={(e) => {setPass2(e.target.value)}}
                            />
                        </Form.Group>

                         {/* DOB Form Input */}
                        <Form.Group controlId="formDateOfBirth">
                            <Form.Label>Date of Birth</Form.Label>
                            <Form.Control
                                required
                                type="date"
                                placeholder="Select Date of Birth"
                                value={date_of_birth}
                                onChange={(e) => {setDateOfBirth(e.target.value)}}
                            />
                        </Form.Group>

                        <Form.Group controlId="formEmail">
                            <Form.Label>Email</Form.Label>
                            <Form.Control
                                required
                                type="email"
                                placeholder="Enter email"
                                value={email}
                                onChange={(e) => {setEmail(e.target.value)}}
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


                       
                        <Button variant="primary" type="submit"> 
                            Create Account 
                        </Button> 

                    </Form>
                </Modal.Body>

            </Modal>

        </>
        
    );

}

export default SignUp
