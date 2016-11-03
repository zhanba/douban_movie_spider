
import ReactDom from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import Drawer from 'material-ui/Drawer';
import RemoveRedEye from 'material-ui/svg-icons/image/remove-red-eye';
import { List, ListItem } from 'material-ui/List';
import Subheader from 'material-ui/Subheader';
import IconMenu from 'material-ui/IconMenu';
import MenuItem from 'material-ui/MenuItem';
import IconButton from 'material-ui/IconButton';
import FontIcon from 'material-ui/FontIcon';
import {grey400, darkBlack, lightBlack} from 'material-ui/styles/colors';
import MoreVertIcon from 'material-ui/svg-icons/navigation/more-vert';
import {Toolbar, ToolbarGroup, ToolbarSeparator, ToolbarTitle} from 'material-ui/Toolbar';

import CommunicationChatBubble from 'material-ui/svg-icons/communication/chat-bubble';

import Movies from './Movies' 

import React, { Component } from 'react';

export class App extends Component {
    render() {
        return (
            <div>Hello Movies <Movies /></div>
        );
    }
}

export default App;
