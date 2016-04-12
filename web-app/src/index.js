import 'babel-polyfill';
import React from 'react';
import ReactDOM from 'react-dom';
import { configureStore } from './store/configureStore';
import { Root } from './containers/Root';
import * as HerbRESTActions from './actions/HerbRESTActions.js';
import * as HerbActions from './actions/HerbActions.js';

//import './styles/libs/font-awesome/scss/font-awesome.scss'
import './styles/herb_manager.scss';


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
