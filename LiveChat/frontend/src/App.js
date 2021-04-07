import {BrowserRouter as Router, Route} from 'react-router-dom'

// Individual Pages
import HomePage from './components/HomePage'
import aboutPage from './components/aboutPage'
import 'bootstrap/dist/css/bootstrap.min.css'
import UserProfilePage from './components/UserProfilePage';


function App() {

  return (
    <div className="container">
        <Router>
            <Route exact path="/" render = {HomePage} />
            <Route exact path="/en/about" render = {aboutPage} />
            <Route exact path="/:username" render={UserProfilePage} />
        </Router>
    </div>
  );
}

export default App;
