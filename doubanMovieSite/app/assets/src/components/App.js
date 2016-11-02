import React from 'react';
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

import Map from './Map';

const iconButtonElement = (
  <IconButton
    touch={true}
    tooltip="more"
    tooltipPosition="bottom-left"
  >
    <MoreVertIcon color={grey400} />
  </IconButton>
);

const rightIconMenu = (
  <IconMenu iconButtonElement={iconButtonElement}>
    <MenuItem>Reply</MenuItem>
    <MenuItem>Forward</MenuItem>
    <MenuItem>Delete</MenuItem>
  </IconMenu>
);

const rightIcon = (<FontIcon className="muidocs-icon-custom-sort" />);

const rightToolbar = (
    <Toolbar>
        <ToolbarGroup>
          <FontIcon className="muidocs-icon-custom-sort" />
          <ToolbarSeparator />
          <rightIconMenu />
        </ToolbarGroup>
      </Toolbar>
);

const App = () => (
    <MuiThemeProvider>
        <div>
            <Drawer width={400}>
                <List>
                    <Subheader>Layers</Subheader>
                    <ListItem 
                        primaryText="Inbox"
                        leftIcon={<RemoveRedEye />}
                        rightIcon={<CommunicationChatBubble className="shift" />}
                        rightIconButton={rightIconMenu} />
                    <ListItem primaryText="Starred" leftIcon={<RemoveRedEye />} />
                    <ListItem primaryText="Sent mail" leftIcon={<RemoveRedEye />} />
                    <ListItem primaryText="Drafts" leftIcon={<RemoveRedEye />} />
                    <ListItem primaryText="Inbox" leftIcon={<RemoveRedEye />} />
                </List>
            </Drawer>
            <AppBar className="header"/>
            <Map />
        </div>
    </MuiThemeProvider>
);

export default App;
