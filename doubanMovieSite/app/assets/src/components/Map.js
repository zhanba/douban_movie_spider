import React, { Component, PropTypes } from 'react';
import ol from 'openlayers';
import 'openlayers/dist/ol.css';

export class Map extends Component {
    constructor() {
        super();
    }

    initMap() {
        const url_root = new URL('http://localhost:8080/geoserver/wfs');
        const params = {
            service: 'wfs',
            version: '2.0.0',
            request: 'GetFeature',
            typeNames: 'testLayer:counties_china',
            outputFormat: 'application/json',
            exceptions: 'application/json',
            count: 100
        };

        Object.keys(params).forEach(key => url_root.searchParams.append(key, params[key]));

        const headers = new Headers({'Content-Type': 'application/json'});

        const source = new ol.source.Vector();

        fetch(url_root, {
            method: 'get',
            mode: 'cors',
            headers: headers
        }).then(function(res) {
            if (res.ok) {
                res.json().then(function(json) {
                    console.log(json);
                    var features = new ol.format.GeoJSON().readFeatures(json);
                    source.addFeatures(features);
                });
            }
        }).catch(function(error) {
            console.log(error.message);
        });

        const china_countries = new ol.layer.Vector({
            source: source
        });
        const osm = new ol.layer.Tile({
            source:new ol.source.OSM()
        });
        const view = new ol.View({
            center: ol.proj.fromLonLat(this.props.center),
            zoom: this.props.zoom
        });
        const map = new ol.Map({
            view: view,
            target: 'map',
            layers: [osm, china_countries]
        });
    }

    componentDidMount() {
        this.initMap();
    }

    render() {
        return (
            <div id="map" className="map"></div>
        );
    }
}

Map.propTypes = {
    center: PropTypes.arrayOf(PropTypes.number),
    zoom: PropTypes.number
};

Map.defaultProps = {
    center: [118.79, 32.04],
    zoom: 6
};

export default Map;
