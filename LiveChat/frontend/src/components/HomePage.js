
// Styling and Default components
// import { button } from 'bootstrap';
import { Button } from 'react-bootstrap';
import Navigation from './Navigation';

import {Link} from 'react-router-dom'
    

const HomePage = () => {

    

    return (
        <div>
            <Navigation />
            <h1> Welcome to LiveChat 🚀  </h1>


            <Button variant="primary">Sign up</Button> <br />
            <Button variant="outline-primary">Log in</Button> <br />


            <p>Copyright &copy; 2021</p>
            <Link to='/about'>About</Link>
        </div>
    )
}

export default HomePage
