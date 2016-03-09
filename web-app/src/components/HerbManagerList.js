import React, { Component } from 'react';

export default class HerbManagerList extends Component {

	constructor(props, context) {
		super(props, context)
	}

	render() {
		let list_items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14];
		return (
			<div className="manager-list-container">
				<ul>
					{list_items.map(function(item, id) {
						return <HerbManagerListItem key={id} id={id} actions={this.props.actions}/>
					}, this)}
				</ul>
			</div>
		);
	}
}

class HerbManagerListItem extends Component {

	constructor(props, context) {
		super(props, context)
	}

	handleClick() {
		this.props.actions.setSelectedHerb(this.props.id)
	}

	render() {
		return (
			<li className="manager-list-item" onClick={this.handleClick.bind(this)}>
				<div></div>
			</li>
		);
	}
}