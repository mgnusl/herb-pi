import React, { Component } from 'react';
import { Provider } from 'react-redux';
import DevTools from './DevTools';
import HerbManager from './HerbManager';


/**
 * Redux Store Wrapping & Devlopment Tools
 *
 * Provider is a component provided to us by the 'react-redux' bindings that
 * wraps our app - thus making the Redux store/state available to our 'connect()'
 * calls in component hierarchy.
 *
 * DevTools provides us with some handy features in dev mode.
 */

module.exports = class Root extends Component {
  render() {
    const { store } = this.props;
    const style = {
      height: "100%"
    }
    return (
      <Provider store={store}>
        <div style={style}>
          <HerbManager />
          <DevTools />
        </div>
      </Provider>
    );
  }
};
