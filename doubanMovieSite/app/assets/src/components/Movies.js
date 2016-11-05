import React, { Component } from 'react';
import {GridList, GridTile} from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';
import StarBorder from 'material-ui/svg-icons/toggle/star-border';

import styles from './Movies.css';

export class Movies extends Component {

    constructor() {
        super();
    }

    static defaultProps = {
        movies: [],
        count: 0
    }

    getMovieGrid(movies) {
        if (movies !== null && movies !== []) {
            return movies.map((movie) => (
                <GridTile
                    key={movie.cover_url}
                    title={movie.name}
                    actionIcon={<IconButton><StarBorder color="white" /></IconButton>}
                >
                    <img src={movie.cover_url} />
                </GridTile>
            ))
        }
    }

    render() {
        return (
            <div className={styles.root}>
                <GridList className={styles.gridList} cols={4}>
                    {this.getMovieGrid(this.props.movies)}
                </GridList>
            </div>
        );
    }
}

export default Movies;
