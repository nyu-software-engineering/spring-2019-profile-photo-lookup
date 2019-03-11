import React, { Component } from 'react';
import './home.css';
import { connect } from 'react-redux';
import UploadDropzone from './uploadDropzone.js';

class Home extends Component {

    render() {
        return (
            <div className="App container">
                <h1>Welcome to RIS!</h1>
                <div><UploadDropzone /></div>
            </div>
        );
    }
}

function mapStateToProps(state) {
    return {
        names: state.analysis.names
    };
}

export default connect(mapStateToProps, null)(Home);
