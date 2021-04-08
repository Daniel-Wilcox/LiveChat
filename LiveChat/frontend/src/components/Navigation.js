// import { Navbar, Nav, FormControl, Form, Button } from 'bootstrap';
// import {useState, useEffect} from 'react'
import {useState} from 'react'

import { useHistory} from 'react-router-dom'
// import { BrowserRouter as Router, Switch, Route, Link, useHistory, useParams, Redirect } from 'react-router-dom'

import { Navbar, Nav, Form, FormControl, Button } from 'react-bootstrap'




const Navigation = () => {

    const history = useHistory();
    const [username, setUsername] = useState("");


    const handleClickSubmit = (e) => {
        const user_url = `/${username}`;
        history.push(user_url);
    };

    const handleEnterSubmit = (e) => {
        if (e.key === "Enter"){
            const user_url = `/${username}`;
            history.push(user_url);
        }
    };


    return (
        <>
            
            <Navbar fixed="top" bg="primary" variant="dark">
                <Navbar.Brand href="/"> 🚀 </Navbar.Brand>
                <Nav className="mr-auto">
                    <Nav.Link href="/">Home</Nav.Link>
                    <Nav.Link href="/en/friends">Friends</Nav.Link>
                    <Nav.Link href="/en/tags">Tags</Nav.Link>
                </Nav>

                <Form inline >
                    <FormControl  
                        sm={2}
                        type="text" 
                        placeholder="Search Users" 
                        className="mr-sm-2" 
                        onChange={e => setUsername(e.target.value)}
                        onKeyPress={handleEnterSubmit}
                    />
                    <Button variant="outline-light" onClick={handleClickSubmit}>Search</Button>

                </Form>

            </Navbar>

        </>
        
          
    )
}

export default Navigation
