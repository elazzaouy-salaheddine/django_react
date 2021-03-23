import React, { Component } from 'react';
import { HashRouter as Router, Route, Switch } from "react-router-dom";
import Architect from '../models/architect/Architect';



export default class Navbarbottom extends Component {
    render() {
        return (
            <div className="header-navbar navbar-expand-sm navbar navbar-horizontal navbar-fixed navbar-light navbar-without-dd-arrow" role="navigation" data-menu="menu-wrapper">
            <div className="navbar-header d-xl-none d-block">
                <ul className="nav navbar-nav flex-row">
                    <li className="nav-item mr-auto"><a className="navbar-brand" href="index.html">
                            <div className="brand-logo">
                                <img className="logo" src={"static/frontend/app-assets/images/logo/logo.png"} />
                            </div>
                            <h2 className="brand-text mb-0">Frest</h2>
                        </a></li>
                    <li className="nav-item nav-toggle"><a className="nav-link modern-nav-toggle pr-0" data-toggle="collapse"><i className="bx bx-x d-block d-xl-none font-medium-4 primary toggle-icon"></i></a></li>
                </ul>
            </div>
            <div className="shadow-bottom"></div>
      
            <div className="navbar-container main-menu-content" data-menu="menu-container">
              
                <ul className="nav navbar-nav" id="main-menu-navigation" data-menu="menu-navigation" data-icon-style="filled">

                    <li>
                        <a href="index.html" className='pr-2'>Dashboard</a>

                    </li>
                    <li>
                        <a href="index.html" className='pr-2'>Gte</a>

                    </li>
                    <li>
                        <a href="index.html" className='pr-2 '>Nov Energie </a>

                    </li>
                    <li>
                        <a href="index.html" className='pr-2'>Clients</a>

                    </li>
                    <li>
                        <a href="index.html" className='pr-2'>Lots</a>

                    </li>

                    <li>
                        <a href="index.html" className='pr-2'>Architect</a>

                    </li>
                    <li>
                        <a href="index.html" className='pr-2'>Opc</a>

                    </li>
                  

                </ul>
            </div>
        
        </div>
        )
    }
}
