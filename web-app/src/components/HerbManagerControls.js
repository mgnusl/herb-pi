import React, { Component } from 'react';
import { Button } from 'react-bootstrap';

export default class HerbManagerControls extends Component {

	constructor(props, context) {
		super(props, context)
	}

	onPlusClick() {
		this.props.actions.herbActions.setTopContainerContent(1)
	}

	onMinusClick() {
		console.log("Prompt user for herb removal")
	}

	render() {
		if (this.props.topContent.selected === -1) {
			return (
				<div className="manager-controls-container">
					<Button className="glyphicon glyphicon-plus" bsSize="large" onClick={this.onPlusClick.bind(this)}></Button>;
				</div>
			);
		} else {
			return (
				<div className="manager-controls-container">
					<Button className="glyphicon glyphicon-minus" bsSize="large"></Button>;
				</div>
			);
		}
	}
}