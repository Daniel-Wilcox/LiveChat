
// Styling and Default components
// import { button } from 'bootstrap';
import { Button } from 'react-bootstrap';
import {Link} from 'react-router-dom'
// import {LinkContainer} from 'react-router-bootstrap'
import Navigation  from "./Navigation";
import SignUp from './SignUp';
import 'bootstrap/dist/css/bootstrap.min.css';

    

const HomePage = () => {

    const myStyle = {


        fullpage_style: {
            width: "100%",
            height: "100%",
        },
        navbar_style: {
            width: "100%",
            padding_bottom: "10%",

        },
        contentPage_style: {
            width: "100%",
            position: "relative",
            bottom: "-120px",
            textAlign: "center",
        },
        footer_style: {
            width: "100%",
            position: "relative",
            bottom: "-400px",
            textAlign: "center",


        },
        
        




        
    }




    return (
        <div style={myStyle.fullpage_style}>
            <Navigation style={myStyle.navbar_style}/>

            
            <div style={myStyle.contentPage_style}>
            <h1> Welcome to LiveChat 🚀  </h1>
            <br />
            <br />

            <SignUp />
            <br />
            <br />
            <Link to='/LogIn'><Button variant="outline-primary">Log in</Button></Link>

            <p style={myStyle.footer_style}>
                Copyright &copy; 2021
                <br />
                <Link to='/en/about'>About</Link>
            </p>
                
            </div>


           
        </div>
    )
}

export default HomePage
