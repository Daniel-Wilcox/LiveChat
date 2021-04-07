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
            <Route exact path="/" component = {HomePage} />
            <Route exact path="/en/about" component = {aboutPage} />
            <Route exact path="/:username" component={UserProfilePage} />
        </Router>
    </div>
  );
}

export default App;
