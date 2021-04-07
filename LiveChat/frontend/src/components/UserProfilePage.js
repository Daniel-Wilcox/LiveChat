import Navigation from './Navigation'
import {useState, useEffect} from 'react'
import { useParams} from 'react-router-dom'
// import noUserProfilePage from './noUserProfilePage'


const UserProfilePage = (props) => {

    // const validUser = false;

    const [validUser, setValidUser] = useState(false);
    const { params } = useParams();

    const [userData, setUserData] = useState({
        "username": "",
        "user_icon": "",
        "user_bio": "",
        "date_joined": "",
        "is_active": false,
        "is_hosting": false,
    });

    // const api_url = ("http://localhost:8000/api/user/"+props.match.params.username);
    const api_url = ("http://localhost:8000/api/user/"+params.username);
    
    

    // useEffect(() => {
    //     fetch(api_url)
    //         .then(data => {
    //             return data.json();
    //         })
    //         .then(data => {
    //             setUserData(data);
    //             setValidUser(true);
    //         })
    //         .catch(err => {
    //             setValidUser(false);
    //         });
    // }, [api_url]);

    // function getUserProfileInfo() {

    // };


    // const UserProfile = () => {
    //     return (
    //         <>
    //             <Navigation />
    //             <br />
    //             <br />
    //             <br />
    //             <br />
    //             <br />
    //             <br />
    //             <h1> Welcome to {props.match.params.username}'s profile page! 😄  </h1>
    //         </>

    //     );

    // };

    // const noUserFound () {
    //     return (
    //         <>
    //             <Navigation />
    //             <br />
    //             <br />
    //             <br />
    //             <br />
    //             <br />
    //             <br />
    //             <h1> Username {props.match.params.username} does not seem to exist 😢  </h1>
    //         </>
    //     );
    // };


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
                <h1> Welcome to {props.match.params.username}'s profile page! 😄  </h1>
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
                <h1> Username {props.match.params.username} does not seem to exist 😢  </h1>
            </>
            )
        );

}

export default UserProfilePage
