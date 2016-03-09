import React, { Component } from 'react';

export default class HerbManagerControls extends Component {

	constructor(props, context) {
		super(props, context)
	}

	render() {
		return (
			<div className="manager-controls-container">
				<div className="manager-controls-button">
					<HerbManagerControlsButton text="Add" />
				</div>
			</div>
		);
	}
}

class HerbManagerControlsButton extends Component {
	
	constructor(props, context) {
		super(props, context)
	}

	handleClick() {

	}

	render() {
		return (
			<div className="manager-controls-button" onClick={this.handleClick.bind(this)}>
				<p>{this.props.text}</p>
			</div>
		);
	}
}