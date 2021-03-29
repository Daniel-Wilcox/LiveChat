import {useState} from 'react'
import { Button, Modal, Form } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'
import {Link} from 'react-router-dom'

function SignUp() {

    const [username, setUsername] = useState('');
    const [pass1, setPass1] = useState('');
    const [pass2, setPass2] = useState('');
    const [date_of_birth, setDateOfBirth] = useState('');
    const [email, setEmail] = useState('');
    const [check, setCheck] = useState(false);

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);


    // const handleUpdate = (e, updater) => {
    //     updater(e.target.value);
    //     console.log(username);

    // }

    const handleSubmit = (e) => {
        console.log(`username {username}`);
        // console.log(username)
        // console.log(username)
        // console.log(username)
        // console.log(username)

    };




    return (
        <>
          <Button variant="primary" onClick={handleShow}>
            Sign Up
          </Button>
    
          <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>Sign Up</Modal.Title>
            </Modal.Header>

            <Modal.Body>
                <Form>
                <Form.Group controlId="formUsername">
                    <Form.Label>User Name</Form.Label>
                    <Form.Control required type="username" placeholder="Enter username" onChange={() => setUsername(e.target.value)} />
                    <Form.Text className="text-muted">
                        This is the username that others will see in LiveChat.
                    </Form.Text>
                </Form.Group>
{/* 
                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control required type="password" placeholder="Password" onChange={() => setPass1(e.target.value)}/>
                </Form.Group>

                <Form.Group controlId="formBasicPasswordConfirm">
                    <Form.Label>Password</Form.Label>
                    <Form.Control required type="password" placeholder="Confirm Password" onChange={() => setPass2(e.target.value)}/>
                </Form.Group>

                <Form.Group controlId="formDOB">
                    <Form.Label>Select Date of Birth</Form.Label>
                    <Form.Control required type="date" name="dob" placeholder="Date of Birth" onChange={() => setDateOfBirth(e.target.value)}/>
                </Form.Group>

                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control required type="email" placeholder="Enter email" onChange={() => setEmail(e.target.value)}/>
                    <Form.Text className="text-muted">
                        We'll never share your email with anyone else.
                    </Form.Text>
                </Form.Group>

                <Form.Group controlId="formBasicCheckbox">
                    <Form.Check required type="checkbox" label="Confirm above information" onChange={() => setCheck(e.target.value)}/>
                    <Form.Text className="text-muted">
                        By clicking Sign Up, you are indicating that you have read and acknowledge the <Link to='p/tos'>Terms of Service</Link> and <Link to='p/Privacy'>Privacy Notice</Link>.
                    </Form.Text>
                </Form.Group> */}

   
                

                </Form>
            </Modal.Body>
            
            <Modal.Footer>
            <Button variant="primary" type="submit" onClick={(handleSubmit)}>Submit</Button>
            {/* <Button variant="primary" type="submit" onClick={(handleSubmit)}>Submit</Button> */}
            </Modal.Footer>
          </Modal>
        </>
      );
    // return (
    //     <>
    //       <Button variant="primary" onClick={handleShow}>
    //         Sign Up
    //       </Button>
    
    //       <Modal show={show} onHide={handleClose}>
    //         <Modal.Header closeButton>
    //           <Modal.Title>Sign Up</Modal.Title>
    //         </Modal.Header>

    //         <Modal.Body>
    //             <Form>
    //             <Form.Group controlId="formUsername">
    //                 <Form.Label>User Name</Form.Label>
    //                 <Form.Control required type="username" placeholder="Enter username" onChange={() => setUsername(e.target.value)} />
    //                 <Form.Text className="text-muted">
    //                     This is the username that others will see in LiveChat.
    //                 </Form.Text>
    //             </Form.Group>

    //             <Form.Group controlId="formBasicPassword">
    //                 <Form.Label>Password</Form.Label>
    //                 <Form.Control required type="password" placeholder="Password" onChange={() => setPass1(e.target.value)}/>
    //             </Form.Group>

    //             <Form.Group controlId="formBasicPasswordConfirm">
    //                 <Form.Label>Password</Form.Label>
    //                 <Form.Control required type="password" placeholder="Confirm Password" onChange={() => setPass2(e.target.value)}/>
    //             </Form.Group>

    //             <Form.Group controlId="formDOB">
    //                 <Form.Label>Select Date of Birth</Form.Label>
    //                 <Form.Control required type="date" name="dob" placeholder="Date of Birth" onChange={() => setDateOfBirth(e.target.value)}/>
    //             </Form.Group>

    //             <Form.Group controlId="formBasicEmail">
    //                 <Form.Label>Email address</Form.Label>
    //                 <Form.Control required type="email" placeholder="Enter email" onChange={() => setEmail(e.target.value)}/>
    //                 <Form.Text className="text-muted">
    //                     We'll never share your email with anyone else.
    //                 </Form.Text>
    //             </Form.Group>

    //             <Form.Group controlId="formBasicCheckbox">
    //                 <Form.Check required type="checkbox" label="Confirm above information" onChange={() => setCheck(e.target.value)}/>
    //                 <Form.Text className="text-muted">
    //                     By clicking Sign Up, you are indicating that you have read and acknowledge the <Link to='p/tos'>Terms of Service</Link> and <Link to='p/Privacy'>Privacy Notice</Link>.
    //                 </Form.Text>
    //             </Form.Group>

   
                

    //             </Form>
    //         </Modal.Body>
            
    //         <Modal.Footer>
    //         <Button variant="primary" type="submit" onClick={(handleSubmit)}>Submit</Button>
    //         {/* <Button variant="primary" type="submit" onClick={(handleSubmit)}>Submit</Button> */}
    //         </Modal.Footer>
    //       </Modal>
    //     </>
    //   );
}

export default SignUp
