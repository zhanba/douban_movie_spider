import React, { Component } from 'react';

export class Movies extends Component {

    constructor() {
        super();
        this.state = {
            movies: {},
            count: 0
        }
    }

    getMvoies() {
        const movies_url = '/api/movies';
        var that = this;

        fetch(movies_url)
        .then(function(res) {
            if (res.ok) {
                res.json().then(function(json) {
                    console.log(json);
                    that.setState({
                        movies: json.movies,
                        count: json.count
                    });
                });
            }
        }).catch(function(error) {
            console.log(error.message);
        });
    }

    componentDidMount() {
        this.getMvoies();
    }

    render() {
        return (
            <div>{this.state.count}</div>
        );
    }
}

export default Movies;
