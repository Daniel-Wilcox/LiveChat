import Navigation from './Navigation';

import {Link} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css'

const aboutPage = () => {
    return (
        <div>
            <Navigation />
            <h3>This is the about page.</h3>
            <h4>Version 0.0.1</h4>
            <Link to='/'>Home</Link>
        </div>
    )
}

export default aboutPage
