// import { Navbar, Nav, FormControl, Form, Button } from 'bootstrap';

import { Navbar, Nav, Form, FormControl, Button } from 'react-bootstrap'

const Navigation = () => {
    return (
        <>
            <Navbar bg="primary" variant="dark">
                <Navbar.Brand href="/">Navbar</Navbar.Brand>
                <Nav className="mr-auto">
                    <Nav.Link href="/">Home</Nav.Link>
                    <Nav.Link href="/">Features</Nav.Link>
                    <Nav.Link href="/">Pricing</Nav.Link>
                </Nav>

                <Form inline>
                    <FormControl type="text" placeholder="Search Users" className="mr-sm-2" />
                    <Button variant="outline-light">Search</Button>
                </Form>

            </Navbar>

        </>
        
          
    )
}

export default Navigation
