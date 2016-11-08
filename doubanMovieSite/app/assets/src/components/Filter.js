import React, { Component } from 'react';

export default class Filter extends Component {

    constructor() {
        super();
    }

    static defaultProps = {
        year: [1980, 2020],
        genres: [],

    }

    render() {
        return (
            <div>
                Filter
            </div>
        );
    }
}
