import React, {Component} from 'react';
import HerbManagerControls from './../components/HerbManagerControls.js';
import HerbManagerList from './../components/HerbManagerList.js';
import HerbManagerForm from './../components/HerbManagerForm.js';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import * as HerbControlsActions from '../actions/HerbControlsActions.js';
import * as HerbRESTActions from '../actions/HerbRESTActions.js';
import * as HerbFormActions from '../actions/HerbFormActions.js';
import * as HerbActions from '../actions/HerbActions.js';



/**
 * Main Application Component
 *
 * It is common practice to have a 'Root' container/component require our main app component (HerbManager).
 * Again, this is because it serves to wrap the rest of our application with the Provider
 * component to make the Redux store available to the rest of the app.
 */

export default class HerbManager extends Component {

	constructor(props, context) {
		super(props, context)
	}
  
	render() {
		return (
			<div className="manager-content">
        <div className="manager-top-container">
          {(() => {
            switch(this.props.topContent.contentIndex) {
              case 0: return <HerbManagerList topContent={this.props.topContent} herbsData={this.props.herbsData} actions={this.props.actions} />;
              case 1: return <HerbManagerForm actions={this.props.actions}/>
              default: return undefined;
            }
          })()}
        </div>
				<HerbManagerControls topContent={this.props.topContent} bottomContent={this.props.bottomContent} actions={this.props.actions} />
			</div>
		);
	}
}

/**
 * Map Store State to Props
 *
 * Keep in mind that 'state' isn't the state of local object, but your single
 * state in this Redux application. 'counter' is a property within our store/state
 * object. By mapping it to props, we can pass it to the child component Counter.
 */

function mapStateToProps(state) {
  return {
    topContent: state.topContent,
    bottomContent: state.bottomContent,
    herbsData: state.herbs
  };
}

/*  */

/**
 * Dispatch Wrap Redux Actions
 *
 * Turns an object whose values are 'action creators' into an object with the same
 * keys but with every action creator wrapped into a 'dispatch' call that we can invoke
 * directly later on. Here we imported the actions specified in 'CounterActions.js' and
 * used the bindActionCreators function Redux provides us.
 *
 * More info: http://redux.js.org/docs/api/bindActionCreators.html
 */

function mapDispatchToProps(dispatch) {
  return {
    actions: {
      herbControlsActions: bindActionCreators(HerbControlsActions, dispatch),
      herbRESTActions: bindActionCreators(HerbRESTActions, dispatch),
      herbFormActions: bindActionCreators(HerbFormActions, dispatch),
      herbActions: bindActionCreators(HerbActions, dispatch)
    }
  };
}

/*  */

/**
 * Connect Component Hierarchy with Store
 *
 * 'connect' is provided to us by the bindings offered by 'react-redux'. It simply
 * connects a React component to a Redux store. It never modifies the component class
 * that is passed into it, it actually returns a new connected componet class for use.
 *
 * More info: https://github.com/rackt/react-redux
 */

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(HerbManager);
