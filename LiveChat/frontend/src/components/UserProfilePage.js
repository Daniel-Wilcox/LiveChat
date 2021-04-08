import Navigation from './Navigation'
import {useState, useEffect} from 'react'
// import noUserProfilePage from './noUserProfilePage'
import { useParams } from 'react-router-dom'

import axios from 'axios'


import Image from 'react-bootstrap/Image'



function UserProfilePage(props) {

    const myStyles = {
        profile_icon: {
            width: "30%",
        },
    };

    // axios.defaults.proxy.host = "http://localhost";
    // axios.defaults.proxy.port = "8000";

    

    

    

    const [validUser, setValidUser] = useState(false);

    const myParams = useParams();
    const [urlUsername, setUrlUsername] = useState(myParams.username);
    

    const [userData, setUserData] = useState({
        "username": "",
        "user_icon": "",
        "user_bio": "",
        "date_joined": "",
        "is_active": false,
        "is_hosting": false,
    });

    const api_url = ("/api/user/"+urlUsername);


    useEffect(() => {

        const fetchData = async () => { 
            const result = await axios(api_url);
            setUserData(result.data);
            setValidUser(true);
        }
        fetchData();
        
        return () => {
            setValidUser(false);
            setUrlUsername("");
        }
    }, [api_url]);


    return (
        validUser ? (
            <>
                <Navigation />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                
                
                <center>
                    <h1> Welcome to {urlUsername}'s profile page! 😄  </h1>
                    <Image src={userData.user_icon} alt={`${urlUsername}'s profile icon`} style={myStyles.profile_icon} roundedCircle />
                    <br />
                    <br />
                    <br />
                    <h3>{`${urlUsername}'s bio:`}</h3>
                    <br />
                
                    <p> {userData.user_bio} </p>
                </center>

                

            </>
        ) : (
            <>
                <Navigation />
                <br />
                <br />
                <br />
                <br />
                <br />
                <br />
                <center>
                    <h1> Username {urlUsername} does not seem to exist 😢  </h1>
                </center>
            </>
        )
    );
        
}

export default UserProfilePage
