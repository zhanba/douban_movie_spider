import React, { Component } from 'react';
import ReactDom from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';
import Drawer from 'material-ui/Drawer';
import MenuItem from 'material-ui/MenuItem';

import Movies from './Movies';
import Filter from './Filter';
import './App.css';

class App extends Component {

    constructor() {
        super();
        this.state = {
            open: false,
            movies: [],
            count: 0
        };
        this.openDrawer = this.openDrawer.bind(this);
    }

    openDrawer() {
        this.setState({
            open: true
        });
    }

    getMovies() {
        const movies_url = '/api/movies';
        const that = this;

        fetch(movies_url)
        .then(function(res) {
            if (res.ok) {
                res.json().then(function(json) {
                    that.setState({
                        movies: json.movies,
                        count: json.count
                    });
                });
            }
        }).catch(function(error) {
            console.error(error.message);
        });
    }

    componentDidMount() {
        this.getMovies();
    }

    render() {
        return (
            <MuiThemeProvider>
                <div>
                    <AppBar
                        title="Search Movies"
                        iconClassNameRight="muidocs-icon-navigation-expand-more"
                        onLeftIconButtonTouchTap={this.openDrawer}
                    />
                    <Movies movies={this.state.movies} />
                    <Drawer 
                        docked={false}
                        width={400}
                        open={this.state.open}
                        onRequestChange={(open) => this.setState({open})}>
                        <MenuItem>Menu Item</MenuItem>
                        <MenuItem>Menu Item 2</MenuItem>
                        <Filter />
                    </Drawer>
                </div>
            </MuiThemeProvider>
        );
    }
}

export default App;
