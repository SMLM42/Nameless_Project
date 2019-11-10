import React, { Component } from 'react';
import logo from './logo.svg';
import Test from './Test';
import './App.css';
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from './pages/home';

class App extends Component {
	render() {
		return (
			<Router>
				<Route exact path="/" component={Home} />
				<Route component={Home} />
			</Router>
		);
	}
}


export default App;
