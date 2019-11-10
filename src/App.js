import React, { Component } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from './pages/home';
import Page2 from './pages/page2';

class App extends Component {
	render() {
		return (
			<Router>
				<Switch>
					<Route exact path="/" component={Home} />
					<Route component={Page2} />
				</Switch>
			</Router>
		);
	}
}


export default App;
