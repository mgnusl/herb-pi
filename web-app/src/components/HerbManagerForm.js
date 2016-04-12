import React, { Component } from 'react';
import { reduxForm } from 'redux-form';
import { Button, Input } from 'react-bootstrap';

class HerbManagerForm extends Component {

	constructor(props, context) {
		super(props, context)
	}

	render() {
		const {fields: {name}, handleSubmit} = this.props;
		return (
			<div className="manager-form-container">
				<form onSubmit={handleSubmit}>
			        <div>
				          <Input type="text" label="Name" placeholder="name your herb.." onChange={param => param.onChange(param.val)}/>
				          <Button type="submit" value="Submit"/>
			        </div>
				</form>
			</div>
		)
	}
}

HerbManagerForm = reduxForm({
  form: 'herb',
  fields: ['name']
})(HerbManagerForm);

export default HerbManagerForm;
