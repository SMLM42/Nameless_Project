import React, {Component} from 'react';

export default class Test extends Component {
	componentDidMount() {
		fetch('/api')
			.then(res => res.json())
			.then(res => console.log(res));
	}

	render() {
		return <div></div>;
	}
}
