import React, { Component } from 'react';
import Navbar from './Navbar';
import Navbarbottom from './Navbarbottom';
import Footer from './Footer';


export default class Base extends Component {
    render() {
        return (
            <>
                <Navbar/>
                <Navbarbottom/>
                <Footer/>
            </>
        )
    }
}
