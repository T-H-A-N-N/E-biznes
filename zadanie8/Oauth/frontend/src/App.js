import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Register from './Register';
import Login from './Login';

const App = () => {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/register" component={Register} />
                    <Route path="/login" component={Login} />
                </Switch>
            </div>
        </Router>
    );
};

export default App;
