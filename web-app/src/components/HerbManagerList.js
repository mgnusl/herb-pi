import React, { Component } from 'react';


export default class HerbManagerList extends Component {

	constructor(props, context) {
		super(props, context)
	}

	render() {
		if (this.props.herbsData.isFetching) {
			return (
				<div className="manager-fetching-container">
					<p>Fetching herb data..</p>
				</div>
			);
		} else {
			return (			
				<ul>
					{this.props.herbsData.items.map(function(herbData, id) {
						return <HerbManagerListItem selected={(this.props.topContent.selected===id)}
													key={id} id={id} herbData={herbData} 
													actions={this.props.actions}/>
					}, this)}
				</ul>
			);
		}
	}
}

class HerbManagerListItem extends Component {

	constructor(props, context) {
		super(props, context)
	}

	handleClick() {
		this.props.actions.herbControlsActions.setSelectedHerb(this.props.id)
	}

	render() {

		let className = "manager-list-item"
		if (this.props.selected) {
			className += " selected-item"
		}

		return (
			<li className={className} onClick={this.handleClick.bind(this)}>
				<div><p>{this.props.herbData.name}</p><p>{this.props.herbData.name}</p></div>
			</li>
		);
	}
}