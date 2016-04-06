import React, { Component } from 'react';


export default class HerbManagerList extends Component {

	constructor(props, context) {
		super(props, context)
	}

	render() {
		let list_items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14];
		if (this.props.herbsData.isFetching) {
			return (
				<div className="manager-fetching-container">
					<p>Loading...</p>
				</div>
			);
		} else {
			return (
				<div className="manager-list-container">
					<ul>
						{this.props.herbsData.items.map(function(herbData, id) {
							return <HerbManagerListItem key={id} id={id} herbData={herbData} actions={this.props.actions}/>
						}, this)}
					</ul>
				</div>
			);
		}
	}
}

class HerbManagerListItem extends Component {

	constructor(props, context) {
		super(props, context)
	}

	handleClick() {
		this.props.herbControlsActions.setSelectedHerb(this.props.id)
	}

	render() {
		return (
			<li className="manager-list-item" onClick={this.handleClick.bind(this)}>
				<div><p>{this.props.herbData.name}</p></div>
			</li>
		);
	}
}