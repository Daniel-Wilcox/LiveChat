
// Styling and Default components
// import { button } from 'bootstrap';
import { Button } from 'react-bootstrap';
import Navigation from './Navigation';
import {Link} from 'react-router-dom'
// import {LinkContainer} from 'react-router-bootstrap'
// import { axios } from 'axios'
import SignUp from './SignUp';
import 'bootstrap/dist/css/bootstrap.min.css'
    

const HomePage = () => {

    // const api_url = 'http://localhost:8000/';




    return (
        <div>
            <Navigation />
            <h1> Welcome to LiveChat 🚀  </h1>

            <SignUp />
            <br />
            <Link to='/LogIn'><Button variant="outline-primary">Log in</Button> <br /></Link>


            <p>Copyright &copy; 2021</p>
            <Link to='/about'>About</Link>
        </div>
    )
}

export default HomePage
