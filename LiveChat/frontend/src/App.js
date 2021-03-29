import {BrowserRouter as Router, Route} from 'react-router-dom'

// Individual Pages
import HomePage from './components/HomePage'
import aboutPage from './components/aboutPage'
import 'bootstrap/dist/css/bootstrap.min.css'


function App() {

  return (
    <div className="container">
        <Router>
            <Route path='/' exact render = {HomePage} />
            <Route path='/about' render = {aboutPage} />
        </Router>
    </div>
  );
}

export default App;
