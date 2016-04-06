import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import './styles/herb_manager.scss';
import { configureStore } from './store/configureStore';
import { Root } from './containers/Root';
import * as HerbRESTActions from './actions/HerbRESTActions.js';


/**
 * Configure Redux store with our config 
 * settings and fetch herb data
 */

const store = configureStore();
store.dispatch(HerbRESTActions.fetchHerbs())

/**
 * Render redux-wrapper-root react component.
 */

ReactDOM.render(
  <Root store={store}/>,
  document.getElementById('root')
);
